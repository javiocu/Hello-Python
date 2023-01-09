# Parte del curso dedicada a variables

my_string_variable = "Los nombres de las variables son importantes"

print(my_string_variable)

my_int_variable = 5 

print(my_int_variable)

my_bool_variable = True

print(my_bool_variable)

my_variable_compuesta = (str(my_int_variable), str(my_bool_variable), my_string_variable)

print("----------")
# Para pegar variables se pueden convertir en str, concatenación:

print(str(my_int_variable), str(my_bool_variable), my_string_variable)

# Funciones del sistema (Built-in, funciones precargadas) ¡CUIDADO CON ABUSAR DE ESTA SINTAXIS!

print(len(my_variable_compuesta))

# Variables en una sola línea
name, surname, alias, age = "Javi", "Ocaña", "Javiocu", 28


print("--------------------------------------------")

print("Me llamo", name, surname, "y mi alias es", alias, sep=" ")


# Se puede poner un input para pedir información:

#age = input("¿Cuantos años tienes? ")

print("Entonces tienes", age, "años")


# Intentamos forzar el tipo de variable, sin embargo solo sirve de forma visual, si cambiamos el tipo de variable no avisa y lo cambia de str a int
address: str = "Calle algo, Nº 27"

address = 32

print(type(address))