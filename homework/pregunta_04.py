"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


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
    from collections import Counter
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    
    meses = []
    for row in csvfile:
        mes = row[9:11]
        meses.append(mes)
    meses = Counter(meses)    
    meses = sorted(meses.items(), key=lambda item: item[0])
    return meses
    
pregunta_04()