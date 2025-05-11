Coomon - easy - harmfull 

| when there's input there's cross site scripting 

- **Spreading [worms](https://hacksplaining.com/glossary/worms) on social media sites.** Facebook, Twitter and YouTube have all been successfully attacked in this way.
- **Session hijacking.** Malicious JavaScript may be able to send the session ID to a remote site under the hacker's control, allowing the hacker to impersonate that user by hijacking a session in progress.
- **Identity theft**. If the user enters confidential information such as credit card numbers into a compromised website, these details can be stolen using malicious JavaScript. 

solution : 
Escaping editable content in this way means it will never be treated as executable code by the browser. This closes the door on most XSS attacks.


Escaping editable content in this way means it will never be treated as executable code by the browser. This closes the door on most XSS attacks.

#### Allowlist Values

If a particular dynamic data item can only take a handful of valid values, the best practice is to restrict the values in the data store, and have your rendering logic only permit known good values. For instance, instead of asking a user to type in their country of residence, have them select from a drop-down list.
#### Implement a Content-Security Policy

Browsers support [Content-Security Policies](https://www.html5rocks.com/en/tutorials/security/content-security-policy/) that allow the author of a web-page to control where JavaScript (and other resources) can be loaded and executed from. XSS attacks rely on the attacker being able to run malicious scripts on a user's web page - either by injecting inline `<script>` tags somewhere within the `<html>` tag of a page, or by tricking the browser into loading the JavaScript from a malicious third-party domain.

By setting a content security policy in the response header, you can tell the browser to _never_ execute inline JavaScript, and to lock down which domains can host JavaScript for a page:

```
Content-Security-Policy: script-src 'self' https://apis.google.com
```

**By listing the URIs from which scripts can be loaded, you are implicitly stating that inline JavaScript is not allowed.**

Inline scripts tags are considered bad practice in modern web-development - mixing content and code makes web-applications difficult to maintain - but are common in older, legacy sites

[[Permission Policy header]]
[[CSP Violation Reports]]
these help with CSS (not styling lol )

#### Sanitize HTML

Some sites have a legitimate need to store and render raw HTML. If your site stores and renders rich content, you need to use a HTML sanitization library to ensure malicious users cannot inject scripts in their HTML submissions.



### PHP

The [`echo`](https://www.php.net/manual/en/function.echo.php) command **does not** escape HTML by default, which means that any code like the following, which pulls data directly out of the HTTP request, is vulnerable to XSS attacks:

```
<?php
  echo $_POST["comment"];
?>
```

Be sure to use the [`strip_tags`](https://www.php.net/strip_tags) function or the [`htmlspecialchars`](https://www.php.net/htmlspecialchars) function to safely escape parameters:

```
<?php
  echo strip_tags($_POST["comment"]);
?>
```


security tests are needed within the code to check for these types of vulnerabilities specially in blocks where there's input to be integrated 

### another add up 
### Http-only cookie

meaning that cookies will be received, stored, and sent by the browser, but cannot be modified or read by JavaScript.

with a bit of wikipedia : 

An _http-only cookie_ cannot be accessed by client-side APIs, such as [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript"). This restriction eliminates the threat of cookie theft via [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting "Cross-site scripting") (XSS).[[23]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-23) However, the cookie remains vulnerable to [cross-site tracing](https://en.wikipedia.org/wiki/Cross-site_tracing "Cross-site tracing") (XST) and [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery "Cross-site request forgery") (CSRF) attacks. A cookie is given this characteristic by adding the `HttpOnly` flag to the cookie.

links to implement further :
https://www.acunetix.com/websitesecurity/cross-site-scripting/?utm_source=hacksplaining&utm_medium=post&utm_campaign=articlelink