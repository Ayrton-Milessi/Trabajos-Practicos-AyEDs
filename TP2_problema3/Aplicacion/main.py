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