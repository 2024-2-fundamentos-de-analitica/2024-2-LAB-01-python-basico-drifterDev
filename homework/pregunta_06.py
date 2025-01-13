"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


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

    a = open("files/input/data.csv", "r").readlines()
    b = {}
    for i in a:
        c = ((i.split("\t"))[-1]).split(",")
        for j in c:
            d = j.strip()
            e = d.split(":")
            f = e[0]
            g = int(e[1])
            if f in b:
                if g > b[f][0]:
                    b[f][0] = g
                if g < b[f][1]:
                    b[f][1] = g
            else:
                b[f] = [g, g]
    return sorted([(k, v[1], v[0]) for k, v in b.items()])
