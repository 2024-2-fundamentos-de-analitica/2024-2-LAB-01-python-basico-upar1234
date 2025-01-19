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
    dic = {}
    lis = []
    letters = [x for x in [['A',0],['B',0],['C',0],['D',0], ['E',0]]]
    csvfile = open("C:/Universidad/Sistemas/Fundamentos de analítica/Labs/2024-2-LAB-01-python-basico-upar1234/files/input/data.csv", "r")
    for line1 in csvfile:
        x=line1.split('\t')
        letter = x[0]
        nums = x[4]
        # print(nums, end='\n')
        nums = str(nums).strip('\n')
        nums = nums.split(',')
        for let in letters:
            if let[0] == str(letter):
                for element in nums:
                    element = element.split(':') 
                    let[1] += int(element[-1])
                    
    dic = dict(letters)
    
    return dic
    
pregunta_12()