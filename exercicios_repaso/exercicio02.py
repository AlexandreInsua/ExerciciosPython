# Pide constantemente numeros ata que se introduce -1. Logo mostra a súa suma.
print("Suma de números (-1 para finalizar)")
num = 0
acumulator = 0
while num != -1:
    num = float(input("Introduza un número: "))
    acumulator += num
print("A suma dos número é: ", acumulator)