import os
from Funciones.col import blanco, rojo

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
        