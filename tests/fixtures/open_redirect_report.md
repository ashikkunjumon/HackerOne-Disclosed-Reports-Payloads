# Open redirect in /auth/callback

## Summary

The `next` parameter is validated with a naive prefix check.

### Steps to reproduce

1. Visit the following URL:

```
https://target.com/auth/callback?next=//evil.com
```

2. Observe the 302 to `//evil.com`.

The following also work:

```
https://target.com/auth/callback?next=/\/evil.com
https://target.com/auth/callback?next=https://target.com@evil.com
```

### Vulnerable code

```python
def is_safe(url):
    return url.startswith("/")
```

### Server log

```
127.0.0.1 - - [01/Jan/2020] "GET /auth/callback?next=//evil.com HTTP/1.1" 302 -
```

### Reference

See https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
