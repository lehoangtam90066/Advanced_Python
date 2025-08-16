from flask import request

# Đây là một controller có thể được gọi từ application.py
def ham1():
    data = request.args.get('data')
    # Xử lý logic ở đây
    return f'Bạn đã gửi: {data}'
