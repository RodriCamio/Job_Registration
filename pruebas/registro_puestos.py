from funciones_ejemplos.fun_ejemplos import ingrese, converint, esperar, limpiar, pregunta, verificar_sn
from funciones_ejemplos.col import blanco, rojo, verde
from funciones_ejemplos.variables import puestos, fecha, horario_turno
from hoja_de_texto.texto import cargar_datos, hoja_revision, inicio_hoja_revision, inicio_texto, leer_a, leer_b

while True:
    limpiar()
    print(f'{blanco}Registro de Puestos {fecha}')
    print('\nMenu:\n1 - Agregar registro\n2 - Ver registro\n3 - Ver ficha tecnica\n4 - Salir\n')
    opcion = input(f'>>>{rojo} ')
    print(f'{blanco}')
    opcion = converint(opcion)
    if opcion == 1:
        limpiar()
        print('Agregar Registro:\n')
        inicio_texto()
        turno = ingrese('numero de turno')
        supervisor = ingrese('nombre y apellido de supervisor')
        turno = converint(turno)
        cargar_datos('Turno', turno)
        cargar_datos('Supervisor', supervisor)
        cargar_datos('Horario', horario_turno)
        for i in puestos:
            limpiar()
            print('Agregar Registro:\nIngrese "s" = ok o "n"= tiene alguna falla')
            estado_puesto = verificar_sn(f'Estado del Puesto {i}')
            if estado_puesto == 'S':
                cargar_datos(f'\nPuesto {i}', estado_puesto)
            elif estado_puesto == 'N':

                inicio_hoja_revision(f'\nPuesto {i}', 'REVISAR')  
                cargar_datos(f'\nPuesto {i}', 'REVISAR')                
                prendida = verificar_sn('Esta encendido el puesto')
                hoja_revision(f'- Esta Prendida?', f'{prendida}')
                while True:
                    if prendida == 'S':
                        monitor = verificar_sn('El o los monitores estan ok')
                        hoja_revision(f'- Monitor', f'{monitor}')
                        teclado = verificar_sn('El teclado')
                        hoja_revision(f'- Teclado', f'{teclado}')
                        mouse = verificar_sn('El mouse')
                        hoja_revision(f'- Mouse', f'{mouse}')
                        limpiar()
                        print('Describa con sus palabras')
                        otro = pregunta('alguna observacion')
                        hoja_revision(f'- Otro', f'{otro}') 
                        break
                    elif prendida == 'N':
                        motivo = verificar_sn('Conoce el motivo')
                        motivo = motivo.upper()
                        if motivo == 'S':
                            tiene_motivo = ingrese('el motivo por el cual esta apagado el puesto')
                            estado_final = (f'Puesto apagado, debido a {tiene_motivo}')
                            hoja_revision(f'\nPuesto apagado', f'debido a {tiene_motivo}\n')
                            break
                        elif motivo == 'N':
                            estado_final = 'Puesto apagado'
                            hoja_revision(f'\nPuesto apagado','No se sabe motivo')
                            limpiar()
                            print('Describa con sus palabras')
                            otro = pregunta('alguna observacion')
                            hoja_revision(f'- Otro', f'{otro}\n') 
                            break
                        else:
                            print('Error\nIngrese si o no por favor')
                            esperar() #espera 3 seg      
                    else:
                        print('Error\nIngrese si o no por favor')
                        esperar() #espera 3 seg.
            else:
                print('Error\nIngrese si o no por favor')
                esperar() #espera 3 seg.    
    elif opcion == 2:
        leer_a()
    elif opcion == 3:
        leer_b()
    elif opcion == 4:
        break
    else:
        print('Error\n\nIntentelo nuevamente')
    