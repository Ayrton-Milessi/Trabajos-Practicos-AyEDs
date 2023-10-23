from TP2_problema3.Modulos.Monticulo_1 import MonticuloBinario_Tupla_Minimo
from TP2_problema3.Modulos.Monticulo_2 import MonticuloBinario_Tupla_Maximo

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
            self.listaVertices[clave] = nuevoVertice #agregamos el vertice al diccionario.
            return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n] # Devuelve el vertice con la clave n si existe.
        else:
            return None

    def obtenerVertices(self):
        return self.listaVertices.keys() #Devuelve las claves de todos los vertices en el grafo.

    def agregarArista(self, de, a, capacidad=0, precio=0):
        #La seccion de los if comprueba si existe el vertice "A" y "B" en el diccionario, si no existen los agregamos la arista con su peso y costo.
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], capacidad, precio)

    def dijkstraCapacidad(self, unGrafo, inicio, destino):
        cp = MonticuloBinario_Tupla_Maximo() #monticulo de maximo
        ruta= [] #lista para guardar los caminos posibles
        if inicio in self.listaVertices:
            inicio= self.obtenerVertice(inicio) #elegimos la ciudad de origen
            inicio.asignarDistancia(float('inf')) #la distancia es infinito
            cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
            while not cp.estaVacia(): #mientras qu el monticulo no este vacio
                verticeActual= cp.eliminarMax() #obtenemos la maxima distancia
                for verticeSiguiente in verticeActual[1].obtenerConexiones(): #recorremos todas las conexiones del vertice
                    nuevaDistancia= min(verticeActual[1].obtenerDistancia(), verticeActual[1].obtenerCapacidad(verticeSiguiente))
                    if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia(nuevaDistancia)
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente, nuevaDistancia)
                        if verticeSiguiente.obtenerId() == destino:
                            nuevoGrafo= Grafo() # Creamos un nuevo grafo para almacenar el camino
                            destino= self.obtenerVertice(destino)
                            while destino.obtenerPredecesor() is not None:
                                predecesor = destino.obtenerPredecesor()
                                ponderacion_capacidad = predecesor.obtenerCapacidad(destino)
                                ponderacion_precio = predecesor.obtenerPrecio(destino)
                                nuevoGrafo.agregarArista(predecesor.obtenerId(), destino.obtenerId(), ponderacion_capacidad, ponderacion_precio)
                                destino = predecesor
                            ruta.append(nuevoGrafo)# Agregamos el camino al resultado
        return ruta  # Devolvemos la lista de caminos posibles
    
    def dijkstraPrecio(self, unGrafo, inicio):
        for v in self.listaVertices.values():
             v.asignarDistancia(float('inf'))
        cp= MonticuloBinario_Tupla_Minimo() #monticulo de minimo
        if inicio in self.listaVertices:
            inicio= self.obtenerVertice(inicio)
            inicio.asignarDistancia(0)
            cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])  # Construimos el montículo con los vértices del grafo
            while not cp.estaVacia():
                verticeActual= cp.eliminarMin() # Obtenemos el vértice con la mínima distancia
                for verticeSiguiente in verticeActual[1].obtenerConexiones():
                    nuevaDistancia= verticeActual[1].obtenerDistancia() + verticeActual[1].obtenerPrecio(verticeSiguiente)
                    if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia( nuevaDistancia ) # Actualizamos la distancia del vértice siguiente
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente,nuevaDistancia)

    def caminoCorto(self, unGrafo, inicio, destino):
        if inicio in unGrafo.listaVertices and destino in unGrafo.listaVertices:
            grafo_peso= self.dijkstraCapacidad(unGrafo, inicio, destino) # Calculamos los caminos por capacidad
            camino= []
        else:
            raise RuntimeError("Verifique la ciudad de inicio o de destino") # Lanzamos una excepción si los vértices no existen
        if grafo_peso:
            for grafo in grafo_peso:
                grafo.dijkstraPrecio(grafo, inicio)
                ponderacion_precio= grafo.obtenerVertice(destino).obtenerDistancia()
                camino.append([grafo, ponderacion_precio])
            grafo_dist = min(camino, key=lambda x: x[1])  # Seleccionamos el camino con la menor distancia de precio
            ponderacion_precio = grafo_dist[1]  # Obtenemos la ponderación de precio
            ponderacion_capacidad = self.listaVertices[destino].obtenerDistancia()  # Obtenemos la ponderación de capacidad
            caminos= []
            actual= self.obtenerVertice(destino)
            while actual is not None:
                caminos.insert(0, actual)
                actual= actual.obtenerPredecesor()
            return caminos, ponderacion_capacidad, ponderacion_precio # Devolvemos el camino más corto por precio y capacidad
        else:
            raise RuntimeError("No existe camino a ese destino") # Lanzamos una excepción si no hay camino a ese destino
    
    def __iter__(self):
        return iter(self.listaVertices.values())

    def __contains__(self, n):
        return n in self.listaVertices

    def __str__(self):
        resultado = ""
        for valor in self.listaVertices.values():
            resultado += f" {str(valor.id) } --> conectado a ---> { str([x for x in valor.conectadoA.keys()])}\n"
        return resultado