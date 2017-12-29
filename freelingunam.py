#-*- coding: utf-8 -*-
import requests
"""
file: Archivo a procesar
outf: Tipo de análisis a realizar
  tagged  Tokenizado, lematizado y etiquetado POS.
  parsed  Parseado sintácticamente
  dep     Árbol de dependencias
lang: Idioma
  es      Español
  en      Inglés
  fr      Francés
  auto    Detección automática 
format: Formato de la respuesta
  plain   Texto plano, tal como Freeling arroja el resultado
  json    JSON, estructurado de acuerdo al análisis realizado
  html    HTML, para ser mostrado en una página web
"""

#Archivo a ser enviado
files = {'file': open('test/texto1.txt', 'rb')}
#Parámetros
params = {'outf': 'tagged', 'format': 'json'}
#Enviar petición
url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
r = requests.post(url, files=files, params=params)
#Convertir de formato json
obj = r.json()

print(obj)
#Ejemplo, obtener todos los lemas
# for sentence in obj:
#     for word in sentence:
#         print(word["lemma"])