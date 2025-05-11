# 🌊 CSRF – Cross-Site Request Forgery

> A CSRF attack tricks the browser into **sending unwanted requests** on behalf of a logged-in user.  
> It uses the **user’s own session and cookies** to perform actions they never intended.

---

## 1 | How CSRF Works 🕵️

A malicious website (attacker.com) silently sends a forged request to your site (e.g., `bank.com/transfer?amount=1000`).  
Because the browser **automatically sends session cookies**, the request **looks valid** to your server.

📌 *Image: `csrf_attack_flow.svg` – attacker.com → victim browser → bank.com*

---

## 2 | What Can Be Exploited?

- 🚀 **POST actions** (like money transfers, deletions)
- 🪱 **Worms**: Self-replicating CSRF exploits (e.g., auto-comment or auto-like spam on social media)
- ⚠️ **Admin actions**: Changing email/password, adding users

**Anything your app allows the user to do, CSRF can trigger if not protected.**

---

## 3 | Key Defenses Against CSRF 🔐

### ✅ 1. Only Use GET for Read-Only Actions

Follow **REST principles**:
- ✅ `GET /profile` → fetch data  
- ❌ `GET /delete-user` → dangerous!  
Use `POST`, `DELETE`, `PUT`, `PATCH` for any operation that changes data.

---

### ✅ 2. Use Anti-Forgery Tokens

Send a **secret, unique token** in every form or request:

```html
<form method="POST" action="/update">
  <input type="hidden" name="csrf_token" value="abc123xyz456">
  <input type="text" name="email">
</form>
````

🔒 The server validates this token on form submission.  
Reject requests if the token is **missing, expired, or invalid**.

📌 _Image: `csrf_token_flow.svg` – form + token → POST → token check_

---

### ✅ 3. Set SameSite Cookie Attribute

Prevent cookies from being sent on cross-origin requests:

```http
Set-Cookie: sessionid=abc123; HttpOnly; Secure; SameSite=Strict
```

|Value|Meaning|
|---|---|
|`Lax`|Allows safe top-level GETs only|
|`Strict`|Blocks all cross-origin cookies|
|`None`|Allows cross-origin use, must be Secure|

📌 _Image: `samesite_matrix.png` – table comparing Strict, Lax, None_

---

## 4 | Framework Support 🔧

### ⚙️ Express (Node.js)

Use [`csurf`](https://github.com/expressjs/csurf):

```js
const csrf = require('csurf');
app.use(csrf());
```

Each request gets a token you can include in forms or AJAX headers.

---

### 🐘 PHP

Check out:

- [OWASP PHP CSRF Guard](https://wiki.owasp.org/index.php/PHP_CSRF_Guard)
    
- Use `session_start()` and store your CSRF token in `$_SESSION`
    

Example:

```php
<input type="hidden" name="csrf_token" value="<?php echo $_SESSION['csrf_token']; ?>">
```

---

## 5 | Summary Checklist ✅

|Check|Best Practice|
|---|---|
|✅|Use POST/PUT/DELETE for side-effectful actions|
|✅|Embed a **per-session CSRF token** in every form|
|✅|Validate token server-side|
|✅|Add `SameSite=Strict` on cookies|
|✅|Never trust requests from 3rd-party origins|

---

## 6 | Bonus Tip: Detect & Monitor CSRF Attempts

- Log requests with **missing or invalid CSRF tokens**
    
- Look for **high-frequency POSTs from unusual referrers**
    
- Consider alerting on these patterns
    

---

## 7 | Learn More 🔎

- 🛡️ [Hacksplaining CSRF Demo](https://hacksplaining.com/exercises/csrf)
    
- 📘 [OWASP CSRF Guide](https://owasp.org/www-community/attacks/csrf)
    
- 🔧 [ExpressJS csurf Middleware](https://github.com/expressjs/csurf)
    
- 🐘 [PHP CSRF Guard](https://wiki.owasp.org/index.php/PHP_CSRF_Guard)
    

---

## 8 | Key Takeaway

> “**If your user can do it, a CSRF attack can fake it.**  
> Tokens, SameSite cookies, and RESTful verbs help keep you safe.”

---

