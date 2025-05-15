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
    return [tuple([line.strip().split()[1],line.strip().split()[3]]) for line in lines]

def mapper(sequence):
    """Mapper"""
    result = []
    for key,value in sequence:
        words = value.split(',')
        for word in words:
            result.append(tuple([word, key]))
    return result

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += int(value)
    return counter

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """



    lines = get_lines()
    columns = get_columns(lines)
    mapped  = mapper(columns)
    ans = reducer(sorted(mapped))
    return ans
# print(pregunta_11())