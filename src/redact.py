"""Fail-closed redaction of author- and corpus-side secrets.

Anything credential-shaped is replaced with a typed placeholder. Anything
that looks secret but cannot be confidently typed causes the whole value to
be dropped, because publishing a live credential in a wordlist is a worse
failure than losing one payload.
"""

import math
import re
import urllib.parse

CREDENTIALS: tuple[tuple[re.Pattern, str], ...] = (
    (re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"), "<JWT>"),
    # No \b anchors on the prefix-based patterns below: a credential glued
    # directly to adjacent word characters (no separator) would otherwise
    # slip through untouched, and the entropy backstop is not guaranteed to
    # catch it if the glue text dilutes the combined token's entropy. The
    # prefixes are distinctive enough that matching mid-token is safe.
    (re.compile(r"AKIA[0-9A-Z]{16}"), "<AWS_KEY>"),
    (re.compile(r"ASIA[0-9A-Z]{16}"), "<AWS_KEY>"),
    (re.compile(r"ghp_[A-Za-z0-9]{30,}"), "<GITHUB_TOKEN>"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{20,}"), "<GITHUB_TOKEN>"),
    (re.compile(r"nvapi-[A-Za-z0-9_-]{20,}"), "<NVIDIA_KEY>"),
    # `sk-` is only two letters, so unlike the other prefixes it matches
    # inside ordinary words -- "desk-", "task-", "kiosk-". A lookbehind for a
    # word character is narrower than \b: it still catches a key glued after
    # punctuation or an equals sign, which is what the adjacency bypass used,
    # while refusing to fire mid-word.
    (re.compile(r"(?<![A-Za-z0-9_])sk-[A-Za-z0-9]{20,}"), "<API_KEY>"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "<SLACK_TOKEN>"),
    # Written as -{5} rather than five literal dashes so this source file
    # does not itself trip the audit script's private-key check.
    (re.compile(r"-{5}BEGIN [A-Z ]*PRIVATE KEY-{5}"), "<PRIVATE_KEY>"),
)

# Hosts that carry meaning in a payload and must survive normalisation.
# The IP entries (169.254.169.254, 127.0.0.1) are inert today: _HOST only
# matches hostnames with an alphabetic TLD suffix, so it never captures a
# dotted-quad IP in the first place. They stay here to document intent and
# become live if _HOST is ever extended to match bare IPs.
SAFE_HOSTS = frozenset({
    "evil.com", "attacker.com", "example.com", "target.com", "localhost",
    "169.254.169.254", "127.0.0.1", "metadata.google.internal",
    "burpcollaborator.net", "interact.sh",
})

_HOST = re.compile(r"\bhttps?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", re.IGNORECASE)

# Distinct hosts are renamed by position, not all to one name. Collapsing every
# host to target.com destroys the payload it is protecting: an open redirect
# whose source and destination are both target.com demonstrates nothing. The
# first host in a payload is the victim, the second is where it sends you.
POSITIONAL_HOSTS = ("target.com", "evil.com", "evil2.com", "evil3.com")

# Hostnames without a scheme are normalised too, but only when they end in one
# of these TLDs. A generic "label.label" pattern would rewrite ordinary payload
# content -- /etc/passwd.txt, index.html, win.ini, shell.php.jpg -- and
# corrupting a payload is a worse outcome than leaving a hostname in it.
#
# Deliberately absent, because each collides with a common code idiom that
# appears inside real payloads: .is (Object.is), .id (element.id), .at
# (Array.at), .name (window.name), .in, .it, .sh, .so, .py, .pl.
_BARE_TLDS = (
    "com", "net", "org", "edu", "gov", "mil", "int", "info", "biz", "io",
    "co", "ai", "ad", "ae", "af", "ag", "ai", "al", "ao", "ar", "au", "aw",
    "az", "ba", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bm", "bn", "bo",
    "br", "bs", "bt", "bw", "bz", "ca", "cf", "cg", "ch", "ci", "cl", "cm",
    "cn", "cr", "cu", "cv", "cy", "cz", "de", "dj", "dk", "dm", "dz", "ec",
    "ee", "eg", "er", "es", "et", "eu", "fi", "fj", "fm", "fo", "fr", "ga",
    "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr",
    "gt", "gu", "gw", "gy", "hk", "hn", "hr", "ht", "hu", "ie", "il", "iq",
    "ir", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr",
    "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "lt", "lu", "lv",
    "ly", "ma", "mc", "md", "mg", "mk", "ml", "mm", "mn", "mo", "mq", "mr",
    "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng",
    "ni", "nl", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph",
    "pk", "pn", "pr", "ps", "pt", "pw", "qa", "ro", "rs", "ru", "rw", "sa",
    "sb", "sc", "se", "sg", "si", "sk", "sl", "sm", "sn", "sr", "sv", "sy",
    "sz", "td", "tg", "th", "tj", "tm", "tn", "tr", "tt", "tv", "tw", "tz",
    "ua", "ug", "uk", "us", "uy", "uz", "va", "vc", "ve", "vg", "vn", "vu",
    "ws", "ye", "za", "zm", "zw",
)

# A second level is structural rather than enumerated: any of these before a
# country code, so google.co.in and mtn.com.gh both resolve whole instead of
# matching "google.co" and leaving a dangling ".in".
_SECOND_LEVEL = ("com", "co", "org", "net", "ac", "gov", "edu", "ne", "or")

_BARE_HOST = re.compile(
    # A preceding "." is allowed: reports write templated hosts such as
    # www.[TEAM].slack.com, and excluding "." shielded the victim name. Label
    # matching is greedy and scans left to right, so a full subdomain still
    # matches from its leftmost label rather than its suffix.
    # "%" is excluded as well as word characters: percent-encoded text such as
    # "%2Fgoogle.co" otherwise matched as a host ("2fgoogle" is a valid label
    # shape) and was rewritten across the encoding boundary.
    r"(?<![\w@%-])"
    r"((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"(?:(?:" + "|".join(_SECOND_LEVEL) + r")\.)?"
    r"(?:" + "|".join(_BARE_TLDS) + r"))"
    r"(?![\w-])",
    re.IGNORECASE,
)
# A home directory names a person. The researcher is credited in the
# provenance line already; their machine's username does not need to be in a
# wordlist. System paths like /etc/passwd are the payload itself and are left
# exactly as they are.
_HOME_PATH = re.compile(r"(?<![\w-])(/(?:Users|home))/[A-Za-z0-9._-]+", re.IGNORECASE)

_ENTROPY_TOKEN = re.compile(r"\b[A-Za-z0-9+/_-]{32,}\b")
_ENTROPY_THRESHOLD = 3.5


def _shannon(value: str) -> float:
    if not value:
        return 0.0
    counts = {ch: value.count(ch) for ch in set(value)}
    total = len(value)
    return -sum((n / total) * math.log2(n / total) for n in counts.values())


def redact(text: str) -> str | None:
    out = text
    for pattern, placeholder in CREDENTIALS:
        out = pattern.sub(placeholder, out)

    assigned: dict[str, str] = {}

    def normalise(match: re.Match) -> str:
        host = match.group(1)
        # POSITIONAL_HOSTS are checked too: the bare pass runs over the scheme
        # pass's output, and would otherwise treat evil2.com as a fresh host
        # and rename it again.
        if host.lower() in SAFE_HOSTS or host.lower() in POSITIONAL_HOSTS:
            return match.group(0)
        if host.lower() not in assigned:
            position = min(len(assigned), len(POSITIONAL_HOSTS) - 1)
            assigned[host.lower()] = POSITIONAL_HOSTS[position]
        return match.group(0).replace(host, assigned[host.lower()])

    out = _HOME_PATH.sub(lambda m: f"{m.group(1)}/user", out)
    out = _HOST.sub(normalise, out)
    # Bare hostnames run second, sharing the same assignment map, so the
    # schemed and unschemed forms of one host resolve to the same name.
    out = _BARE_HOST.sub(normalise, out)

    # Percent-encoded URLs hide the host from both passes above, because the
    # separators are encoded even though the hostname itself is not. Decode a
    # copy to FIND the hosts, then replace the literal hostname in the original
    # -- replacing a matched region instead would rewrite across the encoding
    # and mangle it, which is the corruption this avoids.
    if "%" in out:
        decoded = urllib.parse.unquote(urllib.parse.unquote(out))
        for host in _HOST.findall(decoded) + _BARE_HOST.findall(decoded):
            if host.lower() in SAFE_HOSTS or host.lower() in POSITIONAL_HOSTS:
                continue
            if host not in out:
                continue
            if host.lower() not in assigned:
                position = min(len(assigned), len(POSITIONAL_HOSTS) - 1)
                assigned[host.lower()] = POSITIONAL_HOSTS[position]
            out = out.replace(host, assigned[host.lower()])

    # Fail closed: an unclassified high-entropy blob may be a live secret.
    for token in _ENTROPY_TOKEN.findall(out):
        if token.startswith("<") or token.lower() in SAFE_HOSTS:
            continue
        if _shannon(token) >= _ENTROPY_THRESHOLD:
            return None

    return out
