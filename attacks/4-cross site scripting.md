# 🧨 Cross-Site Scripting (XSS): When Inputs Turn into Attacks

> “**Where there is input, there is XSS.**”

Cross-Site Scripting (XSS) is a common and dangerous web vulnerability where attackers inject **malicious scripts** into trusted websites. These scripts run in the user’s browser and can hijack sessions, steal data, or alter page behavior without user consent.

---

## 1 | Why XSS Is Dangerous ⚠️

Attackers exploit **unescaped or unsanitized input** to execute JavaScript in a victim’s browser.

### Real-World Impacts:

- **🪱 Spread worms** on platforms like Facebook, Twitter, and YouTube  
- **🔓 Hijack sessions** by stealing cookies or tokens  
- **🎭 Identity theft** by spoofing login forms or stealing entered data  
- **📥 Install malware** or redirect users to harmful downloads  
- **🎥 Access devices** (cam/mic) via overlay tricks

📌 *Image: `xss_attack_flow.svg` – input → render → execute JS*

---

## 2 | XSS Attack Example 🧪

```php
<!-- Vulnerable PHP snippet -->
<?php
  echo $_POST["comment"];
?>
````

**What happens:**  
If someone submits `<script>alert('Hacked!')</script>`, that script runs for every visitor.

---

## 3 | Key Prevention Techniques 🔐

### ✅ Escape Output (everywhere)

Use escaping functions to **prevent code from executing**:

```php
<?php
  echo htmlspecialchars($_POST["comment"]);
?>
```

✅ Also valid:

- `strip_tags()` → removes all HTML tags
    
- `htmlspecialchars()` → encodes HTML chars like `<`, `>` into safe entities
    

📌 _Image: `php_escape_functions.png` – visual comparison of outputs_

---

### ✅ Sanitize Rich HTML

If your app allows rich text (e.g., blog posts, forums):

- Use a **server-side HTML sanitization library**:
    
    - PHP: `HTMLPurifier`
        
    - JavaScript: `DOMPurify`
        
- Only allow tags/attributes you trust
    

---

### ✅ Use Allowlists

Whenever possible, **avoid free-text inputs** for predictable values.

**Example:** Instead of:

```html
<input type="text" name="country">
```

Use:

```html
<select name="country">
  <option>Morocco</option>
  <option>France</option>
  <option>USA</option>
</select>
```

---

### ✅ Implement a Content Security Policy (CSP)

Restrict what JavaScript is allowed to load and execute:

```http
Content-Security-Policy: script-src 'self' https://apis.google.com
```

|Benefit|Outcome|
|---|---|
|Blocks inline `<script>`|Safer rendering|
|Only allows trusted domains|No 3rd-party injection|

📌 _Image: `csp_block_inline.png` – blocked inline script error in console_

---

### ✅ Set HttpOnly Cookies

Set authentication cookies with the `HttpOnly` flag:

```http
Set-Cookie: sessionid=abc123; HttpOnly; Secure
```

- 🔒 Prevents **JavaScript access** to cookies
    
- Protects against XSS stealing session tokens
    

📌 _Image: `cookie_http_only_flag.png` – DevTools showing HttpOnly attribute_

---

## 4 | Security Tips for Developers 💻

- Test all user-input fields for XSS vectors (`<img src=x onerror=alert(1)>`)
    
- Escape **before render**, not after
    
- NEVER trust input from:
    
    - Forms
        
    - URL parameters
        
    - Cookies
        
    - Hidden fields
        
- Use a **WAF** (Web App Firewall) to catch known payloads
    

---

## 5 | Quick Reference Table 🧭

|Threat|Fix|
|---|---|
|Unescaped output|`htmlspecialchars()` or equivalent|
|Rich content|Use an allowlist + sanitizer|
|Inline `<script>`|Disallow via CSP|
|Cookie theft|Use `HttpOnly` cookies|
|JS in attributes|Disallow user control of attributes like `onerror`, `onclick`|

---

## 6 | Further Reading & Tools 🛠️

- 📚 [OWASP XSS Guide](https://owasp.org/www-community/xss)
    
- 🔎 [XSS Testing Tool](https://www.acunetix.com/websitesecurity/cross-site-scripting/?utm_source=hacksplaining&utm_medium=post&utm_campaign=articlelink)
    
- 🔗 [Content Security Policy Tutorial](https://www.html5rocks.com/en/tutorials/security/content-security-policy/)
    
- 🛡️ [Hacksplaining: XSS](https://www.hacksplaining.com/prevention/cross-site-scripting)
    

---

## 7 | Summary

> XSS is easy to introduce and hard to detect.  
> Secure input → escape output → sanitize HTML → set headers → test everything.

---
