# Pregunta cantas operacións vai realizar (entre 0 e 30).
# Pide ao usuario o resultado dunha operacion de 2 díxitos.
# Sé é correcto súmase un punto, móstrase a mensaxe correcta e unha nova operacion.
# En caso incorrecto, réstase 1, e móstrase outra operación operación.
# Mostra o tempo de realización.
import datetime
import random
import math



def estableceCalculo():
    num1, num2 = numAleatorio()
    calculo = random.randrange(0,5)
        
    if calculo == 0:
        resultado = num1 + num2
        resposta = int(input("Canto é a suma de {} máis {} ", num1, num2))
        darResultado(resposta, resultado)

    elif calculo == 1:
        resultado = num1 - num2
        resposta = int(input("Canto é a resta de {} menos {} ", num1, num2))
        darResultado(resposta, resultado)

    elif calculo == 2:
        resultado = num1 * num2
        resposta = int(input("Canto é {} por {} ", num1, num2))
        darResultado(resposta, resultado)

    elif calculo == 3:
        resultado = num1 / num2
        resposta = int(input("Canto é {} dividido por {} ", num1, num2))
        darResultado(resposta, resultado)

    elif calculo == 4:
        resultado = num1 ** 2
        resposta = int(input("Canto é {} ao cadrado?".format(num1)))
        darResultado(resposta, resultado)

    elif calculo == 5:
        resultado = math.sqrt(num1)
        resposta = int(input("Cal é a raiz cadrada de {} ", num1, num2))
        darResultado(resposta, resultado)

def numAleatorio():
    aleatorio1 = random.randrange(1,99)
    aleatorio2 = random.randrange(1,99)
    return aleatorio1, aleatorio2 

def darResultado(resposta, resultado):
    if resposta == resultado:
        puntuacion += 1
        print("Resultado correcto. Tes {} puntos", puntuacion)
    else:
        puntuacion -= 1
        if puntuacion < 0:
            puntuacion = 0
            print("Resultado incorrecto. Tes {} puntos", puntuacion)


inicio = datetime.datetime.now()
operacions = int(input("Cantas operacións queres adiviñar?: "))
puntuacion = 0

for o in range(0,operacions):
    estableceCalculo()

final = datetime.datetime.now()
realizacion = final-inicio
print("Tempo de realización: " + str(realizacion))

