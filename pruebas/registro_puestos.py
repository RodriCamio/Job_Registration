from funciones_ejemplos.fun_ejemplos import ingrese, converint, esperar
from funciones_ejemplos.col import blanco, rojo, verde
from funciones_ejemplos.variables import puestos, horario_turno 
from hoja_de_texto.texto import cargar_datos, hoja_revision, inicio_hoja_revision, inicio_texto

while True:
    print(f'{blanco}Registro de Puestos')
    print('\nMenu:\n1 - Agregar registro\n2 - Ver registro\n3 - Salir')
    opcion = input('>>> ')
    opcion = converint(opcion)
    if opcion == 1:
        print('Agregar Registro:\n')
        inicio_texto()
        turno = ingrese('numero de turno')
        turno = converint(turno)
        cargar_datos('Turno',turno)
        supervisor = ingrese('nombre y apellido de supervisor')
        cargar_datos('Supervisor', supervisor)
        for i in puestos:
            estado_puesto = ingrese(f'"Si" en caso de que el estado de Puesto {i} sea OK o "No" si tiene alguna falla')
            estado_puesto = estado_puesto.upper()
            if estado_puesto == 'SI':
                cargar_datos('\nPuesto {i}', estado_puesto)
                break
            elif estado_puesto == 'NO':
                inicio_hoja_revision('Puesto',{i})
                cargar_datos('\nPuesto {i}', 'REVISAR')                
                prendida = ingrese('si esta encendido el puesto')
                prendida = prendida.upper()
                hoja_revision(f'- Esta Prendida?', f'{prendida}')
                if prendida == 'SI':
                    pass
                elif prendida == 'NO':
                    while True:
                        motivo = input('¿Conoce el motivo? (si o no)')
                        motivo = motivo.upper()
                        if motivo == 'SI':
                            tiene_motivo = ingrese('el motivo por el cual esta apagado el puesto')
                            estado_final = (f'Puesto apagado, debido a {tiene_motivo}')
                            hoja_revision(f'\nPuesto apagado, debido a {tiene_motivo}')
                            break
                        elif motivo == 'NO':
                            estado_final = 'Puesto apagado'
                            hoja_revision('No se sabe motivo')
                            break
                        else:
                            print('Error\nIngrese si o no por favor')
                            esperar() #espera 3 seg.
                else:
                    print('Error\nIngrese si o no por favor')
                    esperar() #espera 3 seg.
                monitor = ingrese('estado de el/los monitores')
                hoja_revision(f'- Monitor', f'{monitor}')
                teclado = ingrese('estado del teclado')
                hoja_revision(f'- Teclado', f'{teclado}')
                mouse = ingrese('estado del mouse')
                hoja_revision(f'- Mouse', f'{mouse}')
                otro = ingrese('alguna observacion')
                hoja_revision(f'- Otro', f'{otro}')
            else:
                print('Error\nIngrese si o no por favor')
                esperar() #espera 3 seg.    
    elif opcion == 2:
        pass
    elif opcion == 3:
        break
    else:
        print('Error\n\nIntentelo nuevamente')
    