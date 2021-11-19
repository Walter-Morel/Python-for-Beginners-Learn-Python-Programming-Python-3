"""Supongamos que estás planeando utilizar tus conocimientos de Python para crear un servicio de red social. 
Decides alojar tu aplicación en servidores que se ejecutan en la nube. Eliges un proveedor de alojamiento 
que cobra 0,51 dólares por hora. Lanzarás tu servicio usando un servidor y quieres saber 
cuánto le costará operar por día y por mes. 
 
Escribe un programa en Python que muestre las respuestas a las siguientes preguntas: 
 
¿Cuánto cuesta operar un servidor por día? 
 
¿Cuánto cuesta operar un servidor por mes?"""


costo_hora = 0.51
costo_dia = 24 * costo_hora
costo_mes = 30* costo_dia

print('Costo del servicio por dia es: ${:.2f}.'.format(costo_dia))
print('Costo del servicio por mes es de : ${:.2f}.'.format(costo_mes))
