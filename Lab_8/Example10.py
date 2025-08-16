import json
import sys


sys.stdout.reconfigure(encoding='utf-8')

# Chuỗi JSON mẫu
json_data = '''{
    "kind": "Response",
    "items": [
        {
            "id": "7cmvABXyUC0",
            "statistics": {
                "viewCount": "784",
                "commentCount": "2"
            }
        }
    ],
    "pageInfo": {
        "totalResults": 1,
        "resultsPerPage": 1
    }
}'''


data = json.loads(json_data)


print("Kind:", data['kind'])
print("Video ID:", data['items'][0]['id'])
print("View Count:", data['items'][0]['statistics']['viewCount'])
print("Comment Count:", data['items'][0]['statistics']['commentCount'])


json_string = json.dumps(data, indent=4)
print("\nChuỗi JSON sau khi chuyển đổi:")
print(json_string)
