"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    import csv
    from collections import Counter

    
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    letras = []
    
    for row in csvfile:    
        letras.append(row[0])
    contador = dict(Counter(letras))
    contador = sorted(contador.items(), key=lambda item: item[0])
    return contador
    
    

pregunta_02()