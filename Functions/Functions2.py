def informacion (nombres, apellido, puesto = 'Desconocido'):
    print('{0:10} | {1:10} | {2:10}'.format('Nombre', 'Apellido', 'Puesto'))
    print('{0:10} | {1:10} | {2:<10}'.format(nombres, apellido, puesto))


nombres = input('Por favor dime tu Nombre: ')
apellidos = input('Por favor dime tu Apellido: ')
puesto = input('Por favor dime tu profesión: ')
informacion (f'{nombres}','{apellido}','{puesto}')

