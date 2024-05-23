"""
Defina dos clases, Paciente y Médico. Un paciente puede tener asignado un médico, pero un médico puede tener muchos pacientes.
"""

class Medico:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__pacientes = []

    def get_nombre(self):
        return self.__nombre

    def agregar_paciente(self, paciente):
        self.__pacientes.append(paciente)

    def __str__(self):
        pacientes = ", ".join([paciente.get_nombre() for paciente in self.__pacientes])
        return f"Nombre del médico: {self.__nombre}, Tiene como pacientes: {pacientes}"

class Paciente:
    def __init__(self, nombre, enfermedad):
        self.__nombre = nombre
        self.__enfermedad = enfermedad
        self.__medico = None

    def get_nombre(self):
        return self.__nombre

    def get_enfermedad(self):
        return self.__enfermedad

    def get_medico(self):
        return self.__medico

    def asignar_medico(self, medico):
        self.__medico = medico

    def __str__(self):
        return f"Nombre: {self.__nombre}, Enfermedad: {self.__enfermedad}, Médico de cabecera: {self.__medico.get_nombre() if self.__medico else 'No asignado'}"

def main():
    m1 = Medico("Marcelo")
    p1 = Paciente("Pepe", "Presión alta")
    p2 = Paciente("Ana", "Gripe")

    p1.asignar_medico(m1)
    m1.agregar_paciente(p1)
    m1.agregar_paciente(p2)

    print(p1)
    print(p2)
    print(m1)

main()