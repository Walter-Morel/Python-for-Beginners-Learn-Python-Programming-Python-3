print ('''
________________________________________________________________________
Primero dime tu nombre, apellido y edad, luego ingresa cualquier texto  |
y lo cambiaremos a mayúsculas y minúscula                               |
________________________________________________________________________|''')

nombre = input('Nombre: ')
apellido = input('Apellido: ')
edad = int(input('Edad: '))

print("____________________________________________")
print('Bienvenido...')
print('{0:10} | {1:10} | {2:10}'.format('Nombre','Apellido','Edad'))
print('{0:10} | {1:10} | {2:<10}'.format(nombre,apellido,edad))
print("____________________________________________")

text = input('Por favor, ingresa cuaqluier texto: ')

print('{} {}'.format(nombre, apellido)+' aquí tienes los textos en mayúsculas y minúsculas')
print('Mayúsculas: '+str(text.upper()))
print('Minúsculas: '+str(text.lower()))
