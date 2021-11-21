#Recorremos una lista de contacto

''contacts = {
    'Anne': {
        'phone': '8872-7764',
        'email': 'anne@example.com'},

    'Mark': {
        'phone': '8837-4452',
        'email': 'mark@example.com'},

    'Sven': {
        'phone': '7762-4324',
        'email': 'sven@example.com'}
}

'''for registro in contacto:
    print('El número de {0} es {1}.'.format(registro, contacto[registro]))'''

'''for registro_name, registro_num in contacto.items():
    print('El número de {0} es {1}.'.format(registro_name, registro_num))'''

for contact in contacts:
    print('Información de contacto de {}.'.format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])''

