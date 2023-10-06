class MonticuloBinario:
    def __init__ (self):
        self.lista_pacientes= [0]
        self.tamanio= 0

    def infiltrar_arriba (self, orden):
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

    def infiltrar_abajo(self,i):
        while (i * 2) <= self.tamanio:
           hijo_minimo= self.hijoMin(i)
           if self.lista_pacientes[i] > self.lista_pacientes[hijo_minimo]:
              temporal= self.lista_pacientes[i]
              self.lista_pacientes[i]= self.lista_pacientes[hijo_minimo]
              self.lista_pacientes[hijo_minimo]= temporal
           i = hijo_minimo

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanio:
           return i * 2
        else:
           if self.lista_pacientes[i*2] < self.lista_pacientes[i*2+1]:
              return i * 2
           else:
              return i * 2 + 1

    def eliminarMin(self):
        valor_sacado= self.lista_pacientes[1]
        self.lista_pacientes[1]= self.lista_pacientes[self.tamanio]
        self.tamanio= self.tamanio - 1
        self.lista_pacientes.pop()
        self.infiltrar_abajo(1)
        return valor_sacado
    
    def construir_monticulo(self,lista):
        i= len(lista) // 2
        self.tamanio= len(lista)
        self.lista_pacientes= [0] + lista[:]
        while (i > 0):
            self.infiltrar_abajo(i)
            i= i - 1