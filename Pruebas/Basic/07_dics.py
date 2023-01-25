### Dictionaries ###

my_dicts = dict()

my_other_dicts = {}

print(type(my_dicts))

print(type(my_other_dicts))

my_other_dicts = {"Nombre":"Javier", "Apellido":"Ocaña", "edad":28, 1:"Python"} # Se asigna clave-valor a cada objeto, diferente a los sets

print(type(my_other_dicts))

my_dicts = {
    "Nombre":"Javier",
    "Apellido":"Ocaña",
    "Edad":28,
    "Lenguajes":{"python", "java", "c"}, # SE PUEDEN ALMACENAR SETS DENTRO INCLUSO, LISTAS, LO QUE SEA
    "colores favoritos":{"rojo","azul","colorado"}
}

print(type(my_dicts))
print(my_dicts)

print(my_dicts["Nombre"])  # Facilidad para acceder a un elemento, si sabes la clave, puedes acceder al valor, el valor puede cambiar, 
                           # pero las claves serán las mismas siempre
print(my_dicts["Lenguajes"])
print(type(my_dicts["Lenguajes"]))

my_dicts["Nombre"] = "Pedro" # Se pueden modificar elementos del diccionario, llamando a la clave

del my_dicts["Edad"] # del, built in del propio python permite eliminar elementos concretos del diccionario
print(my_dicts)

print("Pedro" in my_dicts) # HAY QUE BUSCAR POR CLAVE NO POR VALOR
print("Apellido" in my_dicts) # POR CLAVE SI ENCUENTRA

