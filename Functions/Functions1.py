"""#Ejemplo para declarar una función

def saludo(parametro1, parametro2):
    num = input('Bienvenido {} {}!, por favor ingresa un número: '.format(parametro1, parametro2))
    

def es_mayor(num):
    '''Determinamos si el número ingresado  por telcado es mayor que 50'''
    if num < 50:
        return False
    else:
        return True

#Escribimos el bloque de código.
nombre = input('Escribe tu nombre: ')
apellido = input('Escribe tu apellido: ')
num = int(input(saludo(nombre, apellido)))"""

def get_name():
    name = input('Díme tu nombre: ')
    return name

def say_name(name):
    print('Tu nombre es {}'.format(name))
    
def get_and_say_name():
    name = get_name()
    say_name(name)

get_and_say_name()
    


