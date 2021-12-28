import time 
from funciones_ejemplos.fun_ejemplos import horario

puestos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'Aux1', 'Aux2', 'Supervisor', 'Alarmas']

fecha = time.strftime("%d-%m-%Y")
hora = time.strftime('%H:%M')

horario_turno = horario(hora)
carpeta = f'PINES {fecha}'

print(horario_turno)