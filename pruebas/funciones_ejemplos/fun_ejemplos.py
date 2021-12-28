import os
from funciones_ejemplos.col import blanco, rojo
import time

def limpiar():
    if os.name == 'nt':
        os.system('cls')
        print(blanco)
    else:
        os.system('clear')
        
def converint(valor):
    while valor == ' ' or valor.isdecimal() == False:
        limpiar()
        print('Error\nIntente nuevamente: ')
        valor = input(f'{rojo}>>> ')
    print(blanco)
    valor = int(valor)
    return valor

def ingrese(valor):
    a = input(f'{blanco}Ingrese {valor}: {rojo}')
    print(f'{blanco}')
    return a

def esperar():
    time.sleep(3)
    
def verificar_vacio(dato): #función para verificar si está vació el campo
    while dato == "":
        print(f"{blanco}Campo vacio")
        print(f"{blanco}Ingrese nuevamente:")
        dato = input (f">>>{rojo} ")
    return dato

def horario(valor):
    valor = int(valor)
    if valor >= 0 and valor <= 6:
        horario_turno = '00hs a 06hs'
    elif valor >= 6 and valor <= 12:
        horario_turno = '06hs a 12hs'
    elif valor >= 12 and valor <= 18:
        horario_turno = '12hs a 18hs'
    elif valor >= 18 and valor <= 24:
        horario_turno = '18hs a 00hs'
    else:
        print('Error')
        esperar()
    return horario_turno