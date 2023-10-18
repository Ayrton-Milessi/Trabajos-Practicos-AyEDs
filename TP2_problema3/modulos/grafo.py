from TP2_problema3.modulos.Monticulo_2 import MonticuloBinario2
from TP2_problema3.modulos.cola import Cola

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.dist= float("inf")
        self.predecesor= None
        self.color= "white"

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

    def asignarDistancia(self, distancia):
        self.dist= distancia
    
    def obtenerDistancia(self):
        return self.dist
    
    def asignarPredecesor(self, predecesor):
        self.predecesor= predecesor
    
    def obtenerPredecesor(self):
        return self.predecesor
    
    def asignarColor(self, color):
        self.color= color
    
    def obtenerColor(self):
        return self.color
    
    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

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

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    def dijkstra(self,unGrafo,inicio):
        cp = MonticuloBinario2() #monticulo de maximo
        inicio.asignarDistancia(0)
        cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()
            for verticeSiguiente in verticeActual[1].obtenerConexiones():
                nuevaDistancia = verticeActual[1].obtenerDistancia() + verticeActual[1].obtenerPonderacion(verticeSiguiente)
                if nuevaDistancia < verticeSiguiente.obtenerDistancia(): #relajación
                    verticeSiguiente.asignarDistancia(nuevaDistancia)
                    verticeSiguiente.asignarPredecesor(verticeActual[1])
                    cp.decrementarClave(verticeSiguiente,nuevaDistancia)

    def caminoCorto(self, inicio, fin):
        self.dijkstra(self, self.obtenerVertice(inicio)) #usa dijkstra para buscar el vecino más cercano del vertice 'inicio'
        verticeActual= self.obtenerVertice(fin)
        camino=[]
        distanciaCamino= 0
        while verticeActual is not None:
            camino.insert(0, verticeActual.obtenerId()) #inserta el vertice 'inicio' y va agregando los vertices (camino) hasta llegar a 'fin'
            distanciaCamino += verticeActual.obtenerDistancia() #va sumando la distancia del camino
            verticeActual= verticeActual.obtenerPredecesor() #desde el vertice 'fin' vamos retrociendo buscando el camino más corto
        if distanciaCamino == 0:
            return None #no encontro ningun camino para el lugar de inicio hasta el destino
        return [camino, distanciaCamino]

    def cuelloBotella(self, inicio):
        inicio.asignarDistancia(0)
        inicio.asignarPredecesor(None)
        colaVertices = Cola()
        colaVertices.agregar(inicio)
        while (colaVertices.tamano() > 0):
            verticeActual = colaVertices.avanzar()
            for vecino in verticeActual.obtenerConexiones():
                    if (vecino.obtenerColor() == 'blanco'):
                        vecino.asignarColor('gris')
                        vecino.asignarDistancia(verticeActual.obtenerDistancia() + 1)
                        vecino.asignarPredecesor(verticeActual)
                        colaVertices.agregar(vecino)
            verticeActual.asignarColor('negro')
    
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
