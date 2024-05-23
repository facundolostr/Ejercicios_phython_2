"""Defina clases Empresa y Empleado. Una empresa tiene varios empleados, pero un empleado trabaja en una sola empresa."""


class Empresa:
    def __init__ (self, nombre) ->None:
        self.__nombre = nombre
        self.__empleados = []

    @property
    def nombre (self) -> str:
        return self.__nombre

    def contratar_empleados(self, empleado) -> None:
        self.__empleados.append(empleado)

    def numero_empleados(self) -> int:
        return len(self.__empleados)

    def nombre_empleados(self, index=0) -> str:
        return self.__empleados[index]

    def __str__ (self) -> str:
        return f"Bienvenido a la empresa {self.nombre}"


class Empleado:
    def __init__ (self, nombre) ->None:
        self.__nombre = nombre
    
    @property
    def nombre (self) -> str:
        return self.__nombre

    def __str__ (self) -> str:
        return f"{self.nombre}"


def main ():

    e1 = Empleado("Julio")
    e2 = Empleado("Maria")

    empresa = Empresa("Santander")
    empresa.contratar_empleados(e1)
    empresa.contratar_empleados(e2)
    
    print(empresa.numero_empleados())
    print(empresa.nombre_empleados(1))
    
    for i in range(empresa.numero_empleados()):
        print(f"\n Nombre: {empresa.nombre_empleados(i)} \n")


    print(empresa) 



main()