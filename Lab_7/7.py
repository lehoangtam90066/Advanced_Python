from flask import Flask, render_template

app = Flask(__name__)

# Dữ liệu người dùng mẫu (có thể thay thế bằng cơ sở dữ liệu trong thực tế)
user_data = {
    'name': 'Lê Hoàng Tâm',
    'email': 'tam.2274802010780@vanlanguni.vn',
    'age': 20,
    'bio': 'thích đi học và chậm deadline',
    'avatar': 'static/picture.png'  # Đường dẫn đến hình đại diện
}

# Route cho trang hiển thị thông tin cá nhân
@app.route('/')
def profile():
    return render_template('profile_display.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
