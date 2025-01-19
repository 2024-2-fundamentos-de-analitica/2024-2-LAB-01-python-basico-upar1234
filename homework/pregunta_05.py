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
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")    
    
    tups = [x for x in (['A', 0, 10], ['B', 0, 10], ['C', 0, 10], ['D', 0, 10], ['E', 0, 10])]
    for line in csvfile:
        for element in tups:
            if line[0] in element:
                if element[1] <= int(line[2]):
                    element[1] = int(line[2])
                
                if element[2] >= int(line[2]):
                    element[2] = int(line[2])
    l = []
    for sub in tups:
        tupla = tuple(sub)
        l.append(tupla)
    return l
pregunta_05()