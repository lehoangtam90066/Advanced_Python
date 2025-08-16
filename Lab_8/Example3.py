import urllib.parse
import urllib.request

url = 'https://www.python.org/search'
values = {'q': 'basic'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
