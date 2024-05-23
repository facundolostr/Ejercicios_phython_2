"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto # 1
Lista de contactos # 2
Buscar contacto # 3
Editar contacto # 4
Cerrar agenda # 5

"""

import utilidades2 as util
from os import system


class Agenda:
    def __init__ (self) -> None:
        self.__respuesta = None
        self.__OPCION = ("Menu de la agenda", 
            "1) Añadir contacto en la agenda",
            "2) Lista de contactos",
            "3) Buscar contacto",
            "4) Editar contacto",
            "5) Cerrar agenda\n")

        self.__OPCION_EDICION =  ("Menu de edicion",
            "1) Editar nombre",
            "2) Editar numero",
            "3) Editar mail",
            "4) Cerrar edicion\n")
        
        self.__contactos = []

    def _interfaz(self) -> None:
        self.__respuesta = util.menu(self.__OPCION)

        if self.__respuesta == 1:
            self.añadir_contacto()
        elif self.__respuesta == 2:
            self.lista_contactos()
        elif self.__respuesta == 3:
            self.buscar_contacto()
        elif self.__respuesta == 4:
            self.editar_contacto()
        elif self.__respuesta == 5:
            self.cerrar_agenda()
        else:
            raise ValueError("Marque un opcion valida")




    def añadir_contacto(self) ->None:
        system('cls')
        print(util.titulo("Añadiendo contacto"))
        nombre = input("Ingrese el nombre: ")
        nombre_cap = nombre.capitalize()
        numero = int(input("Ingrese el numero: "))

        if numero < 1000000000:
            print("\n---Ingrese un numero valido---\n")
            system('pause')
            self.iniciar()
        
        mail = str(input("Ingrese el mail: "))

        self.__contactos.append({'nombre':nombre_cap,  
                                'telefono':numero, 
                                'mail':mail })


    def lista_contactos(self) -> str:
        system('cls')
        print(util.titulo("Lista de contactos"))
        if len(self.__contactos) == 0:
            print("No tiene contactos en la lista")
        else:
            for x in range(len(self.__contactos)):
                print (f""" Nombre: {self.__contactos[x]['nombre']} ------- Telefono: {self.__contactos[x]['telefono']} ------- Mail: {self.__contactos[x]['mail']} \n""")
        system('pause')
        

    def buscar_contacto(self) -> str:
        system('cls')
        print(util.titulo("Buscador de contactos"))
        buscado = input("Indique la persona que quiera buscar: ")
        buscado_cap = buscado.capitalize()



        for x in range(len(self.__contactos)):
            if self.__contactos[x]['nombre'] == buscado_cap:
                print (f""" Nombre: {self.__contactos[x]['nombre']} ------- Telefono: {self.__contactos[x]['telefono']} ------- Mail: {self.__contactos[x]['mail']} \n""")
                system('pause')
                return x
            else:
                print("No exite esa persona en la agenda")
                return True
                system('pause')


    def editar_contacto(self) -> None:
        system('cls')
        print(util.titulo("Editando contacto"))
        edicion = self.buscar_contacto()
        condicion = False

        if edicion:
            system('pause')
            self.iniciar()

        while condicion == False:
            resp_edit = util.menu(self.__OPCION_EDICION)

            if resp_edit == 1:
                system('cls')
                print(util.titulo(f"Nombre a editar: {self.__contactos[edicion]['nombre']}"))
                nombre_nuevo = input("Ingresa el nuevo nombre: ")
                nombre_nuevo_cap = nombre_nuevo.capitalize()
                self.__contactos[edicion]['nombre'] = nombre_nuevo_cap
                print("\nNombre cambiado\n")
                system('pause')

            elif resp_edit == 2:
                system('cls')
                print(util.titulo(f"Numero a editar: {self.__contactos[edicion]['telefono']}"))
                numero_nuevo = input("Ingresa el nuevo numero: ")
                self.__contactos[edicion]['telefono'] = numero_nuevo
                print("\nNumero cambiado\n")
                system('pause')

            elif resp_edit == 3:
                system('cls')
                print(util.titulo(f"Mail a editar: {self.__contactos[edicion]['mail']}"))
                mail_nuevo = input("Ingresa el mail nuevo: ")
                self.__contactos[edicion]['mail'] = mail_nuevo
                print("\nMail cambiado\n")
                system('pause')

            elif resp_edit == 4:
                condicion = True
            else:
                raise ValueError("Marque un opcion valida")
            
        

    def cerrar_agenda(self) -> bool:
        if self.__respuesta == 5:
            return False
        else:
            return True


    def iniciar(self) -> None:
        while self.cerrar_agenda():
            self._interfaz()
        print(util.titulo("Agenda cerrada"))


def main():

    agenda1 = Agenda()
    agenda1.iniciar()


main()