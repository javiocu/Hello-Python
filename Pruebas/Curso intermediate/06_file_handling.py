### File Handling ###

import os
## .txt file
# txt_file = open("Pruebas/Curso intermediate/my_file.txt", "r") # r es modo lectura (Default), r+ es modo lectura y escritura
txt_file = open("Pruebas/Curso intermediate/my_file.txt", "w+") # w es modo abrir y sobreescribir, si no existe lo crea
txt_file.write ("Mi nombre es Javier\nOcana es mi apellido\nTengo 28 anos\nMi leguito es el mejor perro del planeta")
txt_file = open("Pruebas/Curso intermediate/my_file.txt", "r+") # Hay que cerrar archivo y abrilo de nuevo si se quiere leer
#print (txt_file.read())
#print (txt_file.read(10))

#print (txt_file.readline ()) #Printea una línea, elñ siguiente readline leerá la siguiente línea que no haya leído ya
#print (txt_file.readlines ()) #Printea todas las líneas como una lista


for i in txt_file.readlines(): # Printea todas las líneas con el bucle
    print(i)

txt_file.write ("\nLeguito es mi perro")

txt_file.close () #Es buena práctica cerrar ficheros si no se van a seguir usando

#os.remove ("Pruebas/Curso intermediate/my_file.txt") # Para eliminar el fichero

## .json file
import json

json_file = open("Pruebas/Curso intermediate/my_file.json", "w+")

json_text = {
    "nombre":"Javier",
    "apellido":"Ocaña",
    "edad":28,
    "lenguages":["python", "swift", "java"]}

json.dump (json_text, json_file, indent=4) # Import el contenido de la variable al file que hemos creado más arriba, indent permite meter indentaciones para que se vea más comodo el archivo

json_file.close ()

with open("Pruebas/Curso intermediate/my_file.json") as my_other_file:
    for i in my_other_file.readlines ():
        print(i)

json_file = open("Pruebas/Curso intermediate/my_file.json", "r+")



cargado = json.load (json_file)

print(type(cargado)) # Transforma el json en un diccionario para python