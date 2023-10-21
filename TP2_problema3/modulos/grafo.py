from TP2_problema3.modulos.Monticulo_1 import MonticuloBinario_Tupla_Minimo
from TP2_problema3.modulos.Monticulo_2 import MonticuloBinarioMaximo


class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.dist= float("inf")
        self.predecesor= None

    def agregarVecino(self,vecino, peso, costo):
        self.conectadoA[vecino] = (peso, costo)

    def obtenerConexiones(self):
        return self.conectadoA.keys()
    
    def obtenerId(self):
        return self.id
    
    def obtenerPonderacion(self,vecino):
        peso, costo= self.conectadoA[vecino]
        return peso, costo
    
    def asignarDistancia(self, distancia):
        self.dist= distancia
    
    def obtenerDistancia(self):
        return self.dist
    
    def asignarPredecesor(self, predecesor):
        self.predecesor= predecesor
    
    def obtenerPredecesor(self):
        return self.predecesor
    
    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])
    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices += 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def agregarArista(self, de , a, peso, costo=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], peso, costo)

    


    def dijkstra_precio(self, unGrafo, inicio_usuario, destino_usuario):
        inicio= unGrafo.obtenerVertice(inicio_usuario) #elegimos la ciudad de origen
        destino= unGrafo.obtenerVertice(destino_usuario)
        cp = MonticuloBinario_Tupla_Minimo()  # montículo de máximo
        inicio.asignarDistancia(0)
        cp.construirMonticulo([(v.obtenerDistancia(), v) for v in unGrafo])

        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()

            if verticeActual[1] == destino: #Si el vertice actual es el que buscamos, cortamos aca
                return destino.obtenerDistancia(), self.obtenerCamino(destino)

            for verticeSiguiente in verticeActual[1].obtenerConexiones():
                costo_arista= verticeActual[1].obtenerPonderacion(verticeSiguiente)[1]  #aca obtenemos el costo
                nuevaDistancia = verticeActual[1].obtenerDistancia() + costo_arista
                if nuevaDistancia < verticeSiguiente.obtenerDistancia():  #relajación
                    verticeSiguiente.asignarDistancia(nuevaDistancia)
                    verticeSiguiente.asignarPredecesor((verticeActual[1], costo_arista))  # Almacenamos el predecesor y el costo de la arista desde ese predecesor
                    cp.decrementarClave(verticeSiguiente, nuevaDistancia)

    def obtenerCamino(self, vertice):
        camino = []
        actual = vertice
        while actual is not None:
            camino.append(actual.id)
            if actual.predecesor is not None:  # Si el vértice tiene un predecesor...
                camino.append(actual.predecesor[1])  # ...agregamos el costo de la arista desde ese predecesor
            actual = actual.predecesor[0] if actual.predecesor is not None else None  # Actualizamos 'actual' al predecesor
        camino = camino[::-1]  # Invertimos la lista para que el camino vaya desde el inicio hasta el destino
        return camino

    
    def dijkstra_peso(self, unGrafo, inicio_usuario, destino_usuario):
        pass

    def obtener_max_cuello_botella(self, unGrafo, origen, destino):
        pass

    def obtener_precio_minimo(self, unGrafo, origen, destino):
        return self.dijkstra_precio(unGrafo, origen, destino)

    def __iter__(self):
        return iter(self.listaVertices.values())

    def __contains__(self,n):
        return n in self.listaVertices
    
    def __str__(self):
        resultado= ""
        for vertice in self.listaVertices.values():
            resultado += f"{vertice.obtenerId()} --("
            for vecino in vertice.obtenerConexiones():
                costo= vertice.obtenerPonderacion(vecino)
                resultado += f"{costo}, {vecino.obtenerId()})"
                resultado += "\n"
        return resultado