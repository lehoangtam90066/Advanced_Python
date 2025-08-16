import sys
import urllib.request
import io

# Đặt encoding cho stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
        html_string = html.decode('utf-8')  # Chuyển đổi từ byte sang chuỗi
        # Ghi nội dung vào tệp
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write(html_string)
        print("Nội dung đã được ghi vào tệp output.html")
except urllib.error.URLError as e:
    print(f"Error occurred: {e}")
