# Pide por pantalla nome de persoas, que garda nun array.
# Cando se introduce un valor valeiro, gárdatos nun ficheiro chamado nomes.txt

name = input("Introduza un nome: " )
list_of_names = []

while name != "":
    list_of_names.append(name)
    name = input("Introduza outro nome: ")

print(list_of_names)

file = open("nomes.txt", "W")
for n in list_of_names:
    file.write(n + "\n")
file.close()