#  1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

print("Operacións con dous números.")
num1 = int(input("Inserte un número: "))
num2 = int(input("Inserte outro número: "))
opcion = int(input("Inserte a operación que desexe realizar:\n1.- Sumar.\n2.- Restar.\n.3.- Multiplicar.\n4.- Sair."))
while opcion != 4:
    if opcion == 1:
        resultado = num1 + num2
        print("A suma de {} e {} é {}".format(num1,num2,resultado))
        break;
    elif opcion == 2:
        resultado = num1 - num2
        print("A resta de {} menos {} é {}".format(num1,num2,resultado))
        break;
    elif opcion == 3:
        resultado = num1 * num2
        print("O producto de {} por {} é {}".format(num1,num2,resultado)) 
        break;
    elif opcion == 4:
        print("Fin de programa")
        sys.exit
    else:
        print("A opción debe ser entre 1 e 4.")
        break;

# Solución de Ángel: non usa variables
# if opcion == 1:
#    print("La suma de",n1,"+",n2,"es",n1+n2)
# elif opcion == 2:
#     print("La resta de",n1,"-",n2,"es",n1-n2)
# elif opcion == 3:
#    print("El producto de",n1,"*",n2,"es",n1*n2)
# else:
#    print("Opción incorrecta")
