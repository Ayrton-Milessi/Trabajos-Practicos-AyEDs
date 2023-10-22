class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]: #si el elemento es menor que su padre, intercambian 
             tmp = self.listaMonticulo[i // 2] 
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp  
          i = i // 2 #para ir al padre

    def insertar(self,k): #añade al final de la lista un nuevo elemento al monticulo
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual) #llama a la funcion 'infiltArriba' para mantener la estructura del monticulo

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]: #si el elemento es mayor que su padre, intercambian
              tmp = self.listaMonticulo[i] 
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm #para ir al hijo minimo

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2 #retorna el hijo izquierdo si derecho no existe
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2 #retorna el hijo izquierdo si es menor que el derecho
          else:
              return i * 2 + 1 #retorna el hijo derecho si es menor que el izquierdo

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1] #extrae la raiz
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] #reemplaza la raiz por el ultimo elemento agregado
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop() 
      self.infiltAbajo(1) #llama a la funcion 'infiltAbajo' para mantener la estructura del monticulo
      return valorSacado

    def construirMonticulo(self,unaLista): 
      #metodo para construir un monticulo con una lista ya formada
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

    def __iter__(self): #para iterar sobre el monticulo
        for i in range(1,len(self.listaMonticulo)):
            yield self.listaMonticulo[i]        