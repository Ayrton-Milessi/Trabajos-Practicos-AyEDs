class Nodo_AVL:
   def __init__(self, clave, valor, izquierdo= None, derecho= None, padre= None):
     self.clave= clave
     self.cargaUtil= valor
     self.hijoIzquierdo= izquierdo
     self.hijoDerecho= derecho
     self.padre= padre
     self.factor_equilibrio= 0

   def tiene_hijoIzquierdo(self):
     return self.hijoIzquierdo

   def tiene_hijoDerecho(self):
     return self.hijoDerecho

   def es_hijoIzquierdo(self):
     return self.padre and self.padre.hijoIzquierdo == self

   def es_hijoDerecho(self):
     return self.padre and self.padre.hijoDerecho == self

   def es_raiz(self):
     return not self.padre

   def esHoja(self):
     return not (self.hijoDerecho or self.hijoIzquierdo)

   def tiene_un_hijo(self):
      return self.hijoDerecho or self.hijoIzquierdo

   def tiene_dos_hijos(self):
      return self.hijoDerecho and self.hijoIzquierdo

   def remplazar_dato_nodo(self, clave, valor, h_izq, h_der):
      self.clave= clave
      self.cargaUtil= valor
      self.hijoIzquierdo= h_izq
      self.hijoDerecho= h_der
      if self.tiene_hijoIzquierdo():
          self.hijoIzquierdo.padre = self
      if self.tiene_hijoDerecho():
          self.hijoDerecho.padre = self
  
   def empalmar(self):
      if self.esHoja():
          if self.es_hijoIzquierdo():
              self.padre.hijoIzquierdo= None
          else:
              self.padre.hijoDerecho= None
      elif self.tiene_un_hijo():
          if self.tiene_hijoIzquierdo():
              if self.es_hijoIzquierdo():
                  self.padre.hijoIzquierdo= self.hijoIzquierdo
              else:
                  self.padre.hijoDerecho= self.hijoIzquierdo
              self.hijoIzquierdo.padre= self.padre
          else:
              if self.es_hijoIzquierdo():
                  self.padre.hijoIzquierdo= self.hijoDerecho
              else:
                  self.padre.hijoDerecho= self.hijoDerecho
              self.hijoDerecho.padre= self.padre

   def encontrar_sucesor(self):
      sucesor= None
      if self.tiene_hijoDerecho():
          sucesor= self.hijoDerecho.encontrar_minimo()
      else:
          if self.padre:
            if self.es_hijoIzquierdo():
              sucesor= self.padre
            else:
              self.padre.hijoDerecho= None
              sucesor= self.padre.encontrar_sucesor()
              self.padre.hijoDerecho = self
      return sucesor

   def encontrar_minimo(self):
      actual= self
      while actual.tiene_hijoIzquierdo():
          actual= actual.hijoIzquierdo
      return actual

class AVL:
   def __init__(self):
       self.raiz= None
       self.tamano = 0

   def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz= Nodo_AVL(clave, valor)
        self.tamano += 1

   def _agregar(self, clave, valor, nodoActual):
    if clave < nodoActual.clave:
        if nodoActual.tiene_hijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
        else:
                nodoActual.hijoIzquierdo= Nodo_AVL(clave, valor, padre=nodoActual)
                self.actualizar_equilibrio(nodoActual.hijoIzquierdo)
    else:
        if nodoActual.tiene_hijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
        else:
                nodoActual.hijoDerecho = Nodo_AVL(clave, valor, padre=nodoActual)
                self.actualizar_equilibrio(nodoActual.hijoDerecho)

   def actualizar_equilibrio(self, nodo):
    if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
        self.reequilibrar(nodo)
        return
    if nodo.padre != None:
        if nodo.es_hijoIzquierdo():
                nodo.padre.factor_equilibrio += 1
        elif nodo.es_hijoDerecho():
                nodo.padre.factor_equilibrio -= 1
        if nodo.padre.factor_equilibrio != 0:
                self.actualizar_equilibrio(nodo.padre)
    
   def obtener(self, clave):
       if self.raiz:
           resultado= self._obtener(clave, self.raiz)
           if resultado:
                  return resultado.cargaUtil
           else:
                  return None
       else:
           return None

   def _obtener(self,clave,nodoActual):
       pass
   
   def rotarIzquierda(self, rotRaiz):
    nuevaRaiz= rotRaiz.hijoDerecho
    rotRaiz.hijoDerecho= nuevaRaiz.hijoIzquierdo
    if nuevaRaiz.hijoIzquierdo != None:
        nuevaRaiz.hijoIzquierdo.padre= rotRaiz
    nuevaRaiz.padre= rotRaiz.padre
    if rotRaiz.es_raiz():
        self.raiz= nuevaRaiz
    else:
        if rotRaiz.es_hijoIzquierdo():
                rotRaiz.padre.hijoIzquierdo= nuevaRaiz
        else:
            rotRaiz.padre.hijoDerecho= nuevaRaiz
    nuevaRaiz.hijoIzquierdo= rotRaiz
    rotRaiz.padre= nuevaRaiz
    rotRaiz.factor_equilibrio= rotRaiz.factor_equilibrio + 1 - min(nuevaRaiz.factor_equilibrio, 0)
    nuevaRaiz.factor_equilibrio= nuevaRaiz.factor_equilibrio + 1 + max(rotRaiz.factor_equilibrio, 0)
   
   def rotarDerecha(self, rotRaiz):
       nuevaRaiz= rotRaiz.hijoIzquierdo
       rotRaiz.hijoIzquierdo= nuevaRaiz.hijoDerecho
       if nuevaRaiz.hijoDerecho != None:
           nuevaRaiz.hijoDerecho.padre= rotRaiz
       nuevaRaiz.padre= rotRaiz.padre
       if rotRaiz.es_raiz():
           self.raiz= nuevaRaiz
       else:
           if rotRaiz.es_hijoIzquierdo():
               rotRaiz.padre.hijoIzquierdo= nuevaRaiz
           else:
               rotRaiz.padre.hijoDerecho= nuevaRaiz
       nuevaRaiz.hijoDerecho= rotRaiz
       rotRaiz.padre= nuevaRaiz
       rotRaiz.factor_equilibrio= rotRaiz.factor_equilibrio - 1 - max(nuevaRaiz.factor_equilibrio, 0)
       nuevaRaiz.factor_equilibrio= nuevaRaiz.factor_equilibrio - 1 + max(rotRaiz.factor_equilibrio, 0)

   def reequilibrar(self, nodo):
    if nodo.factor_equilibrio < 0:
            if nodo.hijoDerecho.factor_equilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
    elif nodo.factor_equilibrio > 0:
            if nodo.hijoIzquierdo.factor_equilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

   def __getitem__(self,clave):
       return self.obtener(clave)

   def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False

   def __delitem__(self,clave):
       self.eliminar(clave)

   def __len__(self):
       return self.tamano

   def __iter__(self):
       return self.raiz.__iter__()