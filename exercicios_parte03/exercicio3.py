
# 3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
# Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer 
# parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
total = 0

for num in range(0,100,2):
    total = total + num
print("Total:", total)