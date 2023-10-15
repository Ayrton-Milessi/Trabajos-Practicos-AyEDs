from TP2_problema3.modulos.Grafo import Grafo
# class ColaPrioridad:
#     def __init__(self):
#         pass

aux= Grafo()

with open("rutas.txt", "r") as arch:
    archivo= arch.readlines()
    
    for x in archivo:
        dato= x.strip().split(",")
        nombre1,nombre2= dato[0], dato[1]
        peso_max= dato[2]
        costo= dato[3]


print(costo)



