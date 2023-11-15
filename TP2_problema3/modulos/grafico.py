import matplotlib.pyplot as plt
import networkx as nx

def graficar(path, confirmacion):
    """Esta funcion toma la direcion de un archivo y realiza un grafo dirigido"""
    if confirmacion == "si":
        G = nx.DiGraph()

        # Lee nodos y aristas desde el archivo
        with open(path, "r") as arch:
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

        nx.draw_networkx_nodes(G, pos, node_size=100, node_color="lightblue")
        nx.draw_networkx_edges(G, pos, arrows=True, edge_color="black", width=1.0)

        labels = {nodo: nodo for nodo in G.nodes()}
        font_size = 7
        nx.draw_networkx_labels(G, pos, labels, font_size=font_size, verticalalignment="bottom")

        edge_labels = {}
        for nodo_inicio, nodo_fin, atributos in G.edges(data=True):
            capacidad, precio = atributos["capacidad"], atributos["precio"]
            edge_labels[(nodo_inicio, nodo_fin)] = (capacidad, precio)

        edge_font_size = 5
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=edge_font_size, label_pos=0.3)

        plt.axis('off')
        plt.show()
    else:
        pass