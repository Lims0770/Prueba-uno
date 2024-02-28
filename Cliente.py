
class Persona:
    def __init__(self, nombre, genero, ocupacion, cedula):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    def __str__(self):
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupacion: {self._ocupacion}, cedula: {self._cedula}]')

    def saludar(self):
        print(f'Hola, soy {self._nombre}')



class Cliente(Persona):
    def __init__(self, nombre, genero, ocupacion, cedula, numero_cliente):
        super().__init__(nombre, genero, ocupacion, cedula)
        self._numero_cliente = numero_cliente

    @property
    def numero_cliente(self):
        return self._numero_cliente

    @numero_cliente.setter
    def numero_cliente(self, numero_cliente):
        self._numero_cliente = numero_cliente

    def __str__(self):
        return (f'Cliente: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupacion: {self._ocupacion}, cedula: {self._cedula}, '
                f'numero_cliente: {self._numero_cliente}]')

    def saludar(self):
        print(f'Hola, soy el cliente {self._numero_cliente} - {self._nombre}')



if __name__ == '__main__':
    persona1 = Persona('Juan', 'M', 'Ingeniero', '0912345678')
    print(persona1.__str__())

    persona2 = Persona(genero='F', ocupacion='Estudiante', nombre='Maria', cedula='1234567890')
    print(persona2)

    persona3 = Persona(nombre='Pedro', genero='M', cedula='0987654321', ocupacion='Doctor')
    print(persona3)

    persona1.saludar()



    # Cambiar la cédula de persona3
    persona3.cedula = '1122334455'
    print(persona3)
    
    cliente1 = Cliente('Ana', 'F', 'Abogada', '0987654321', 'C12345')
    print(cliente1.__str__())
    cliente1.saludar()

    # Puedes acceder a los atributos y métodos de Persona desde Cliente
    cliente1.nombre = 'Ana María'
    cliente1.genero = 'M'
    cliente1.saludar()


