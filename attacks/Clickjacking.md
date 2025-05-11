like : 
genuislab.com : GENUISLAB.com
genuisIab.com : GENUIIAB.com
look similar on first sight 
 
 tricks web users into performing an action they did not intend, typically by rendering an invisible page element on top of the action the user thinks they are performing.
- **Harvest login credentials**, by rendering a fake login box on top of the real one.
- **Trick users into turning on their web-cam or microphone**, by rendering invisible elements over the Adobe Flash settings page.
- **Spread [worms](https://hacksplaining.com/glossary/worms) on social media sites** like Twitter and MySpace.
- **Promote online scams** by tricking people into clicking on things they otherwise would not.
- **Spread malware** by diverting users to malicious download links.

scam people into signing into offers that aren't ours 



solutions  : 

iframe access denied |as simple as it sounds
An inline frame (iframe) is **a HTML element that loads another HTML page within the document**.
#### Content Security Policy

The `Content-Security-Policy` [HTTP header](https://hacksplaining.com/glossary/http) is part of the [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) standard, and provides a broader range of protection than the `X-Frame-Options` header (which it replaces). It is designed in such a way that website authors can enumerate individual domains from which resources (like scripts, stylesheets, and fonts) can be loaded, and also domains that are permitted to embed a page.

To control where your site can be embedded, use the `frame-ancestors` directive:

|                      Header                       |                                       Meaning                                        |
| :-----------------------------------------------: | :----------------------------------------------------------------------------------: |
| `Content-Security-Policy: frame-ancestors 'none'` | The page cannot be displayed in a frame, regardless of the site attempting to do so. |
| `Content-Security-Policy: frame-ancestors 'self'` |   The page can only be displayed in a frame on the same origin as the page itself.   |
| `Content-Security-Policy: frame-ancestors *uri*`  |         The page can only be displayed in a frame on the specified origins.          |

#### X-Frame-Options

The `X-Frame-Options` [HTTP header](https://hacksplaining.com/glossary/http) is an older standard that can be used to indicate whether or not a browser should be allowed to render a page in a `<frame>`, `<iframe>` or `<object>` tag. It was designed specifically to help protect against clickjacking, but has since between made obsolete by content security polices.

There are three permitted values for the header:

|Value|Meaning|
|:-:|:-:|
|`DENY`|The page cannot be displayed in a frame, regardless of the site attempting to do so.|
|`SAMEORIGIN`|The page can only be displayed in a frame on the same origin as the page itself.|
|`ALLOW-FROM *uri*`|The page can only be displayed in a frame on the specified origins.|

#### Frame-Killing

In older browsers, the most common way to protect users against clickjacking was to include a frame-killing JavaScript snippet in pages to prevent them being included in foreign iframes. You might still see code like the following in legacy web applications:

```
<style>
  /* Hide page by default */
  html { display : none; }
</style>

<script>
  if (self == top) {
    // Everything checks out, show the page.
    document.documentElement.style.display = 'block';
  } else {
    // Break out of the frame.
    top.location = self.location;
  }
</script>
```

> **An example frame-killing script:** when the page loads, this code will check that the domain of the page matches the domain of the browser window, which will _not_ be true when the page is embedded in an iframe.

Most sites don't need to be embedded in iframes, so a frame-killing script is easy to implement. If embedding _is_ required in your application, consider adding an allowlist of domains, so you have control over where your content is embedded.

Frame-killing offers a large degree of protection against clickjacking, but it can be error-prone. Be sure to set appropriate HTTP headers as the first recourse in protecting your site.


links  : 
| alma3erifa HAHAHA
https://crypto.stanford.edu/~dabo/pubs/papers/framebust.pdf
