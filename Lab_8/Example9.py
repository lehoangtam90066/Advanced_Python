import requests

API_KEY = 'AIzaSyCfKDzIrnmLSyZLq_fHyKzifb_s_4p****'
video_id = '7cmvABXYuC0'
url = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&part=statistics&key=" + API_KEY
response = requests.get(url).json()
print(response)
