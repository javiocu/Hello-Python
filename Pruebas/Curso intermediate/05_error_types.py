### Error Types ###

# Repaso sobre los tipos de error que puede lanzar python y por qué los lanza

# SyntaxError
# print "Hola comunidad!" # Error, falta algún tipo de elemento de sintaxis, algún paréntesis, alguna comilla no cerrada, etc.

print ("Hola comunidad!")


# NameError
# print (name) # Error, el elemento no está definido, no sabe python qué estás llamando.
language = 2
print(language)


# IndexError
listita = ["python", "java", "C++", "R", "Kotlin"]
#print (listita[5]) # Error, el indexado no existe, está fuera de rango
print (listita[4])


# ModuleNotFindError
# import maths  No encuentra el módulo porque no existe
import math


# AttributeError
# print(math.PI) # No es capaz de encontrar PI, en la propia consola nos ayuda a saber qué es lo que está mal
print(math.pi)


# KeyError
my_other_dicts = {"Nombre":"Javier", "Apellido":"Ocaña", "edad":28, 1:"Python"}
#print(my_other_dicts["apllido"]) # Nos devuelve un error diciendo que esa key no existe en el diccionario, nos hemos equivocado al escribirla
print (my_other_dicts["Apellido"])


# ImportError
#from math import Pi # No encuentra nada que se llame "Pi" en el módulo

from math import pi

print(pi)

# ValueError
#my_int = int("10 años") # La cadena de texto que pasamos al int no se puede ejecutar con la función
my_int = int("10") 
print (type(my_int))


# ZeroDivisionError
#print(2/0) # Obvio
print(4/2)