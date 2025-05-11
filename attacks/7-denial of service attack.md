[![Schematic diagram of a distributed denial of service attack. | Download ...](https://tse1.mm.bing.net/th/id/OIP.hCFrcOeRDSIHgnPcmXw3PwHaJe?pid=Api)](https://www.researchgate.net/figure/Schematic-diagram-of-a-distributed-denial-of-service-attack_fig1_358566960)

---

## 🛑 Denial-of-Service (DoS) & Distributed Denial-of-Service (DDoS) Attacks

### What Is a DoS Attack?

A Denial-of-Service (DoS) attack aims to make a website or service unavailable to legitimate users by overwhelming it with excessive traffic or resource requests. When multiple systems are used to launch such attacks simultaneously, it's termed a Distributed Denial-of-Service (DDoS) attack.([Wikipédia](https://en.wikipedia.org/wiki/Denial-of-service_attack?utm_source=chatgpt.com "Denial-of-service attack"))

### How Do They Work?

Attackers often employ botnets—networks of compromised computers—to flood a target server with requests, exhausting its resources and rendering it inaccessible to genuine users. This can lead to service outages, revenue loss, and reputational damage.

### Real-World Examples

- **UK Government Websites**: In May 2025, the pro-Russian group NoName057(16) claimed responsibility for DDoS attacks on various UK websites, including local councils and the Association for Police and Crime Commissioners. While some sites experienced temporary disruptions, others remained unaffected .([The Guardian](https://www.theguardian.com/technology/2025/may/07/pro-russian-hackers-claim-to-have-targeted-several-uk-websites?utm_source=chatgpt.com "Pro-Russian hackers claim to have targeted several UK websites"))
    
- **Royal Family's Website**: In October 2023, the British royal family's official website, royal.uk, was taken offline for about 90 minutes due to a DDoS attack claimed by the hacker group KillNet. The attack overwhelmed the site with traffic, but no sensitive information was compromised .([Vanity Fair](https://www.vanityfair.com/style/2023/10/russian-hackers-crashing-the-royal-familys-website?utm_source=chatgpt.com "Russian Hackers Claim Responsibility for Crashing the Royal Family's Website"))
    

### Mitigation Strategies

- **Traffic Filtering**: Implement firewalls and intrusion detection systems to filter out malicious traffic.
    
- **Rate Limiting**: Limit the number of requests a user can make in a given timeframe.
    
- **Redundancy**: Distribute resources across multiple servers and data centers to prevent a single point of failure.
    
- **Content Delivery Networks (CDNs)**: Use CDNs to distribute traffic and reduce the load on the primary server.
    

---

## 🧩 Regular Expression Denial-of-Service (ReDoS)

### What Is ReDoS?

ReDoS is a type of attack that exploits the inefficiencies in regular expression (regex) processing. By providing specially crafted input, attackers can cause the regex engine to consume excessive CPU resources, leading to service slowdowns or crashes.([Wikipédia](https://es.wikipedia.org/wiki/ReDoS?utm_source=chatgpt.com "ReDoS"), [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca3012?utm_source=chatgpt.com "CA3012: Review code for regex injection vulnerabilities"))

### How Does It Work?

Certain regex patterns can exhibit exponential time complexity when processing specific inputs. Attackers exploit this by submitting inputs that trigger worst-case performance scenarios, causing the application to hang or crash.([Wikipédia](https://es.wikipedia.org/wiki/ReDoS?utm_source=chatgpt.com "ReDoS"))

### Example

Consider the regex pattern:

```regex
^(a+)+$
```

When processing the input string `"aaaaaaaaaaaaaaaaaaaaaaaaaaaa!"`, the regex engine may undergo catastrophic backtracking, leading to significant CPU usage and potential denial of service.([docs.guardrails.io](https://docs.guardrails.io/docs/vulnerabilities/javascript/insecure_use_of_regular_expressions?utm_source=chatgpt.com "Insecure Use of Regular Expressions - GuardRails"))

### Mitigation Strategies

- **Input Validation**: Sanitize and validate all user inputs before processing.
    
- **Regex Optimization**: Avoid using nested quantifiers and ambiguous patterns that can lead to backtracking.
    
- **Timeouts**: Set execution time limits for regex operations to prevent long-running processes.
    
- **Use Safe Libraries**: Employ regex libraries that are designed to handle complex patterns efficiently and are resistant to ReDoS attacks.([arXiv](https://arxiv.org/abs/2303.01996?utm_source=chatgpt.com "Exploiting Input Sanitization for Regex Denial of Service"))
    

---

## 🔒 Best Practices for Developers

- **Avoid User-Controlled Regex**: Never allow users to input regex patterns that the server will execute.
    
- **Educate and Train**: Ensure that developers are aware of the risks associated with regex and DoS attacks.
    
- **Regular Audits**: Conduct periodic code reviews and security audits to identify and remediate potential vulnerabilities.
    
- **Stay Updated**: Keep all libraries and dependencies up to date to benefit from security patches and improvements.
    

---

## 📚 Further Reading

- [OWASP: Regular Expression Denial of Service (ReDoS)](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)
    
- [CISA: Understanding Denial-of-Service Attacks](https://www.cisa.gov/news-events/news/understanding-denial-service-attacks)
    
- [Cloudflare: What is a DDoS Attack?](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)
    
