from flask import Flask, request
app  = Flask(__name__)
def index():
    username = request.cookies.get('username')
    

