"""
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes

"""

import utilidades2 as util

class Boleteria:
    def __init__ (self, evento:str, cant_local:int) -> None:
        self.__evento = evento
        self.__cant_local = cant_local
        self.__local_vendidas = 0

    @property
    def evento (self):
        return self.__evento

    def vender_localidades (self, cantidad:int) -> str:
        if self.__local_vendidas > self.__cant_local or self.__local_vendidas + cantidad > self.__cant_local:
            raise ValueError ("No hay localidades suficientes")
        else:
            self.__local_vendidas += cantidad
        return print (f"Se vendieron: {cantidad}")

    def localidades_agotadas(self) -> bool:
        print (util.titulo ("Evaluando si las localidades estan agotadas"))
        if self.__local_vendidas == self.__cant_local:
            return print (True)
        else:
            return print (False)

    def __str__(self) -> str:
        return f"{self.evento} - Localidades vendidas: {self.__local_vendidas} de {self.__cant_local}"


def main ():
    b = Boleteria ("Lolapalooza", 1000)
    print (b) # Evento: Lolapalooza - Localidades vendidas: 0 de 1000
    b.vender_localidades(300)
    # b.vender_localidades(1100) # ValueError: No hay localidades suficientes
    print(b)

    b.localidades_agotadas() # False
    
    b.vender_localidades(700) 
    b.localidades_agotadas() # True
    print(b) # Evento: Lolapalooza - Localidades vendidas: 1000 de 1000 

main()