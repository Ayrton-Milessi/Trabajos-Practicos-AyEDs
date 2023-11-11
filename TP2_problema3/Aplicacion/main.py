from TP2_problema3.modulos.grafo import Grafo
from TP2_problema3.modulos.grafico import graficar

path= "rutas.txt"

grafo= Grafo()
with open(path, "r") as arch:
    archivo = arch.readlines()
    for x in archivo:
        dato = x.strip().split(",")
        ciudad_inicio, ciudad_destino = dato[0], dato[1]
        capacidad_maxima = int(dato[2])
        precio = int(dato[3])
        
        grafo.agregarVertice(ciudad_inicio)
        grafo.agregarVertice(ciudad_destino)
        grafo.agregarArista(ciudad_inicio, ciudad_destino, capacidad_maxima, precio)

conf=input("Ingrese 'si' para graficar el grafo. De lo contrario, ingrese 'no' ---> ").lower()
while conf != "si" and conf != "no":
    print("Ingreso una confirmacion incorrecta")
    conf=input("Por favor ingrese 'si' o 'no' ---> ").lower()
resultado= graficar(path, conf)

inicio= "CiudadBs.As."
show_all= input("Si desea ver todos los recorridos ingrese si: ").lower()
if show_all == "si":
    print("Todos los recorridos son:")
    for clave, valor in grafo.listaVertices.items():
        print("----------------------------------------")
        grafo.dijkstra(grafo, inicio, clave)

else:
    destino= input("Ingrese una ciudad como destino: ")

    while destino not in grafo.listaVertices:
        print("Ingreso una ciudad que no es parte de los posibles caminos")
        print("Las ciudades posibles son: ")
        for clave, valor in grafo.listaVertices.items():
            print(f"{clave}")
        print("\n")
        destino= input("Ingrese una ciudad como destino: ")

    grafo.dijkstra(grafo, inicio, destino)