# Le un ficheiro txt con números separados por punto e coma e
# devólveos levados ao cadrado

file = open("numbers.txt", 'r')
text = file.read()

numbers = text.split(";") 

numbers_raised = []

for i in numbers:
    i  = int(i)
    a = i*i
    numbers_raised.append(a)

print("Serie inicial: ", numbers, "\nElevada a 2: ", numbers_raised)
file.close()
