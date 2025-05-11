To build secure software you need to understand the threats you face, where malicious inputs might enter the system, anticipate failure conditions, understand the principles of security, and have a processes to correct security issues and learn from them as they are discovered.

With a good sketch of your system, it can help to apply the **STRIDE** model for identifying threats at each access point

S : spoofing 
T : Tampering 
R" Repudiation 
I : Information disclosure
D" Denial of Service
E: Elevation of privelege

Data classification : 

Applications that handle sensitive data may also require a **data classification** strategy that will break your data into broad categories, so you can concentrate on protecting the most sensitive data.

|                 |                                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| Public Data     | Data available to everyone, like company blogs                                          |
| Private Data    | Data available to authenticated users                                                   |
| Restricted Data | Sensitive data that may be owned by particular users, like profile information          |
| High Risk Data  | Access tokens, passwords and credentials for third-party APIs that must never be shared |
A good SDLC involves **issue-tracking**, **source control**, a **build process**, **unit tests**, a **continuous integration** environment and **code reviews**. Deployment of code should be automated, and you should be able to rollback code easily when issues occur.
 :
 ood SDLC consists of the following elements:

- **Source control.** All code your team writes should eventually enter source control, and certainly should be kept in a tool like `git` before being released. This will allow you to analyze code changes for potential security flaws, and review code running in your production environment.
- **Build Automation.** Automate your build process to avoid any disparities between the code you test against and the code you run in production. This generally means using a package manager to manage dependencies and writing a build script that compiles code or generates assets.
- **Unit Testing.** Your build process should also execute any unit tests you have. Writing unit tests is a good way to verify security requirements have been met (e.g. "only authenticated users can view the profile page"), and act as a form of documentation as the code is changed.
- **Continuous Integration.** You should run your build process and unit tests whenever code is pushed into source control, so your development team gets immediate feedback when security requirements are violated by a set of code changes.
- **Code Reviews.** Each code change should be reviewed by someone other than the author of the code change before being deployed. A reviewer acting as a second pair of eyes will often be able to spot possible security flaws before they go live.
- **Push-button Deployment.** Your process for deploying to test and then production environments should be as simple as possible. Anything that requires human intervention opens the door for user-error, meaning you code may not deploy cleanly or at all.
- **Rollback Capability.** You should have a process for undoing releases and quickly deploying a prior version of the code. This is _essential_ if you ever deploy code with a security vulnerability, since you need to undo the mistake as soon as it is discovered.
-
Follow the **principle of least privilege:** each process, program and user should operate with the least amount of privilege required to achieve their goals. Applying this principle will mitigate the harm an attacker can do if they successfully compromise your system.

**Validate input**: any input coming from an untrusted source (like an HTTP request) should be validated to ensure it is an expected format, and rejected otherwise

**Encrypting** data at rest and in transit will protect against monster-in-the-middle attacks and protect sensitive information from being read if it is stolen.

Your code should **fail securely:** it is important to anticipate failure conditions, and ensure you do not leak internal architectural details in error messages. If unexpected error conditions arise, ensure you can roll back any database transactions to ensure data in not left in a corrupted state.


Make sure your systems are **observable**: your running code should issue logging statements and logs should be viewable at run time. You should be able to observe the type and volume of traffic hitting your servers and how much of your available bandwidth is being used

When designing a system, pay particular attention to **trust boundaries**, where untrusted input enters the application. It often helps to think about **sources** - where input enters the system - and **syncs** - places in the code where sensitive operations are performed. Tracing through the code from each source to each sync will help highlight potential vulnerabilities.

Mistakes happen, and it's key that you learn lessons any time a vulnerability makes it into production. A **post-mortem** should be performed to identity where safeguards failed to protect you. Remember, you are generally looking for failures in the _process_ rather than individuals to blame - since nobody should be acting alone, and errors are generally caused by oversights rather than recklessness.

Finally, it's important not to make security protocols for your development team or users too onerous, or people will neglect to follow them. It's true that the securest software is the application with no users, but that's not the goal here!


[[Information Leakage]]

[[file upload vulnerabilities]]

