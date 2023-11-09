import heapq as MonticuloMinimo

class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = 0
        self.predecesor = None

    def agregarVecino(self, vecino, capacidad=0, precio=0): # Agrega un vertice vecino con su respectivo peso y costo.
        self.conectadoA[vecino] = (capacidad, precio)

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerCapacidad(self,vecino):
        return self.conectadoA[vecino][0]
    
    def obtenerPrecio(self, vecino):
        return self.conectadoA[vecino][1]

    def asignarDistancia(self, distancia):
        self.distancia = distancia

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, predecesor):
        self.predecesor = predecesor

    def obtenerPredecesor(self):
        return self.predecesor

    def __str__(self):
        return str(self.id)
    
    def recorrer(x):
        while (x.obtenerPredecesor()):
            print(x.obtenerId())
            x = x.obtenerPredecesor()
        print(x.obtenerId())

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave): 
        if clave not in self.listaVertices:
            self.numVertices += 1
            nuevoVertice = Vertice(clave) # Crea un nuevo objeto de vertice con la clave dada
            self.listaVertices[clave] = {} #agregamos el vertice al diccionario.

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n] # Devuelve el vertice con la clave n si existe.
        else:
            return None

    def obtenerVertices(self):
        return self.listaVertices.keys() #Devuelve las claves de todos los vertices en el grafo.

    def agregarArista(self, desde, a, capacidad, precio):
        self.listaVertices[desde][a]= (capacidad, precio)

    def dijkstra(self, grafo, ciudad_inicio, ciudad_destino):
        visitados = set()
        capacidad_minima = {}
        precio_minimo = {}
        anterior = {}
        
        capacidad_minima[ciudad_inicio] = float('inf')
        precio_minimo[ciudad_inicio] = 0
        
        cola_ciudades = [(-capacidad_minima[ciudad_inicio], ciudad_inicio)]
        
        while cola_ciudades:
            capacidad, ciudad = MonticuloMinimo.heappop(cola_ciudades)
            capacidad = -capacidad
            
            if ciudad in visitados:
                continue
            
            visitados.add(ciudad)
            
            for vecino, (capacidad_vecino, precio) in grafo.listaVertices[ciudad].items():
                cuello_botella = min(capacidad, capacidad_vecino)
                precio_vecino = precio + precio_minimo[ciudad]  # Corrección para obtener el precio acumulado
                precio = precio_vecino
                
                if vecino not in visitados and cuello_botella > capacidad_minima.get(vecino, 0):
                    capacidad_minima[vecino] = cuello_botella
                    precio_minimo[vecino] = precio
                    anterior[vecino] = ciudad
                    MonticuloMinimo.heappush(cola_ciudades, (-cuello_botella, vecino))
        
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
            if capacidad_minima[ciudad_destino] == float("inf"):
                capacidad_minima[ciudad_destino] = 0
            print(f'Se permite llevar hasta {capacidad_minima[ciudad_destino]}Kg en el camino')
            print(f'El precio es de ${int(precio_minimo[ciudad_destino])*1000}')
    
    def __iter__(self):
        return iter(self.listaVertices.values())

    def __contains__(self, n):
        return n in self.listaVertices

    def __str__(self):
        resultado = ""
        for valor in self.listaVertices.values():
            resultado += f" {str(valor.id) } --> conectado a ---> { str([x for x in valor.conectadoA.keys()])}\n"
        return resultado