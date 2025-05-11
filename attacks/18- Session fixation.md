# 🔐 Session Security: Protecting User Identity on the Web

Websites that handle user accounts often create a **session** after a user logs in. This session links the user to their identity for the duration of their interaction with the site.  
The server uses a **session ID**, exchanged with the browser, to track the user's state across HTTP requests.

---

## 🛡️ How to Secure Sessions

### 1. ❌ Never Pass Session IDs in GET or POST Parameters

Avoid using session IDs in:
- URLs (`https://example.com/?sid=abc123`)
- POST form bodies

**Why?**  
Session IDs passed this way can be leaked:
- In the `Referer` header when the user clicks an outbound link
- In browser history and bookmarks
- In web server logs or proxy logs

✅ **Best Practice:** Use **HTTP cookies** to store session IDs.

---

### 2. 🔄 Regenerate Session ID on Login

When a user logs in, **regenerate the session ID** to prevent session fixation.

```php
// In PHP
session_regenerate_id(true);
````

This invalidates any session ID that may have been set before authentication.

---

### 3. ✅ Accept Only Server-Generated Session IDs

Configure your application to reject manually injected session IDs from untrusted sources.  
(Though this alone doesn’t fully prevent session fixation.)

---

### 4. ⏱️ Session Timeout & Rotation

- Set **expiration times** on sessions (e.g., 15-30 minutes of inactivity)
    
- **Periodically regenerate session IDs**, especially during privilege escalation (e.g., after login or role change)
    

---

### 5. 🔚 Implement a Strong Logout Mechanism

Your logout function should:

- Invalidate the session ID on the server
    
- Delete the session cookie from the browser
    

```php
// PHP example
session_unset();
session_destroy();
setcookie("PHPSESSID", "", time() - 3600);
```

---

### 6. 🌐 Detect Suspicious Referrers

Force re-authentication if a session is accessed from an unexpected referrer (e.g., via webmail or unknown third-party).

```js
// JS idea: if document.referrer is not from your domain, trigger logout or warning
if (!document.referrer.includes("yourdomain.com")) {
  window.location.href = "/logout";
}
```

---

## 📋 Summary Checklist

|Action|Purpose|
|---|---|
|Use cookies for session IDs|Prevent leakage via URL or forms|
|Regenerate on login|Prevent session fixation|
|Invalidate old IDs|Reduce session hijack risk|
|Invalidate on logout|Properly end user sessions|
|Monitor referrers|Detect suspicious access|

---

## 🔗 References

- [PHP Manual: `session_regenerate_id()`](https://www.php.net/manual/en/function.session-regenerate-id.php)
    
- [Hacksplaining: Session Fixation](https://hacksplaining.com/prevention/session-fixation)
    
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
    

---

> ✅ Keep session management secure to prevent user impersonation and data theft.
