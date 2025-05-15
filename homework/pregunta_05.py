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

def get_columns_1y2(lines)-> list:
    return [tuple(line.strip().split()[:2]) for line in lines]


def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = (key, int(value), int(value))
        else: 
            value = int(value)
            mayor = counter[key][1]
            menor = counter[key][2]
            if value > mayor:
                mayor = value
            if value < menor:
                menor = value
            counter[key] = (key, mayor, menor)
    return list(counter.values())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    lines = get_lines()
    columns = get_columns_1y2(lines)
    ans = reducer(columns)
    return sorted(ans)
# print(pregunta_05())
