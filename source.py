import urllib.request 
from urllib.request import urlopen
html = urlopen("https://www.google.com/")
content = html.read()
print(content)


request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/') 
print(request_url.read()) 


# install it
urllib.request.install_opener(opener)
f = urllib.request.urlopen('https://www.python.org/')
