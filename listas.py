# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:47:22 2021

@author: amontinsua
"""

"""
LISTAS

"""

import numpy as np
import collections
import itertools

def eliminar_repetidos (lista_l):
	lista_sin_repes = []
	for item in lista_l:
		if item not in lista_sin_repes:
			lista_sin_repes.append(item)
	return lista_sin_repes
	
"""
Ordena la lista por número de repeticiones, de menos a más repetidos
"""
def orderByElementMasRepe(lista_l):
	from itertools import groupby
	pares = [(valor, sum(1 for x in ocurrencias)) for valor, ocurrencias in groupby(lista_l)] #obtiene una lista de tuplas: [(valor1, numVecesRepe), (valor2, numVecesRepe),...]
	lista_ordenada = [valor for valor, ocurrencias in sorted(pares, key=lambda x: x[1], reverse=True)]
	return lista_ordenada
"""
Devuelve True si todos los elementos de la lista que le pasamos como parámetro son iguales; en caso contrario devuelve False
"""
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)
    

lista1 = [1,2,3,4,5,5,6,6,7,7,7,7,7]
lista_equals = [5,5,5]
all_elem_equal_lista1 = all_equal(lista1)
print("todos iguales=", all_elem_equal_lista1)

all_elem_equal_lista2 = all_equal(lista_equals)
print("todos iguales=", all_elem_equal_lista2)

lista1_ordenada_por_repes = orderByElementMasRepe (lista1)
print("lista1_ordenada_por_repes=", lista1_ordenada_por_repes)

lista1_sin_repe = eliminar_repetidos (lista1)
print("lista1_sin_repe=", lista1_sin_repe)