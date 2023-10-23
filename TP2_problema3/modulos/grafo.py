from TP2_problema3.Modulos.Monticulo_1 import MonticuloBinario_Tupla_Minimo
from TP2_problema3.Modulos.Monticulo_2 import MonticuloBinario_Tupla_Maximo

class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = 0
        self.predecesor = None

    def agregarVecino(self, vecino, capacidad=0, precio=0):
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
            nuevoVertice = Vertice(clave)
            self.listaVertices[clave] = nuevoVertice
            return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def agregarArista(self, de, a, capacidad=0, precio=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], capacidad, precio)

    def dijkstraCapacidad(self, unGrafo, inicio, destino):
        cp = MonticuloBinario_Tupla_Maximo()
        ruta= []
        if inicio in self.listaVertices:
            inicio= self.obtenerVertice(inicio)
            inicio.asignarDistancia(float('inf'))
            cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])
            while not cp.estaVacia():
                verticeActual= cp.eliminarMax()
                for verticeSiguiente in verticeActual[1].obtenerConexiones():
                    nuevaDistancia= min(verticeActual[1].obtenerDistancia(), verticeActual[1].obtenerCapacidad(verticeSiguiente))
                    if nuevaDistancia > verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia(nuevaDistancia)
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente, nuevaDistancia)
                        if verticeSiguiente.obtenerId() == destino:
                            nuevoGrafo= Grafo()
                            destino= self.obtenerVertice(destino)
                            while destino.obtenerPredecesor() is not None:
                                predecesor = destino.obtenerPredecesor()
                                ponderacion_capacidad = predecesor.obtenerCapacidad(destino)
                                ponderacion_precio = predecesor.obtenerPrecio(destino)
                                nuevoGrafo.agregarArista(predecesor.obtenerId(), destino.obtenerId(), ponderacion_capacidad, ponderacion_precio)
                                destino = predecesor
                            ruta.append(nuevoGrafo)
        return ruta
    
    def dijkstraPrecio(self, unGrafo, inicio):
        for v in self.listaVertices.values():
             v.asignarDistancia(float('inf'))
        cp= MonticuloBinario_Tupla_Minimo()
        if inicio in self.listaVertices:
            inicio= self.obtenerVertice(inicio)
            inicio.asignarDistancia(0)
            cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
            while not cp.estaVacia():
                verticeActual= cp.eliminarMin()
                for verticeSiguiente in verticeActual[1].obtenerConexiones():
                    nuevaDistancia= verticeActual[1].obtenerDistancia() + verticeActual[1].obtenerPrecio(verticeSiguiente)
                    if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                        verticeSiguiente.asignarDistancia( nuevaDistancia )
                        verticeSiguiente.asignarPredecesor(verticeActual[1])
                        cp.decrementarClave(verticeSiguiente,nuevaDistancia)

    def caminoCorto(self, unGrafo, inicio, destino):
        if inicio in unGrafo.listaVertices and destino in unGrafo.listaVertices:
            grafo_peso= self.dijkstraCapacidad(unGrafo, inicio, destino)
            camino= []
        else:
            raise RuntimeError("Verifique la ciudad de inicio o de destino")
        if grafo_peso:
            for grafo in grafo_peso:
                grafo.dijkstraPrecio(grafo, inicio)
                ponderacion_precio= grafo.obtenerVertice(destino).obtenerDistancia()
                camino.append([grafo, ponderacion_precio])
            grafo_dist= min(camino, key=lambda x: x[1])
            ponderacion_precio= grafo_dist[1]
            ponderacion_capacidad= self.listaVertices[destino].obtenerDistancia()
            caminos= []
            actual= self.obtenerVertice(destino)
            while actual is not None:
                caminos.insert(0, actual)
                actual= actual.obtenerPredecesor()
            return caminos, ponderacion_capacidad, ponderacion_precio
        else:
            raise RuntimeError("No existe camino a ese destino")
    
    def __iter__(self):
        return iter(self.listaVertices.values())

    def __contains__(self, n):
        return n in self.listaVertices

    def __str__(self):
        resultado = ""
        for valor in self.listaVertices.values():
            resultado += f" {str(valor.id) } --> conectado a ---> { str([x for x in valor.conectadoA.keys()])}\n"
        return resultado