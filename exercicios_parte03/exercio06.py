
# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).


print("~~ Creando listas ~~")

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []


for i in range(0,11):
    lista1.append(i)

for i in range(-10,1):
    lista2.append(i)

for i in range(0,21,2):
    lista3.append(i)

for i in range(-19,0,2):
    lista4.append(i)

for i in range(0,51,5):
    lista5.append(i)


print("Números do 0 ao 10: ", lista1)
print("Números do -10 ao 0: ", lista2)
print("Números pares do 0 ao 20: ", lista3)
print("Números impares do -20 ao 0: ", lista4)
print("Números múltiplos de 5 do 0 ao 50: ", lista5)

