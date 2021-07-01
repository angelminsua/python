# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:30:01 2021
Este programa encuentra dentro de un diccionaio cuyos values son listas, la key con la lista más larga
@author: amontinsua
"""

def maximum_keys(dic):
    longitudes =  max([len(v) for k, v in dic.items()])
    print("longitudes=", longitudes)
    keys = filter(lambda x:len(dic[x]) == longitudes,dic.keys())
    return keys,longitudes
    
dic = {'a': [1],  'c': [99, 66], 'b': [23333]}
result = maximum_keys (dic)
print("clave del diccionario con la lista más larga:", list(result[0]))
print("longitud de la list más larga:", (result[1]))