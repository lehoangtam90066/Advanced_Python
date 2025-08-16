from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission (e.g., verify user credentials)
        email = request.form.get('lehoangtam090066@gmail.com')
        password = request.form.get('123')
        keep_logged_in = request.form.get('keep_logged_in')
        # For now, just redirect to the home page after form submission
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/')
def home():
    return '<h1>Welcome to the Home Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)
