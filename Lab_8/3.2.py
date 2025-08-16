import urllib.request

try:
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
except urllib.error.URLError as e:
    print(f"Error occurred: {e}")
