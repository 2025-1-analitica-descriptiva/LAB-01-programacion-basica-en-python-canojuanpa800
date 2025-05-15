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


def get_columns_2y1(lines)-> list:
    return [tuple([line.strip().split()[1], line.strip().split()[0]]) for line in lines]


def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        key = int(key)
        if key not in counter:
            counter[key] = [value]
            # print(counter)
        else:
            # print(counter[key])
            counter[key] = counter[key] + [value]
    return list(counter.items())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    lines = get_lines()
    columns = get_columns_2y1(lines)
    ans = reducer(columns)
    return sorted(ans)
# print(pregunta_07())



