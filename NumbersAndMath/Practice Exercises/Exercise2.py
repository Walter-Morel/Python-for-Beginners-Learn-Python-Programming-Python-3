"""Partiendo del ejemplo anterior, supongamos también que ha ahorrado 918 dólares para financiar su nuevo 
proyecto. Se pregunta cuántos días podrá mantener un servidor en funcionamiento antes de que se le acabe el dinero. 
Por supuesto, espera que su red social se haga popular y requiera 20 servidores para 
servidores para satisfacer la demanda. ¿Cuánto costará su funcionamiento en ese momento? 
 
Escribe un programa en Python que muestre las respuestas a las siguientes preguntas: 
 
¿Cuánto cuesta operar un servidor por día? 
 
¿Cuánto cuesta operar un servidor al mes? 
 
¿Cuánto cuesta operar veinte servidores por día? 
 
¿Cuánto cuesta explotar veinte servidores al mes? 
 
¿Cuántos días puedo operar un servidor con 918 dólares?"""

costo_hora = 0.51
costo_dia = 24 * costo_hora
costo_mes = 30* costo_dia
costo_veintePorDia = 20 * costo_dia
costo_veintePorMes = 20 * costo_mes
presupuesto = 918
operativo_porDia = presupuesto / costo_dia

print('Costo del servicio por dia es: ${:.2f}.'.format(costo_dia))
print('Costo del servicio por mes es de : ${:.2f}.'.format(costo_mes))
print('Costo de veinte servidores por dia : ${:.2f}.'.format(costo_veintePorDia))
print('Costo de veinte servidores por mes : ${:.2f}.'.format(costo_veintePorMes))
print('Con un presupuesto de ${0:2f} tu servicio puede estar operativo {1:.0f} dias.'.format(presupuesto,operativo_porDia)) 
