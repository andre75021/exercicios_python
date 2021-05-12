"""Web service de geocodigo do google."""
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    local = input('Entre com o endereço: ')
    if len(local) < 1:
        break
    parametro = dict()
    parametro['address'] = local
    if api_key is not False:
        parametro['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parametro)
    print(url)
    uh = urllib.request.urlopen(url, context=ctx)
    dados = uh.read().decode()
    print('dados obtidos: ', len(dados))
    print(dados)
    try:
        js = json.loads(dados)
    except Exception as e:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Falha em obter dados')
        continue
    print(json.dumps(js, indent=4))
    latitude = js['results'][0]['geometry']['location']['lat']
    longitude = js['results'][0]['geometry']['location']['lng']
    endereço_formatado = js['results'][0]['formatted_address']
    print('Latitude: ', latitude)
    print('Longitude: ', longitude)
    print(endereço_formatado)
