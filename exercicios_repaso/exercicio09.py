# Pídelle ao usuario dúas palabras. Substitúe a primeira pola segunda nun ficheiro
#  que se lle pasa como argumento e crea un novo ficheiro cos cambios.


words = input("Introduza a palabra que se vai buscar e a substituta: ").split()

print("Palabra a buscar: ", words[0] , ".Palabra substituta: ", words[1])

with open("frases.txt", "r") as file
text = file.read()
print("Texto orixinal:\n")
print(text)
# metodo replace() -> devolve unha copia dun String 
# onde n subcadeas son substituídas por outras n veces
# (0 para reemprazar en todo o texto)
text2 = text.replace(words[0], words[1])

file2 = open("frases2.txt", "w")
file2.write(text2) 
print("Texto modificado:\n")
print(text2)
file.close()
file2.close()

