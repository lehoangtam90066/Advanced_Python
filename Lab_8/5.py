import csv
from urllib.request import urlopen
import sys

# Địa chỉ để đọc dữ liệu
url = 'http://sixty-north.com/c/t.txt'

# Đọc dữ liệu từ URL
with urlopen(url) as story:
    lstStory = story.readlines()

# Chuyển đổi byte thành chuỗi và loại bỏ ký tự xuống dòng
lstStory = [line.decode('utf-8').strip() for line in lstStory]

# Lưu dữ liệu vào tệp CSV
with open('story.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Ghi từng dòng vào tệp CSV
    for line in lstStory:
        writer.writerow([line])  # Ghi từng dòng dưới dạng danh sách

# Sử dụng sys.stdout.buffer.write để in thông báo
sys.stdout.buffer.write('Dữ liệu đã được lưu vào story.csv\n'.encode('utf-8'))
