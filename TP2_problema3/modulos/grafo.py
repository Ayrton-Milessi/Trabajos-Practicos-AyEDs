from TP2_problema3.Modulos.Monticulo_2 import MonticuloBinario2

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.dist= float("inf")

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]


class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    def dijkstra(unGrafo,inicio):
        cp = MonticuloBinario2()
        inicio.asignarDistancia(0)
        cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()
            for verticeSiguiente in verticeActual.obtenerConexiones():
                nuevaDistancia = verticeActual.obtenerDistancia() \
                        + verticeActual.obtenerPonderacion(verticeSiguiente)
                if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarDistancia( nuevaDistancia )
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    cp.decrementarClave(verticeSiguiente,nuevaDistancia)

    def __iter__(self):
        return iter(self.listaVertices.values())