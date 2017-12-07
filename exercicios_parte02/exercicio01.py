# 1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
# (es suficiente con mostrar True o False):
# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

print("Vamos a analizar dous números\n---------------------")
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

if num1 == num2:
    print("{} e {} son iguais.".format(num1,num2))
else:
    print("Os números son diferentes: ")
    if num1 < num2:
        print("{} é maior que {}.".format(num1, num2))
    else:
        print("{} é menor que {}.".format(num1, num2))    


# Solución de Angel
# print("¿Son iguales? ", n1 == n2)
# print("¿Son diferentes?", n1 != n2)  /*** Se non son iguais, son diferentes! ***\
#print("¿El primero es mayor que el segundo?", n1 > n2)
#print("¿El segundo es mayor o igual que el primero?", n1 <= n2)
