
# 3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
# Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer 
# parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
total = 0

for num in range(0,101,2): #así inclúe o 100
    total = total + num
print("Total:", total)


# Solución de Ángel
# suma = sum( range(0, 101, 2) )
# print(suma)

# Segunda forma con bucles
# num = 0
# suma = 0

# while num <= 100:
#    if num % 2 == 0:
#        suma += num
#    num += 1
