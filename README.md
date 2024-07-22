## Flask Application Design for a Conference Speaker Landing Page

### HTML Files

**index.html:**

- Title: "Personal Brand Landing Page"
- Content:
    - Introduction and professional headshot
    - List of services offered (e.g., keynote speeches, workshops)
    - Call-to-action (e.g., contact form, booking information)

### Routes

**@app.route('/')**

- Decorator maps the root URL ('/') to the index.html file.
- Function displays the landing page.

**@app.route('/contact', methods=['GET', 'POST'])**

- Decorator maps the '/contact' URL to this route.
- Function defines a contact form:
    - GET method: Displays the contact form.
    - POST method: Handles form submission, validates input, and sends an email or processes the data.

**@app.route('/book', methods=['GET'])**

- Decorator maps the '/book' URL to this route.
- Function:
    - GET method: Displays a booking page with a form for requesting a speaker engagement.
    - Collects information such as date, location, and topic.

**@app.route('/services')**

- Decorator maps the '/services' URL to this route.
- Function:
    - Defines a page that lists the services offered in more detail.
    - Provides descriptions, pricing, and testimonials.