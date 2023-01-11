### Exceptions ###

number_one, number_two, number_three = 5, 1, "1"

#print(5 + "5")


#print(number_one + number_two)


#Try except

try:
    print(number_two + number_three)
except:
    print("No se suma")
    print(number_one + number_two)

#Try except else

try:
    print(number_two + number_three)
    print("No se ha producido un error")
except:
    print(number_one + number_two)
    print("Se ha producido un error")
else:                                   #ELSE SE EJECUTA SI NO HAY EXCEPTION, es decir si se ejecuta el try sin errores
    print("Este es el else")

#Try except else finally

try:
    print(number_two + number_three)
    print("No se ha producido un error")
except:
    print(number_one + number_two)
    print("Se ha producido un error")
else:                                   #ELSE SE EJECUTA SI NO HAY EXCEPTION, es decir si se ejecuta el try sin errores
    print("Este es el else")
finally:
    print("La ejecución continúa")      # El finally se eejecuta siempre, independientemente de si hay errores o no


try:
    print(number_two + number_three)
    print("No se ha producido un error")
except TypeError:                       # Se pueden especificar errores de un tipo concreto
    print(number_one + number_two)
    print("Se ha producido un error TypeError")
except ValueError:                      # Se pueden meter varios except específicos en la misma try
    print("Se ha producido un error ValueError")

s = "-----------"
print(s)

# También se puede meter la información de un error en un log por ejemplo o subirla a algún sitio si la sacas por el terminal:
try:
    print(number_two + number_three)
    print("No se ha producido un error")
except TypeError as error:                       # Se nombra el error y se saca con print
    print(error)
except ValueError:                      # Se pueden meter varios except específicos en la misma try
    print("Se ha producido un error ValueError")


print(number_one + number_three)