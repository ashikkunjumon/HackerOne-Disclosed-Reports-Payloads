# Ian Dunn

2 payloads.

### `8001d319`

```
<script>alert('XSS');</script>
```

— [Stored XSS from ticket messages in admin table in SupportFlow](https://hackerone.com/reports/145091) · Ian Dunn · [whitehatter](https://hackerone.com/whitehatter) · $50.0

### `b61c000f`

```
https://target.com/wordpress/wp-login.php?redirect_to=https%3A%2F%2Ftarget.com%2Fwordpress%2Fwp-admin%2F&reauth=1
```

**Parameter:** `redirect_to`
— [Potential Open-Redirection](https://hackerone.com/reports/765227) · Ian Dunn · [damn007](https://hackerone.com/damn007)
