import requests
import pandas as pd

# Danh sách video ID cần truy vấn
video_ids = ["7cmvABXyUC0", "9eH-7x7swEM", "JndzGxbwvG0", "l0P5_E6J_g0"]

# Thay thế bằng API KEY của bạn
API_KEY = "YOUR_API_KEY"
base_url = "https://www.googleapis.com/youtube/v3/videos"

# Tạo danh sách để lưu trữ các thông tin video
items = []

# Lặp qua từng video ID để lấy thông tin
for video_id in video_ids:
    parameters = {
        'part': 'statistics',  # Chọn phần cần lấy dữ liệu
        'id': video_id,
        'key': API_KEY
    }

    response = requests.get(base_url, params=parameters)

    # Kiểm tra mã trạng thái phản hồi
    if response.status_code == 200:
        data = response.json()
        
        # Lấy thông tin từ dữ liệu trả về
        if 'items' in data and len(data['items']) > 0:
            statistics = data['items'][0]['statistics']
            item = {
                'videoid': video_id,
                'viewCount': statistics.get('viewCount', 0),
                'likeCount': statistics.get('likeCount', 0),
                'dislikeCount': statistics.get('dislikeCount', 0),
                'favoriteCount': statistics.get('favoriteCount', 0),
                'commentCount': statistics.get('commentCount', 0)
            }
            items.append(item)
        else:
            print(f"No data found")
