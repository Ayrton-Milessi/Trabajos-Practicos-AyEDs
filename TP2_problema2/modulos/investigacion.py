from TP2_problema2.modulos.avl import AVL
import datetime

class TemperaturasDB:
    def __init__(self):
        self.avl= AVL()


    def guardar_temperatura(self, temp, fecha):
        objeto_fecha= datetime.strptime(fecha,"%d/%m/%Y") # especificamos que formato de fecha que queremos y lo convertimos en un objeto
        self.avl.agregar(objeto_fecha,temp)

    def devolver_temp(self, fecha):
        objeto_fecha= datetime.strptime(fecha, "%d/%m/%Y")
        temperatura= self.avl.obtener(objeto_fecha) # Buscamos la temperatura deseada
        return temperatura

    def max_temp_rango(self, fecha1,fecha2):
        self

    
    def _max_temp_rango(self, nodo, fecha1, fecha2, max_temp):
        if fecha1 <= nodo.clave <= fecha2:
            max_temp = max(max_temp, nodo.cargaUtil)
        
        if fecha1 < nodo.clave:
            pass
        

    def temp_extermos_rango(self, fecha1,fecha2):
        pass

    def borrar_temperatura(fecha):
        pass

    def devolver_temperaturas(fecha1, fecha2):
        pass

    def cantidad_muestras(self):
        pass