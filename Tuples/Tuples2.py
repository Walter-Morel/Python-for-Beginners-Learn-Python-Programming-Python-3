'''contact_info = ['Mark', '8897-5542']
(phone, email) = contact_info

print(phone)
print(email)'''

contacts = [('Mark', '7763-3345'), ('Sven', '6653-7764')]

def alto_y_bajo (num):
    '''Determinamos si el número es alto o bajo'''
    masAlto = max(num)
    masBajo = min(num)
    return(masAlto,masBajo)

loteriaNum = [16, 4, 42, 15, 23, 8]
(masAlto, masBajo) = alto_y_bajo(loteriaNum)

print('El número mas alto de loteria es: {}'.format(masAlto))
print('El número mas bajo de loteria es: {}'.format(masBajo))


for (name, phone) in contacts:
    print('El número de {} es el {}'.format(name,phone))




