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

        fecha1_objeto = datetime.strptime(fecha1, "%d/%m/%Y") #las fechas estaban en str, asique los pasamos a formato "datetime" para que las comparaciones funcionen
        fecha2_objeto = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_objeto <= nodo.clave <= fecha2_objeto:
            max_temp = max(max_temp, nodo.cargaUtil)
        
        if fecha1_objeto < nodo.clave:
            max_temp= self._max_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2, max_temp)

        if fecha2_objeto > nodo.clave:
            max_temp= self._max_temp_rango(nodo.hijoDerecho, fecha1, fecha2, max_temp)
        
        return max_temp
    
    #Se realiza exactamente lo mismo pero buscando el minimo
    def min_temp_rango(self, fecha1, fecha2):
        min_temp= float("inf")
        return self._min_temp_rango(self.avl.raiz, fecha1, fecha2, min_temp)

    def _min_temp_rango(self, nodo, fecha1, fecha2, min_temp):
        if nodo is None: # primero verificamos que el nodo exista para no realizar llamadas innecesarias
            return min_temp
        
        fecha1_objeto = datetime.strptime(fecha1, "%d/%m/%Y") #las fechas estaban en str, asique los pasamos a formato "datetime" para que las comparaciones funcionen
        fecha2_objeto = datetime.strptime(fecha2, "%d/%m/%Y")
        if fecha1_objeto <= nodo.clave <= fecha2_objeto:
            min_temp = min(min_temp, nodo.cargaUtil)
        
        if fecha1_objeto < nodo.clave:
            min_temp= self._min_temp_rango(nodo.hijoIzquierdo, fecha1, fecha2, min_temp)

        if fecha2_objeto > nodo.clave:
            min_temp= self._min_temp_rango(nodo.hijoDerecho, fecha1, fecha2, min_temp)
        
        return min_temp

    def temp_extremos_rango(self, fecha1, fecha2):
        return self.min_temp_rango(fecha1, fecha2), self.max_temp_rango(fecha1,fecha2)

    def borrar_temperatura(self, fecha):
        if fecha is None:
            raise ValueError("Debe ingresar una fecha valida")
        fecha_= datetime.strptime(fecha, "%d/%m/%Y")
        self.avl.eliminar(fecha_)

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_objeto = datetime.strptime(fecha1, "%d/%m/%Y") 
        fecha2_objeto = datetime.strptime(fecha2, "%d/%m/%Y")

        for x in self.avl:
            if x >= fecha1_objeto and x <= fecha2_objeto:
                fecha_formateada = x.strftime("%d/%m/%Y") #Hago que la fecha se muestre como dia mes anio, ya que en formato datetime salia un 00:00:00 el cual no aportaba nada
                print(f"{fecha_formateada}, temperatura: {self.avl.obtener(x)}")

    def cantidad_muestras(self):
        return self.avl.tamano