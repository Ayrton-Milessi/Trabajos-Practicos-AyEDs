from collections import defaultdict
import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregarArista(self, origen, destino, capacidad_maxima, precio):
        self.vertices[origen][destino] = (capacidad_maxima, precio)

def maximo_cuello_botella(grafo, ciudad_inicio, ciudad_destino):
    visitados = set()
    capacidad_minima = {}
    precio_minimo = {}
    anterior = {}
    
    capacidad_minima[ciudad_inicio] = float('inf')
    precio_minimo[ciudad_inicio] = 0
    
    cola_ciudades = [(-capacidad_minima[ciudad_inicio], ciudad_inicio)]
    
    while cola_ciudades:
        capacidad, ciudad = heapq.heappop(cola_ciudades)
        capacidad = -capacidad
        
        if ciudad in visitados:
            continue
        
        visitados.add(ciudad)
        
        for vecino, (capacidad_vecino, precio) in grafo.vertices[ciudad].items():
            cuello_botella = min(capacidad, capacidad_vecino)
            precio_vecino = precio + precio_minimo[ciudad]  # Corrección para obtener el precio acumulado
            precio = precio_vecino
            
            if vecino not in visitados and cuello_botella > capacidad_minima.get(vecino, 0):
                capacidad_minima[vecino] = cuello_botella
                precio_minimo[vecino] = precio
                anterior[vecino] = ciudad
                heapq.heappush(cola_ciudades, (-cuello_botella, vecino))
    
    if ciudad_destino not in capacidad_minima:
        print(f"No hay ruta directa desde {ciudad_inicio} a {ciudad_destino}.")
    else:
        print(f"Ruta desde {ciudad_inicio} a {ciudad_destino}:")
        ciudad_actual = ciudad_destino
        camino = []
        while ciudad_actual:
            camino.append(ciudad_actual)
            ciudad_actual = anterior.get(ciudad_actual)
        camino.reverse()
        print(" -> ".join(camino))
        print(f'Se permite llevar hasta {capacidad_minima[ciudad_destino]}Kg en el camino')
        print(f'El precio es de ${int(precio_minimo[ciudad_destino])*1000}')

grafo = Grafo()

# Leer las rutas desde el archivo y agregarlas al grafo
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

# Permite al usuario elegir un destino
destino = "Frias"

# Calcular el peso máximo y precio mínimo para transportar mobiliario
maximo_cuello_botella(grafo, 'CiudadBs.As.', destino)
