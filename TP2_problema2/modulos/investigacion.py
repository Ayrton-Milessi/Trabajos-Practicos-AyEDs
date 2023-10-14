from TP2_problema2.modulos.avl import AVL
from datetime import datetime

class TemperaturasDB:
    def __init__(self):
        self.avl= AVL()


    def guardar_temperatura(self, temp, fecha:str):
        objeto_fecha= datetime.strptime(fecha,"%d/%m/%Y") # especificamos que formato de fecha que queremos y lo convertimos en un objeto
        self.avl.agregar(objeto_fecha,temp)

    def devolver_temp(self, fecha):
        objeto_fecha= datetime.strptime(fecha, "%d/%m/%Y")
        temperatura= self.avl.obtener(objeto_fecha) # Buscamos la temperatura deseada
        return temperatura

    def max_temp_rango(self, fecha1,fecha2):
        max_temp= float("-inf")
        return self._max_temp_rango(self.avl.raiz, fecha1, fecha2, max_temp)
    
    def _max_temp_rango(self, nodo, fecha1, fecha2, max_temp):
        if nodo is None: # primero verificamos que el nodo exista para no realizar llamadas innecesarias
            return max_temp

        nodo_clave_str = nodo.clave.strftime("%d/%m/%Y")
        if fecha1 <= nodo_clave_str <= fecha2:
            max_temp = max(max_temp, nodo.cargaUtil)
        
        if fecha1 < nodo_clave_str:
            max_temp= self._max_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2, max_temp)

        if fecha2 > nodo_clave_str:
            max_temp= self._max_temp_rango(nodo.hijoDerecho, fecha1, fecha2, max_temp)
        
        return max_temp
    
    #Se realiza exactamente lo mismo pero buscando el minimo
    def min_temp_rango(self, fecha1, fecha2):
        min_temp= float("inf")
        return self._min_temp_rango(self.avl.raiz, fecha1, fecha2, min_temp)

    def _min_temp_rango(self, nodo, fecha1, fecha2, min_temp):
        if nodo is None: # primero verificamos que el nodo exista para no realizar llamadas innecesarias
            return min_temp
        nodo_clave_str = nodo.clave.strftime("%d/%m/%Y")
        if fecha1 <= nodo_clave_str <= fecha2:
            min_temp = min(min_temp, nodo.cargaUtil)
        
        if fecha1 < nodo_clave_str:
            min_temp= self._min_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2, min_temp)

        if fecha2 > nodo_clave_str:
            min_temp= self._min_temp_rango(nodo.hijoDerecho, fecha1, fecha2, min_temp)
        
        return min_temp

    def temp_extermos_rango(self, fecha1, fecha2):
        fecha1_objeto= datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_objeto= datetime.strptime(fecha2, "%d/%m/%Y")

        return self.min_temp(fecha1_objeto, fecha2_objeto), self.max_temp_rango(fecha1_objeto,fecha2_objeto)

    def borrar_temperatura(fecha):
        pass

    def devolver_temperaturas(fecha1, fecha2):
        pass

    def cantidad_muestras(self):
        pass


