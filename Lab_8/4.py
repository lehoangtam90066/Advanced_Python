import urllib.request
import os
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Địa chỉ trang web chứa các hình ảnh
base_url = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/"
# Lấy nội dung HTML từ trang web
response = urllib.request.urlopen(base_url)
html = response.read().decode('utf-8')

# Sử dụng BeautifulSoup để phân tích HTML
soup = BeautifulSoup(html, 'html.parser')

# Tìm tất cả các thẻ <img> và lấy các URL hình ảnh
img_tags = soup.find_all('img')

# Lưu tất cả các hình ảnh
for img in img_tags:
    img_url = img.get('src')
    if img_url:  # Kiểm tra nếu img_url không phải là None
        # Kết hợp URL nếu cần thiết
        img_url = urljoin(base_url, img_url)
        # Tạo tên tệp để lưu
        img_name = os.path.basename(img_url)
        
        # Kiểm tra nếu tệp đã tồn tại và thêm số vào tên tệp nếu cần
        counter = 1
        original_name, file_extension = os.path.splitext(img_name)
        while os.path.exists(img_name):
            img_name = f"{original_name}_{counter}{file_extension}"
            counter += 1
        
        # Tải xuống và lưu hình ảnh
        try:
            urllib.request.urlretrieve(img_url, img_name)
            sys.stdout.buffer.write(f"Lưu ảnh: {img_name} từ {img_url}\n".encode('utf-8'))
        except Exception as e:
            sys.stdout.buffer.write(f"Lỗi khi lưu ảnh {img_name}: {e}\n".encode('utf-8'))
