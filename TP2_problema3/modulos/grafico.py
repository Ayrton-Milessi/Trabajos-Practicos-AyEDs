from TP2_problema3.Modulos.grafo import Grafo
import matplotlib.pyplot as plt
import networkx as nx

def graficar(grafo, confirmacion):
    if confirmacion.lower() == "si":
        G = nx.Graph()

        # Lee nodos y aristas desde el archivo
        with open("rutas.txt", "r") as arch:
            archivo = arch.readlines()
            for x in archivo:
                dato = x.strip().split(",")
                ciudad_inicio, ciudad_destino = dato[0], dato[1]
                capacidad_maxima = int(dato[2])
                precio = int(dato[3])
                G.add_edge(ciudad_inicio, ciudad_destino)
                G[ciudad_inicio][ciudad_destino]['capacidad'] = capacidad_maxima
                G[ciudad_inicio][ciudad_destino]['precio'] = precio


        pos = nx.spring_layout(G, k=0.5)

        node_size = 100
        nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color="lightblue")
        nx.draw_networkx_edges(G, pos, arrows=True, edge_color="black", width=1.0)

        labels = {nodo: nodo for nodo in G.nodes()}
        font_size = 7
        nx.draw_networkx_labels(G, pos, labels, font_size=font_size, verticalalignment="bottom")

        edge_labels = {(nodo_inicio, nodo_fin): (atributos["capacidad"], atributos["precio"]) for nodo_inicio, nodo_fin, atributos in G.edges(data=True)}
        edge_font_size = 5
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=edge_font_size, label_pos=0.3)

        plt.axis('off')
        plt.show()
    else:
        pass