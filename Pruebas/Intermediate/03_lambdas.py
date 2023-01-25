### Lambdas ###

# La lambda se entiende como una función, pero funciones anónimas, siempre hemos definido nombres para las funciones, con las lambdas no.

sum_two_values = lambda first_value, second_value: print(first_value + second_value)# se pueden almacenar en variables


# Se usan principalmente para acceder rapidamente a cosas muy concretas, que hagan algo muy CONCRETO

sum_two_values(3, 4)



multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))


# Se pueden meter en funciones

def sum_three_values (este):
    return sum_two_values (este, este + 1)

sum_three_values(2)