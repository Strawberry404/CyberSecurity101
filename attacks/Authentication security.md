Authentication is import to prevent access to data , networks , websites etc ... 

The App is scalable and so the risks and the attacks

types of authentication : 

## How authentication works

For people, authentication involves setting up a username, password, and other authentication methods, such as a facial scan, fingerprint, or PIN. To protect identities, none of these authentication methods are saved to the service’s database. Passwords are hashed (not encrypted) and the hashes are saved to the database. When a user enters a password, the entered password is also hashed, then the hashes are compared. If the two hashes match, then access is granted. For fingerprints and facial scans, the information is encoded, encrypted, and saved on the device.

## Types of authentication methods

In modern authentication, the authentication process is delegated to a trusted, separate identity system, as opposed to traditional authentication where each system verifies identifies itself. There has also been a shift in the type of authentication methods used. Most applications require a username and password, but as bad actors have gotten savvier at stealing passwords, the security community has developed several new methods to help protect identities.

### Password-based authentication

the problem with this is users often reuse their premade easy password which creates vulnerabilities from their side 
can we do something about it ? yes 

### Token-based authentication

In token-based authentication both a device and the system generate a new unique number called a time-based one-time PIN (TOTP) every 30 seconds. If the numbers match, the system verifies that the user has the device.

### One-time password

One-time passwords (OTP) are codes generated for a specific sign-in event that expire shortly after they’re issued. They are delivered via SMS messages, email, or a hardware token.

### Push notification

Some apps and services use push notifications to authenticate users. In these instances, people receive a message on their phone asking them to approve or deny the access request. Because sometimes people accidentally approve push notifications even though they are trying to sign in to the services who sent the notification, this method is sometimes combined with an OTP method. With OTP the system generates a unique number that the user has to enter. This makes the authentication more phishing resistant.

### Multifactor authentication

One of the best ways to cut down on account compromise is to require two or more authentication methods, which may include any of the previously listed methods. An effective best practice is to require any two of the following:

- Something the user knows, typically a password.
- Something they have, such as a trusted device that is not easily duplicated, like a phone or hardware token.
- Something the user is, like a fingerprint or face scan.