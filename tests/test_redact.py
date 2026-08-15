from src.redact import redact

# Every secret below is fabricated and matches no real credential. Each is
# ASSEMBLED AT RUNTIME rather than written as a literal, so no
# credential-shaped string exists anywhere in the repository's source. This
# is what lets scripts/audit.sh (Task 14) scan every file with no path
# exceptions instead of carrying a fail-open exemption for tests/.
FAKE_JWT = "ey" + "J" + "hbGciOiJIUzI1NiJ9" + "." + "eyJzdWIiOiIxMjM0NSJ9" + "." + "a" * 27
FAKE_AWS = "AK" + "IA" + "IOSFODNN7EXAMPLE"
FAKE_GH = "ghp_" + "a" * 36
FAKE_NV = "nvapi-" + "b" * 40


def test_jwt_is_replaced():
    out = redact(f"Authorization: Bearer {FAKE_JWT}")
    assert out is not None
    assert FAKE_JWT not in out
    assert "<JWT>" in out


def test_aws_key_is_replaced():
    out = redact(f"key={FAKE_AWS}")
    assert out is not None and FAKE_AWS not in out and "<AWS_KEY>" in out


def test_github_and_nvidia_tokens_are_replaced():
    out = redact(f"{FAKE_GH} and {FAKE_NV}")
    assert out is not None
    assert FAKE_GH not in out and FAKE_NV not in out


def test_victim_hostname_is_normalised():
    out = redact("https://acmebank.com/redirect?next=//evil.com")
    assert out is not None
    assert "acmebank.com" not in out
    assert "target.com" in out


def test_known_safe_hosts_are_preserved():
    out = redact("http://169.254.169.254/latest/meta-data/")
    assert out is not None
    assert "169.254.169.254" in out


def test_safe_hostnames_survive_normalisation():
    # This one genuinely exercises the SAFE_HOSTS branch: attacker.com is
    # hostname-shaped, so _HOST matches it and the allowlist must spare it.
    out = redact("http://attacker.com/collect")
    assert out is not None
    assert "attacker.com" in out
    assert "target.com" not in out


def test_hostname_normalisation_is_case_insensitive_in_the_scheme():
    # Scheme casing alone must not defeat normalisation — report text
    # contains HTTPS:// and Https:// as often as https://.
    for scheme in ("HTTPS", "Https", "HtTpS", "HTTP"):
        out = redact(f"{scheme}://acmebank.com/path")
        assert out is not None
        assert "acmebank.com" not in out, scheme
        assert "target.com" in out


def test_a_credential_glued_to_adjacent_text_is_still_redacted():
    # Word boundaries fail when a credential abuts other word characters.
    # The entropy backstop is not guaranteed to catch it: low-entropy glue
    # text can pull the combined token under the threshold.
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    out = redact(f"aaaaaaaaaaaa{fake_aws}aaaaaaaaaaaa")
    assert out is not None
    assert fake_aws not in out


def test_sk_prefix_does_not_match_inside_ordinary_words():
    # "desk-", "task-", "kiosk-" must not be mistaken for an API key.
    for word in ("desk", "task", "kiosk", "risk"):
        text = f"{word}-{'a1b2c3d4e5' * 3}"
        out = redact(text)
        assert out is None or "<API_KEY>" not in out, word


def test_sk_key_after_punctuation_is_still_redacted():
    fake = "sk-" + "abcdefghij0123456789klmn"
    out = redact(f"authorization=({fake})")
    assert out is not None
    assert fake not in out
    assert "<API_KEY>" in out


def test_high_entropy_unclassifiable_blob_is_dropped():
    blob = "Zx9Kq2Lm8Rt4Wv7Yb1Nc6Ho3Pj5Sd0Fg" * 4
    assert redact(f"secret={blob}") is None


def test_ordinary_payload_survives_unchanged():
    payload = "{{config.__class__.__init__.__globals__['os'].popen('id').read()}}"
    assert redact(payload) == payload


# --- positional host normalisation -------------------------------------------
#
# Normalising every host to target.com collapsed the victim and the attacker
# into one name, which destroys the payload: an open redirect whose source and
# destination are both target.com demonstrates nothing.


def test_two_distinct_hosts_stay_distinct():
    out = redact("https://acmebank.com/?next=https://attacker-controlled.io/steal")
    assert out is not None
    assert "acmebank.com" not in out
    assert "attacker-controlled.io" not in out
    assert "target.com" in out
    assert "evil.com" in out


def test_the_same_host_twice_maps_to_one_name():
    out = redact("https://acmebank.com/a?next=https://acmebank.com/b")
    assert out is not None
    assert out.count("target.com") == 2
    assert "evil.com" not in out


def test_a_third_host_gets_its_own_name():
    out = redact("https://one.com/?a=https://two.com/&b=https://three.com/")
    assert out is not None
    for name in ("target.com", "evil.com", "evil2.com"):
        assert name in out


def test_safe_hosts_do_not_consume_a_position():
    # evil.com is already meaningful; a victim host beside it must still
    # become target.com rather than being pushed to evil2.com.
    out = redact("https://acmebank.com/?next=https://evil.com/")
    assert out is not None
    assert "target.com" in out
    assert out.count("evil.com") == 1


# --- bare hostnames (no scheme) ----------------------------------------------
#
# Hostnames without http:// escaped normalisation entirely, so a payload like
# "www.[TEAM].slack.com/?redir=..." published the victim verbatim. The risk in
# fixing it is over-matching: payloads are full of hostname-shaped strings that
# are not hosts, and corrupting a payload is worse than leaving a hostname.


def test_a_bare_hostname_is_normalised():
    out = redact("www.acmebank.com/?redir=llink")
    assert out is not None
    assert "acmebank.com" not in out
    assert "target.com" in out


def test_a_protocol_relative_bare_host_is_normalised():
    out = redact("//acmebank.com/callback")
    assert out is not None
    assert "acmebank.com" not in out


def test_bare_and_schemed_forms_of_one_host_agree():
    out = redact("https://acmebank.com/a then acmebank.com/b")
    assert out is not None
    assert out.count("target.com") == 2
    assert "acmebank.com" not in out


def test_file_paths_are_not_mistaken_for_hosts():
    # These are the payloads the fix must not corrupt.
    for payload in (
        "../../../../etc/passwd",
        "/etc/passwd.txt",
        "....//....//boot.ini",
        "%2e%2e%2fwin.ini",
        "/var/www/index.html",
        "shell.php.jpg",
        "../../config.yml",
    ):
        out = redact(payload)
        assert out == payload, payload


def test_code_idioms_are_not_mistaken_for_hosts():
    for payload in (
        "<svg onload=alert(document.domain)>",
        "{{config.__class__.__init__.__globals__}}",
        "javascript:alert(document.cookie)",
        "Object.is(1,1)",
        "version 1.2.3 affected",
    ):
        out = redact(payload)
        assert out == payload, payload


def test_safe_bare_hosts_are_preserved():
    out = redact("Host: metadata.google.internal")
    assert out is not None
    assert "metadata.google.internal" in out


def test_a_host_after_a_template_placeholder_is_normalised():
    # Reports write templated hosts like www.[TEAM].slack.com. The victim is
    # still named, and a preceding "." must not shield it.
    out = redact("www.[TEAM].slack.com/?redir=llink")
    assert out is not None
    assert "slack.com" not in out
    assert "target.com" in out


def test_a_subdomain_is_matched_from_its_leftmost_label():
    out = redact("api.staging.acmebank.com/v1")
    assert out is not None
    assert "acmebank" not in out and "staging" not in out


def test_percent_encoded_content_is_not_corrupted():
    # "%2Fgoogle.co" once matched as a host because "2fgoogle" is a valid
    # label shape, rewriting across the encoding boundary and mangling it.
    payload = "https://acmebank.com/link?url=http%3A%2F%2Fgoogle.co.in"
    out = redact(payload)
    assert out is not None
    assert "%2F%2F" in out
    assert "acmebank.com" not in out


def test_a_compound_tld_is_not_split():
    out = redact("go to example-shop.co.uk/cart")
    assert out is not None
    assert ".co.uk" not in out
    assert "target.com" in out
    assert not out.endswith(".uk")


def test_percent_encoded_hosts_are_normalised():
    # %2F%2Facmebank.com hides the host from the scheme and bare passes, but
    # the hostname itself is not encoded -- so decode to find it, then replace
    # the literal, which cannot corrupt the encoding around it.
    out = redact("https://evil.com/r?url=http%3A%2F%2Facmebank.com%2Fadmin")
    assert out is not None
    assert "acmebank.com" not in out
    assert "%3A%2F%2F" in out          # encoding preserved
    assert "%2Fadmin" in out


def test_decoding_does_not_corrupt_the_surrounding_encoding():
    payload = "http%3A%2F%2Fgoogle.co.in%2Fsearch"
    out = redact(payload)
    assert out is not None
    assert out.count("%2F") == payload.count("%2F")
    assert "google.co.in" not in out


# --- home directory paths -----------------------------------------------------
#
# Researchers' PoC output carries their own usernames -- /Users/bl4de/,
# /home/abenavides/. Public in the source report, but aggregating them into a
# greppable dataset is the same argument that applies to any other identifier.


def test_home_directory_usernames_are_normalised():
    for payload, expected in (
        ("open '/Users/bl4de/package.json'", "open '/Users/user/package.json'"),
        ("file:///home/abenavides/#.js", "file:///home/user/#.js"),
        ('fs.writeFileSync("/home/kali/restricted/../secret.txt")',
         'fs.writeFileSync("/home/user/restricted/../secret.txt")'),
    ):
        assert redact(payload) == expected, payload


def test_system_paths_are_untouched():
    # /etc/passwd and friends are the payload; only a home directory carries a
    # person's name.
    for payload in (
        "../../../../etc/passwd",
        "/var/www/html/index.php",
        "/proc/self/environ",
        "/home/",
        "C:\\Windows\\win.ini",
    ):
        assert redact(payload) == payload, payload
