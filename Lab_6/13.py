from flask import Flask, request, render_template

app = Flask(__name__)

# Route cho trang tải tệp
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']  # Lưu ý: tên phải trùng với name trong form HTML
        f.save('/var/www/uploads/uploaded_file.txt')
        return 'File uploaded successfully!'
    return render_template('upload.html')  # Hiển thị form tải tệp nếu là GET

# Route cho trang tìm kiếm
@app.route('/timkiem', methods=['GET', 'POST'])
def ham_nay_cho_trang_tim_kiem():
    noidung_cantim = ''
    if request.method == 'POST':
        noidung_cantim = request.form.get('txtnoidung', '')  # Lấy giá trị từ form
        # Xử lý tìm kiếm ở đây, ví dụ:
        return f'Bạn đã tìm kiếm: {noidung_cantim}'
    return render_template('timkiem.html')  # Hiển thị form tìm kiếm nếu là GET

if __name__ == '__main__':
    app.run(debug=True)
