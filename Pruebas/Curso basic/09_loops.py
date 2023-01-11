### Loops ###

s = "------------"

# While

my_condition = 0

while my_condition < 10: 
    print(my_condition)
    my_condition += 1
else:
    print("Mi condición es mayor igual que 10")

while my_condition < 10: 
    print(my_condition)
    my_condition += 1
#elif my_condition == 10:  # No se puede añadir ningún elif ni ningún if pero sí else
    print("Mi condición es igual que 10")


print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    print(my_condition)
    if my_condition == 15:
        print("Mi condición es igual a 15")
        break
else:
    print("Mi condición es mayor igual que 20")


# For para iteración de múltiples elementos

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

print(s)

my_other_tuple = ("Brais", "Javier", "Pedro", "Juan")

for element in my_other_tuple:
    print(element)

print(s)

my_set = {"Brais", "Javier", "Pedro", "Juan"}

for element in my_set:
    print(element)

print(s)


my_dict = {"Nombres":"Javier", "Datos":"Brais", "Perico":"Juan"}

for element in my_dict:   # Si no se modifica, un diccionario devolverá las keys
    print(element)
    if element == "Datos":
        print("Ha encontrado Datos")
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha conlcuido")


my_dict = {"Nombres":"Javier", "Datos":"Brais", "Perico":"Juan"}

for element in my_dict:   # Si no se modifica, un diccionario devolverá las keys
    print(element)
    if element == "Datos":
        print("Ha encontrado Datos")
        continue                # EJECUTA UN SKIP DE R, empieza a continúa ejecutando pero la siguiente ronda, no ejecuta lo que sigue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha conlcuido")
