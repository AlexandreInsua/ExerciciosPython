# 2) Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

print("Lendo números impares: ")
num = int(input("Introduce un número: "))

while num % 2 == 0:
    num = int(input("Introduce un número: "))
    print("{} é nun número impar.".format(num))


# Solución de Ángel
# numero = 0
# while numero % 2 == 0:  # Mientras sea par repetimos el proceso
#    numero = int(input("Introduce un número impar: ") )
