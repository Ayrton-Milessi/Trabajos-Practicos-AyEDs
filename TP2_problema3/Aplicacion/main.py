from TP2_problema3.Modulos.grafo import Grafo
import matplotlib.pyplot as plt # Lo usamos para poder poner la ponderacion en el grafico
import networkx as nx #Funcion para graficar Grafos.

grafo= Grafo()
with open("rutas.txt", "r") as arch:
    archivo = arch.readlines()
    for x in archivo:
        dato = x.strip().split(",")
        ciudad_inicio, ciudad_destino = dato[0], dato[1]
        capacidad_maxima = int(dato[2])
        precio = int(dato[3])
        
        grafo.agregarVertice(ciudad_inicio)
        grafo.agregarVertice(ciudad_destino)
        grafo.agregarArista(ciudad_inicio, ciudad_destino, capacidad_maxima, precio)

#este fragemento sirve para imprimir el grafo en consola
for vertice in grafo.obtenerVertices():
    print(f"Vertice: {vertice}")
    for vecino in grafo.listaVertices[vertice].obtenerConexiones():
        capacidad, costo = grafo.listaVertices[vertice].obtenerCapacidad(vecino),grafo.listaVertices[vertice].obtenerPrecio(vecino)
        print(f"Camino hacia {vecino.obtenerId()} - Peso máximo: {capacidad} - Precio: {costo}")
    print("\n")

print('*'*100)
inicio = "CiudadBs.As."
destino = "S.delEstero"

grafo.maximo_cuello_botella(grafo, inicio, destino)