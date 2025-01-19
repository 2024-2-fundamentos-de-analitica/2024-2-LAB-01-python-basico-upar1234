"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    from collections import Counter
    import csv
    dic = {}
    lis = []
    letters = [x for x in [['a',0],['b',0],['c',0],['d',0], ['e',0],['f',0], ['g',0]]]
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    for line1 in csvfile:
        x=line1.split('\t')
        num = x[1]
        third = x[3].split(sep=',')
        l = [(x, num) for x in third]
        lis.append(l) 
    for element in lis:
        for ele in element:
            for elemento in letters:
                if str(ele[0]) in elemento:
                    elemento[1] += int(ele[1])
    dic = dict(letters)
    return dic
    print(dic)
                    
                
        
pregunta_11()