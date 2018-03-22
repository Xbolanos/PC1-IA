
"""
Variables globales
"""

ARCHIVO_CENSOS = "./pruebas/properties.csv"

ARCHIVO_VOTOS = "./pruebas/minutes.csv"

votos = []

censos = []

datos = {
    "SAN JOSE": {
        "rango": [1, 20]
    },
    "ALAJUELA": {
        "rango": [21, 35]
    },
    "CARTAGO": {
        "rango": [36, 43]
    },
    "HEREDIA": {
        "rango": [44, 53]
    },
    "GUANACASTE": {
        "rango": [54, 64]
    },
    "PUNTARENAS": {
        "rango": [65, 75]
    },
    "LIMON": {
        "rango": [76, 81]
    }
}

"""
Carga archivos csv a las variables globales "votos" y "censos"
como listas de listas
"""


def cargar_csv():

    import csv

    global censos
    global votos

    with open(ARCHIVO_CENSOS, 'r') as csv_censos:
        csv_reader1 = csv.reader(csv_censos)

        for i in csv_reader1:
            censos += [i]

    with open(ARCHIVO_VOTOS, 'r') as csv_votos:
        csv_reader2 = csv.reader(csv_votos)

        for j in csv_reader2:
            votos += [j]

    cargar_datos()


'''
Guarda los datos de votaciones en un diccionario para un mejor acceso
a esta información
'''


def cargar_datos():
    for key in datos:
        primer_canton = datos[key]["rango"][0]
        ultimo_canton = datos[key]["rango"][1]+1
        votos_en_provincia = []

        for fila in votos:
            votos_en_provincia += [fila[primer_canton:ultimo_canton]]
        votos_en_provincia = votos_en_provincia[:17]

        datos[key]["votos"] = votos_en_provincia


"""
Calcula probabilidad de hombres por cada 100 mujeres en un cantón
Entrada: lista
Salida: float
"""


def calc_prob(canton):
    total = eval(canton[1])
    poblacion = eval(canton[5])

    return (poblacion/(poblacion+100))


"""
Retorna elemento aleatorio de una lista con una probabilidad dada
Entrada: lista con elementos a elegir de manera aleatorio
         lista con probabilidad de cada elemento
Salida: elemento aleatorio de la primera lista
"""


def random_pick(lista, probabilidad):
    import random

    x = random.uniform(0, 1)
    prob_acumulada = 0.0

    for item, prob_item in zip(lista, probabilidad):
        prob_acumulada += prob_item
        if x < prob_acumulada:
            break
    return item


'''
Retorna la cantidad de votos que hubo en cierta provincia
Entrada: string con el nombre de la provincia
Salida: total de votos en dicha provincia
'''


def votes_quantity_by_province(province):
    province_votes = datos[province]["votos"]
    total_votes = 0

    for column in range(len(province_votes[0])):
        total_votes += int(province_votes[16][column])

    return total_votes


'''
Retorna la cantidad de votos que hubo en todo el pais
'''


def votes_quatity_general():
    total_votes = 0

    for key in datos:
        total_votes += votes_quantity_by_province(key)

    return total_votes


'''
Retorna las probabilidades de que cierto votante pertenesca a cierto canton de
        cierta provincia
Entrada: cantidad de votos totales
         nombre de la provincia a evaluar
         lista donde se guardaran las probabilidades
         lista donde se guardaran los cantones
Salida: lista con probabilidades
        lista con cantones
'''


def probs_by_province(total_votes, province, probs, cantons):
    province_cantons = datos[province]["votos"]

    for column in range(len(province_cantons[0])):
        cantons += [province_cantons[0][column]]
        probs += [int(province_cantons[16][column])/total_votes]


'''
Retorna las probabilidades de que cierto votante pertenesca a cierto canton
        sobre todos las provincias
Entrada: cantidad de votos totales
         lista donde se guardaran las probabilidades
         lista donde se guardaran los cantones
Salida: lista con probabilidades
        lista con cantones
'''


def general_probs(total_votes, probs, cantons):
    for key in datos:
        probs_by_province(total_votes, key, probs, cantons)


'''
Retorna un canton elegido al azar segun su probabilidad de que exista un
        un votante de dicho canton
Entrada: El nombre de la provincia a la que pertenece, o por el contrario nada
Salida: Un canton elegido segun provincia o segun todas las provincias
'''


def pick_canton(province="NONE"):
    if province == "NONE":

        total_votes = votes_quatity_general()

        probs = []
        cantons = []

        general_probs(total_votes, probs, cantons)

        return random_pick(cantons, probs)

    else:
        total_votes = votes_quantity_by_province(province)

        probs = []
        cantons = []

        probs_by_province(total_votes, province, probs, cantons)

        return random_pick(cantons, probs)


'''
Retorna una lista con diferentes muestras de votantes generadas aleatoriamente
Entrada: cantidad de muestras a generar
Salida: lista con las muestras
'''


def generar_muestra_pais(n):
    cargar_csv()

    for muestra in range(0, n):
        pass


'''
Retorna una lista con diferentes muestras de votantes generadas aleatoriamente
        para cierta provincia
Entrada: cantidad de muestras a generar
         nombre de la provincia
Salida: lista con las muestras
'''


def generar_muestra_provincia(n, nombre_provincia):
    cargar_csv()


def main():
    cargar_csv()
    pick_canton()


if __name__ == '__main__':
    main()
