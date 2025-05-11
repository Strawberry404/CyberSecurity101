**Buy a certificate, install it, and configure your web server to use it.**

It's really as simple as that. Web servers are typically able to serve the same content over HTTP (on port 80) and HTTPS (on port 443). Any non-trivial website should use HTTPS.

**But make sure you know how to force your web server to elevate to a secure connection, and do so whenever a user is authenticating or establishing a session.** A common way of enforcing this is to make sure that cookies are set to `secure` -- that way, sessions can _only_ be established over HTTPS.
## Let's Encrypt

If you are looking to add or renew a security certificate, [Let's Encrypt](https://letsencrypt.org/) is a quick and easy way to install one. The project - sponsored by Mozilla, Facebook, and the Electronic Frontier Foundation - aims to make encryption ubiquitous across the web by eliminating payment, web  
server configuration and certificate renewal tasks. We highly recommend you take a look!

The code samples below illustrate how to elevate traffic to an HTTPS connection in various set-ups.

### Reverse Proxies

It is fairly common to put **Apache** or **Nginx** between your web server and the outside world. If you have this setup, it is very easy to redirect HTTP requests to use HTTPS.  


The equivalent in Nginx is:

```nginx
server {
  listen 80;
  rewrite ^(.*) https://$host$1 permanent;
}
```