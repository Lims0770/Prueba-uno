#!/usr/bin/env python3

direccion_ip = input("Ingrese una dirección IP (formato xxx.xxx.xxx.xxx): ")

octetos = direccion_ip.split('.')
primer_octeto = int(octetos[0])

if 1 <= primer_octeto <= 126:
    resultado = 'Clase A'
elif 128 <= primer_octeto <= 191:
    resultado = 'Clase B'
elif 192 <= primer_octeto <= 223:
    resultado = 'Clase C'
else:
    resultado = 'No pertenece a ninguna clase conocida'

print(f"La dirección IP {direccion_ip} pertenece a la {resultado}.")
