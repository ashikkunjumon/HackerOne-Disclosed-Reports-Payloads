# HackerOne Disclosed Reports Payloads

Real payloads from disclosed HackerOne reports — every one of them worked.

## 📊 Statistics

| Metric | Count |
|---|---|
| **Total Payloads** | 1,598 |
| **Classes Covered** | 10 |
| **Programs Represented** | 152 |
| **Bounty Behind Them** | $440,965.0 |

*Last Updated: August 15, 2026 at 19:40 UTC*

## 📁 Browse

| Class | Payloads |
|---|---|
| [Open Redirect](payloads/open-redirect.md) | 139 |
| [Cross-site Scripting](payloads/xss.md) | 803 |
| [Server-Side Request Forgery](payloads/ssrf.md) | 147 |
| [SQL Injection](payloads/sqli.md) | 134 |
| [Server-Side Template Injection](payloads/ssti.md) | 30 |
| [Path Traversal](payloads/path-traversal.md) | 184 |
| [XML External Entities](payloads/xxe.md) | 21 |
| [Cross-Site Request Forgery](payloads/csrf.md) | 44 |
| [Insecure Direct Object Reference](payloads/idor.md) | 24 |
| [Remote Code Execution](payloads/rce.md) | 72 |

| Category | Description |
|---|---|
| [By Program](by-program/) | Payloads that worked, per program |
| [Top Payloads](top-payloads/) | Ranked by bounty |
| [Wordlists](wordlists/) | Raw strings, one per line, tool-ready |

## 📄 Data

- `payloads.json` — structured record per payload, with full provenance
- `payloads.txt` — flat payload + report URL list (single-line payloads only;
  multi-line payloads are in `payloads.json` and `payloads/` instead)
- `payloads/` — one page per vulnerability class, grouped by technique
- `wordlists/` — deduplicated raw strings for ffuf, Burp Intruder and friends
  (single-line payloads only, so every line loads as one entry)

Every payload links back to the disclosed report it came from and the
researcher who found it.
