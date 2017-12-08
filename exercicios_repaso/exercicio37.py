# Programa que traduzca una palabra o frase a código morse. (busca en la wikipedia para más información)
# Intentar hacer el ejercicio usando diccionarios.
# Añadir una función que reproduzca el sonido del código morse.
# Pista:

import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second

winsound.Beep(Freq,Dur)

# import winsound

def convertirMorse(frase):
   alfabeto={}
   alfabeto["a"]=".-"
   alfabeto["b"]="-..."
   alfabeto["c"]="-.-."
   alfabeto["d"]="-.."
   alfabeto["e"]="."
   alfabeto["f"]="..-."
   alfabeto["g"]="--."
   alfabeto["h"]="...."
   alfabeto["i"]=".."
   alfabeto["j"]=".---"
   alfabeto["k"]="-.-"
   alfabeto["l"]=".-.."
   alfabeto["m"]="--"
   alfabeto["n"]="-."
   alfabeto["ñ"]="--.--"
   alfabeto["o"]="---"
   alfabeto["p"]=".--."
   alfabeto["q"]="--.-"
   alfabeto["r"]=".-."
   alfabeto["s"]="..."
   alfabeto["t"]="-"
   alfabeto["u"]="..-"
   alfabeto["v"]="...-"
   alfabeto["w"]=".--"
   alfabeto["x"]="-..-"
   alfabeto["y"]="-.--"
   alfabeto["z"]="--.."
   alfabeto["0"]="-----"
   alfabeto["1"]=".----"
   alfabeto["2"]="..---"
   alfabeto["3"]="...--"
   alfabeto["4"]="....-"
   alfabeto["5"]="....."
   alfabeto["6"]="-...."
   alfabeto["7"]="--..."
   alfabeto["8"]="---.."
   alfabeto["9"]="----."
   alfabeto["."]=".-.-.-"
   alfabeto[","]="-.-.--"
   alfabeto["?"]="..--.."
   alfabeto["\""]=".-..-."
   alfabeto["!"]="--..--"
   alfabeto[" "]="/"



   morse = ""
   for letra in frase:
       try:
           morse = morse + alfabeto[letra]
       except:
           #print("no existe ese caracter en morse")
           pass
   return morse


def sonidoMorse(frase):
   morse = convertirMorse(frase)
   for simbolo in morse:
       if(simbolo == "."): # reproduzco un punto (1/2 segundo)
           Freq = 1500 # Set Frequency To 2500 Hertz
           Dur = 50 # Set Duration To 1000 ms == 1 second
           winsound.Beep(Freq,Dur)
       elif (simbolo == "-"):# reproduzco una raya (1 segundo)
           Freq = 1500 # Set Frequency To 2500 Hertz
           Dur = 200 # Set Duration To 1000 ms == 1 second
           winsound.Beep(Freq,Dur)
       else: #reproduzco un espacio (2 segundos)
           Freq = 37 # Set Frequency To 2500 Hertz
           Dur = 1000 # Set Duration To 1000 ms == 1 second
           winsound.Beep(Freq,Dur)

  
  


print( convertirMorse("sos") )
# sonidoMorse("sos")
print( convertirMorse("aqui grupo 003. chegamos a posicion preliminar"))
sonidoMorse("aqui grupo 003. chegamos a posicion preliminar")