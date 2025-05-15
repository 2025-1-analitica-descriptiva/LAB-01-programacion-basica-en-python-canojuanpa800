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

def get_second_column(lines)-> list:
    return [int(line.strip().split()[1]) for line in lines]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lines = get_lines()
    second_column = get_second_column(lines)
    ans = sum(second_column)
    return ans
