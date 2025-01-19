"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    import csv
    from collections import Counter
    
    lista1 = []
    lista2 = []
    dic = {}
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    reader = csv.reader(csvfile)
    for row in reader:
        row = str(row)
        row = row.replace("'", '')
        row = row.replace(",",' ' )
        row = row[:-1]
        row = row.split(sep = '\\t')
        row = row[4]
        clave_val = str(row).split()
        for element in clave_val:
            tup=element.split(sep=':')
            dic[tup[0]]=tup[1]
            lista1.append(element)  
    lista1 = [element.split(sep=':') for element in lista1]
    for element in lista1:
        lista2.append(element[0])    
    count = Counter(lista2)
    count = sorted(count.items(), key=lambda x: x[0])
    dic = dict(count)
    print(dic)
    return dic
    
    
            
pregunta_09()