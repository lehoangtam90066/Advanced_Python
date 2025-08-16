from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách các bài đăng
blog_posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    content = request.form['content']
    
    # Thêm bài đăng mới vào danh sách
    blog_posts.append({'title': title, 'content': content})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
