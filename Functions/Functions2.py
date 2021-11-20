def informacion (nombres, apellido, puesto = 'Desconocido'):
    print('{0:10} | {1:10} | {2:20}'.format('Nombre', 'Apellido', 'Puesto'))
    print('{0:10} | {1:10} | {2:<20}'.format(nombres, apellido, puesto))


nombres = input('Por favor dime tu Nombre: ')
apellidos = input('Por favor dime tu Apellido: ')
puesto = input('Por favor dime tu profesión: ')
#informacion ('{}','{}','{}'.format(nombres, apellidos, puesto))
informacion (f'{nombres}',f'{apellidos}',f'{puesto}')
