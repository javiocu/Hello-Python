### Listas ###

s = "------------"

# Formas de definir
my_list = [1, 2, 3, 4, "Javier", "Ocaña", 28]

print(my_list)


my_second_list = ["Javier", "Ocaña", 28, 1.71, 87]

print(my_second_list[2])

my_list_integers = [1, 4, 6, 4, 233, 23, 56, 19]

print(my_second_list.index(87))

name, surname, age, height, taller = my_second_list


print(name)

print(surname)

print(age)

print(s)

# Se pueden concatenar listas
print(my_list + my_second_list)

print(type(my_list))

# Se pueden adjuntar, insertar o eliminar datos. Al insertar o eliminar se modifican los index de la lista original

my_list.append(my_second_list) # Mete la lista como un objeto dentro de la misma lista AL FINAL, usar print si se quieren adjuntar dos listas
print(my_list)

my_list.insert(1, "Rojo") # Insertar
print(my_list)

my_list.remove("Rojo") # Eliminar
print(my_list)

print(s)


print(my_list.pop(0)) # Igual que el remove pero devuelve el valor que elimina, por default el último valor de la lista, se le puede dar un valor de índice
print(my_list)

print(s)

my_new_list = my_list.copy() # Copia la lista

my_list.clear() # Vacía la lista, pero no la elimina
print(my_list)

print(my_new_list)

my_new_list.reverse() # Da la vuelta al index

print(my_new_list)

my_list_integers.sort() # Ordena por orden alfabético o por números, no combinable entre tipos de objetos

print(my_list_integers)


