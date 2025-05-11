Access control enforces policy such that users cannot act outside their intended permissions. Failures typically lead to unauthorized information disclosure, modification, or destruction of all data or performing a business function outside the user's limits.
[[Directory Traversal]]
[[cross-site request forgery]]


**Correctly applied access control rules are key to keeping your data secure.** Almost all applications need to protect sensitive data and operations, so putting careful thought into how to restrict access is important when designing a system.


your access control strategy should cover three aspects:

- **Authentication** - correctly identifying a user when they return to the application.
  
  
  Authorization is often implemented by granting each user a specific role. (Administrative users are frequently differentiated from regular users, for instance.) More granular permissioning schemes need to be implemented if individual documents or data items need to have separate privileges.
  
  
- **Authorization** - deciding what actions a user should and should not be able to perform once they have been authenticated.
  
  Authorization schemes often implement an idea of **ownership**. Certain resources can **belong** to a user or group of users, and may not be accessible to others without their permission.
  
- **Permission Checking** - evaluating authorization at the point-in-time when a user attempts to perform an action.
  
  access control schemes are often declared as **policies** that white-list or black-list specific entities and groups against certain actions.



- **Decide what the biggest risks are to your organization, and focus on mitigating those risks.**
- **Design and document your access control scheme upfront.** Access control needs to be implemented correctly throughout your system. Without an agreed upon set of rules, it is hard to define what a "correct" implementation looks like.
- **Attempt to centralize access control decisions in your codebase.** This doesn't necessarily mean having all access decisions flow through one code-path, but you should have a standard method of evaluating access control decisions. This might consist of function decorators, web access path checking, a stored procedure layer in your database, inline assertions in the code, or calls out to a dedicated permissioning component or in-house API.
- **Test access control critically.** Make sure your testing procedures genuinely attempt to find holes in your access control scheme. Treat it like an attacker would, and you will be better prepared when your first real attack occurs. If you have the time and budget, consider employing an external team to perform penetration testing.

# Solutions :
[MustBe](https://github.com/derickbailey/mustbe) and [ACL](https://www.npmjs.com/package/acl) are mature libraries that focus on different aspects of access control: web server routing and the evaluation of access control rules, respectively.

usefull links 
https://www.cs.purdue.edu/homes/ninghui/courses/426_Fall10/handouts/426_Fall10_lect09.pdf

https://wiki.owasp.org/index.php/Testing_for_Authorization