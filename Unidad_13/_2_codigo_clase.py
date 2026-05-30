# Queremos calcular el Factorial de un numero n
# Por ejemplo, hagamos el factorial(4) = 1*2*3*4 = 4*3*2*1
# 0 es condicion de corte
"""
Descompongo el n en numeros naturales
4, 3, 2, 1
((1*2)*3)*4 = 4*3*2*1
"""

# n = 4
# parcial = 1
# # range descompone el 4 en 0,1,2,3 correccion +1 => 1,2,3,4
# for x in range(n): # que retoran range(4): 0,1,2,3 / n+1: 1,2,3,4 # condicion de corte esta en el for
#     parcial = parcial * (x+1) # 6 * 4 = 24

# print(f"El factorial de {n} con for in es {parcial}")


# Esto en forma recursiva
# Declarar la funcion recursiva
# El factorial de 4 es : 4*3*2*1 = 1*2*3*4
def factorial_recursivo(n):
    # Valido numero entrante
    if n < 0:
        raise ValueError("No se admite negativos en factorial")
    # Condicion de corte
    if n == 0:
        return 1
    else:
        # condicion recursiva
        return n * factorial_recursivo(n - 1)  # el retorno es la misma


# Invocacion
# try:
#     n = 2900
#     print(f"El factorial de {n} con for in es {factorial_recursivo(n)}")
# except Exception as e:
#     print(f"ERROR: {e}")

# calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75]

# def sumar_forin(calificaciones):
#     parcial = 0
#     for c in calificaciones:
#         parcial = parcial + c
#     return parcial

from functools import reduce
def sumar_lambda(calificaciones):
    return reduce( lambda n1, n2 : n1 + n2 , calificaciones)

calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75]
def sumar_lista_recursiva(calificaciones): #[]
    if len(calificaciones) == 0: # caso base/corte
        return 0 
    else:
        return calificaciones[0] + sumar_lista_recursiva(calificaciones[1:]) # caso recursivo

print(f"La suma de calificaciones con recursividad es {sumar_lista_recursiva(calificaciones)}")


categorias = ["Electrónica", "Muebles", "Electrodomésticos"]

import unicodedata
def normalizar(texto):
    """Convierte a minúsculas y elimina acentos."""
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

import re
def buscar_elemento_recursivo(categorias, categoria):
    if len(categorias)==0: #caso base
        return False
    #if normalizar(categorias[0]) == normalizar(categoria):    #caso base
    if re.search(normalizar(normalizar(categoria), categorias[0])):    #caso base
        return True
    else:
        return buscar_elemento_recursivo(categorias[1:], categoria)    # caso recursivo
    

buscar_elemento_recursivo("Electrónica")

productos = [
    {"nombre": "Notebook", "categoria": "Electrónica", "precio": 1200},
    {"nombre": "Silla", "categoria": "Muebles", "precio": 300},
    {"nombre": "Cafetera", "categoria": "Electrodomésticos", "precio": 150}
]

def buscar_nombre_recursivo(productos, nombre):
    if len(productos)==0: #caso base
        return False
    #if normalizar(categorias[0]) == normalizar(categoria):    #caso base
    if re.search(normalizar(normalizar(nombre), productos[0]["nombre"])):    #caso base
        return True
    else:
        return buscar_nombre_recursivo(productos[1:], nombre)    # caso recursivo