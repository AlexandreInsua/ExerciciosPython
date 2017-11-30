# Pide constantemente numeros ata que se introduce -1. Logo mostra a súa suma, e o maior.
print("Suma de números (-1 para finalizar)")
numeros = []
n = 0
suma = 0
media = 0
maior = 0 

while n != -1:
    numeros.append(n) 
    n = float(input("Introduza un número: "))
for i in numeros:
    suma += i
    media = suma/len(numeros)
    if maior < i:
        maior = i
    
print("A suma dos números é: ", suma)
print("A media dos números é: ", media)
print("O maior dos números é: ", maior)