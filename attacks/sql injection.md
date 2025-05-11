Serioucness : high 

**SQL injection** is a type of [injection attack](https://hacksplaining.com/glossary/code-injection). Injection attacks occur when maliciously crafted inputs are submitted by an attacker, causing an application to perform an unintended action. Because of the ubiquity of [SQL](https://hacksplaining.com/glossary/sql) databases, SQL injection is one of the most common types of attack on the internet.

- **Extract sensitive information**, like Social Security numbers, or credit card details.
- **Enumerate the authentication details of users registered on a website,** so these logins can be used in attacks on other sites.
- **Delete data or drop tables**, corrupting the database, and making the website unusable.
- **Inject further malicious code** to be executed when users visit the site.


by removing the string concatenation method instead use parameterized statements 

https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/?utm_source=hacksplaining&utm_medium=post&utm_campaign=articlelink

https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/?utm_source=hacksplaining&utm_medium=post&utm_campaign=articlelink

third party stolutions : 
used by facebook google etc ...
https://lifehacker.com/understanding-oauth-what-happens-when-you-log-into-a-s-5918086 I

#### Parameterized Statements

Programming languages talk to SQL databases using **database drivers.** A driver allows an application to construct and run SQL statements against a database, extracting and manipulating data as needed. **Parameterized statements** make sure that the parameters (i.e. inputs) passed into SQL statements are treated in a safe manner.

This : 

```php
// Connect to the database.
Connection conn = DriverManager.getConnection(URL, USER, PASS);

// Construct the SQL statement we want to run, specifying the parameter.
String sql = "SELECT * FROM users WHERE email = ?";

// Generate a prepared statement with the placeholder parameter.
PreparedStatement stmt = conn.prepareStatement(sql);

// Bind email value into the statement at parameter index 1.
stmt.setString(1, email);

// Run the query...
ResultSet results = stmt.executeQuery(sql);

while (results.next())
{
    // ...do something with the data returned.
}
```
instead of this :
```php
// The user we want to find.
String email = "user@email.com";

// Connect to the database.
Connection conn = DriverManager.getConnection(URL, USER, PASS);
Statement stmt = conn.createStatement();

// Bad, bad news! Don't construct the query with string concatenation.
String sql = "SELECT * FROM users WHERE email = '" + email + "'";

// I have a bad feeling about this...
ResultSet results = stmt.executeQuery(sql);

while (results.next()) {
  // ...oh look, we got hacked.
}
```

```postgresql
var pg = require('pg');

var connection = "postgres://username:password@localhost/database";

var client = new pg.Client(connection);

// Query and parameters passed separately.
client.connect(function(err) {
  client.query(
    'select * from users where email = ?',
    [email],
    function(err, result) {
      // Do something with the retrieved data.
    });
  });

client.end();
```

```php
$statement = $dbh->prepare("select * from users where email = ?");
$statement->execute(array(email));
```