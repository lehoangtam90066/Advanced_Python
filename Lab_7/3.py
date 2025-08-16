from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route để hiển thị form đăng ký
@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

# Route để xử lý dữ liệu đăng ký
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Logic để lưu thông tin người dùng vào cơ sở dữ liệu ở đây
    print(f'Tài khoản mới được tạo: {username}, Email: {email}')  # Thay thế bằng lưu trữ thực tế

    return "Đăng ký thành công! Bạn có thể đăng nhập."

if __name__ == '__main__':
    app.run(debug=True)
