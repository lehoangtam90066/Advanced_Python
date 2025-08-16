from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
