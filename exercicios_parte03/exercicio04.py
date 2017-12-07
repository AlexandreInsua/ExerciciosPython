# 4) Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:

print("~~ Sumando números ~~")
num = int(input("Introduza o número de cifras: "))
suma = 0
for i in range(0,num):
    sumando = int(input("Introduza un número: "))
    suma = suma + sumando
print("A suma dos {} números é {}. A media é {}".format(num, suma, suma / num))

# Ángel non usa a variable intermedia 'sumando'
# suma = 0
# numeros = int(input("¿Cuántos números quieres introducir? ") )
# for x in range(numeros):
#    suma += float(input("Introduce un número: ") )
# print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)
