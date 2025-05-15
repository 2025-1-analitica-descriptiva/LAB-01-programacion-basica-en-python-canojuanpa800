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
    result = [tuple(word.split(":")) for word in sequence]
    return result 

def reducer(sequence):
    """Reducer"""
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = (key, int(value), int(value))
        else: 
            value = int(value)
            menor = counter[key][1]
            mayor = counter[key][2]
            if value > mayor:
                mayor = value
            if value < menor:
                menor = value
            counter[key] = (key, menor, mayor)
    return list(counter.values())



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    lines = get_lines()
    columns = get_column_five(lines)
    cadenas = get_cadenas(columns)
    mapped = mapper(cadenas)
    ans = reducer(mapped)
    return sorted(ans)
# print(pregunta_06())
