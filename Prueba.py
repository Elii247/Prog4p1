'''correcto uso de if '''      '''Uso incorrecto'''
from os.path import isabs
from traceback import print_tb

if(variables)                        if($variables)
    x=9                                  x=9
    '''No se  pueden utilizar caracteres especiales la iniciar una variables y tampoco se uti
    liza el ; o el {} para cerrar el if'''

    '''ejemplo de if simple'''

    #Definimos una variable x con una cadena
     x = "El valor de (a+b)*c es"

    #Podemos realizar multiples asignaciones
    a,b,c= 4,3,2

    #Realizamos unas operaciones con a,b,c
    d= (a+b)*c

    #Definimos una variable booleana
    imprimir = True

    #Si imprimir , print()
    if imprimir:
        print(x,d)
    #Salida : El valor de (a+b)*c es 14

'''se puede utilizar el ; para tener dos sentencias en la misma linea ejemplo'''
x = 5; y = 10

'''Recomendacion:  en una linea de codigo no puede exeder los 79 caracteres 
podemos utilizar el \ para que el codigo sea mas lejible'''

'''Si tenemos un bloque de codigo con () simplemente tenemos que saltar a la siguiente
linea del codigo ejemplo'''
x= (1+2+3+4+
    5+6)

'''se puede utilizar la misma logica para llamar funciones solo que aqui mostrara que  funcion esta llamando'''
def funcion (a,b,c):
    return a+b+c
d = funcion(10,
            23,
            3)
'''podemos dar el mismo valor a diferentes variables con el mismo codigo'''

x = y = z = 10

'''O tambien podemos asignar varios valores separados por coma.'''
x,y = 4,2
x,y,z = 1,2,2

'''Reglas al momento de nombrar variables'''
'''1: El nombre no puede empezar por un numero
   2: No se permiten uso de - 
   3: Tampoco se permite el uso de espacios 
   4: No utilizar palabras reservadas
   Ejemplos: '''
#Validos
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

#No valiado
2variable = 10
var-iable = 10
var iable = 10

''' Variables y alcance
Un concepto muy importante cuando definimos una variable, 
es saber el alcance o scope que tiene. En el siguiente ejemplo 
la variable con valor 10 tiene un alcance global y la que tiene el valor 5 dentro de 
la función, tiene un alcance local. Esto significa que cuando hacemos print(x), estamos accediendo a la variable global 
x y no a la x definida dentro de la función.'''

z= 10

def funcion():
    z = 5

funcion()
print(x)

def suma (a,b):
    c= a + b
    return c

print(suma("hola","mundo"))

'''Typear las variables si son enteros y demas'''
def multiplicacion(a: int,b: int):
    c =  a* b
    return c
d = suma(5,8)
print(d)
print(multiplicacion(5,8))


''''Comando para mostrar palabras reservadas'''
import keyword
print(keyword.kwlist)

'''Siclos //For// Whille//
el continue salta hata el final del bloque, dejando sin ejecutar lo restante, pero continua
en la siguiente iteraccion'''
    for i in range(3):
        if i == 1:
            continue
        print(i)
'''El break se utiliza para romper la ejecuion del bucle, saliendo del mismo'''

x= 0
while True:
    print(x)
    if x == 2:
        break
        x += 1

"""cuando una funcion no tiene un retorno python la ejecutara por defecto como //None//"""

"""Si realizamos una comparación usando el operador relacional == se nos devolverá True o False.

x = (5 == 1)
print(x)
# Salida: False
También podemos asignar nosotros True a una variable.

x = True
if x:
    print("Python!")
    
# Salida: Python!
Por otro lado None se devuelve por defecto cuando una función no cuenta con un return.

def mi_funcion():
    pass

print(mi_funcion())
# Salida: None""

El uso de lambda nos 
permite crear funciones lambda,una especie de funciones “para vagos”. 
Dichas funciones
no tienen un nombre per se, salvo asignado explícitamente."""

print("La uma es",(lambda a,b: a+b)(3,5))
#Salida: La suma es 8

""" Por último, yield está asociado a los generadores y las corrutinas, 
un concepto un tanto avanzado pero muy interesante. En el siguiente generador vemos como se generan 
tres valores, obteniendo uno cada vez que iteramos el generador.
"""
def gerador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n
for i in gerador():
    pirnt(i)

"""if
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor"""



Pertenencia e Identidad: in, is
"""El uso de in nos permite saber si un determinado elemento 
está en una clase 
iterable, devolviendo True en el caso de que sea cierto."""
Lista = ["a","b","c"]
print("a"in Lista)




DUDA AVERIGUAR
"""El uso de is nos permite saber si dos variables apuntan en 
realidad al mismo objeto. Por debajo se usa la función id() y es 
importante notar que 
la igualdad == no implica que is sea True."""
a = [1, 2]
b = [1, 2]
c = a

print(a is b) # False
print(a is c) # True


Eliminar variables: del

"""El uso de del nos permite eliminar una variable del scope, 
pudiendo resultar útil cuando trabajamos con variables que 
almacenan gran cantidad de datos. Es una manera explícita de 
indicar que ya no queremos una variable, pero no olvidemos 
que Python tiene garbage collector."""
a = 10
del a
print(a)

# Salida: NameError: name 'a' is not defined

Context Manager : with, as
"""El uso de with y as es muy utilizado a la hora de manejar
 ficheros, pero en realidad pertenecen a los context 
managers o gestores de contexto, un concepto algo avanzado."""
with open('fichero.txt', 'r') as file:
    print(file.read())





