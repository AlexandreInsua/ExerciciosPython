# Realiza un programa en python que pida 2 números enteros por pantalla (mínimo y máximo). 
# El programa pintará en pantalla los números comprendidos entre esos 2 valores.
# Se mostrará un error si los 2 números son iguales o si el valor mínimo es mayor que el máximo.


num1 = int(input("Inserir o mínimo: "))
num2 = int(input("Inserir o máximo: "))

if num1 == num2:
    print("Os números non poden der iguais.")
    exit
elif num1 > num2:
    print("O primeiro número non pode ser maior que segundo")
else:
    print("Os número comprendidos entre {} e {} son: ".format(num1, num2))
    for i in range(num1 + 1,  num2):
        print(i)