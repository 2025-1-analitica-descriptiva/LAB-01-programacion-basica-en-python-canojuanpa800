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

def get_columns(lines)-> list:
    return [tuple([line.strip().split()[0],contar_elementos(line.strip().split()[3]), contar_elementos(line.strip().split()[4])]) for line in lines]

def contar_elementos(sequence):
    return len(sequence.split(","))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """

    lines = get_lines()
    columns = get_columns(lines)
    return columns
# print(pregunta_10())