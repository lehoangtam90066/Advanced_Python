import urllib.request

url = 'https://www.google.com/search?q=test'
with urllib.request.urlopen(url) as x:
    html_content = x.read()
    print(html_content)  
