from TP2_problema3.modulos.grafo import Grafo
import matplotlib.pyplot as plt # Lo usamos para poder poner la ponderacion en el grafico
import networkx as nx #Funcion para graficar Grafos.

grafo= Grafo()
with open("rutas.txt", "r") as arch:
    archivo= arch.readlines()
    for x in archivo:
        dato= x.strip().split(",")
        nombre1,nombre2= dato[0], dato[1]
        peso_max= int(dato[2])
        costo= int(dato[3])
        # Grafo
        if nombre1 not in grafo:
            grafo.agregarVertice(nombre1)
        if nombre2 not in grafo:
            grafo.agregarVertice(nombre2)
        grafo.agregarArista(nombre1, nombre2, peso_max, costo)

# PARTE GRAFCA
G= nx.DiGraph() #crear un nuevo grafo de NetworkX
for vertice in grafo.obtenerVertices(): #copia los nodos y aristas del grafo a G
    G.add_node(vertice)
for vertice in grafo.obtenerVertices():
    for vecino in grafo.listaVertices[vertice].obtenerConexiones():
        capacidad, precio = grafo.listaVertices[vertice].obtenerCapacidad(vecino), grafo.listaVertices[vertice].obtenerPrecio(vecino)
        G.add_edge(vertice, vecino.obtenerId(), capacidad=capacidad, precio=precio)

pos = nx.spring_layout(G, k=0.5) #Usamos la distribucion de "primavera" para una mejor visualizacion

node_size = 100 #tamanio de vertices
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color="lightblue") #representar los vertices
nx.draw_networkx_edges(G, pos, arrows=True, edge_color="black", width=1.0) #representar las aristas

#etiquetar los vertices con sus id's
labels = {nodo: nodo for nodo in G.nodes()}
font_size = 7
nx.draw_networkx_labels(G, pos, labels, font_size=font_size, verticalalignment="bottom")

#etiquetar las aristas con los atributos (Capacidad y Precio)
edge_labels = {(nodo_inicio, nodo_fin): (atributos["capacidad"], atributos["precio"]) for nodo_inicio, nodo_fin, atributos in G.edges(data=True)}
edge_font_size = 5
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=edge_font_size, label_pos=0.3)

plt.axis('off') #oculta el recuadro
plt.show() #muestra el gráfico

#este fragemento sirve para imprimir el grafo en consola
for vertice in grafo.obtenerVertices():
    print(f"Vertice: {vertice}")
    for vecino in grafo.listaVertices[vertice].obtenerConexiones():
        capacidad, costo = grafo.listaVertices[vertice].obtenerCapacidad(vecino),grafo.listaVertices[vertice].obtenerPrecio(vecino)
        print(f"Camino hacia {vecino.obtenerId()} - Peso máximo: {capacidad} - Precio: {costo}")
    print("\n")

print('*'*100)
inicio = "CiudadBs.As."
destino = "S.delEstero"
caminos, distancia_peso, distancia_precio= grafo.caminoCorto(grafo, inicio, destino)

print(f"Ruta con mayor capacidad para transportar y menor costo para ir desde {inicio} hasta {destino} es:")
for i, v in enumerate (caminos):
    print(i+1,"-",v.obtenerId())
print(f"Se permite llevar hasta {distancia_peso}Kg en el camino")
print(f"El precio es de ${int(distancia_precio)*1000}")
