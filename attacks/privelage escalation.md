**Privilege escalation vulnerabilities allow attackers to impersonate other users, or gain permissions they should not have.** These vulnerabilities occur when code makes access decisions on the back of untrusted inputs.

## Risks

Many websites hold sensitive data on behalf of their users. If an attacker can exploit **horizontal escalation** vulnerabilities to gain access to another user's data, you are betraying your users' trust, which can have reputational, legal, and financial implications.

If an attacker can exploit **vertical escalation** vulnerabilities to gain administrative access, they can interrupt critical functions and possibly compromise your application.

## Protection

Privilege escalation vulnerabilities are system flaws that grant a malicious user excessive or wrong permissions after they have authenticated themselves. (These are distinct from **session hijacking** vulnerabilities that allow an attacker to impersonate another user.)

Escalation vulnerabilities in websites occur when access control decisions are made on the back of untrusted input. Since HTTP is [stateless protocol](https://hacksplaining.com/glossary/http), websites need some mechanism of continuing the conversation with the user after login, over multiple HTTP request-response cycles. This typically means sending information in HTTP responses that will be transmitted back in subsequent requests; an attacker will try to manipulate the re-transmitted data to fool the system into giving them more power than they should.

There are three possible approaches to prevent this happening:

- **Keep critical information on the server side**, and only send session IDs to the client.
- **Tamper-proof the data sent to the client**, by using a digital signature.
- **Encrypt the data sent to the client**, so it is opaque to the client.

We will discuss each approach in turn.

#### Keeping it Server Side

The simplest approach philosophically is to not transmit sensitive data to the client-side. Typically this means only the **session ID** is passed back and forth between client and server, and all session-related data is kept on the server. This removes the possibility of tampering, since a malicious user never gets to see the data.

While secure, this approach puts some extra obligations on the server. Session state has to be persisted and looked up with each HTTP request. Unless you are running everything in a single process on a single server, this means writing the session state away to a data-store or shared memory. The scalability implications of this approach need to be thought through carefully.

#### Tamper-Proofing Cookies

If you want to send data back to the client-side and be sure it hasn't been tampered with when it returns, you need to [digitally sign](https://en.wikipedia.org/wiki/Digital_signature) the data. Many web frameworks allow you to encode session state, and accompany it with a digital signature which must be sent back with the data. Upon receipt of the returned data, the digital signature is recalculated. Any modifications will result in a different signature, indicating the data has been tampered with, and must be discarded.

This approach guarantees the integrity of the data, but does not make it opaque to the client. So it may not be appropriate if you are storing data about a user you don't want them to be able to see -- like credit scores or other types of ratings!

Note that with this approach, the HTTP response and request carry the entirety of the session. Be careful not to store too much data in your sessions, or the responsiveness of your site will be affected.

#### Encrypting Data

If you want the session state to be opaque _and_ tamper-proof, you need to encode _and_ encrypt the data. This introduces some computational overhead -- the data will need to be decrypted with each request, and re-encrypted with each response -- but should not put a great strain on your servers.