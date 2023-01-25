### Tuplas ###

s = "------------"

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28, 1.70, "Javier", "Ocaña", "Javier")

my_other_tuple = (2, 4, 56, 67)


print(my_tuple)

print(type(my_tuple))

print(my_tuple[0])

print(my_tuple.count("Javier"))

print(my_tuple.count(3))

print(s)

print(my_tuple.index("Javier"))

# my_tuple[1] = "Comida" # TypeError: 'tuple' object does not support item assignment LAS TUPLAS SON INMUTABLES, NO TE DEJAN MODFICARLAS, SOLO ACCEDER Y CONTAR DATOS
                        # Por lo demás son igual que una lista
# print(my_tuple)

# Sí se pueden sumar las tuplas

print(my_tuple + my_other_tuple)