from .monticulo import MonticuloBinario #importamos el monticulo binario

class sala_de_emergencia:
    def __init__(self):
        self.cola= MonticuloBinario() #la cola de espera va a tener la estructura del monticulo

    def ingresar_paciente(self, paciente):
        self.cola.insertar(paciente) #llega un paciente (se añade al monticulo)
    
    def atender_paciente(self):
       return self.cola.eliminarMin() #se atiende un paciente (se elimina del monticulo)
    
    def total_pacientes(self):
        return self.cola.tamanoActual #devuelve el número de pacientes que estan esperando
    
    def __iter__(self):
        return iter(self.cola)