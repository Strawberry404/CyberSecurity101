Security Settings :
1.  Open accounts that comes by default with servers and content management systems **Disable them in production !!**
2. Secure directories to not expose files 
3. in production : turn off client side error reporting  - enforce use of https everywhere - disable dev tools in console etc...
4. controll of environments : controlled appropriately from test envirements etc ...
5. Regulate admin and management interaces  , access restriction 
6. authentication credentials for production systems are shared on a need to know basis , elevate permissions *temporarly*
7. CDN and domains defenition 

- **Automate your build process.** An ad-hoc build processes makes it easy for insecure software settings to slip through. Make sure you have a scripted, repeatable build process, so you know what software (and what versions) you are running at any given time. [[Tests to do along the way]]
- **Review new software components and disable default credentials as soon as possible.** Each new library, toolkit and server introduces new security risks - ensure these are considered during your code reviews.
- **Clearly separate code and configuration.** Environment-specific and sensitive configuration should be stored outside the codebase - either in configuration files or dedicated systems (like databases). Hard-coded credentials and backdoors open your site to being compromised.[[envirenement]]
- **Create dedicated accounts with appropriate privileges.** Access to production servers and databases should follow _the principle of least privilege_. Users and processes should only have the permissions they require to function, and any escalation of privileges (for example, during release windows,) should be temporary and subject to formal review process.[[privelages]]
- **Script your deployment process.** Make sure deployment to staging and production systems is done through a repeatable, scripted process. You should know what version of your code is running on each environment - and be able to vouch that each environment is running the appropriate configuration. After each release, perform (at least a cursory) "smoke-test" [[System Testing]]to ensure the correct software and configuration got deployed.
- **Segregate environments.** Production and staging environments should use different sets of credentials, since they will typicllay have different access levels. Try to ensure there is no network access between environments, so attackers cannot move sideways between environments with different access levels.
- **Add extra security for administrative systems.** If possible, avoid opening your administrative tools to the internet at large. Prescribe a secure password policy for administrators, and ensure your team knows to take security seriously. Implement multi-factor authentication if feasible. Make sure you know who has access to what system, and have a plan in place for when access has to be revoked (for instance, if team-members leave).