#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pregunta cantas operacións vai realizar (entre 0 e 30).
# Pide ao usuario o resultado dunha operacion de 2 díxitos.
# Sé é correcto súmase un punto, móstrase a mensaxe correcta e unha nova operacion.
# En caso incorrecto, réstase 1, e móstrase outra operación operación.
# Mostra o tempo de realización.
import datetime
import random
import math
puntuacion = 0
def estableceCalculo():
    num1, num2 = numAleatorio()
    calculo = random.randrange(0,5)
        
    if calculo == 0:
        resultado = num1 + num2
        resposta = int(input("Canto é a suma de {} máis {} ". format(str(num1), str(num2))))
         darResultado(resposta, resultado)

    elif calculo == 1:
        resultado = num1 - num2
        resposta = int(input("Canto é a resta de {} menos {} ". format(str(num1), str(num2))))
         darResultado(resposta, resultado)

    elif calculo == 2:
        resultado = num1 * num2
        resposta = int(input("Canto é {} por {} ". format(str(num1), str(num2))))
         darResultado(resposta, resultado)

    elif calculo == 3:
        resultado = num1 // num2
        resposta = int(input("Canto é {} dividido por {} ". format(str(num1), str(num2))))
         darResultado(resposta, resultado)

    elif calculo == 4:
        resultado = num1 ** 2
        resposta = int(input("Canto é {} ao cadrado?". format(str(num1))))
         darResultado(resposta, resultado)

    elif calculo == 5:
        resultado = math.sqrt(num1)
        resposta = int(input("Cal é a raiz cadrada de {} ".format(str(num1))))
         darResultado(resposta, resultado)

def numAleatorio():
    aleatorio1 = random.randrange(1,10)
    aleatorio2 = random.randrange(1,10)
    return aleatorio1, aleatorio2 

def darResultado(resposta, resultado):
    global puntuacion
    if resposta == resultado:
        puntuacion = puntuacion + 1
        print("Resultado correcto. Tes {} puntos".format(puntuacion))
    else:
        puntuacion = puntuacion -1
        if puntuacion < 0:
            puntuacion = 0
            print("Resultado incorrecto. Tes {} puntos".format(puntuacion))


inicio = datetime.datetime.now()
operacions = int(input("Cantas operacións queres adiviñar?: "))



for o in range(0,operacions):
    print(puntuacion)
    estableceCalculo()

final = datetime.datetime.now()
realizacion = final-inicio
print("Tempo de realización: " + str(realizacion))

# IMPORTACIÓNS 
# from random import randint 
# from time import time 
# tempo_inicial = time 
# enteiro aleatorio 
# randint(0,9)
