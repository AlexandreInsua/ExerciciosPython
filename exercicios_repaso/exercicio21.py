# Realiza un programa en python que pida constantemente números por pantalla al usuario. 
# El programa terminará cuando se inserte un numero negativo.
# Se mostrarán todos los números insertados por pantalla y se guardarán todos ellos en el disco duro.
# (NOTA: no se guadrá el último número negativo insertado)

# crea una lista valeira para gardar os número 
numberList = []

num = int(input("Inserte un número: "))


while num > 0:
    numberList.append(num)
    texto = input("Inserte un número: ")
    num = int(texto)

print(numberList)

acumulador = ""

file = open("num21.txt","w")

for n in numberList:
    acumulador = acumulador + str(n) + ","

acumulador = acumulador[:-1]

file.write(acumulador)

file.close()
