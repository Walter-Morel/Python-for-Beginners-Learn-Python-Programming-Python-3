'''conten = open('C:/Log/test.txt')
contenido = conten.read()

print(contenido)
conten.close()'''

comentario = input('Indica un comentario: ')
with open('C:/Log/test.txt', 'w') as the_file:
    the_file.write('{}\n'.format(comentario))
with open('C:/Log/test.txt') as the_file:
    print(the_file.read())