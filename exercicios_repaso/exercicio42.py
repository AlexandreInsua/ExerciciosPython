# Crea un diccionario
# rellenalo con nombres de persona(key) y los nombres de sus hijos(value)
# Muestra el diccionario por pantalla (nombres de las personas junto con sus hijos)

hijosPersona = {}

hijosPersona["Maria"] = ["pepito","luisito","anita"]
hijosPersona["Pedro"]= ["juanito","luisita"]
hijosPersona["Manuel"]=["pedrito"]


for clave in hijosPersona:
   print(clave+" Tiene los siguientes hijos")
   for hijo in hijosPersona[clave]:
       print("    "+hijo)

#otra forma clave/valor
for clave,valor in hijosPersona.items():
   print(clave+" Tiene los siguientes hijos")
   for hijo in valor:
       print("    "+hijo)


