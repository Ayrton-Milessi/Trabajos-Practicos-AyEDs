from TP2_problema3.Modulos.grafo import Grafo
import matplotlib.pyplot as plt # Lo usamos para poder poner la ponderacion en el grafico
import networkx as nx #Funcion para graficar Grafos.

grafo= Grafo()
grafo_costo= Grafo()

visual= nx.DiGraph()

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
            visual.add_node(nombre1) #parte visual
            grafo.agregarArista(nombre1, nombre2, peso_max)
            visual.add_edge(nombre1, nombre2, weight=peso_max)#parte visual
        else:
            grafo.agregarArista(nombre1, nombre2, peso_max) # Si la ciudad de origen ya existe en el grafo, agregamos una nueva arista con el peso máximo
            visual.add_edge(nombre1, nombre2, weight=peso_max)#parte visual
        

posicion = nx.circular_layout(visual) #elegimos una disposicion para los nodos

etiquetas = nx.get_edge_attributes(visual, 'weight') #obtiene las ettiquetas de peso
nx.draw_networkx_edges(visual, posicion)
nx.draw_networkx_edge_labels(visual, posicion, edge_labels=etiquetas) #dibuja las etiquetas de las aristas

nx.draw_networkx_nodes(visual, posicion) #dibuja los nodos

node_labels = {node: node for node in visual.nodes()} #generamos un diccionario de etiquetas para los nodos del grafo
nx.draw_networkx_labels(visual, posicion, labels=node_labels) #dibuja las etiquetas de los nodos

plt.axis('off')  # Para que no sea vea encuadrado
plt.show()


#-------------------------------------------------------------------------
#                           grafo para visualizar
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