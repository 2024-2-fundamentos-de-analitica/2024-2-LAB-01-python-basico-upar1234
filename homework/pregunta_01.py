"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    import csv
    
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    
    edades = []
    for row in csvfile:        
        edad = row[2]
        edades.append(int(edad))
    total = sum(edades)
    return total
        
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
pregunta_01()