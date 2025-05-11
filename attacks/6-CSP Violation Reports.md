[![Content Security Policy (CSP): Everything You Should Know](https://tse4.mm.bing.net/th?id=OIP.st1CsoIyLH1ewZDGxDGRwQHaFD&pid=Api)](https://www.akshaykhot.com/content-security-policy/)

To enhance your web application's security, implementing both **Content Security Policy (CSP)** and **Permissions Policy** headers is crucial. Here's an overview of each and how they can be applied:

---

### 🛡️ Content Security Policy (CSP)

CSP is a security standard that helps prevent cross-site scripting (XSS), clickjacking, and other code injection attacks by specifying which dynamic resources are allowed to load. It enables you to control the sources from which content like scripts, styles, and images can be loaded.([Wikipédia](https://en.wikipedia.org/wiki/Content_Security_Policy?utm_source=chatgpt.com "Content Security Policy"))

**Example CSP Header:**

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://apis.example.com; object-src 'none'; frame-ancestors 'none';
```

**Key Directives:**

- `default-src`: Sets the default policy for fetching resources such as JavaScript, Images, CSS, Fonts, AJAX requests, Frames, HTML5 Media.
    
- `script-src`: Specifies valid sources for JavaScript.
    
- `object-src`: Specifies valid sources for the `<object>`, `<embed>`, and `<applet>` elements.
    
- `frame-ancestors`: Specifies valid parents that may embed a page using `<frame>`, `<iframe>`, `<object>`, `<embed>`, or `<applet>`.([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src?utm_source=chatgpt.com "CSP: script-src - HTTP - MDN Web Docs - Mozilla"), [Genesys Cloud Developer Center](https://developer.genesys.cloud/forum/t/embedded-client-apps-adding-support-for-configurable-permissionspolicy/12672?utm_source=chatgpt.com "Adding support for configurable PermissionsPolicy - Announcements"))
    

**Benefits:**

- Mitigates XSS attacks by restricting the sources of executable scripts.
    
- Prevents clickjacking by controlling frame embedding.
    
- Enforces HTTPS to ensure secure data transmission.
    

**Implementation Tips:**

- Start with a **report-only** mode to monitor violations without enforcing the policy:
    
    Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report-endpoint/;

- Gradually tighten the policy based on the reports received.
    

For detailed guidance, refer to the [MDN Web Docs on CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP).

---

### 🔒 Permissions Policy

Formerly known as Feature Policy, Permissions Policy allows you to enable or disable the use of certain browser features and APIs in the web application or its iframes.([Chrome for Developers](https://developer.chrome.com/docs/privacy-security/permissions-policy?utm_source=chatgpt.com "Control browser features with Permissions Policy | Privacy & Security"))

**Example Permissions Policy Header:**

```http
Permissions-Policy: geolocation=(self), microphone=(), camera=()
```

**Common Directives:**

- `geolocation`: Controls access to the Geolocation API.
    
- `microphone`: Controls access to the Microphone.
    
- `camera`: Controls access to the Camera.
    
- `fullscreen`: Controls access to the Fullscreen API.
    
- `payment`: Controls access to the Payment Request API.([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy/geolocation?utm_source=chatgpt.com "Permissions-Policy: geolocation - HTTP - MDN Web Docs"), [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Permissions_Policy?utm_source=chatgpt.com "Permissions Policy - HTTP - MDN Web Docs"))
    

**Benefits:**

- Enhances privacy by restricting access to sensitive APIs.
    
- Improves security by limiting the potential attack surface.
    
- Provides better control over third-party content embedded via iframes.
    

**Implementation Tips:**

- Define policies based on the principle of least privilege—only allow features that are necessary.
    
- Regularly review and update the policy as the application evolves.
    

For more information, consult the [MDN Web Docs on Permissions Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy).([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy?utm_source=chatgpt.com "Permissions-Policy - HTTP - MDN Web Docs - Mozilla"))
