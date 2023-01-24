### Regular expressions ###

# Mecanismo o estándar en el lenguaje que nos vale para inspeccionar por ejemplo si una cadena de texto tiene elementos



import re

my_string = "Esta es la lección número 7: Lección expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de fichero"

## match
match = re.match("Esta es la lección", my_string, re.I)
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones regulares", my_string))          # No lo encuentra porque busca desde el principio

print(match.span())

start, end = match.span()

print(my_string[start:end])


## search

search = re.search("lección", my_string, re.I)    # Encuentra el patrón si está aunque no esté al principio

print(search)

## findall


findall = re.findall("lección", my_string, re.I) # Saca listado de las veces que lo encuentra

print(findall)


## split

split = re.split(":", my_string)    # Busca el patrón que le digas y divide en dos partes

print(split)

## sub

print(re.sub("expresiones regulares", "RegEx", my_string))

print(my_string)


print(re.sub("Lección|lección", "LECCIÓN", my_string))

print(re.sub("[l|L]ección", "LECCIÓN", my_string))




