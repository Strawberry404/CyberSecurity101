[![How to install and configure Free Domain SSL Certificate Using Lets Encrypt](https://tse1.mm.bing.net/th?id=OIP.oTcubQMYf194lsryuTff9AHaEK&pid=Api)](https://devopsideas.com/free-domain-ssl-certificate-using-lets-encrypt/)

To secure your website with HTTPS, follow these steps:

---

## 🔐 1. Obtain an SSL/TLS Certificate

Use **Let's Encrypt** to get a free, automated SSL/TLS certificate. It simplifies the process of securing your site with HTTPS.

### Steps:

1. **Install Certbot**: Certbot is a tool that automates the process of obtaining and renewing Let's Encrypt certificates.([Wikipédia](https://de.wikipedia.org/wiki/Let%E2%80%99s_Encrypt?utm_source=chatgpt.com "Let’s Encrypt"))
    
    ```bash
    sudo apt update
    sudo apt install certbot python3-certbot-nginx
    ```
    
2. **Obtain and Install Certificate**: Run Certbot to obtain and install the certificate for Nginx:
    
    ```bash
    sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
    ```
    
    This command will automatically configure Nginx to use the obtained certificate.
    
3. **Automate Renewal**: Set up a cron job to renew the certificate automatically:
    
    ```bash
    echo "0 0 * * * /usr/bin/certbot renew --quiet" | sudo tee -a /etc/crontab > /dev/null
    ```
    
    This schedules the renewal to run daily at midnight.
    

---

## 🔁 2. Redirect HTTP to HTTPS

Ensure that all HTTP traffic is redirected to HTTPS to enforce secure connections.

### Nginx Configuration:

Add the following server block to your Nginx configuration:([phoenixNAP | Global IT Services](https://phoenixnap.com/kb/redirect-http-to-https-nginx?utm_source=chatgpt.com "How to Redirect HTTP to HTTPS in Nginx | phoenixNAP KB"))

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}
```

This configuration listens on port 80 and redirects all requests to the corresponding HTTPS URL.

---

## 🛡️ 3. Implement HTTP Strict Transport Security (HSTS)

HSTS instructs browsers to always use HTTPS when communicating with your site, preventing protocol downgrade attacks.

### Nginx Configuration:

Within your HTTPS server block, add the following line:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
```

- `max-age=31536000`: Enforces HTTPS for one year.
    
- `includeSubDomains`: Applies the rule to all subdomains.
    
- `preload`: Allows your domain to be included in browsers' HSTS preload lists.([Wikipédia](https://fr.wikipedia.org/wiki/HTTP_Strict_Transport_Security?utm_source=chatgpt.com "HTTP Strict Transport Security"))
    

---

## 🍪 4. Secure Cookies

Ensure that session cookies are transmitted securely.

### Nginx Configuration:

Add the following line within your HTTPS server block:([phoenixNAP | Global IT Services](https://phoenixnap.com/kb/redirect-http-to-https-nginx?utm_source=chatgpt.com "How to Redirect HTTP to HTTPS in Nginx | phoenixNAP KB"))

```nginx
proxy_cookie_path / "/; Secure; HttpOnly; SameSite=Strict";
```

- `Secure`: Ensures cookies are sent over HTTPS only.
    
- `HttpOnly`: Prevents JavaScript from accessing the cookies.
    
- `SameSite=Strict`: Restricts cookies from being sent with cross-site requests.([support.inspire-tech.com](https://support.inspire-tech.com/hc/en-us/articles/115000116642-How-to-configure-a-SECURE-Flag-for-Cookies?utm_source=chatgpt.com "How to configure a SECURE Flag for Cookies? – Inspire-Tech Customer Support"))
    

---

## ✅ 5. Test Your Configuration

After completing the setup, test your site's SSL configuration using tools like [SSL Labs' SSL Test](https://www.ssllabs.com/ssltest/). This will help identify potential vulnerabilities and ensure that your SSL/TLS setup is correctly configured.([ownCloud Documentation](https://doc.owncloud.com/server/next/admin_manual/installation/letsencrypt/using_letsencrypt.html?utm_source=chatgpt.com "Using Let's Encrypt SSL Certificates"))

---

By following these steps, you can effectively secure your website with HTTPS, ensuring encrypted communication and enhanced security for your users.