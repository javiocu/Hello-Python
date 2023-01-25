### Type Hints ###

# Python es un lenguable dinámico, puedes cambiar el tipo de dato que al principio era una cosa y que termine siendo otra

my_string_variable = "My string variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))


# Python tienen un tipado débil, no podemos forzar que algún valor sea el tipo que queremos

my_type_string_variable: str = "My typed String Variable" # si pusiera int no tiraría error

print(my_type_string_variable)
print(type(my_type_string_variable))