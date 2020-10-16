import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""

# start-->
class Suma:
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def sumar(self):
        result = self.__number1 + self.__number2
        return result


print(Suma(2, 4).sumar())


"""
***************************************************************
@@ ejercicio 2 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*5 = 40
"""
# start-->


class Multiplicacion:
    def __init__(self, number1, number2, number3):
        self.__number1 = number1
        self.__number2 = number2
        self.__number3 = number3

    def multiplicar(self):
        result = self.__number1 * self.__number2 * self.__number3
        return result


print(Multiplicacion(2, 4, 5).multiplicar())


"""
***************************************************************
@@ ejercicio 3 @@
un metodo python que haga la suma de los numeros de la lista
numerosLista = [2,5,4,6,9,12]
"""


# start-->
def SumaLista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma


print(SumaLista([2, 5, 4, 6, 9, 12]))


"""
***************************************************************
@@ ejercicio 4 @@
colocar este proyecto en github
colocar aca debajo la url
enviar la url al correo balbino_a@hotmail.com
"""


# github url-->
def getGithubUrl():
    return ""
