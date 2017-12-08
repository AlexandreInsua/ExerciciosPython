# Realiza un programa en python que pida la anchura de un triángulo 
# y lo pinte en la pantalla (en modo consola) mediante asteriscos.

anchura = int(input("inserte a anchura do lado: "))

aux = "*"

for i in range(anchura):
    print(aux)
    aux = aux + "*"
