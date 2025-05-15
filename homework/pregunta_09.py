"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def get_lines():
    lines = []
    with open("./files/input/data.csv","r",encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def get_column_five(lines)-> list:
    return [line.strip().split()[4] for line in lines]

def get_cadenas(sequence):
    result = []
    lista_elementos = [item.split(',') for item in sequence]
    [result.extend(item) for item in lista_elementos] 
    return result 

def mapper(sequence):
    """Mapper"""
    result = [tuple([word.split(":")[0],1]) for word in sequence]
    return result 

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += value
    return counter


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    lines = get_lines()
    columns = get_column_five(lines)
    cadenas = get_cadenas(columns)
    mapped = mapper(sorted(cadenas))
    ans = reducer(mapped)
    return ans
print(pregunta_09())