from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Cần thiết cho flash và CSRF

# Định nghĩa lớp form với FlaskForm
class NameForm(FlaskForm):
    name = StringField('Nhập tên của bạn:', validators=[DataRequired()])
    submit = SubmitField('Gửi')

# Route trang chính
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # Gửi thông báo flash
        flash(f'Chào mừng, {form.name.data}!')
        return redirect(url_for('success'))
    return render_template('form.html', form=form)

# Route trang hiển thị thông báo flash
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
