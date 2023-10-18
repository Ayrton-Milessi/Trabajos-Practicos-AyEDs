from TP2_problema3.modulos.grafo import Grafo
#import matplotlib.pyplot as plt # Lo usamos para poder poner la ponderacion en el grafico
#import networkx as nx #Funcion para graficar Grafos.

grafo= Grafo()
grafo_costo= Grafo()

with open("rutas.txt", "r") as arch:
    archivo= arch.readlines()
    for x in archivo:
        dato= x.strip().split(",")
        nombre1,nombre2= dato[0], dato[1]
        peso_max= int(dato[2])
        costo= int(dato[3])

        # Grafo
        if nombre1 not in grafo:
            grafo.agregarVertice(nombre1) # Los vertices van a ser los nombres de "inicio" de las ciudades
            grafo.agregarArista(nombre1, nombre2, peso_max)
        else:
            grafo.agregarArista(nombre1, nombre2, peso_max) # Si la ciudad de origen ya existe en el grafo, agregamos una nueva arista con el peso máximo


inicio=grafo.obtenerVertice("Rosario")


grafo.dijkstra(grafo, inicio)

miGrafo= grafo

for vertice in miGrafo.obtenerVertices():
    v = miGrafo.obtenerVertice(vertice)
    print(f"Vertice: {v.obtenerId()}")
    print(f"Distancia desde el inicio: {v.obtenerDistancia()}")
    predecesor = v.obtenerPredecesor()



