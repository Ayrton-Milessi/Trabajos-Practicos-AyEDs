from .monticulo import MonticuloBinario

class sala_de_emergencia:
    def __init__(self):
        self.cola= MonticuloBinario()

    def ingresar_paciente(self, paciente):
        self.cola.insertar(paciente)
    
    def atender_paciente(self):
       return self.cola.eliminarMin()
    
    def total_pacientes(self):
        return self.cola.tamanoActual
    
    def __iter__(self):
        return iter(self.cola)