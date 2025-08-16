from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu người dùng mẫu (có thể thay thế bằng cơ sở dữ liệu trong thực tế)
user_data = {
    'name': 'Lê Hoàng Tâm',
    'email': 'tam.2274802010780@vanlanguni.vn',
    'age': 20,
    'bio': 'thích đi học và chậm dealine'
}

# Route cho trang hiển thị thông tin cá nhân
@app.route('/')
def profile():
    return render_template('profile_display.html', user=user_data)

# Route để hiển thị form chỉnh sửa thông tin
@app.route('/edit', methods=['GET'])
def edit_profile():
    return render_template('profile_edit.html', user=user_data)

# Route để xử lý dữ liệu từ form chỉnh sửa
@app.route('/edit', methods=['POST'])
def update_profile():
    user_data['name'] = request.form.get('name')
    user_data['email'] = request.form.get('email')
    user_data['age'] = request.form.get('age')
    user_data['bio'] = request.form.get('bio')
    
    return redirect(url_for('profile'))  # Chuyển hướng về trang hiển thị thông tin

if __name__ == '__main__':
    app.run(debug=True)

