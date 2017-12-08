
# Programa (en python) que calcule áreas de: cuadrados(en función de su lado),
# rectángulos(en función de sus lados, circunferencias(en función de su radio) y triángulos
# rectángulos(en función de su base y su altura).
# Primero se pedirá el objeto que se va a calcular(cuadrado, rectángulo, circunferencia o triangulo
#  rectangulo.
# Luego se pedirán los datos necesarios de esa figura y se mostrará el valor del area por pantalla.


print("Selecciona tipo de figura")
print("1- Cuadrado")
print("2- Rectángulo")
print("3- Circunferencia")
print("4- Triangulo rectángulo")
print("5- Salir")
tipo = int(input("Seleccona opción:"))


if tipo == 5:
    exit()


print("Introduce los datos necesarios")
if tipo == 1:
    lado = float(input("Introduce el lado de cuadrado:"))
    area = lado * lado
elif tipo == 2:
    base = float(input("Introduce la base del rectangulo:"))
    altura = float(input("Introduce la altura del rectangulo:"))
    area = base * altura
elif tipo == 3:
    radio = float(input("Introduce el radio de la circunferencia:"))
    area = 3.141519 * radio * radio
elif tipo == 4:
    base = float(input("Introduce la base del triangulo:"))
    altura = float(input("Introduce la altura del triangulo:"))
    area = base * altura / 2.0
else:
    area = 0
    print("ERROR EN LA OPCIÓN SELECCIONADA")


print("Area:" + str(area))
