nombre = input('Dime el nombre de una persona: ')
comentario = input('Deja un comentario acerca de {}: '.format(nombre))

dic_notas = {
    'notas':{
        'nombre' : f'{nombre}',
        'comentario': f'{comentario}'
        }
    }
for d_notas in dic_notas:
    print('Comentaste sobre '+dic_notas[d_notas]['nombre']+' lo siguiente: '+dic_notas[d_notas]['comentario'])
    