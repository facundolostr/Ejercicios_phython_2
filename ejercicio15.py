"""
Se pide implementar una clase CalendarioMes con los siguientes métodos:

__init__(): toma como parámetro un entero que representa el número de días del mes (entre 28 y 31). Debe lanar una excepción si no es un día válido.

agregar_evento(): toma como parámetro un día (número entero) y el nombre de un evento (cadena) y lo almacena en el calendario. Debe lanar una excepción si no es un día válido.

eliminar_evento(): toma como parámetro un día y el nombre de un evento y lo elimina del calendario.

Debe lanzar una excepción si no existe un evento con ese nombre.

obtener_eventos_dia(): toma como parámetro un día y devuelve una lista con los eventos programados para ese día, o la lista vacía si no hay eventos en ese día. Debe lanzar una excepción si no es un día válido.


"""

import utilidades2 as util


class CalendarioMes:
    def __init__ (self, dias_mes:int):
        if dias_mes > 28 and dias_mes < 31:
            self.__dias_mes = dias_mes
        else:
            raise ValueError("Rango de dias no valido, ingrese un numero entre el 28 y 31")
        self.__evento = {}

    def _dia_valido(self, dia:int) -> bool:
        if dia < 1 or dia > self.__dias_mes:
            raise ValueError(f"Dia del mes no valido, el mes tiene un alcance de {self.__dias_mes} dias") 

    def agregar_evento(self, dia:int ,evento:str ) -> None: #convertir capitalizado para evitar errores tipograficos
        self._dia_valido(dia)

        evento_cap = evento.capitalize()
        print(util.titulo(f"Agendado el evento: '{evento_cap}' del calendario en el dia: {dia}"))
        if dia not in self.__evento:
            self.__evento[dia] = []
        self.__evento[dia].append(evento_cap)


    def eliminar_evento(self, dia:int , evento:str ) -> None:
        self._dia_valido(dia)

        evento_cap = evento.capitalize()
        print(util.titulo(f"Borrando el evento: '{evento_cap}' del calendario en el dia: {dia}"))
        if evento_cap in self.__evento[dia] and dia in self.__evento:
            self.__evento[dia].remove(evento_cap)
        else:
            raise ValueError(f"No exite el evento: '{evento}'")

    def obtener_eventos_dia (self, dia:int) -> list:
        self._dia_valido(dia)
        
        return print(f"Eventos agendados el dia {dia}: {self.__evento.get(dia, [])}")


def main():

    d = CalendarioMes (30) # El mes tiene un alcance de 30 dias
    # c = CalendarioMes (5) # ValueError("Dia del mes no valido, solo se permite entre 28 y 31")
    d.agregar_evento(5, "Cumpleaños") #El 5 de ese mes, hay un Cumpleaños
    # d.agregar_evento(31, "Cena") # ValueError("Dia del mes no valido, el mes tiene un alcance de 30 dias")
    d.agregar_evento(10, "Cena")
    d.agregar_evento(10, "Ir a clases")
    d.agregar_evento(10, "Correr")

    d.obtener_eventos_dia(10) # ["Cena","Ir a clases", "Correr"]
    # d.obtener_eventos_dia(34) # ValueError("Dia del mes no valido, el mes tiene un alcance de 30 dias")

    d.eliminar_evento(10, "cena")
    # d.eliminar_evento(10, "Montar a caballo") # ValueError ("No existe el evento: 'Montar a caballo'")
    # d.eliminar_evento(31, "cena") # ValueError ("No existe el evento: 'Montar a caballo'")

    d.obtener_eventos_dia(10) # ["Ir a clases", "Correr"]

    d.obtener_eventos_dia(5) # ["Cumpleaños"]

    d.obtener_eventos_dia(11) # []







main()