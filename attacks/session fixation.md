Websites with user accounts typically implement an authentication mechanism to identify returning users.Post-authentication, a **session** will often be established. The server and browser will exchange a **session ID** so the server knows which user the browser is representing with each HTTP request.

## Protection

#### Don't Pass Session IDs in GET/POST Variables

Passing session IDs in [query strings](https://hacksplaining.com/glossary/urls), or in the body of [POST requests](https://hacksplaining.com/glossary/http#http-methods), is problematic. Not only does it make crafting of malicious URLs possible, but session IDs can be leaked in the following ways:

- If the user follows an out-bound link (the `Referer` header will describe where the user browsed from).
- In the browser history and in bookmarks.
- In logs on your web server, and any proxy servers.

Session IDs are better passed in [HTTP cookies](https://hacksplaining.com/glossary/cookies). See the [code samples](https://hacksplaining.com/prevention/session-fixation#code-samples) below for examples of how to do this.

for examples of how to do this.

#### Regenerate the Session ID at Authentication

Session fixation attacks can be defeated by simply regenerating the session ID when the user logs in.

#### Accept Only Server-Generated Session IDs

It is a good practice to ensure that only server-generated session IDs are accepted by your web server. (On its own, this won't resolve session fixation vulnerabilities, though. A hacker can easily get a new server-generated ID and pass it onto a victim in a crafted URL.)


#### Timeout and Replace Old Session IDs

Periodically replace session IDs as a second layer of defense, should they get leaked.

#### Implement a Strong Logout Function

The logout function on your website should mark session IDs as obsolete. (You do have a logout function, right?)

#### Require a New Session When Visiting From Suspicious Referrers

Consider forcing your users to login again, if they visit your site from a separate website (e.g. web-mail).

PHP:
Sessions are tracked with cookies in PHP. Force generation of a new session ID using [](https://php.net/manual/en/function.session-regenerate-id.php)`session_regenerate_id(true)`.