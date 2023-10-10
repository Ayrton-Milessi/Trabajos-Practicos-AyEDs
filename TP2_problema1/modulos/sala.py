from .monticulo import MonticuloBinario

class sala_de_emergencia:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def ingresar_paciente(self, paciente):
        self.monticulo.insertar(paciente)
    
    def atender_paciente(self):
       return self.monticulo.eliminarMin()
    
    def total_pacientes(self):
        return self.monticulo.tamanio
    
    def __iter__(self):
        return iter(self.monticulo)