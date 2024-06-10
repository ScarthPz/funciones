# ingresar 3 nombres, almacenarios en una lista y en un archivo csv. 


import os
os.system("cls")
import csv
from funcion_ej_nm_largo import*

nombres = []
with open("nombres.csv","w", newline="") as archivo:
    escritor = csv.writer(archivo)
    for vuelta in range(3):
        nom = input("Ingrese nombre : ")
        nombres.append(nom)
    escritor.writerow(nombres)



# mostrar el nombre mas largo

nombre_mas_largo(nombres)
# hay error aqui 