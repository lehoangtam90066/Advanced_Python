from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return redirect(url_for('profile_form'))  # Chuyển hướng đến form nhập thông tin cá nhân

# Route để hiển thị form nhập thông tin cá nhân
@app.route('/profile', methods=['GET'])
def profile_form():
    return render_template('profile_form.html')

# Route để xử lý dữ liệu từ form và hiển thị thông tin
@app.route('/profile', methods=['POST'])
def profile():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    bio = request.form.get('bio')

    return render_template('profile_display.html', name=name, email=email, age=age, bio=bio)

if __name__ == '__main__':
    app.run(debug=True)
