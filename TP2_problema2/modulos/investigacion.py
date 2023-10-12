from TP2_problema2.modulos.avl import AVL
import datatime

class Temperaturas_DB:
    def __init__(self):
        self.arbol= AVL()

    def guardar_temperatura(self, temperatura, fecha):
        self.arbol.agregar(temperatura, fecha)

    def devolver_temperatura(self, fecha):
        self.arbol.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        pass

    def min_temp_rango(self, fecha1, fecha2):
        pass

    def temp_extremos_rango(self, fecha1, fecha2):
        pass

    def borrar_temperatura(self, fecha):
        self.arbol.eliminar(fecha)

    def devolver_temperaturas(self, fecha1, fecha2):
        pass

    def cantidad_muestras(self):
        return len(self.arbol)