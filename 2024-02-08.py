#!/usr/bin/env python3

class Vehiculo:

    def __init__(self, marca, modelo, pais_procedencia, year_fabricacion, tipo_combustible=None, chasis=None, cilindraje=None):

        if not (marca and modelo and pais_procedencia and year_fabricacion):
            print("Los elementos obligatorios (marca, modelo, país de procedencia, year de fabricación) son necesarios.")
        
        self.marca = marca
        self.modelo = modelo
        self.pais_procedencia = pais_procedencia
        self.year_fabricacion = year_fabricacion
        
        # Atributos opcionales
        self.tipo_combustible = tipo_combustible
        self.chasis = chasis
        self.cilindraje = cilindraje

    def __str__(self):
      
        return f"[+] Listando el Vehiculo \nMarca: {self.marca}\n Modelo:{self.modelo}\n año:{self.year_fabricacion}"


if __name__ == "__main__":
    
    
    mi_auto = Vehiculo("Toyota", "Corolla", "Japón", 2022, "Gasolina", "123456789", 2000)
    print(mi_auto)
