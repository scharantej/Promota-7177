
from flask import Flask, render_template, request

app = Flask(__name__)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate input
        # ...

        # Send email or process data
        # ...
    return render_template('contact.html')

# Booking page
@app.route('/book')
def book():
    return render_template('book.html')

# Services page
@app.route('/services')
def services():
    services = [
        {'name': 'Keynote Speeches', 'description': '...', 'price': '...'},
        {'name': 'Workshops', 'description': '...', 'price': '...'},
        {'name': 'Consulting', 'description': '...', 'price': '...'}
    ]
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
