airport = [
    ('Aeropuerto Adolfo Suárez Madrid-Barajas', 'MAD'),
    ('Base Aérea de Torrejón de Ardoz', 'TOJ'),
    ('Aeropuerto de Málaga-Costa del Sol', 'AGP'),
    ('Aeropuerto de Melilla', 'MLN')
]


for (name, code_IATA) in airport:
    print('Aeropuerto: {} - Código IATA: {}'.format(name, code_IATA))