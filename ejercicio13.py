"""Escribir una clase Cuenta que tenga el siguiente comportamiento:

c = Cuenta('Pérez')   
d = Cuenta('López')            
c.acreditar(100, 'Sueldo') 
c.transferir(30, d)      
c.extraer(60, 'Shopping')        
c.saldo() ==> 10
d.saldo() ==> 40 
print(c) Cuenta de Pérez (10)
c.movimientos() ==> [('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
d.movimientos() ==> [('acreditación',30,'Cuenta de Pérez')]
d.extraer(100, 'Deudas') ==> ERROR ValueError: Fondos Insuficientes"""


class Cuenta():
    def __init__ (self, nombre):
        self.__nombre = nombre
        self.__movimientos: list[tuple] = [()]
        self.__dinero_almacenado = 0

    @property
    def nombre (self) -> str:
        return self.__nombre

    @property
    def dinero_almacenado(self) -> int:
        return self.__dinero_almacenado

    def saldo(self) -> str:
        return print(f"La cuenta '{self.nombre}' tiene almacenado: ${self.dinero_almacenado} \n")

    def acreditar (self, importe, motivo) -> None:
        self.__dinero_almacenado += importe
        self.__movimientos.append(('Acreditación',importe,motivo))

    def transferir (self, importe, destinatario) -> None:
        if importe > self.__dinero_almacenado:
            raise ValueError ("Dinero Insuficientes")
        else:
            self.__dinero_almacenado -= importe
            self.__movimientos.append(('transferencia',importe, f"Cuenta de: '{destinatario.nombre}'"))
            destinatario.__dinero_almacenado += importe
            destinatario.__movimientos.append(('transferencia',importe, f"Cuenta de: '{self.nombre}'"))

    def extraer(self, importe, motivo) -> None:
        if importe > self.__dinero_almacenado:
            raise ValueError ("Dinero Insuficientes")
        else:
            self.__dinero_almacenado -= importe
            self.__movimientos.append(('Extraccion',importe,motivo))
    

    def movimientos (self) -> list[tuple]:
        for elementos in self.__movimientos:
            return print(self.__movimientos)

    def __str__ (self) -> str:
        return f"\n{'-'*5} Esta es la caja de {self.nombre}, que contiene: ${self.dinero_almacenado} {'-'*5}\n"  


def main ():
    c = Cuenta('Pérez')
    d = Cuenta('López') 

    c.acreditar(100, 'Sueldo')
    c.acreditar(1000, 'Venta')

    d.acreditar(500, 'Sueldo')

    d.saldo() # ==> 500
    c.saldo() # ==> 1100

    c.extraer(800, 'Shopping')
    c.saldo()
    # d.extraer(600, 'Deudas') ==> ValueError ("Dinero Insuficiente")

    c.movimientos() # ==> [('acreditación',100,'Sueldo'), ...]
    d.movimientos()

    print(c) # Cuenta de Pérez (1100)
    print(d)
    
    c.transferir(300, d)
    # c.transferir(500, d)  ==> ValueError ("Dinero Insuficiente")
    c.movimientos()
    d.movimientos()

    c.saldo()
    d.saldo()


main()



