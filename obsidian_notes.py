
#!/usr/bin/env python3

import os
import re
import fileinput

a = 1
b = 4
num_lines = 84
ruta_archivo = "My_Clippings.txt"

# variables book_info = {Author: , Tile: , Date: }, quote_info = {take_date: , posicion; , page: , quote: }

# funciones para la obtencion de la line_list
# Patrones
Title_Pattern = r'((^.*?)(\s\())'
year_pattern = r'\((\d{4})\)\w+|\b(\d{4})\b'
Author_pattern = r'\(()(([A-Z\u00C0-\u017F][a-z\u00C0-\u017F]*)\s([A-Z\u00C0-\u017F][a-z\u00C0-\u017F]*)[^[\]]*?)\)' # iterar primero por los match y printiar match.group(2) para que salga sin parentesis
position_pattern = r'([0-9]\w+\-[0-9]\w+)'
take_date_pattern = r'(([0-9]{1,2})\s[de]\w+\s([a-z]*)\s[de]\w+\s([0-9]{4}))' # Revisar los grupos de captura tenemos uno por cada parametro de la fecha
page_pattern = r'página (\d+)'
quote_title_pattern = r'^([\w\u00C0-\u017F\,\¿]+(?:\s+[\w\u00C0-\u017F\,]+){0,10}|[^\.\?]+)'




def open_file(ruta_archivo):
    return  open(ruta_archivo, 'r', encoding='utf-8')

 
def extract_line_range(archivo, start, end):
    with open_file(ruta_archivo) as file:
        lines = file.readlines()
        extracted_lines = lines[start:end+1]
        extracted_lines.remove("\n")
        return extracted_lines


def get_lines(ruta_archivo, a, b):
    line_list = []
    for i in range(num_lines):
        extracted_lines = extract_line_range(ruta_archivo, a, b)#o 1, 4
        line_list.append(extracted_lines)
        a = b + 2
        b = b + 5
    return line_list
# funciones para filtrar la información y cambiar su formato


## Función para obtener el match de una regex en base al grupo
def re_result(num, line, pattern):
    match = re.search(pattern, line)
    result = match.group(num) if match else None
    return result

## Función para obtener la información de libro
def get_book_info(line):
    book_info = {"Author": None, "Title": None, "Year": None}
    

    book_info['Author'] = re_result(2, line, Author_pattern)
    book_info['Year'] = re_result(0, line, year_pattern)
    book_info['Title'] = re_result(2, line, Title_Pattern)
    
    author = book_info.get('Author')
    title = book_info.get('Title')
    
    if author and title and author in title:
        title = title.replace(f"{author} - ", '')
        book_info['Title'] = title
    else:
        pass
        
    return book_info

# funcion para tomar la información de pos

def get_pos_date_info(line): # date format dd/mm/aaaa
    pos_date_info = {'Position': None, 'Date': None, 'Page': None}
    # pos info
    pos_date_info['Position'] = re_result(0, line, position_pattern)
    pos_date_info['Page'] = re_result(0, line, page_pattern)
    # date compose
    date_list = []
    for i in range(3):
        i += 2
        value = re_result(i, line, take_date_pattern)
        date_list.append(value)
    
    date_list[1] = month_to_number(date_list[1])

    pos_date_info['Date'] = f"{date_list[0]}/{date_list[1]}/{date_list[2]}"


    return pos_date_info

# quote



def get_quote(line):
    quote_info = {'Quote': None, 'QuoteT': None}
    quote_info['Quote'] = line
    quoteT = re_result(0, line, quote_title_pattern)
    
    if "\n" in quoteT:
        quoteT = quoteT.replace("\n", '')
    else:
        pass

    quote_info['QuoteT'] = quoteT
        
    return quote_info
    

# funcion para cambiar de month a el numero
def month_to_number(month):
    months_esp = {
        'enero': "01" , 'febrero': "02", 'marzo': "03", 'abril': "04",
        'mayo': "05", 'junio': "06", 'julio': "07", 'agosto': "08",
        'septiembre': "09", 'octubre': "10", 'noviembre': "11", 'diciembre': "12"
    }
    month_number = months_esp.get(month)
    return month_number



def get_dic(line):
    dic = {}
    dic.update(get_book_info(line[0]))
    dic.update(get_pos_date_info(line[1]))
    dic.update(get_quote(line[2]))

    return dic
        

def no_None_print(dic, x):
    
    if dic[x] is None:
        dic[x] = ''
    else: 
        pass

    return dic[x]

def make_quote_note(dic):

    dic['Page'] = no_None_print(dic, 'Page')
    dic['Author'] = no_None_print(dic, 'Author')
    dic['Year'] = no_None_print(dic, 'Year')


    Template_quote = f"""---
Fecha de toma: {dic['Date']}
Libro: [[{dic['Title']}]]
posición: {dic['Position']}
página: {dic['Page']}
---
# {dic['QuoteT']}
>{dic['Quote']}

{dic['Author']}, {dic['Year']} """

    return Template_quote


def main_note_content(dic):
    dic['Author'] = no_None_print(dic, 'Author')
    
    dic['Year'] = no_None_print(dic, 'Year')
    Template_bookNote = f"""---
    Autor: {dic['Author']}
    Año: {dic['Year']}
    ---
    # {dic['Title']}
    """
    return Template_bookNote





def crear_carpetas():
    # Crear carpeta de notas
    carpeta_notas = 'Notas'
    if not os.path.exists(carpeta_notas):
        os.makedirs(carpeta_notas)

    # Crear carpeta de archivos sobre libros
    carpeta_libros = 'Libros'
    if not os.path.exists(carpeta_libros):
        os.makedirs(carpeta_libros)

    return carpeta_notas, carpeta_libros

def crear_nota(titulo, contenido, carpeta_notas):
    # Crear archivo de nota en la carpeta de notas
    nombre_archivo = f"{titulo}.md"
    ruta_archivo = os.path.join(carpeta_notas, nombre_archivo)
   
    if os.path.exists(ruta_archivo):
        return None

    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido)
        
        return titulo

def actualizar_libro(libro, nota, carpeta_libros):
    # Crear o actualizar archivo sobre el libro en la carpeta de libros
    nombre_archivo_libro = f"{libro}.md"
    ruta_archivo_libro = os.path.join(carpeta_libros, nombre_archivo_libro)

    with open(ruta_archivo_libro, 'a') as archivo_libro:
            archivo_libro.write(f"- [[[{nota}]]\n")

    return ruta_archivo_libro



if __name__ == "__main__":
    lines = get_lines(ruta_archivo, a, b)
    # make main dic
    carpeta_notas, carpeta_libros = crear_carpetas()
    i = 1
    for line in lines:
        dic = get_dic(line) # Diccionario de una quoute
        quote_content = make_quote_note(dic)
        quote = crear_nota(dic['QuoteT'], quote_content, carpeta_notas) # creamos la nota
        main_note_content2 = main_note_content(dic)
        main_note = crear_nota(dic['Title'], main_note_content2, carpeta_libros)
        actualizar_libro(main_note, quote, carpeta_libros)
        print(f"Nota numero {i} terminada")
        i += 1
        


    
