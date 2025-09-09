from fpdf import FPDF

questions = {
    "Section 1: How the Web Works": [
        "What happens when you type a URL into your browser and press Enter?",
        "What is DNS and how does it work?",
        "What is an HTTP request and what are its parts?",
        "What is an HTTP response and what does it contain?",
        "What are the most common HTTP methods?",
        "What is the difference between HTTP and HTTPS?",
        "What is TLS/SSL and how does it ensure secure communication?",
        "What is a CDN and how does it help web performance?",
        "What is a web server and how does it serve files to clients?",
        "What are status codes in HTTP? Can you explain 200, 301, 404, and 500?",
        "What is the role of a browser in rendering web content?",
        "What is a browser rendering engine? Name some rendering engines.",
        "How does a browser parse HTML?",
        "What is the DOM? How is it created?",
        "What is the CSSOM and how does it relate to the DOM?",
        "Explain the critical rendering path.",
        "What is a reflow and repaint in the browser?",
        "How does browser caching work?",
        "What is preloading, prefetching, and preconnecting in web performance?",
        "What is the purpose of the Content-Type header?",
        "What are cookies, and how are they used in HTTP?",
        "What is the Same-Origin Policy?",
        "What is CORS, and how does it work?",
        "What is a service worker and how does it affect web performance?",
        "What are first paint and first contentful paint?",
        "What is lazy loading and how does it improve performance?",
        "What is a web manifest and what is it used for?",
        "How do SPAs affect browser behavior compared to MPAs?",
        "What is the purpose of the browser cache-control header?",
        "What tools can you use to analyze how a page is rendered?"
    ],
    "Section 2: HTML Basics to Advanced": [
        "What is HTML and why is it important?",
        "What’s the difference between HTML and XHTML?",
        "What are semantic HTML tags? Why are they important?",
        "Name 5 semantic HTML elements and their uses.",
        "What is the purpose of the <!DOCTYPE> declaration?",
        "What are void (self-closing) elements in HTML?",
        "What is the difference between <div> and <span>?",
        "What is the difference between id and class?",
        "How is the alt attribute used in <img> tags?",
        "What is accessibility in HTML?",
        "What are ARIA attributes?",
        "What is the difference between <section>, <article>, and <aside>?",
        "How would you make a form accessible?",
        "What input types are available in HTML5?",
        "What are data attributes (data-*) and how are they used?",
        "What is the <meta> tag used for?",
        "What are the different types of <meta> tags?",
        "How does the <base> tag affect URL resolution?",
        "What is the difference between <script>, <noscript>, and <template>?",
        "What is defer vs async in script loading?",
        "What are custom elements in HTML?",
        "What are web components?",
        "What is Shadow DOM?",
        "How can you make an image responsive using HTML?",
        "What is the <picture> element and how is it different from <img>?",
        "What are inline, block, and inline-block elements?",
        "What’s the difference between relative and absolute URLs?",
        "How do srcset and sizes attributes help with responsive images?",
        "What’s the purpose of the lang attribute in <html>?",
        "What is the difference between name and id in form elements?",
        "What is a label element and how does it work with inputs?",
        "What’s the purpose of the action and method attributes in a form?",
        "What are HTML entities and when are they used?",
        "What is the use of the <iframe> element?",
        "How does browser security affect <iframe> usage?",
        "What is contenteditable in HTML?",
        "What’s the difference between <b> and <strong>?",
        "What is the difference between <i> and <em>?",
        "How do HTML5 elements support mobile responsiveness?",
        "What are deprecated HTML tags?"
    ],
    "Section 3: HTML + SEO + Performance + Best Practices": [
        "What is semantic HTML and how does it help SEO?",
        "How do <h1> to <h6> tags affect SEO?",
        "What is the importance of using alt attributes for images?",
        "What is Open Graph and how is it implemented in HTML?",
        "How do Twitter Cards work with HTML?",
        "What is the impact of using nofollow in anchor tags?",
        "What is the role of structured data in HTML?",
        "What is lazy loading of images?",
        "How can you defer rendering of non-critical HTML?",
        "What is the effect of too much DOM depth?",
        "What is Time to Interactive (TTI), and how can HTML impact it?",
        "How can improper nesting of HTML tags affect performance and rendering?",
        "What are common accessibility issues in HTML markup?",
        "How can Lighthouse help evaluate HTML performance?",
        "What is CLS (Cumulative Layout Shift) and how can HTML markup affect it?",
        "What is FID (First Input Delay) and how is it related to HTML?",
        "How can poor HTML structure affect screen readers?",
        "How should you structure your HTML for performance and maintainability?",
        "How do you use ARIA roles with HTML for accessibility?",
        "What HTML best practices improve performance on mobile?"
    ],
    "Section 4: Troubleshooting & Debugging": [
        "How do you debug HTML rendering issues in different browsers?",
        "What tools in browser DevTools help inspect HTML?",
        "How do you validate HTML code?",
        "What are some common causes of broken layout due to HTML issues?",
        "How do you handle HTML rendering differences across browsers?",
        "What are common HTML validation tools?",
        "What is a rendering quirk mode in browsers?",
        "What can cause an HTML page to load as blank?",
        "How do you debug malformed HTML from server responses?",
        "How can incorrect HTML affect JavaScript behavior?"
    ]
}

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "HTML & Web Fundamentals Interview Questions (100 Questions)", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
q_number = 1

for section, qs in questions.items():
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, section, ln=True)
    pdf.set_font("Arial", size=12)
    for q in qs:
        pdf.multi_cell(0, 10, f"{q_number}. {q}")
        q_number += 1
    pdf.ln(5)

pdf.output("HTML_Web_Interview_Questions_100.pdf")
