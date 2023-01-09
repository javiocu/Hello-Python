### Operadores aritméticos ###
s = "---------" # Separador

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(20 % 6) # Resto
print(s)


### Operadores aritméticos no tan básicos ###

print(10 // 3) # Aproximación de la división, floor division

print(2 ** 3)

print("Hola " * 2) # Se multiplica por dos

print(s)

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 >= 1 == 2)

print(s)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaba" >= "aaac") # Ordenación alfabética por ASCII
print("Hola" <= "Python")
print("Hola" == "Casa")
print("Hola" != "Python")
print("Hola" >= "Python" == "HOLA")

print(s)

### Operadores lógicos ### SE ESCRIBEN TAL CUAL

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 and 2 <= 1 or ("Hola" < "Python" and 4 > 3))
print(s)

print(not(3 > 4 and "Hola" > "Python"))
