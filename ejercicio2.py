"""
Cree clases Escritor y Libro. Un escritor ha escrito varios libros, pero un libro solo tiene un escritor
"""


class Escritor:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__libros_escritos = []

    @property
    def nombre(self) ->str:
        return self.__nombre

    def asignar_libro(self, libro) -> None:
        self.__libros_escritos.append(libro)

    def cantidad_libros_escritos(self) -> int:
        cantidad = len(self.__libros_escritos)
        return cantidad

    def __str__ (self) -> str:
        libros = ", ".join([libros.get_nombre() for libros in self.__libros_escritos])
        return f"El escritor: {self.nombre}  escribio: {libros}"


class Libro:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre


    @property
    def nombre(self) ->str:
        return self.__nombre

    def get_nombre(self) -> str:
        return self.nombre

    def __str__ (self) -> str:
        return f"{self.nombre}"


def main ():

    libro1 = Libro("El Principito")
    libro2 = Libro("El gato con botas")

    escritor = Escritor("Borges")

    escritor.asignar_libro(libro1)
    escritor.asignar_libro(libro2)

    print(escritor) # El escritor "Borges" escribio "El principito", "el gato con botas"




main()