import urllib.error
import urllib.request
try:
    url_google = urllib.request.urlopen('https://www.huynhhoc.com/')
    print(url_google.real())
except urllib.error.URLError as e:
    print('Error: ', e.reason)