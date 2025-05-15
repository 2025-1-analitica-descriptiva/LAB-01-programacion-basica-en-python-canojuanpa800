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

def get_third_column(lines)-> list:
    return [line.strip().split()[2] for line in lines]

def get_month(sequence):
    return [date.split("-")[1] for date in sequence]

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += 1
    return list(counter.items())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    lines = get_lines()
    dates = get_third_column(lines)
    months = get_month(dates)
    ans =  reducer(months)
    return sorted(ans)
# print(pregunta_04())