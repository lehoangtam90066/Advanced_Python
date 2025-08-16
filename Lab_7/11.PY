from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu bài đăng mẫu (thay cho cơ sở dữ liệu)
posts = [
    {'id': 1, 'title': 'First Blog Post', 'content': 'This is the first post content', 'category': 'Technology'},
    {'id': 2, 'title': 'Second Blog Post', 'content': 'This is the second post content', 'category': 'Lifestyle'}
]

# Route trang chủ hiển thị các bài đăng
@app.route('/')
def home():
    return render_template('blog_home.html', posts=posts)

# Route để thêm bài đăng mới
@app.route('/post', methods=['POST'])
def add_post():
    new_id = len(posts) + 1
    title = request.form['title']
    content = request.form['content']
    category = request.form['category']
    posts.append({'id': new_id, 'title': title, 'content': content, 'category': category})
    return redirect(url_for('home'))

# Route để chỉnh sửa bài đăng
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if request.method == 'POST':
        # Cập nhật dữ liệu bài đăng
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        post['category'] = request.form['category']
        return redirect(url_for('home'))
    return render_template('edit_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
