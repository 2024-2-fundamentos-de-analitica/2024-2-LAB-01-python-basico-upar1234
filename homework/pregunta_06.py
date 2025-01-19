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
    
    import csv
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
    for clave in dic.keys():
        lista2.append([clave, 10, 0])
    for element in lista1:
        element = element.split(sep=':')
        clave = element[0]
        for elemento in lista2:
            if str(clave) == str(elemento[0]):
                if int(element[-1]) < int(elemento[1]):
                    elemento[1] = int(element[-1])
                if int(element[-1]) > int(elemento[2]):
                    elemento[2] = int(element[-1])
    l = []
    for element in lista2:
        tup = tuple(element)
        l.append(tup)
    l.sort(key=lambda x: x[0])
    
    return l
                
        
        
pregunta_06()