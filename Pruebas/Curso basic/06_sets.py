### Sets ###


my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # En principio se puede entender como lista, y el tipo es diccionario ("dic")

my_other_set = {"Javier", 28, "Ocaña", 1.70} # Si lo rellenas se convierte en set

print(type(my_other_set))

# print(my_other_set[1]) # TypeError: 'set' object is not subscriptable

my_other_set.add(4500) # Al meter el elemento, no lo añade al final, un set está desordenado

print(my_other_set)

my_other_set.add(4500) # Un set no admite repetidos, solo admite un objeto de cada. Así no tiene que guardar orden, ordena por un hash interno.

print(my_other_set)

print("Javier" in my_other_set) # Se puede comprobar que existe un objeto en un set
print("Javior" in my_other_set)

# Las principales diferencias son:
#   - No se puede repetir objetos
#   - Los objetos no se ordenan, es aleatorio
#   - Los objetos no son accesibles


my_other_set.clear()
print(my_other_set)