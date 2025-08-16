from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Dữ liệu người dùng mẫu (có thể thay thế bằng cơ sở dữ liệu trong thực tế)
user_data = {
    'name': 'Lê Hoàng Tâm',
    'email': 'tam.2274802010780@vanlanguni.vn',
    'age': 20,
    'bio': 'thích đi học và chậm deadline',
    'avatar': 'static/picture.png',  # Đường dẫn đến hình đại diện
    'is_following': False,  # Trạng thái follow ban đầu
    'follower_count': 120  # Số người theo dõi ban đầu
}

# Route cho trang hiển thị thông tin cá nhân
@app.route('/')
def profile():
    return render_template('profile_display.html', user=user_data)

# Route để thay đổi trạng thái follow/unfollow
@app.route('/toggle_follow', methods=['POST'])
def toggle_follow():
    # Đổi trạng thái follow khi nhấn nút
    if user_data['is_following']:
        user_data['follower_count'] -= 1
    else:
        user_data['follower_count'] += 1
    user_data['is_following'] = not user_data['is_following']
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
