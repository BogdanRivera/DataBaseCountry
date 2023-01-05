import csv


def lee_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        datos = []
        for row in reader:
            dicc = {key: value for key, value in zip(header, reader)}
            datos.append(dicc)
    return datos
