from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')  # Sử dụng .get() để tránh KeyError
    password = request.form.get('password')  # Sử dụng .get() để tránh KeyError

    # Kiểm tra thông tin đăng nhập (thay thế bằng logic thực tế của bạn)
    if username == "admin" and password == "password":
        return "Đăng nhập thành công!"
    else:
        return "XIN CHÀO VĂN LANG"

if __name__ == '__main__':
    app.run(debug=True)
