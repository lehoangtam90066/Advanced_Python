from flask import Flask, make_response, render_template
app = Flask(__name__)
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp