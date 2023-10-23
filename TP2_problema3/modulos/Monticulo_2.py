class MonticuloBinario_Tupla_Maximo:
  def __init__(self):
    self.tuplaMonticulo = [float("-inf")]  # Iniciamos el monticulo con un valor infinitamente negativo
    self.tamanoActual = 0

  def infiltArriba(self, indice_elemento):
    while indice_elemento // 2 > 0:  # Mientras el elemento tenga un padre:
      if self.tuplaMonticulo[indice_elemento][0] > self.tuplaMonticulo[indice_elemento // 2][0]:  # Si el elemento es mayor que el padre:
        temporal = self.tuplaMonticulo[indice_elemento // 2]  # Guardamos el padre en una variable temporal
        self.tuplaMonticulo[indice_elemento // 2] = self.tuplaMonticulo[indice_elemento]  # Reemplazamos al padre con el elemento
        self.tuplaMonticulo[indice_elemento] = temporal  # Reemplaza al elemento con el padre
      indice_elemento = indice_elemento // 2  # Actualiza el indice al del padre

  def insertar(self, dato):
    self.tuplaMonticulo.append(dato)  # Agregamos el nuevo elemento al final del monticulo
    self.tamanoActual += 1
    self.infiltArriba(self.tamanoActual)  # Llamamos a infiltrar para que acomode el elemento donde corresponda

  def infiltAbajo(self, i):
    while (i * 2) <= self.tamanoActual:  # Mientras el elemento tenga por lo menos un hijo:
      hm = self.hijoMax(i)  # indice del hijo mayor
      if self.tuplaMonticulo[i][0] < self.tuplaMonticulo[hm][0]:
        temporal = self.tuplaMonticulo[i]
        self.tuplaMonticulo[i] = self.tuplaMonticulo[hm]
        self.tuplaMonticulo[hm] = temporal
      i = hm

  def hijoMax(self, i):  # Devuelve el indice del hijo mayor del elemento en la posición i
    if i * 2 + 1 > self.tamanoActual:
      return i * 2
    else:  # Si el elemento tiene dos hijos:
      if self.tuplaMonticulo[i * 2][0] > self.tuplaMonticulo[i * 2 + 1][0]:  # Si el hijo izquierdo es mayor que el derecho:
        return i * 2
      else:
        return i * 2 + 1

  def eliminarMax(self):  # Esta función elimina y retorna el elemento más grande del monticulo
    valorSacado = self.tuplaMonticulo[1]  # Guardamos el valor de la raiz (ya que es el más grande)
    self.tuplaMonticulo[1] = self.tuplaMonticulo[self.tamanoActual]  # Reemplazamos con el último elemento
    self.tamanoActual = self.tamanoActual - 1
    self.tuplaMonticulo.pop()  # Eliminamos el último elemento ya que está en la raiz ahora
    self.infiltAbajo(1)  # Acomodamos la nueva raiz como corresponda
    return valorSacado

  def construirMonticulo(self, unaLista):  # Construye un monticulo a partir de una lista
    i = len(unaLista) // 2
    self.tamanoActual = len(unaLista)
    self.tuplaMonticulo = [0] + unaLista[:]
    while i > 0:
      self.infiltAbajo(i)
      i -= 1

  def decrementarClave(self, vertice, nueva_clave):
    for i in range(1, len(self.tuplaMonticulo)):
      if self.tuplaMonticulo[i][1] == vertice: #Si encontramos el vertice que buscamos:
        aux = self.tuplaMonticulo[i] # guardamos la tupla en una variable temporal
        if nueva_clave > aux[0]: 
          return
        tupla = (nueva_clave, vertice)  
        self.tuplaMonticulo[i] = tupla # reemplazamos la tupla "vieja" por la nueva
        self.infiltArriba(i) #reordenamos el monticulo para mantener sus propiedades
        break

  def estaVacia(self):
    return self.tamanoActual == 0

  def __iter__(self):  # Permite iterar sobre los elementos del monticulo
    for i in range(1, len(self.tuplaMonticulo)):
      yield self.tuplaMonticulo[i]