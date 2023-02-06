from urllib.request import urlopen
html = urlopen("http://www.google.com/")
content = html.read()
print(content)
