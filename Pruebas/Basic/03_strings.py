### Strings ###

s = "---------" # Separador

my_string = "Esto es un ejemplo de string"
my_string_second = "Segundo string"

print(my_string)
print(my_string_second)

# Se pueden meter saltos de línea entre medias \n o con tabulación \t

my_string_second_con_salto = "\n Segundo string"
my_string_second_con_tab = "\t Segundo string"

print(my_string + my_string_second_con_salto)
print(my_string + my_string_second_con_tab)

# Formateo

name, surname, age = "Javi", "Ocaña", 28

print("Mi nombre es %s %s, y mi edad es %d") # s para str, d para int, f para float

print("Mi nombre es {} {}, y mi edad es {}".format(name, surname, age)) # Si usamos format, se ponen llaves y se rellena por orden

print("Mi nombre es %s %s, y mi edad es %d" %(name, surname, age)) # Si usamos %, se tiene que especificar el formateo de cada una con % y el tipo

print(f"Mi nombre es {name} {surname}, y mi edad es {age}") # Se pone una f delante del print para formatear y 
                                                            # que saque el valor tal cual de las variables que se llamen

# Desempaquetado de caracteres

language = "python"
a, b, b, c, d, e = "Python" # Se empaquetan cada valor de la str en cada variable a-e

print(a)
print(b)

print(s)

# División

language_slice = language[1:]

print(language_slice)



language_slice = language[:]

print(language_slice)


language_slice = language[-5:2]

print(language_slice)

# Funciones
print(s)
print(language)
print(language.capitalize())

print(language.upper())

print(language.count("t"))

print(language.isnumeric())
print("1".isnumeric())
print(s)

print(language.upper().isupper()) # Se pueden encadenar funciones punto a punto
print(language.upper().islower())