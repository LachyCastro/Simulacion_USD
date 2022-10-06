from random import choices, randint, random
import numpy as np
import statistics as stat
import random

lecturas = open("lecturas.txt", "r").readlines() #Lecturas dia despues del anuncio de compra gobierno usd
lecturas = [int(x) for x in lecturas ]


def media(x):
    return stat.mean(x)

def moda(x):
    return stat.mode(x)


def simular(func, lecturas, cantidad_dias):  
    for i in range(cantidad_dias):
        precio_actual = func(lecturas) # Media o moda de las lecturas para saber el precio del dia
        precio_especulativo = [precio_actual + randint(2,5) for i in range(200)] # Se toman en cuenta las personas que sobrespeculan dado un precio actual
        precio_conservador = [precio_actual - randint(2,5) for i in range(100)] # Quieren vender rapido
        print("Precio pasado", i, "dias es de", precio_actual, "cup")
        precios_guia = [random.gauss(precio_actual,1) for i in range(700)] # gente que se guia por el precio de el dia
        lecturas = precio_conservador + precio_especulativo + precios_guia
        

simular(media, lecturas, 50)
simular(moda, lecturas, 50) # La moda acelera mucho el precio la idea era usar el valor de la moda en la distribucion de gauss simulando
                            # asi las personas que se guian por el precio publicado

