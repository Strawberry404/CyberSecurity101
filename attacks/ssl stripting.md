**SSL stripping is where an attacker intercepts and downgrades a secure HTTPS connection to an unsecured HTTP connection, allowing them to read, intercept and manipulate sensitive traffic exchanged between a user and a website.**

It is a type of **Monster-in-the-Middle Attack** where the attacker prevents tricks the user agent into sending credentials over an insecure connection, while acting as a proxy to the webserver that upgrades the traffic to a secure connection. As a result upstream servers are unable to detect the attack.


You should tell the browser to always connect using HTTPS by implementing HTTP Strict Transport Security (HSTS). This is done by adding an HTTP response header:

```
Strict-Transport-Security "max-age=31536000";
```

#### Nginx

If you use Nginx as your web server, a secure configuration to add HSTS to your response will look like this:

```
server {
  listen 80;
  server_name example.com;

  # Redirect HTTP traffic to HTTPS
  return 301 https://$server_name$request_uri; 
}
  
server {
  listen 443 ssl; server_name example.com;

  # Uses the following certificate to encrypt traffic, 
  # and the paired private key to decrypt it.
  ssl_certificate /path/to/ssl/certificate.crt;  
  ssl_certificate_key /path/to/ssl/private.key;

  # Enable HSTS with a max-age of 1 year (31536000 seconds).
  add_header Strict-Transport-Security "max-age=31536000";

  # Ensures the use of a minimally strong version of TLS 
  ssl_protocols TLSv1.3; 
}
```



[](https://security.stackexchange.com/posts/272356/timeline)


The goal of the SSLstrip attack is to prevent the client from switching from http to https. Historically on the web there were two main ways the website(s) could cause the user to switch from http to https.

1. Links included in pages can use https urls.
2. The server can respond to a http request with a redirect to a https url.

The attacker prevents item 1 by rewriting page content, they prevent item 2 by requesting pages from the server over https while serving them to the client over http.
cute links :
https://github.com/moxie0/sslstrip
https://github.com/moxie0/sslstrip