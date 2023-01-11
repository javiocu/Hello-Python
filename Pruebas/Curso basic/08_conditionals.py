### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta lal condición del if")


########################################
my_condition = 5*2

if my_condition:
    print("Se ejecuta lal condición del segundo if") # phyton comprueba que la variable tiene valor asociado != de False, y lo considera True

my_condition = 1

if my_condition == 10:
    print("Se ejecuta lal condición del tercer if")

if my_condition >= 10:
    print("Es mayor o igual que 10")
else:
    print("Es menor que 10")

########################################

if my_condition >= 10 and my_condition <= 20:
    print("Es mayor o igual qué 10 y menor o igual que 20")
else:
    print("Es menor que 10 o mayor que 20")

########################################

if my_condition >= 10 and my_condition <= 20:
    print("Es mayor o igual qué 10 y menor o igual que 20")
elif my_condition == 1:
    print("Es igual a 1")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor que 10 o mayor que 20")






########################################

print("La ejecución continúa")