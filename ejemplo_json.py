# -*- coding: utf-8 -*-
#importacion de librerias
import urllib.request
import json

#leer json local
data = json.loads(open("cancha.json").read())
print (data)
print ((data[2]))

#leer json url
url = "http://servidor/data/cancha.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())
print (data)
print ((data[2]))

#leer json api
url = "http://localhost:11551/api/datos"
try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    print (data)
    print ((data[2]))
    # Loop para mostrar resultados
    for item in data:
        print ((item['Name']))

except urllib.error.HTTPError as e:
    print((e.code))