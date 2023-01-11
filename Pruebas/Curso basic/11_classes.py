### Classes ###
# Sirve para definir elementos que python no tiene de base, para crear los tuyos propios, como una persona, que no es un diccionario ni una lista,
# sino una clase nueva definida por nosotros
# LAS CLASES SE DEFINEN CON CAMEL CASE!!

class MyEmptyPerson: # Así de fácil se define una clase
    pass      # Con pass se saltan los posibles errores, sino se pone al definir una clase, saltará error

class Person0:
    def __init__(self, name, surname):    # init sirve para definir la clase, simpre tiene que llamar a self, después se pueden poner lo que quieras
        pass  # Al poner el pass, le indicamos que no queremos que haga nada con esos parametros introducidos

probando_persona = Person0("Javier", "Ocaña")

print(probando_persona)


class Person1:
    def __init__(self, name, surname):
        self.name = name #Al poner el punto algo, le asignamos una propiedad, como .copy o .insert, en este caso .name
        self.surname = surname

        #TODO ESTO SE CONOCE COMO CONSTRUCTOR

probando_persona = Person1("Javier", "Ocaña")

print(probando_persona.surname) #Ahora sí imprime el nombre


class Person2:
    def __init__(self):
        self.name = "Javier" # También se pueden definir variables internas en el constructor
        self.surname = "Ocaña"

        #TODO ESTO SE CONOCE COMO CONSTRUCTOR

probando_persona = Person2()

print(probando_persona.name) #Ahora sí imprime el nombre

class Person3:
    def __init__(self, name, surname):
        self.fullname = f"{name} {surname}" # Otra opción

probando_persona = Person3("Javier", "Ocaña")

print(probando_persona.fullname) #Ahora sí imprime el nombre



## También es posible definir funciondes dentro de los constructores para un tipo de calse en concreto:

class Person:
    def __init__(self, nombre, apellido, nombre_privado):
        self.name = nombre
        self.surname = apellido
        self.__privadoName = nombre_privado #Propiedad privada, no se puede acceder desde fuera del constructor, así se protege
    def get_privadoName (self):
        return self.__privadoName # Así con getprivadoName podría acceder al dato desde fuera pero no lo podría modificar
    def andar (self):  # La función se llama a sí misma (self)
        print(f"{self.name} {self.surname} está sentado")
    
persona1 = Person("Javier", "Ocaña", "JAVIEROCAÑACUESTAPRIVADO")

print(type(persona1))


persona1.andar()

print(persona1.get_privadoName())