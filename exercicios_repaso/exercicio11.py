#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Garda nun ficheiro os números do 1 ao 1 000 000

file = open("numeros.txt", "w")
for i in range(1,1000001): # O limite superiior é iguan a n+1
    text = "{} ".format(str(i)) # forta
    file.write(text)
file.close()

