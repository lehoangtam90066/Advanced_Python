from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách các bài đăng với bình luận
blog_posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    content = request.form['content']
    
    # Thêm bài đăng mới vào danh sách với danh sách bình luận rỗng
    blog_posts.append({'title': title, 'content': content, 'comments': []})
    
    return redirect(url_for('index'))

@app.route('/comment/<int:post_id>', methods=['POST'])
def comment(post_id):
    comment_text = request.form['comment']
    
    # Kiểm tra xem bài đăng tồn tại và thêm bình luận vào bài đăng
    if 0 <= post_id < len(blog_posts):
        blog_posts[post_id]['comments'].append(comment_text)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
