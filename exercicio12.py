#!/usr/bin/env python
# -*- coding: utf-8 -*-

# abre un ficheiro de texto e comproba se esta valeiro ou non

file = open("empty.txt", "r")
text =  file.read()

if text == '':
    print("O ficheiro '{}' está valeiro".format(file.name))
else:
    print(text)