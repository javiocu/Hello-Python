### Modules ###

# Los módulos sirven para centralizar código, y no tener que repetir cosas que ya están en otro fichero
# Por ejemplo, my_function está ya en my_module.py, lo cargamos

import my_module     #Todo lo que haya aquí me lo cargas y que yo pueda disponer de él, esto hace que todo le cueste más al programa

my_module.my_function(1, 2, 3) # Ya dispondríamos de la función en cuestión y de todo lo que haya en my_module.py


#PYTHON NO ACEPTA FICHEROS COMO MÓDULOS QUE EMPICEN CON UN NÚMERO


# Si queremos solo cargar una función en concreto para no saturar usamos from import, de esta forma estaría disponible directamente sin necesidad de poner my_module delante


from my_module import printValue

my_module.printValue(1)


# También es válido importar varios elementos

from my_module import printValue, my_function

printValue("Comida")


# También se puede poner alias

from my_module import printValue as printeameesta


printeameesta("Comida 2")