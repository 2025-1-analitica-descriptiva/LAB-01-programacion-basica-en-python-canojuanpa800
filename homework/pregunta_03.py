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

def get_columns_1y2(lines)-> list:
    return [tuple(line.strip().split()[:2]) for line in lines]

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += int(value)
    return list(counter.items())



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    lines = get_lines()
    mapped_list = get_columns_1y2(lines)
    ans = reducer(mapped_list)
    return sorted(ans)
# print(pregunta_03())