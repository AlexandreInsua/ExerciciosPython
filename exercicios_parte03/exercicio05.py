# 5) Se parte de que existe una lista con números numeros = [1, 3, 6, 9]. 
#  Realiza un programa que pida al usuario un número entero del 0 al 9, mientras el usuario no inserte un numero correcto (0-9)
#  se repetirá el proceso volviendo a pedir otro número.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
# Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

print(" ~~ verificando números ~~")
numeros = [1, 3, 6, 9]
validos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = int(input("Introduza un número (de 0 a 9): "))

while num not in validos:
    num = int(input("Introduza un número correcto, por favor (de 0 a 9):" ))

if num in numeros:
    print("Acertaches, {} está na lista de números.".format(num))
else:
    print("Mal! :(\n{} non está na lista de números.".format(num))