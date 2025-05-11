Nothing is built from scratch no more (too little )
we do depend on libraries frameworks and tools  especially with package management tools such as pip , gems , npm 
sometimes

- **SQL Injection vulnerabilities** that allow execution of arbitrary SQL statements against a database.
- **Cross-Site Scripting vulnerabilities** that permit attackers to execute malicious Javascript in the browser.
- **Command Injection vulnerabilities** that allow execution of arbitrary scripts on the server.
## Protection : 
**Automate your build and deployment processes.** To make your code secure, you need to know what code you are running. This means declaring all third-party libraries within build scripts or dependency management systems; building and deploying from source control; and keeping records of deployment logs.


**Deploy known-good versions of software.** Dependency management tools often allow you to leave the version of each dependency indeterminate, which is shorthand for "grab the latest available version at build time." Try to avoid this - upgrade versions deliberately, when you have had chance to review the release notes, and pin dependency versions in your code.

**Be careful of private dependencies.** Large organizations often mix public and private dependencies in the same codebase. You should be careful how you configure the precedence of repositories in your build process, since [dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) attacks - where an attacker uploads a malicious copy of a private dependency to a public repository - have caught many organizations off guard.



**Perform regular code reviews** so your whole development team knows what third-party libraries are being used, and which parts of your codebase depend on them.

**Make penetration testing part of your development lifecycle.** Penetration testing tools will attempt to take advantage of known exploits, checking whether your technology stack contains vulnerable components.
https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/

https://docs.gitlab.com/ee/development/integrations/secure.html
https://retirejs.github.io/retire.js/
https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities