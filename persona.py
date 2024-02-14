#!/usr/bin/env python3

class Persona:
    '''
    Clase para representar objetos de tipo Persona.
    '''
    def __init__(self, nombre, genero, ocupacion=None):
        # Método que inicializa el objeto de tipo Persona (constructor).
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def __str__(self):
        # Método especial que se llama cuando se utiliza la función str(objeto).
        return f'Persona: [nombre: {self._nombre}, genero: {self._genero}, ocupación: {self._ocupacion}]'

    def saludar(self):
        # Método personalizado para imprimir un saludo.
        print(f'Hola, soy {self._nombre}')

# Ejemplos de uso
if __name__ == '__main__':
    # Crear instancias de la clase Persona
    obj_persona1 = Persona('Luis', 'M', 'Estudiante')
    print(obj_persona1.__str__())  # Se llama al método __str__
    
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria')
    print(obj_persona2)  # __str__ se llama automáticamente
    
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    
    # Llamar al método personalizado saludar
    obj_persona1.saludar()
