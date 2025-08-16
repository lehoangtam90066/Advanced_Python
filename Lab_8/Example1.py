import urllib.request
url_google = urllib.request.urlopen('http://www.google.com/')
print(url_google.read())