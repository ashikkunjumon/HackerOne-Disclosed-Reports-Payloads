# HackerOne Disclosed Reports Payloads

**Real bug bounty payloads extracted from disclosed HackerOne reports — every
one of them worked on a live production target.**

A searchable payload list for XSS, SQL injection, SSRF, path traversal, SSTI,
XXE, open redirect, CSRF, IDOR and RCE, drawn from 1,015 disclosed
HackerOne reports. Every payload links back to the report it came from and the
researcher who found it.

## 📊 Statistics

| Metric | Count |
|---|---|
| **Total Payloads** | 1,601 |
| **Classes Covered** | 10 |
| **Programs Represented** | 152 |
| **Bounty Behind Them** | $440,965 |

*Last Updated: August 17, 2026 at 16:07 UTC*

## Payloads by vulnerability class

| Class | Payloads |
|---|---|
| [Open Redirect](payloads/open-redirect.md) | 139 |
| [Cross-site Scripting](payloads/xss.md) | 803 |
| [Server-Side Request Forgery](payloads/ssrf.md) | 150 |
| [SQL Injection](payloads/sqli.md) | 134 |
| [Server-Side Template Injection](payloads/ssti.md) | 30 |
| [Path Traversal](payloads/path-traversal.md) | 184 |
| [XML External Entities](payloads/xxe.md) | 21 |
| [Cross-Site Request Forgery](payloads/csrf.md) | 44 |
| [Insecure Direct Object Reference](payloads/idor.md) | 24 |
| [Remote Code Execution](payloads/rce.md) | 72 |

Each page groups payloads by technique variant, so the `svg onload` cases sit
together rather than scattered through a flat list.

## Wordlists for ffuf, Burp Intruder and sqlmap

[`wordlists/`](wordlists/) holds one plain-text file per class — deduplicated
raw payload strings, one per line, no markdown and no commentary. Load them
directly with `ffuf -w`, paste into Burp Intruder, or feed to any fuzzer that
takes a wordlist.

## How this differs from a generic payload list

Collections like PayloadsAllTheThings are curated lists of payloads that
*should* work. Every entry here is one that **did** — it appears in a public
HackerOne report, used against a real production target and accepted as a valid
finding. 277 of them also earned a bounty, totalling
$440,965. The report link is on every entry, so you can read the
context a payload was used in rather than guessing at it.

## Browse

| Category | Description |
|---|---|
| [By Program](by-program/) | Payloads that worked, per bug bounty program |
| [Top Payloads](top-payloads/) | Ranked by bounty paid |
| [Wordlists](wordlists/) | Raw strings, one per line, tool-ready |

## Data files

- `payloads.json` — structured record per payload, with full provenance
- `payloads.txt` — flat payload + report URL list (single-line payloads only;
  multi-line payloads are in `payloads.json` and `payloads/` instead)
- `payloads/` — one page per vulnerability class, grouped by technique
- `wordlists/` — deduplicated raw strings for ffuf, Burp Intruder and friends
  (single-line payloads only, so every line loads as one entry)

## How the data is built

Rebuilt daily from the public archive of disclosed HackerOne reports. Payloads
are extracted deterministically, then filtered so that vulnerable source code,
log lines and reference links do not end up in the dataset. Victim hostnames
are normalised — `target.com` is where a payload starts, `evil.com` is where it
sends you — and anything credential-shaped is dropped rather than published.

## Related projects

- [Self-Hosted Bug Bounty & Disclosure Programs](https://github.com/ashikkunjumon/Self-Hosted-Bug-Bounty-Programs)
  — 7,500+ vulnerability disclosure and bug bounty programs, indexed by country
- [Bug Bounty Dorks Automation](https://github.com/ashikkunjumon/Bug-Bounty-Dorks-Automation)
  — search-engine dorks for recon and for finding programs to test
