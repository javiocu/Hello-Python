### Higher order functions ###

# Las funciones de orden superior son funciones que utilizan otras funciones

def sum_five (value):
    return value + 5

def sum_one(value):
    return value + 1

def sum_two_values_and_one (first_value, second_value):  # Todavía no son funciones de orden superior
    return sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2))


print("-------------------")

def sum_one(value):
    return value + 1

def sum_two_values_and_one (first_value, second_value, F_sum_one):  # AQUÍ YA SÍ, PORQUE A UNA VARIABLE INTERNA LA USAMOS COMO UNA FUNCIÓN DENTRO DE OTRA FUNCIÓN
    return F_sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))  # Aquí llamamos a la función para que sea un parámetro más

print(sum_two_values_and_one(5, 2, sum_five)) # Aquí usamos otra función que suma 5 en lugar de uno, pero la función base no se ha cambiado, es una función de orden superior

print("-------------------")


### Closures ###

def sum_ten (original):         # Son funciones que retornan funciones
    def add(value):
        return value + 10 + original
    return add

add_closure = sum_ten(12)

print(add_closure (5))

print(sum_ten(12)(5))  # Se pueden encadenar los valores que se lequieran dar a las funciones que haya dentro, en este caso el 12 es original y el 5 es value



### Built-in Higher order functions ###

numbers = [2, 5, 10, 21]

def multiply_two (number):
    return number * 2

# Map
print(list(map(multiply_two, numbers)))        # Map itera cada valor que le pasamos en forma de lista y lo pasa por la función generando otro listado iterable
