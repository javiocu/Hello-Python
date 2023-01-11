### Functions ###

def my_function ():
    print("Esto es una función")

# my_fucntion ()


def sum_two_values (first_number, second_number):
    print(first_number + second_number)


def sumando ():
    primero = input("Por favor introduce el primer número a sumar: ")
    while True:
        try:
            primero = float(primero)
            break
        except ValueError:
            primero = input("Opps, eso no es un número, por favor, introduce un primer número: ")
    segundo = input("Por favor introduce un segundo número: ")
    while True:
        try:
            segundo = float(segundo)
            break
        except ValueError:
            segundo = input("Eso no es un número, por favor introduce un número: ")
    suma = primero + segundo
    final = "La suma de ambos número es: " + str(int(suma))  # Recordar que para que devuelva el valor de return hay que printear
    return(final)


def texto_imprimir (*texto):     # Al ponerle el asterisco le puedes poner más de una entrada inicial
    print(texto) # Lo interpreta como una tupla

texto_imprimir("Hola", "lsdfjkljsdf")


def print_upper_text (text):
    print(text.upper())


print_upper_text("probando")