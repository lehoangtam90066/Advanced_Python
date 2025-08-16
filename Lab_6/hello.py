from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Khóa bảo mật cho CSRF

# Định nghĩa form class
class HelloForm(FlaskForm):
    name = StringField('Nhập tên của bạn', validators=[DataRequired()])
    submit = SubmitField('Gửi')

# Route cho trang chính
@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('hello', name=name))
    return render_template('hello.html', form=form)

# Route cho trang chào
@app.route('/hello/<name>')
def hello(name):
    return f'Xin chào, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
