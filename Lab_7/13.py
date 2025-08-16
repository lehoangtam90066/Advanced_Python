from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Dữ liệu mẫu cho người dùng
user_data = {
    'name': 'Lê Hoàng Tâm',
    'email': 'tam.2274802010780@vanlanguni.vn',
    'age': 20,
    'bio': 'thích đi học và chậm deadline',
    'avatar': 'static/picture.png',
    'is_following': False,
    'follower_count': 120,
    'following': []  # Danh sách trang đã follow
}

# Danh sách các trang có thể follow
pages = [
    {'name': 'Tech Blog', 'category': 'Technology'},
    {'name': 'Life Tips', 'category': 'Lifestyle'},
    {'name': 'Health Hub', 'category': 'Health'},
    {'name': 'EduWorld', 'category': 'Education'}
]

# Route cho trang hiển thị thông tin cá nhân
@app.route('/')
def profile():
    return render_template('profile_display.html', user=user_data)

# Route hiển thị các trang mà người dùng đã follow
@app.route('/following')
def following():
    return render_template('following.html', following=user_data['following'])

# Route để follow trang
@app.route('/follow/<page_name>')
def follow_page(page_name):
    for page in pages:
        if page['name'] == page_name and page not in user_data['following']:
            user_data['following'].append(page)
            user_data['follower_count'] += 1
            break
    return redirect(url_for('following'))

# Route để unfollow trang
@app.route('/unfollow/<page_name>')
def unfollow_page(page_name):
    user_data['following'] = [page for page in user_data['following'] if page['name'] != page_name]
    user_data['follower_count'] -= 1
    return redirect(url_for('following'))

if __name__ == '__main__':
    app.run(debug=True)
