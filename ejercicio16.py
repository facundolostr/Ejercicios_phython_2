"""
Implementar la clase CajaFuerte, que recibe en su constructor la cantidad de objetos que puede contener, y tiene el siguiente comportamiento:

c = CajaFuerte(12345,20)    
c.abrir(12345)
c.poner("Reloj")
c.poner("Cadena")
c.poner(1000)
c.cerrar()
c.poner("Reloj Oro") ==> ValueError ("La caja esta cerrada")
c.abrir(3456) ==> ValueError ("Error en la clave")
c.abrir(12345)
c.sacar("Cadena")
c.sacar("Tortuga")  ==> ValueError ("El objeto Tortuga no esta en la caja")
c.abrir(12345) ==> ValueError("La caja esta abierta")
c.cerrar()
"""

import utilidades2 as util


class CajaFuerte:
    def __init__ (self, contraseña:int, cant_almacenamiento:int)->None:
        self.__contraseña = contraseña
        self.__cant_almacenamiento = cant_almacenamiento
        self.__objetos_almacenados:list[str] = []
        self.__plata_almacenada:float = 0
        self.__permitido:bool = False

    @property
    def contraseña(self) -> int:
        return self.__contraseña

    @property
    def almacenamiento(self) -> int:
        return self.__cant_almacenamiento

    def abrir(self,contraseña:int) -> None:
        if self.__permitido == True:
            raise ValueError("La caja ya esta abierta")
        elif self.contraseña == contraseña:
            self.__permitido = True
            print(util.titulo("La caja se abrio"))
        else:
            raise ValueError("Error en la clave")

    def poner(self, objeto) -> None: #puede almacenar tanto un str (objeto) como una cantidad de plata (int) // Hay que diferenciar cada uno
        if self.__permitido == True:
            if isinstance(objeto, str): 
                if len(self.__objetos_almacenados) < self.almacenamiento:
                        self.__objetos_almacenados.append(objeto) 
                else:
                    raise ValueError(f"Hay demasiados objetos en la caja. Solo puede almacenar: {self.almacenamiento} cosas")
            elif isinstance(objeto, int):
                self.__plata_almacenada += objeto
            else:
                raise ValueError("Solo se puede almacenar un objeto o una cantidad de plata")
        else:
            raise ValueError ("No se pueden colocar nuevos objetos, la caja esta cerrada")

    def mostrar_cosas_almacenadas(self) -> str:
        if self.__permitido == True:
            objetos_almacenados = ", ".join([str(objeto) for objeto in self.__objetos_almacenados])
            print(f"Tiene almacenado: {objetos_almacenados} y ${self.__plata_almacenada} en efectivo")
        else:
            raise ValueError("La caja esta cerrada, no esta permitido mostrar el contenido")

    def sacar(self,objeto) -> None:
        if self.__permitido == True:
            if isinstance(objeto, str): 
                if objeto in self.__objetos_almacenados:
                        self.__objetos_almacenados.remove(objeto)
                elif objeto not in self.__objetos_almacenados:
                    raise ValueError(f"el objeto: '{objeto}' no se encuentra en la caja")
                elif len(self.__objetos_almacenados) == 0:
                    raise ValueError("Ya no hay elementos en la caja")
            elif isinstance(objeto, int):
                if self.__plata_almacenada > objeto:
                    self.__plata_almacenada -= objeto
                else:
                    raise ValueError(f"Tienes {self.__plata_almacenada}, no se le puede restar {objeto}")
        else:
            raise ValueError ("La caja esta cerrada, no se puede sacar los objetos")




    def cerrar(self) ->None:
        if self.__permitido == False:
            raise ValueError("La caja ya esta cerrada")
        elif self.__permitido == True:
            self.__permitido = False
            print(util.titulo("La caja se cerro"))







def main():

    c = CajaFuerte(12345,20)  #primero recibe la contraseña y luevo la cantidad de cosas que puede contener  
    c.abrir(12345) #abre la caja con la clave correspondiente
    #c.abrir(12345)# ==> ValueError("La caja esta abierta")
    c.poner("Reloj")
    c.poner("Cadena")
    c.poner(1000)
    c.mostrar_cosas_almacenadas()

    c.sacar("Cadena")
    c.sacar(500)
    c.mostrar_cosas_almacenadas()

    #c.sacar("Tortuga")#  ==> ValueError ("El objeto Tortuga no esta en la caja")
    #c.sacar(1000) # ==> ValueError("Sacaste de mas")
    #c.abrir(3456)# ==> ValueError ("Error en la clave")


    c.cerrar()
    #c.poner("Reloj Oro")# ==> ValueError ("La caja esta cerrada")
    #c.cerrar() # ==> ValueError ("La caja ya esta cerrada")
    #c.sacar("Reloj") # ==> ValueError("La caja esta cerrada no se puede sacar nada")
    #c.mostrar_cosas_almacenadas() ==> ValueError("No se puede mostrar el contenido")



main()
