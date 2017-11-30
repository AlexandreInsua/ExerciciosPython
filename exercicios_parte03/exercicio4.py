# 4) Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:

print("~~ Sumando números ~~")
num = int(input("Introduza o número de cifras: "))
suma = 0
for i in range(0,num):
    sumando = int(input("Introduza un número: "))
    suma = suma + sumando
print("A suma dos {} números é {}. A media é {}".format(num, suma, suma / num))