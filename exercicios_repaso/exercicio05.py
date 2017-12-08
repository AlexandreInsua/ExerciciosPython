# Crea manualmente un fichero llamado numeros.txt 
# Rellena este fichero con números separados por punto y coma. 
# Ej:3;5;66;3;456;22;4;2;45;2;5 
# Crea un programa en python que lea este fichero y eleve al cuadrado todos los números.
#  Y guarda el resultado en otro fichero llamado numeros2.txt


file = open("numbers.txt", 'r')
text = file.read()

numbers = text.split(";") 

square_numbers = []

file2 = open("numbers2.txt", "w")

for number in numbers:
    number  = int(number)
    square = number * number
    file2.write(str(square) + ";")
    square_numbers.append(square)

print("Serie inicial: ", numbers, "\nElevada a 2: ", square_numbers)


file.close()
