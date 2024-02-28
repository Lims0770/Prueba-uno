#!/usr/bin/env python3

class Persona:
    '''
    Clase para representar objetos de tipo Persona.
    '''
    def __init__(self, nombre, genero, ocupacion, cedula):
        # Método que inicializa el objeto de tipo Persona (constructor).
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula  # Nuevo atributo cedula

    # Métodos para obtener y establecer el valor de cedula
    def get_cedula(self):
        return self._cedula

    def set_cedula(self, cedula):
        self._cedula = cedula

    # Encapsular todos los atributos con métodos de acceso
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre
        

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_ocupacion(self):
        return self._ocupacion

    def set_ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    def __str__(self):
        # Método especial que se llama cuando se utiliza la función str(objeto).
        return f'Persona: [nombre: {self._nombre}, genero: {self._genero}, ocupación: {self._ocupacion}, cedula: {self._cedula}]'

    def saludar(self):
        # Método personalizado para imprimir un saludo.
        print(f'Hola, soy {self._nombre}')

# Ejemplos de uso
if __name__ == '__main__':
    persona1 = Persona('Juan', 'M', 'Estudiante', '1234567890')
    print(persona1.__str__())

    persona1.set_cedula('9876543210')

    print(f"Cédula de persona1: {persona1.get_cedula()}")
