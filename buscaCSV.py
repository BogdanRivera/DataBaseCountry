import importa


def findCountry(pais, data):
    for country in data:
        if pais in data:
            return country
    else:
        return None
