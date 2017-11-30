# Pide constantemente numeros ata que se introduce -1. Logo mostra a súa suma.
print("Suma de números (-1 para finalizar)")
num1 = 0
sum1 = 0
while num1 != -1:
    num1 = float(input("Introduza un número: "))
    sum1 += num1
print("A suma dos número é: ", sum1)