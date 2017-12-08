# Escribir en python una función que tome un carácter y devuelva True 
# si es una vocal, de lo contrario devuelve False.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def is_vowel(l):
    if l in vowels:
        print (l, " é vogal.")
    else:
        print(l, " é consonante.")

    
is_vowel("a")
is_vowel("g")
is_vowel("e")
is_vowel("t")
is_vowel("o")