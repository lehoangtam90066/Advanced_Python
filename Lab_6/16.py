from flask import Flask, render_template
app = Flask(__name__)
@app.errorhandler(404)
def  page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_sever_error(e):
    return render_template('500.html'), 500