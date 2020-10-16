import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


def suma(number1, numer2, number3):
    result = number1 + numer2 + number3
    return result


# start-->


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


def sumaImpares():
    i = 0
    sumaI = 0
    while i <= 1000:
        if i % 2 != 0:
            sumaI += i
        i += 1
    return sumaI


# start-->


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""


# start-->

def set_radius(self, radius):
        if not isinstance(radius, int):
            print("Error: ", radius, "is not an int")
            return
        self.__radius = radius

        def get_area(self):
            return math.pi * self.__radius ** 2

        def get_perimeter(self):
            return 2 * math.pi * self.__radius

        def get_volume(self)
        return


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Circle:
    def set_radius(self, radius):
        if not isinstance(radius, int):
            print("Error: ", radius, "is not an int")
            return
        self.__radius = radius

        def get_area(self):
            return math.pi * self.__radius ** 2

        def get_perimeter(self):
            return 2 * math.pi * self.__radius

        def get_volume(self)
        return


# setter method for radius attribute


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    class Cliente:
    def _init_(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def abono(self, monto):
        self.monto = self.monto + monto

    def retiro(self, monto):
        self.monto = self.monto + monto


class Banco:
    def _init_(self):


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
