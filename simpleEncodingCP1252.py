#!/usr/bin/env python
# -*- coding: cp1252 -*-

"""
	Este script es una copia de "simpleEncodingUTF8.py" para mostrar 
	m�s claramente algunos posibles errores de codificaci�n
"""

# La librer�a "sys" no permite acceder a informaci�n del sistema
import sys


# Definimos una lista de cadenas de texto con acentos, di�resis y ene
texto_normal = [
	"El veloz murci�lago hind� com�a feliz cardillo y kiwi.\nLa cig�ena tocaba el saxof�n detr�s del palenque de paja.",
	"El ping�ino Wenceslao hizo kil�metros bajo exhaustiva lluvia y fr�o, anoraba a su querido cachorro.",
	"Exh�banse politiquillos zafios,\ncon orejas kilom�tricas\n\ty unas de gavil�n.",
	"�!Joven �emponzonado� con el whisky, qu� fin� te aguarda exhibir!",
	"???????????",
	"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	"???????????",
	"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]
print ">> IMPRIMIMOS CADENAS DE TEXTO NORMAL DIRECTAMENTE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_normal:
	print t

print
print ">> IMPRIMIMOS CADENAS DE TEXTO NORMAL DECODIFICADAS (UTF-8)"
# Imprimimos estas cadenas a la consola decodificadas (utf-8)
for t in texto_normal:
	print t.decode("cp1252")


texto_unicode = [
	u"El veloz murci�lago hind� com�a feliz cardillo y kiwi.\nLa cig�ena tocaba el saxof�n detr�s del palenque de paja.",
	u"El ping�ino Wenceslao hizo kil�metros bajo exhaustiva lluvia y fr�o, anoraba a su querido cachorro.",
	u"Exh�banse politiquillos zafios,\ncon orejas kilom�tricas\n\ty unas de gavil�n.",
	u"�!Joven �emponzonado� con el whisky, qu� fin� te aguarda exhibir!",
	u"???????????",
	u"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	u"???????????",
	u"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]

print
print ">> IMPRIMIMOS CADENAS DE TEXTO UNICODE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_unicode:
	print t


texto_raw_unicode = [
	ur"El veloz murci�lago hind� com�a feliz cardillo y kiwi.\nLa cig�ena tocaba el saxof�n detr�s del palenque de paja.",
	ur"El ping�ino Wenceslao hizo kil�metros bajo exhaustiva lluvia y fr�o, anoraba a su querido cachorro.",
	ur"Exh�banse politiquillos zafios,\ncon orejas kilom�tricas\n\ty unas de gavil�n.",
	ur"�!Joven �emponzonado� con el whisky, qu� fin� te aguarda exhibir!",
	ur"???????????",
	ur"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	ur"???????????",
	ur"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]

print
print ">> IMPRIMIMOS CADENAS DE TEXTO RAW-UNICODE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_raw_unicode:
	print t