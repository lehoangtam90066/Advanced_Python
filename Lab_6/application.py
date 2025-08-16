from flask import Flask
from config import Config  # Import cấu hình từ file config.py

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config.from_object(Config)

# Import routes và các logic từ các module khác
from services import ham1

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
