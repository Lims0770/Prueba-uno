
from tst import empleados

lista_edades = []
promedio = 0

for i in empleados:
    lista_edades.append(i['age'])
    promedio += i['age']

result = promedio / len(lista_edades)
print(result)
