# 2) Utilizando operadores lógicos, determina si una cadena de texto introducida
# por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10
# (es suficiente con mostrar True o False):


print("Vamos a analizar a lonxitude dun String")
string = input("Introduza a cadea que quere analizar: ")
if 3 <= len(string) < 10:
    print("A cadea cumpre con parámetros.")
else:
    print("A cadea non cumpre con parámetros.")

# Solución de Ángel
# cadena = input("Escribe una cadena: ")
# print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?",
# len(cadena) >= 3 and len(cadena) < 10 )
