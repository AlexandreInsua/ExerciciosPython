# Pide por pantalla constantemente un nombre de persona y una edad.
# Esos datos los irás guardando en una colección de tipo diccionario.
# Cuando te inserten el nombre FIN.
# El programa mostrará por pantalla todos los datos guardados


diccionario = {}
nombre=""
while(nombre.lower() != "fin"):
    nombre = input("Introduce un nombre:")
    if(nombre.lower()!="fin"):
        edad = int( input("Introduce una edad:") )
        diccionario[nombre]=edad

for clave,valor in diccionario.items():
    print(clave+"-"+str(valor))
