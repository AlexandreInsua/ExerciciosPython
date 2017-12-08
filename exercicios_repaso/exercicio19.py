# Realiza una función en python que tome como parámetro una cadena de texto,
# esta función nos indicará cuantas mayúsculas y cuantas minúsculas tiene.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def vowels_consonants(string):
    count_vowels = 0
    count_consonants = 0

    for letter in string:
        if letter in vowels:
            count_vowels = count_vowels + 1
        elif letter == '':
            pass
        else:
            count_consonants = count_consonants + 1
    
    print("Número de vogais: ", str(count_vowels))
    print("Numero de consonantes: ", str(count_consonants))

texto = "O masivo avance dos eucaliptos no bosque galego representa un dos principais sinais de alerta no monte galego"

vowels_consonants(texto)

# Ángel usa o método isalpha()
# def contador_Mayus_Minis(cadena):
#    contador_mayus = 0
#    contador_minus = 0
#    for i in cadena:
#        if i.isalpha():
#            if i == i.upper():
#                contador_mayus +=1
#            else:
#                contador_minus +=1
     
#    return contador_mayus, contador_minus

# print(contador_Mayus_Minis("A n G;el-ñas"))
