class MonticuloBinario_Tupla_Minimo:
  def __init__(self):
    self.tuplaMonticulo=[(float ("inf"),)] # Iniciamos el monticulo con un valor infinito, para que cualquier otro valor sea menor
    self.tamanoActual= 0

  def infiltArriba(self, indice_elemento):
    while indice_elemento // 2 > 0: #mientras el elemento tenga un padre:
      if self.tuplaMonticulo[indice_elemento][0] < self.tuplaMonticulo[indice_elemento // 2]: #si el elemento es menor que el padre:
        temporal= self.tuplaMonticulo[indice_elemento // 2] #guardamos el padre en una variable temporal
        self.tuplaMonticulo[indice_elemento // 2]= self.tuplaMonticulo[indice_elemento] #reemplazamos al padre con el elemento
        self.tuplaMonticulo= temporal # Reemplaza al elemento con el padre
      indice_elemento= indice_elemento // 2 #actualiza el indice al del padre

  def insertar(self, dato):
    self.tuplaMonticulo.append(dato) #agregamos el nuevo elemento al final del monticulo
    self.tamanoActual +=1
    self.infiltArriba(self.tamanoActual) #llamamos a infiltrar para que acomode el elemento donde corresponda

  def infiltAbajo(self, i):
    while (i * 2) <= self.tamanoActual: #Mientras el elemento tenga por lo menos un hijo:
      hm= self.hijoMin(i) #indice del hijo menor
      if self.tuplaMonticulo[i][0] > self.tuplaMonticulo[hm][0]:
        temporal= self.tuplaMonticulo[i]
        self.tuplaMonticulo[i]= self.tuplaMonticulo[hm]
        self.tuplaMonticulo[hm]= temporal 
      i= hm

  def hijoMin(self, i): #devuelve el indice del hijo mas chico del elemento en la posicion i
    if i * 2 + 1 > self.tamanoActual:
      return i*2
    else: #si el elemento tiene dos hijos:
      if self.tuplaMonticulo[i*2][0] < self.tuplaMonticulo[i*2+1][0]: #Si el hijo izquierdo es menor que el derecho:
        return i*2
      else:
        return i*2+1
      
  def eliminarMin(self): #esta fc elimina y retorna el elemento mas chico del monticulo
    valorSacado= self.tuplaMonticulo[1] #guardamos el valor de la raiz (ya que es el mas chiquito)
    self.tuplaMonticulo[1]= self.tuplaMonticulo[self.tamanoActual] #reemplazamos con el ultimo elemento
    self.tamanoActual= self.tamanoActual-1
    self.tuplaMonticulo.pop() # eliminamos el ultimo elemento ya que esta en la raiz ahora
    self.infiltAbajo(1) #acomodamos la nueva raiz como corresponda
    return valorSacado
  
  def construirMonticulo(self, unaLista): #Contruye un monticulo a partir de una lista
    i= len(unaLista) // 2
    self.tamanoActual= len(unaLista)
    self.tuplaMonticulo= [(float('inf'),)] + unaLista[:]
    while (i>0):
      self.infiltAbajo(i)
      i -=1

  def decrementarClave(self, i, nuevo_valor):
    if i not in self.tuplaMonticulo: #maneja si esta fuera del rango
      return
    if nuevo_valor < self.tuplaMonticulo[i][0]:
      self.tuplaMonticulo[i]= (nuevo_valor, self.tuplaMonticulo[i][1])
      self.infiltArriba(i)
    elif nuevo_valor > self.tuplaMonticulo[i][0]:
      self.tuplaMonticulo[i]= (nuevo_valor, self.tuplaMonticulo[i][1])
      self.infiltAbajo(i)
  
  def estaVacia(self):
    return self.tamanoActual == 0
  
  def __iter__(self): #permite iterar sobre los elementos del monticulo
    for i in range(1, len(self.tuplaMonticulo)):
      yield self.tuplaMonticulo[i]
