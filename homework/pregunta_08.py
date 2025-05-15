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


def get_columns_2y1(lines)-> list:
    return [tuple([line.strip().split()[1], line.strip().split()[0]]) for line in lines]


def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        key = int(key)
        if key not in counter:
            counter[key] = [value]
        else:
            counter[key] = sorted(list(set(counter[key] + [value])))
    return list(counter.items())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    lines = get_lines()
    columns = get_columns_2y1(lines)
    ans = reducer(columns)
    return sorted(ans)
# print(pregunta_08())