def cat_say(text):
#creamos una variable que se encargue de contar el catacter total de la variable $text
    text_length = len(text)

    print('         {}'.format('_' * text_length))
    print('       < {} >'.format(text))
    print('         {}'.format('-' * text_length))
    print('        /')
    print(' /\_/\ /')
    print('( o.o )')
    print(' > ^ <')

def main():
    text = input('Escribe cualquier texto: ')
    cat_say(text)

if __name__ == '__main__':
    main()
