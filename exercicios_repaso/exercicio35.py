# Crea un programa en python. 
# * Crea una colección de tipo lista de nombres de alumnos y muéstrala por pantalla.
# * Crea un diccionario y rellénalo con nombres de alumnos(key) y sus notas(value). 
# Muestra el diccionario por pantalla.
# * Crea una colección tipo tupla con nombres de profesores y muéstrala por pantalla.



#listas, diccionarios y tuplas
# ---------------  listas   ------------------
listaAlumnos=[]
listaAlumnos.append("Ana")
listaAlumnos.append("Jose")
listaAlumnos.append("Rosa")

#print(listaAlumnos)
for nombre in listaAlumnos:
    print(nombre)

for i in range(0,len(listaAlumnos)):
    #print(i)
    print(listaAlumnos[i])

listaAlumnos.remove("Rosa")

# ------------------ diccionarios -----------clave,valor---------------
notasAlumnos = {}
notasAlumnos["Pedro"] = 4
notasAlumnos["Juan"] = 6
notasAlumnos["Maria"] = 9

print("La nota de maría es: "+ str(notasAlumnos["Maria"]) )
for clave in notasAlumnos:
    print(clave + "=" + str (notasAlumnos[clave])  )

for clave, valor in notasAlumnos.items():
    print(clave + "=" + str(valor)  )

notasAlumnos.pop("Juan")
notasAlumnos["Maria"]=8

# -------------------- tuplas ------------------------------
profesores = ("Angel", "Bea", "Pepe")

for nombreProfe in profesores:
    print(nombreProfe)

