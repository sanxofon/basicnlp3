#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	Este programa intenta mostrar un ejemplo clásico pero considerando 
	la codificación (UTF8, UNICODE, TERMINAL). Además muestra como 
	solicitar información al usuario y como codificar/decodificar esta.
	Ejemplos de ejecución:
	>> python helloWorldUTF8.py
"""
# la función "print" se encarga de codificar apropiadamente la salida
# Al agregar la letra 'u' (antes de las comillas) definimos el texto como UNICODE
print(u"Hola, Anónimo")

# Definimos una variable desde el código
# Podemos usar cualquier palabra (no usada anteriormente)
# y le asignamos como valor una cadena de texto
# Esta variable va a guardar una cadena de texto
# Los caracteres "\n" significan "salto de línea"
pregunta = u"¿Cómo te llamas?\n>> "

# Ahora pedimos al usuario información en la terminal, guardamos la respuesta en una variable
# En Python3 TODAS las cadenas son unicode, no hay decode
nombre = input(pregunta)

# Ahora "decodificamos" el nombre de la codificación actual de la terminal a UNICODE
# Codificación actual de la terminal: "sys.stdin.encoding"
nombre = nombre

# Por último imprimimos un saludo que incluye el nommbre recibido del usuario
# Usamos el signo de suma "+" para unir dos o más cadenas de texto, sean literales o variables
print(u"¡Hola, "+nombre+"!")