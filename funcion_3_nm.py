#ingresar 3 nombres, almacenarlos en una lista y en un archivo csv.
import csv
from funciones_ejercicio1 import *

nombres = []
with open("nombres.csv","w",newline="") as archivo:
    escritor = csv.writer(archivo)
    for vuelta in range(3):
        nombre = input("Ingrese nombre: ")
        nombres.append(nombre)
    escritor.writerow(nombres)

#mostrar el nombre más largo
nombre_mas_largo(nombres)