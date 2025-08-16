from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Định nghĩa một lớp Form bằng Flask-WTF
class DienTen(FlaskForm):
    ten = StringField('Tên bạn là gì?', validators=[DataRequired()])
    nut_guilenserver = SubmitField('Gửi')

# Route cho trang biểu mẫu
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DienTen()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return 'Đã nhận dữ liệu!'

if __name__ == '__main__':
    app.run(debug=True)
