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

    def infiltAbajo(self,i):
        while (i * 2) <= self.tamanoActual:
           hm = self.hijoMin(i)
           if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
           i = hm

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
           return i * 2
        else:
           if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
           else:
              return i * 2 + 1

    