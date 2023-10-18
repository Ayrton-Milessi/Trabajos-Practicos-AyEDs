from TP2_problema3.Modulos.Monticulo_2 import MonticuloBinario2

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.dist= float("inf")
        self.predecesor= None

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
        cp = MonticuloBinario2()
        inicio.asignarDistancia(0)
        cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()
            for verticeSiguiente in verticeActual.obtenerConexiones():
                nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
                if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarDistancia( nuevaDistancia )
                    verticeSiguiente.asignarPredecesor(verticeActual)
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
        return [camino, distanciaCamino]

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __contains__(self,n):
        return n in self.listaVertices
    
    def __str__(self):
        pass #nose como hacer el str xd
#----------------------(deberia quedar asi)----------------------------------
"""
CiudadBs.As. --(100, 4)--> Rufino
Rufino --(90, 3)--> Laboulage
Laboulage --(100, 8)--> VillaMercedes
VillaMercedes --(80, 4)--> SanLuisCap
SanLuisCap --(100, 10)--> Mendoza

CiudadBs.As. --(90, 7)--> Rosario
Rosario --(80, 9)--> MarcosJuarez
MarcosJuarez --(80, 5)--> VillaMaria
VillaMaria --(50, 4)--> CiudadCordoba
CiudadCordoba --(80, 4)--> S.delEstero
S.delEstero --(90, 7)--> SanMiguelTucuman

Rosario --(70, 9)--> Rafaela
Rafaela --(90, 8)--> S.delEstero
S.delEstero --(100, 3)--> SanMiguelTucuman
SanMiguelTucuman --(90, 6)--> Salta
Salta --(90, 9)--> SanSalvadorJujuy

VillaMercedes --(50, 3)--> MinaClavero
MinaClavero --(50, 8)--> Frias
Frias --(50, 6)--> Simoca
Simoca --(50, 8)--> BellaVista
BellaVista --(70, 5)--> SanMiguelTucuman
Mendoza --(50, 3)--> VillaStaRosa
VillaStaRosa --(60, 7)--> LaRioja
LaRioja --(100, 6)--> S.F.ValleCatamarca
S.F.ValleCatamarca --(90, 7)--> SanMiguelTucuman

S.delEstero --(90, 3)--> RosarioFrontera
RosarioFrontera --(70, 7)--> Gral.Guemes
Gral.Guemes --(100, 6)--> SanSalvadorJujuy
Laboulage --(80, 5)--> RioCuarto
RioCuarto --(60, 7)--> SanLuisCap
Laboulage --(90, 3)--> RioCuarto
Rosario --(80, 10)--> CiudadBs.As.
Rosario --(50, 3)--> CiudadCordoba
CiudadCordoba --(70, 6)--> Rosario
CiudadBs.As. --(50, 10)--> CiudadCordoba
CiudadCordoba --(100, 5)--> CiudadBs.As.
VillaMercedes --(70, 8)--> LaRioja 
"""