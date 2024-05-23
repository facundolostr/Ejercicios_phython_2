"""Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponden al nombre del equipo local y el visitante (en ese orden).

Además, tiene los siguientes métodos:

cargar_resultado: Recibe dos números enteros, que corresponden a los goles convertidos por el local y el visitante (en ese orden).

obtener_ganador: Devuelve el nombre del equipo ganador, o None si hubo un empate.

obtener_perdedor: Similar a obtener_ganador, pero devuelve el perdedor o None.

Escribir la clase Liga, que tiene los siguientes métodos:

cargar_partido: Recibe un objeto de clase Partido, y guarda los datos necesarios.

obtener_campeon: Devuelve una cadena con el nombre del equipo que más puntos tiene.

Si hay varios equipos que tengan el puntaje máximo, devolver el nombre de cualquiera ellos.

Se otorgan 3 puntos por partido ganado, 1 por partido empatado y 0 por partido perdido.

Este método debe ser lo más eficiente posible.

"""

import utilidades2 as util


class Partido:
    def __init__ (self, equipo_local:str, equipo_visitante:str) -> None:
        self.__equipo_local = equipo_local
        self.__equipo_visitante = equipo_visitante
        self.__goles_local = None
        self.__goles_visitante = None
        self.__ganador = None
        self.__perdedor = None


    @property
    def equipo_local(self) -> None:
        return self.__equipo_local

    @property
    def equipo_visitante(self) -> None:
        return self.__equipo_visitante

    @property
    def ganador(self) -> None:
        return self.__ganador

    @property
    def perdedor(self) ->None:
        return self.__perdedor
    
    def cargar_resultado (self, gol_local:int, gol_visitante:int) -> None:
        self.__goles_local = gol_local
        self.__goles_visitante = gol_visitante
        print(util.titulo(f"Se esta jugando un partido entre '{self.equipo_local}' y '{self.equipo_visitante}'"))

    def obtener_ganador (self) -> str:
        if self.__goles_local > self.__goles_visitante:
            self.__ganador = self.equipo_local
        elif self.__goles_visitante > self.__goles_local:
            self.__ganador = self.equipo_visitante
        elif self.__goles_visitante == self.__goles_local:
            return print(f"Hubo un empate entre '{self.equipo_local}' y '{self.equipo_visitante}'\n")
        return print(f"El ganador fue: '{self.ganador}' en un {self.__goles_local} a {self.__goles_visitante}\n")


    def obtener_perdedor (self) ->str:
        if self.__goles_local < self.__goles_visitante:
            self.__perdedor = self.equipo_local
        elif self.__goles_visitante < self.__goles_local:
            self.__perdedor = self.equipo_visitante
        elif self.__goles_visitante == self.__goles_local:
            return print(f"Hubo un empate entre '{self.equipo_local}' y '{self.equipo_visitante}'\n")
        return print(f"El perdedor fue: '{self.perdedor}'\n")


class Liga:
    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__partidos = []

    @property
    def nombre(self) -> None:
        return self.__nombre

    def cargar_partido(self, partido:Partido) -> None:
        self.__partidos.append(partido)

    def obtener_campeon(self) -> str:
        puntajes = {}

        for partido in self.__partidos:
            ganador = partido.obtener_ganador()

            if ganador is not None:
                if ganador in puntajes:
                    puntajes[ganador] += 3
                else:
                    puntajes[ganador] = 3
        
        if puntajes:
            campeon = max(puntajes, key=puntajes.get)
            return f"El ganador de la '{self.nombre}' fue: '{campeon}'"
        
        return None






def main():
    partido1 = Partido("Boca","River")
    partido1.cargar_resultado(3,1)
    partido1.obtener_ganador() # El ganador fue "Boca"
    partido1.obtener_perdedor() # El perdedor fue "River"

    partido2 = Partido("San Lorenzo", "Racing")
    partido2.cargar_resultado(1,1)
    partido2.obtener_ganador() # Hubo un empate entre "San Lorenzo" y "Racing"
    partido2.obtener_perdedor() # Hubo un empate entre "San Lorenzo" y "Racing"

    partido3 = Partido("Boca","San Lorenzo")
    partido3.cargar_resultado(1,2)
    partido3.obtener_ganador() # El ganador fue "San Lorenzo"
    partido3.obtener_perdedor() # El perdedor fue "Boca"

    liga = Liga("Champion Ligue")
    liga.cargar_partido(partido1)
    liga.cargar_partido(partido2)
    liga.cargar_partido(partido3)
    

    print(liga.obtener_campeon()) # El ganador de la "Champion Ligue" fue "San Lorenzo"



main()




