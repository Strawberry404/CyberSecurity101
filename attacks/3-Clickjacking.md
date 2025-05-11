Here is a **clean and structured Markdown page** for your Streamlit project: `clickjacking.md`. It introduces **Clickjacking**, explains how attackers exploit it, gives real-life examples, and outlines concrete protections you can implement as a developer.

---

# 🖱️ Clickjacking: When Your Clicks Are Hijacked

Clickjacking is a deceptive technique where an attacker **tricks users into clicking something different from what they perceive**, typically by overlaying invisible UI elements over legitimate pages.

> ⚠️ *What you see ≠ what you click.*

---

## 1 | Real-World Examples 👀

| Scenario | What Happens |
|----------|--------------|
| **Fake login overlay** | The attacker loads a fake login box over the real one to **harvest credentials**. |
| **Invisible iframe on “allow webcam” dialog** | A user thinks they’re closing a popup but ends up **enabling mic/cam access**. |
| **Scam offers** | Users are tricked into clicking “claim prize” buttons that lead to **malicious redirects**. |
| **Social worms** | Users unintentionally click “share” on infected social media posts. |

> **Example:**  
> `genuislab.com` (normal) vs `genui𝖘Iab.com` (with Unicode + capital I's)  
> They **look identical**, but one leads to a **malicious page**.

📌 *Image: `clickjack_overlay_demo.png` – showing transparent iframe above a legitimate button*

---

## 2 | Why It’s Dangerous 🔓

Clickjacking attacks often:

- Steal passwords or tokens via **fake login forms**
- Trigger **dangerous actions** (delete, approve, transfer) behind the scenes
- Enable **device access** like webcam/microphone
- Trick users into **downloading malware**

It’s often hard to detect unless you inspect the page’s actual structure.

---

## 3 | Key Protections 🔐

### 🧱 Content Security Policy (CSP)

Control which domains can embed your content in iframes.

```http
Content-Security-Policy: frame-ancestors 'none';
````

|Directive|Behavior|
|---|---|
|`'none'`|Prevents embedding by any domain|
|`'self'`|Only your own domain can embed it|
|specific URI|Allow only `https://trusted.example.com`|

> 📌 _Image: `csp_directives_chart.png` – visual matrix of CSP rules_

---

### 🧰 X-Frame-Options Header (Legacy)

```http
X-Frame-Options: DENY
```

|Value|Meaning|
|---|---|
|`DENY`|Block framing from **any** domain|
|`SAMEORIGIN`|Allow only **same origin**|
|`ALLOW-FROM uri`|Allow a **specific origin** (not widely supported)|

> ✅ Works on older browsers; modern setups should **use CSP** instead.

---

### 💣 Frame-Killing Script (Legacy JS)

For old browsers lacking CSP/X-Frame support:

```html
<style>
  html { display: none; }
</style>
<script>
  if (self === top) {
    document.documentElement.style.display = 'block';
  } else {
    top.location = self.location;
  }
</script>
```

This forces your site to **break out of iframes** unless it's top-level.

> 📌 _Image: `frame_killer_explained.svg` – flow of JS protecting iframe_

---

## 4 | Implementation Strategy 🧩

1. **Set CSP headers** to deny all unauthorized framing:
    http
    Content-Security-Policy: frame-ancestors 'none';
2. Add `X-Frame-Options: DENY` as a fallback for legacy browsers.
    
3. If required to embed (e.g., dashboards):
    
    - Allowlist specific domains with `'frame-ancestors https://trusted.example.com'`
        
4. Optionally, add **frame-killing JS** for extra protection in older environments.
    
5. Periodically **audit** for unexpected embeddings using browser dev tools or services like [iframe-checker](https://www.tunetheweb.com/tools/test-your-site/clickjacking/)
    

---

## 5 | Additional Resources 🔍

- 📄 [Stanford “Framebusting” Paper (PDF)](https://crypto.stanford.edu/~dabo/pubs/papers/framebust.pdf)
    
- 🔗 [OWASP Clickjacking Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)
    
- 🛡️ [Hacksplaining: Clickjacking](https://www.hacksplaining.com/prevention/clickjacking)
    

---

## 6 | Key Takeaway

> “Clickjacking is **invisible until it isn’t**—protect your users by locking down how and where your app can be embedded.”

---

Last updated: 28/05/2025
