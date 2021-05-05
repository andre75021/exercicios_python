"""Avaliacao1."""
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
