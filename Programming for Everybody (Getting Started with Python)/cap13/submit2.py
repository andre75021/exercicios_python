"""Extraindo dados de XML."""
import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
total = 0
while True:
    url = "http://py4e-data.dr-chuck.net/comments_1099468.xml"
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print(data.decode())
    tree = ET.fromstring(data)
    results = tree.findall('.//count')
    for contador in results:
        total += int(contador.text)
    break
print(total)
