### List Comprehension ###

# Forma rápida de crear una lista a partir de listas con la que estamos trabajando al mismo tiempo


my_original_list = [1, 2, 3, 4, 32, 445, 23]

my_list = [i for i in my_original_list]

print(my_list)

my_range = range(8)
print(my_range)

my_list = [i for i in my_range] # Con un rango nos crea una lista con la que podemos trabajar ya

print(my_list)


my_list = [i + 1 for i in my_range]


print(my_list)


# Se pueden meter funciones también, lo que quieras en verdad

def suma_cinco (valor):
    return  valor + 5

my_list = [suma_cinco(i) for i in my_range]

print(my_list)