# 🛂 Access Control: Keeping Users Within Their Limits

Access control enforces the rules that **restrict users** to only the data and actions they’re allowed to access.  
A failure here can lead to:

- 🕵️ Unauthorized data exposure  
- ✏️ Data corruption or deletion  
- 🛠️ Abuse of business functions by unintended users  

> “**Correctly applied access control rules are key to keeping your data secure.**”

---

## 1 | Core Pillars of Access Control 🎯

### 🔑 1. Authentication
*Who are you?*  
Users must be uniquely and securely identified.  
Examples:
- Login via username + password
- OAuth (Google, GitHub, etc.)
- Multi-factor authentication

> 📌 *Image: `auth_vs_authz_chart.png` – Venn diagram showing Authentication ≠ Authorization*

---

### 🧾 2. Authorization
*What are you allowed to do?*

This is where **roles**, **ownership**, and **scopes** come in:

| Term        | Example                             |
|-------------|-------------------------------------|
| **Role**    | `admin`, `editor`, `viewer`         |
| **Ownership** | User A can access their own orders |
| **Scopes**  | API token limited to read-only      |

Granular systems use **access control lists (ACLs)** or **attribute-based access control (ABAC)**.

---

### 🕒 3. Permission Checking
*Is this specific action allowed now?*

This is a **runtime** decision:

- "Can user 42 delete report 379?"
- "Can this token access `/api/v1/payments/export`?"

You should use:
- Decorators (`@requires_admin`)
- Middleware
- Policy engines (e.g., **OPA**, **Casbin**, or **MustBe.js**)

> 📌 *Image: `permission_check_flow.svg` – user → auth → permissions → resource*

---

## 2 | Access Control Failures 🚫

### Examples:

- **[[8-Directory Traversal]]**
  → User accesses `../admin/config.yaml` from a frontend input field.

- **[[5-Cross-Site Request Forgery (CSRF)]]**
  → Malicious site tricks a logged-in user into triggering unwanted actions.

- **Broken Object-Level Authorization (BOLA)**
  → Accessing `/user/123/orders` without being user 123.

> 📌 *Image: `bola_vs_proper_ac.svg` – comparing broken vs proper access control*

---

## 3 | Best Practices 🛡️

✅ **Design early**: Map out who can do what.  
✅ **Centralize rules**: Use a unified permission-checking method (function, API, middleware).  
✅ **Document**: Write down your policy—otherwise “correct” becomes subjective.  
✅ **Test like a hacker**:  
 – Try to bypass roles, access foreign objects, or elevate permissions  
 – Use tools like Postman + Burp Suite  
✅ **Audit + log decisions**: Log every denied access attempt for security reviews.

> 📌 *Image: `access_control_design_doc.png` – visual of role → permission matrix*

---

## 4 | Recommended Tools & Libraries 🧰

| Tool | Use |
|------|-----|
| [MustBe.js](https://github.com/derickbailey/mustbe) | Routing-based access control for Node.js |
| [ACL](https://www.npmjs.com/package/acl) | Role- and resource-based permission rules |
| [Casbin](https://casbin.org/) | Cross-language, attribute-based access engine |
| [OPA](https://www.openpolicyagent.org/) | Policy-as-code for microservices & APIs |

---

## 5 | Additional Resources 📚

- [🔗 OWASP: Testing for Authorization](https://wiki.owasp.org/index.php/Testing_for_Authorization)
- [🔗 Purdue Lecture Notes on Access Control](https://www.cs.purdue.edu/homes/ninghui/courses/426_Fall10/handouts/426_Fall10_lect09.pdf)
- [🔗 OWASP Top 10: Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

---

## 6 | Key Takeaway

> *“Access control is not just about protecting secrets—it’s about ensuring every user only does what they’re supposed to.”*

---

*Last updated: 2025-4
