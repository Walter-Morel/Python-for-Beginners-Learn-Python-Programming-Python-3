'''Create a Python program that captures and displays a person's to­do list. 
Continually promptthe user for another item until they enter a blank item. 
After all the items are entered, display theto­do list back to the user.'''

#To-Do List

item_list = []
fin = False
while not fin:
    tarea = input('Ingrese alguna tarea y luego presione <enter>: ')
    if len(tarea) == 0:
        fin = True
    else:
        item_list.append(tarea)
        print('Tarea agregada')
print()
TDL = 'To-Do List:'
L_TDL = len(TDL)
print('_' * L_TDL)
print(TDL)
print('_' * L_TDL)
for listado_tarea in item_list:
    print(listado_tarea)

