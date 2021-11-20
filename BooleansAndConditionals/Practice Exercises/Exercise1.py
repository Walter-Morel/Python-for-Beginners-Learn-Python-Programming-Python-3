"""Ejercicios de práctica Booleanos y condicionales  
Ejercicio 1: 
 
Crea un programa que pregunte al usuario qué distancia quiere recorrer. Si quiere viajar menos de 
tres millas, dígale que camine. Si quiere viajar más de tres millas, pero menos de trescientos 
millas, dígale que conduzca. Si quiere viajar trescientas millas o más, dígale que 
volar. 
 
Ejemplo de salida: 
 
¿A qué distancia le gustaría viajar en millas? 2500 
Le sugiero que vuele a su destino"""

distancia = input('Digame cuantas millas quieres viajar: ')

#Convertimos el valor de $distancia en entero
distancia = int(distancia)

if distancia < 3:
    modo_deTransporte = 'caminando'
             
elif distancia < 300:
    modo_deTransporte = 'en coche'
    
else:
    modo_deTransporte = 'en avion'

print('Le suguiero que vaya {}'.format(modo_deTransporte))
