
"""
Variables globales
"""

ARCHIVO_CENSOS = "./properties.csv"

ARCHIVO_VOTOS = "./minutes.csv"

votos = []

censos = []

"""
Carga archivos csv a las variables globales "votos" y "censos"
como listas de listas
"""
def cargar_csv():

    import csv

    global censos
    global votos
    
    with open(ARCHIVO_CENSOS,'r') as csv_censos:
        csv_reader1 = csv.reader(csv_censos)

        for i in csv_reader1:
            censos += [i]

    with open(ARCHIVO_VOTOS,'r') as csv_votos:
        csv_reader2 = csv.reader(csv_votos)

        for j in csv_reader2:
            votos += [j]

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
    
    x = random.uniform(0,1)
    prob_acumulada = 0.0

    for item, prob_item in zip(lista, probabilidad):
        prob_acumulada += prob_item
        if x < prob_acumulada: break
    return item


cargar_csv()


