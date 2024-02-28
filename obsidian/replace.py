#!/usr/bin/env python3

import os
import fileinput
import re

def reemplazar_en_archivos(directorio_base, fechas_a_reemplazar):
    # Construir el patrón de expresión regular con las fechas proporcionadas
    patron = re.compile(r"\[\[(" + '|'.join(map(re.escape, fechas_a_reemplazar)) + r")\]\]")

    # Recorrer los archivos en el directorio base y sus subdirectorios
    for directorio_actual, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            ruta_completa = os.path.join(directorio_actual, archivo)

            # Reemplazar la cadena en el archivo si se encuentra
            with fileinput.FileInput(ruta_completa, inplace=True, openhook=fileinput.hook_encoded("utf-8")) as f:
                for linea in f:
                    # Utilizar el patrón para buscar y reemplazar las fechas
                    linea = patron.sub(r"\1", linea)
                    print(linea, end='')

# Directorio base donde se realizará la búsqueda y reemplazo
directorio_base = r"C:\Users\leom7\Documents\Obsidian Vault\01 Personal"

# Fechas a buscar y reemplazar
fechas_a_reemplazar = [
    '2022-12-05', '2022-12-21', '2022-12-23', '2022-12-27', '2023-02-10', '2023-02-09', '2023-04-02', '2023-08-08', '2023-08-12', 
    '2023-08-13', '2023-09-05', '2023-09-02', '2021-08-28', '2023-08-28', '2023-09-23', '2023-10-13', '2023-11-09', '2023-10-17', 
    '2023-10-22', '2023-10-25', '2023-10-26', '2024-01-29', '2024-02-03', '2024-02-10', '2024-02-25', '2024-02-24', '2024-02-17', 
    '2023-06-02', '2024-02-07'
]

# Llamar a la función para realizar los reemplazos
reemplazar_en_archivos(directorio_base, fechas_a_reemplazar)
