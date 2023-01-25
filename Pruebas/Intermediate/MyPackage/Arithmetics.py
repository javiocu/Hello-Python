### Arithmetics ###


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
    return(print(final))



sumando()