regex stand for regular expressions 
they are often used to describe which characters are akkiwed in a placeholder or which chars appear etc. ...

some examples

|   |   |
|---|---|
|ab**c***|matches a string that has ab followed by zero or more c's|
|ab**c+**|matches a string that has ab followed by one or more c's|
|ab**c?**|matches a string that has ab followed by zero or one c's|
|ab**c2**|matches a string that has ab followed by cc|
|ab**c{2,}**|matches a string that has ab followed by 2 or more c's|
|ab**c{2,5}**|matches a string that has ab followed by 2 up to 5 c's|
|a**(bc)***|matches a string that has a followed by zero or more copies of the sequence bc's|
|a**(bc){2,5}**|matches a string that has a followed by 2 up to 5 copies of the sequence bc's|
also for pattern matching
```python
@app.route('/share/<url>')
def share(link):
  """Return the meta-data for a web-link shared by a user."""

  # Validate the URL has a protocol using a regular expression.
  link = link if re.match("^[a-z]+://.*", link) else f"https://{link}"

  # Go grab the meta-data.
  return OpenGraph(url=link).to_json()
``` 


### Somewhat a part of [[denial of service attack ]]and shut down the system

it's very common and easy to exploit 

## Solution 
## Mitigation

- Don't generate regular expressions directly from untrusted input - define them in your codebase.
- Use a search index like Elasticsearch or Lucene for complex searches, rather than running regular expression matches on large datasets.
- Check any regexes within your codebase for repeating grouped patterns or ambiguous patterns. "Catastrophic" backtracking can be avoided if you follow these rules of thumb:

- Avoid nested quantifiers like `(a+)+`, where a pattern potentially matching multiple characters can be applied multiple times.
- Avoid quantified overlapping disjunctions like `(a|a)+`.
- Avoid quantified overlapping adjacencies like `\d+\d+`.
#### Use Node.js library safe regex :
Make sure to test new expressions you define them in your codebase, and consider adding a unit test to scan for unsafe regular expressions if you develop in Node.js.

links : 
https://cwe.mitre.org/data/definitions/185.html