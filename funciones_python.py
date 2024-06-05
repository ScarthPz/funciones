import os
os.system("cls")


def sumar_2_numeros():
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))
    total = num1+num2
    print("FUNCIÓN: el total de la suma es:", total) 

def restar_2_numeros(p_num1: float, p_num2:float):
    total = p_num1 - p_num2
    print("FUNCIÓN: el total de la resta es: ", total)

def multiplicar_2_numeros():
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))
    total = num1*num2
    return total

def dividir_2_numeros(p_num1:int, p_num2:int):
    total = p_num1/p_num2
    return total  


def validar_numero():
    while True:
        try:
            num = float(input("Ingrese número: "))
            break
        except:
            print("ERROR! Debe ingresar un número entero!")
    return num 

def menu():
    print("""MENÚ
    1. sumar 2 números
    2. restar 2 números
    3. multiplicar 2 números
    4. dividir 2 números
    """)

def validar_opciones(opciones):
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in opciones:
                break
        except:
            print("ERROR! debe ingresar un número entero")
    return opc 

#######################################################

menu()
opc = validar_opciones( [1,2,3,4] )
if opc == 1:
   sumar_2_numeros()
elif opc == 2:
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))
    restar_2_numeros(num1)
elif opc == 3:
    total = multiplicar_2_numeros()
    print("super total de la multiplicación: ", total)
else:
    num1 = int(input("Ingrese primer número: "))
    num2 = int(input("Ingrese segundo número: "))
    lista = []
    lista.append( dividir_2_numeros(num1,num2) )
    print(lista)