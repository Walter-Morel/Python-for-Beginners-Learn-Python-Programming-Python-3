'''contacts = {'Jason': '5555-3333', 'carl': '3333-2222'}
jason_phone = contacts['Jason']
carl_phone = contacts['carl']

print('Dial {} llama a Jason'.format(jason_phone))
print('Dial {} llama a Carl'.format(carl_phone))'''

contactos = {
    'Aaron': ['4424-3333', '4332-4143'] ,
    'Paul': '8872-5674',
    'Marry': '7662-6654',
    'Mark': ['7738-6543', '2231-6653']
}
'''for num in contactos['Aaron']:
    print('Contacto: {}'.format(num))'''

if 'Aaron' in contactos.keys():
    print('El número de Aaron es: ')
    print(contactos['Aaron'][0])
if 'Paul' in contactos.keys():
    print('El número de Paul es: ')
    print(contactos['Paul'])

buscar = int(input('Comprueba si existe un número de contacto: '))
print(f'{buscar}' in contactos.values())