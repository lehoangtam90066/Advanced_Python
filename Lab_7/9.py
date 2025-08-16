from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu bài đăng mẫu (có thể thay thế bằng cơ sở dữ liệu trong thực tế)
posts = []

# Route cho trang chủ
@app.route('/')
def blog_home():
    return render_template('blog_home.html', posts=posts)

# Route để đăng bài
@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    content = request.form['content']
    category = request.form['category']
    
    # Thêm bài đăng mới vào danh sách bài đăng
    posts.append({'title': title, 'content': content, 'category': category})
    return redirect(url_for('blog_home'))

if __name__ == '__main__':
    app.run(debug=True)
