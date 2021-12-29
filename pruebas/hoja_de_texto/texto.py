from funciones_ejemplos.variables import fecha, horario_turno, ruta, carpeta_registro
from funciones_ejemplos.fun_ejemplos import limpiar
import os


def inicio_texto(): #Inicia el texto
    crear_carpeta()
    f = open(f"{ruta}\Registro {fecha} {horario_turno}.txt","a")
    f.write("#"*100)
    f.write(f'\nRegistro de Puestos {fecha}')
    f.close()

def cargar_datos(referencia,valor): #Carga los datos
    if valor == 'S':
        valor = f'OK'
    elif valor == 'N':
        valor == f'REVISAR'
    else:
        pass
    f = open(f"{ruta}\Registro {fecha} {horario_turno}.txt","a")
    f.write(f'\n{referencia}: {valor}')
    f.close()

def inicio_hoja_revision(): #Inicia hoja de revicion
    f = open(f"{ruta}\Hoja de Revision tecnica {fecha} de guardia {horario_turno}.txt","a")
    f.write("#"*100)
    f.write(f'\nHoja de Revision tecnica {fecha}')
    f.close()
    
def hoja_revision(referencia, valor): #carga los datos
    if valor == 'S':
        valor = f'OK'
    elif valor == 'N':
        valor == f'REVISAR'
    else:
        pass
    f = open(f"{ruta}\Hoja de Revision tecnica {fecha} de guardia {horario_turno}.txt","a")
    f.write(f'\n{referencia}: {valor}')
    f.close()
    
def leer_a(): #muestra los resultados
    limpiar()
    print('Resultados')
    with open(f'{ruta}\Registro {fecha} {horario_turno}.txt',"r") as archivo:
        for linea in archivo:
            print(linea)
    input('Presione cualquier tecla para continuar...')

def leer_b(): #muestra los resultados
    limpiar()
    print('Ficha tecnica')
    with open(f'{ruta}\Hoja de Revision tecnica {fecha} de guardia {horario_turno}.txt',"r") as archivo:
        for linea in archivo:
            print(linea)
    input('Presione cualquier tecla para continuar...')
    
def crear_carpeta(): #como su nombre lo indica, crea la carpeta de registros
    if not(os.path.exists(ruta)):
        os.mkdir(carpeta_registro)
    else:
        pass