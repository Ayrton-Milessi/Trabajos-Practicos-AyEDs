class MonticuloBinario:
    def __init__ (self):
        self.lista_pacientes= [0]
        self.tamanio= 0

    def adelantar (self, orden):
        while orden // 2 > 0:
            if self.lista_pacientes[orden] < self.lista_pacientes [orden // 2]:
                aux= self.lista_pacientes[orden // 2]
                self.lista_pacientes[orden // 2]= self.lista_pacientes[orden]
                self.lista_pacientes[orden]= aux
            orden= orden // 2

    def insertar (self, paciente):
        self.lista_pacientes.append(paciente)
        self.tamanio+= 1
        self.adelantar(self.tamanio)

    def 

    