f_desordenada = 'C:/Log/animals.txt'
f_ordenada = 'C:/Log/animals-sorted.txt'
animals = []

try:
    with open (f_desordenada) as animals_file:
        for line in animals_file:
            animals.append(line)
    animals.sort()
except:
    print('No se puede abrir {}.'.format(f_desordenada))
try:
    with open ('f_ordenada', 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('No se puede abrir {}.'.format(f_ordenada))