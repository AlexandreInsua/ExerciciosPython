# Realiza un programa en python que pida constantemente palabras o frases hasta que la palabra 
# insertada sea fin.
# A continuación mostrará un menú al usuario pidiendo que seleccione una de estas opciones:

# Listar palabras que comiencen por a: la cual mostrará las palabras insertadas que comiencen 
# por la letra a (mayúscula o minúscula)
def mostrarComiencanPorA(listaFrases):
    for frase in listaFrases:
        if(frase[0] == 'a' or frase[0]=="A"):
            print(frase)

# Listar palabras que termien por n: la cual mostrará las palabras insertadas que terminen 
# por la letra n (mayúsculas o minúsculas)
def mostrarTerminanPorN(listaFrases):
    for frase in listaFrases:
        if(frase[-1] == 'n' or frase[-1]=="N"):
            print(frase)

# Listas palabras mayores de 3 letras: la cual mostrará las palabras insertadas 
# cuya longitud supera 3 caracteres.
def mostrarMas3Letras(listaFrases):
    for frase in listaFrases:
        if(len(frase) > 3):
            print(frase)

# Mostrar palabras que tengan la letra a: la cual mostrará las palabras insertadas 
# que en su interior posean la letra a.
def mostrarPalabrasLetraA(listaFrases):
    for frase in listaFrases:
        if("a" in frase):
            print(frase)

# Mostrar palabras repetidas: la cual mostrará las palabras repetidas en la lista (si es que hay alguna)
def mostrarPalabrasRepetidas(listaFrases):
    repetidas=[]
    unicas=[]
    for frase in listaFrases:
        if frase not in unicas:
            unicas.append(frase)
        else:
            if frase not in repetidas:
                repetidas.append(frase)
    print(repetidas)

# Mostrar palabras cuya longitud supere la media: la cual mostrará las palabras 
# que tengas más número de caracteres que la media de todas las palabras insertadas.
def mostrarPalabrasLenSupereMedia(listaFrases):
    media = 0
    for frase in listaFrases:
        tamanno = len(frase)
        media = media + tamanno
    media = media / len(listaFrases)
    for frase in listaFrases:
        if(len(frase) > media):
            print(frase)


frases=[]
frase=""
while(frase != "fin"):
    frase = input("Date una frase o palabra:")
    if(frase!="fin"):
        frases.append(frase)

opcion = ""
while(opcion != "7"):
    print("Pulsa 1 para palabras comiencen por a")
    print("Pulsa 2 para palabras terminen por n")
    print("Pulsa 3 para palabras mayores de 3 letras")
    print("Pulsa 4 para palabras tengan letra a")
    print("Pulsa 5 para palabras repetidas")
    print("Pulsa 6 para palabas cuya longitud supere la media")
    print("Pulsa 7 para salir")
    opcion = input("Seleciona opción:")
    if(opcion == "1"):
        mostrarComiencanPorA(frases)
    elif(opcion == "2"):
        mostrarTerminanPorN(frases)
    elif(opcion == "3"):
        mostrarMas3Letras(frases)
    elif(opcion == "4"):
        mostrarPalabrasLetraA(frases)
    elif(opcion == "5"):
        mostrarPalabrasRepetidas(frases)
    elif(opcion == "6"):
        mostrarPalabrasLenSupereMedia(frases)
