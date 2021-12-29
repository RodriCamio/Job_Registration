import os
from funciones_ejemplos.col import blanco, rojo
import time

def limpiar(): #Limpiar pantalla
    if os.name == 'nt':
        os.system('cls')
        print(blanco)
    else:
        os.system('clear')
        
def converint(valor): #Si el campo esta vacio o no es un numero lo pide de nuevo, pero si es un numero lo convierte a entero
    while valor == ' ' or valor.isdecimal() == False:
        limpiar()
        print('Error\nIntente nuevamente: ')
        valor = input(f'{rojo}>>> ')
    print(blanco)
    valor = int(valor)
    return valor

def ingrese(valor): #es un input que empieza con la palabra "Ingrese .... : .... " (lo ultimo lo pone como rojo)
    a = input(f'{blanco}Ingrese {valor}: {rojo}')
    print(f'{blanco}')
    return a

def esperar(): #sirve para que el programa espere 3 seg antes de continuar
    time.sleep(3)
    
def verificar_vacio(dato): #función para verificar si está vació el campo 
    while dato == "":
        print(f"{blanco}Campo vacio")
        print(f"{blanco}Ingrese nuevamente:")
        dato = input (f">>>{rojo} ")
    return dato

def horario(): #Funcion para determinar si la guardia se encuentra entre las 00-06hs o 06-12hs o 12-18hs y por ultimo 18-24hs
    valor = time.strftime('%H')
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

def pregunta(valor): #es un input que empieza con "¿ .... ?: .... " (lo ultimo lo pone como rojo)
    a = input(f'{blanco}¿{valor}?: {rojo}')
    a = a.upper()
    print(f'{blanco}')
    return a

def verificar_sn(referencia): #Si el campo esta vacio o no es una s o n
    valor = pregunta(referencia)
    while valor != 'S' and valor != 'N':
        limpiar()
        print(f'{blanco}Error, ingrese "S" o "N"\nIntente nuevamente: ')
        valor = pregunta(referencia)
    print(blanco)
    return valor

