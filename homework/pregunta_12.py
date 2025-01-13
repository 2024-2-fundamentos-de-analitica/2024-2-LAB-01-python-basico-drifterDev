"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    a = open("files/input/data.csv", "r").readlines()
    b = {}
    for i in a:
        c = i.split("\t")[0]
        d = i.split("\t")[4].split(",")
        d = [int(i.split(":")[1]) for i in d]
        if c[0] in b:
            b[c[0]] += sum(d)
        else:
            b[c[0]] = sum(d)
    return b

