"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    a = open("files/input/data.csv", "r").readlines()
    sum = 0
    for i in a:
        sum += int(((i.split(",")[0]).split("\t"))[1])
    return sum

