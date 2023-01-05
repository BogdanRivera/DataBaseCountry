
def find_country(country, data):
    for i in data:
        if i['Country/Territory'] == country:
            return i
# Columna 5 hasta la 13


def datos_country(pais):
    valores = list(pais.values())
#  key = list(pais.keys())
    llaves = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
    population = valores[5:13]
    poblacion = [int(x) for x in population]
    return llaves, poblacion
