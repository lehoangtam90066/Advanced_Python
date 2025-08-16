from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('new_page'))

@app.route('/new_page')
def new_page():
    return '<h1>Welcome to the new page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
