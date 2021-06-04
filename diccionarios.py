# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:11:52 2021

@author: amontinsua
"""

"""
Combina 2 diccionarios en un nuevo diccionario cuya clave es la clave de los diciconarios originales (sin repetir) y el valor para cada clave es una lista con 2 elementos: los valores que tienen los dicionarios originales para esa clave
"""

import pandas as pd	
from itertools import chain
from collections import defaultdict



def combinar_diccionarios(dict1, dict2):


	dict_combinado = defaultdict(list)
	for k, v in chain(dict1.items(), dict2.items()): #chain('ABC', 'DEF') itera así: A B C D E F
	    dict_combinado[k].append(v)
	 
	"""
	for k, v in dict_combinado.items():
	    print(k, v)
	"""
	return dict_combinado

#Pruebas para entender la función defaultdict
someddict = defaultdict(int) #default value of int is 0
print(someddict[3]) #en vez de dar error te devuelve 0
someddict = defaultdict(list) #default value of list is []
print(someddict[3])  #en vez de dar error te devuelve []

#Creo y combino 2 diccionarios
dic1 = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
dic2 =  dict(nombre='nestor', apellido='Plasencia', edad=22, cursos=['php', 'html'])
print("dic1=", dic1)
print("dic2=", dic2)
dic_comb = combinar_diccionarios (dic1, dic2)
print("dic_comb=", dic_comb)

#Creo un dataframe a partir del diccionario
df_orient_index= pd.DataFrame.from_dict(dic_comb, orient='index')
print("df_orient_index=", df_orient_index.head(10))

#df_orient_col= pd.DataFrame.from_dict(dic_comb, orient='columns') #da error pq dic2 tiene una clave (apellido) que no está en dic1. Probemos con 2 diccionarios con las mismas claves

dic1 = {'nombre' : 'Carlos', 'apellido' : 'Rey',  'edad' : 22 }
dic2 =  dict(nombre='nestor', apellido='Plasencia', edad='22')
dic_comb = combinar_diccionarios (dic1, dic2)
df_orient_col= pd.DataFrame.from_dict(dic_comb, orient='columns')
print("df_orient_col=", df_orient_col.head(10)) 

