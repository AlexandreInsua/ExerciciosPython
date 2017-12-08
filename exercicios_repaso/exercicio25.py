# Crea un programa en python que pida por pantalla 4 valores numéricos e indique por pantalla:

# Cuál es el mayor
def elMayor(n1, n2, n3, n4):
    mayor = n1
    if n2 > mayor:
        mayor = n2
    if n3 > mayor:
        mayor = n3
    if n4 > mayor:
        mayor = n4
    return mayor

# Cuántos es la media
def laMedia(n1,n2,n3,n4):
    media = (n1+n2+n3+n4)/4.0
    return media

# Cuántos superan 5
def superan5(n1,n2,n3,n4):
    listaSuperan5 = []
    if n1 > 5:
        listaSuperan5.append(n1)
    if n2 > 5:
        listaSuperan5.append(n2)
    if n3 > 5):
        listaSuperan5.append(n3)
    if n4 > 5:
        listaSuperan5.append(n4)
    return listaSuperan5

# Cuántos están entre -3 y 3
def entremenos3y3(n1,n2,n3,n4):
    listaEntre = []
    if n1 >= -3 and n1 <= 3:
        listaEntre.append(n1)
    if n2 >= -3 and n2 <= 3:
        listaEntre.append(n2)
    if n3 >= -3 and n3 <= 3:
        listaEntre.append(n3)
    if n4 >= -3 and n4 <= 3:
        listaEntre.append(n4)
    return listaEntre

# Cuántos son negativos
def negativos(n1,n2,n3,n4):
    listaNegativos = []
    if n1 < 0:
        listaNegativos.append(n1)
    if n2 < 0:
        listaNegativos.append(n2)
    if n3 < 0:
        listaNegativos.append(n3)
    if n4 < 0:
        listaNegativos.append(n4)
    return listaNegativos

n1 = int(input("Dame el primer nº:"))
n2 = int(input("Dame el segundo nº:"))
n3 = int(input("Dame el tercer nº:"))
n4 = int(input("Dame el cuarto nº:"))

print("El mayor es:"+ str(elMayor(n1,n2,n3,n4)) )

print("La media es:"+ str(laMedia(n1,n2,n3,n4)) )

print("Los que superan 5 son:"+ str(superan5(n1,n2,n3,n4))  )

print("Estan entre -3 y 3:"+ str(entremenos3y3(n1,n2,n3,n4))  )

print("Son negativos:"+  str(negativos(n1,n2,n3,n4)) )