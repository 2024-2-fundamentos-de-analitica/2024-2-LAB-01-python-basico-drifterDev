"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    a = open("files/input/data.csv", "r").readlines()
    b = {}
    for i in a:
        c = i.split(",")[0][0]
        d = int(((i.split(",")[0]).split("\t"))[1])
        if c in b:
            if d > b[c][0]:
                b[c][0] = d
            if d < b[c][1]:
                b[c][1] = d
        else:
            b[c] = [d, d]
    return sorted([(k, v[0], v[1]) for k, v in b.items()])
