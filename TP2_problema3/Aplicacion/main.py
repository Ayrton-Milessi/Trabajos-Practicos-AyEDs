from TP2_problema3.modulos.grafo import Grafo
#import matplotlib.pyplot as plt # Lo usamos para poder poner la ponderacion en el grafico
#import networkx as nx #Funcion para graficar Grafos.

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
            grafo.agregarArista(nombre1, nombre2, peso_max, costo)
        if nombre2 not in grafo:
            grafo.agregarVertice(nombre2)
            grafo.agregarArista(nombre1,nombre2, peso_max, costo)
        else:
            grafo.agregarArista(nombre1,nombre2, peso_max, costo)


#Este fragemento sirve para imprimir el grafo en consola
for vertice in grafo.obtenerVertices():
    print(f"Vertice: {vertice}")
    for vecino in grafo.listaVertices[vertice].obtenerConexiones():
        capacidad, costo = grafo.listaVertices[vertice].obtenerPonderacion(vecino)
        print(f"Camino hacia {vecino.obtenerId()} - Peso máximo: {capacidad} - Precio: {costo}")
    print("\n")


inicio= "Rosario" #elegimos la ciudad de origen
destino= "Rufino" #elegimos la ciudad de destino final


precio= grafo.obtener_precio_minimo(grafo ,inicio ,destino)

print(f"El precio mas bajo para viajar desde {inicio} a {destino} es de ${int(precio[0])*1000}")
print("El camino que tomo es:", precio[1])
print()
print("Hola Mundo") #imprime un hola mundo
