"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def get_lines():
    lines = []
    with open("files\input\data.csv","r",encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def get_columns(lines):
    return [tuple([line.strip().split()[0],line.strip().split()[4]]) for line in lines]

def mapper(sequence):
    """Mapper"""
    result = []
    for key,value in sequence:
        words = value.split(',')
        for word in words:
            number = word.split(':')[1]
            result.append(tuple([key, number]))
    return result

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += int(value)
    return counter

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    lines = get_lines()
    columns = get_columns(lines)
    mapped  = mapper(columns)
    ans = reducer(sorted(mapped))
    return ans
# print(pregunta_12())