class Nodo_AVL:
   def __init__(self, clave, valor, izquierdo= None, derecho= None, padre= None):
     self.clave= clave
     self.carga_util= valor
     self.hijo_izquierdo= izquierdo
     self.hijo_derecho= derecho
     self.padre= padre

   def tiene_hijo_izquierdo(self):
     return self.hijo_izquierdo

   def tiene_hijo_derecho(self):
     return self.hijo_derecho

   def es_hijo_izquierdo(self):
     return self.padre and self.padre.hijo_izquierdo == self

   def es_hijo_derecho(self):
     return self.padre and self.padre.hijo_derecho == self

   def es_raiz(self):
     return not self.padre

   def es_hoja(self):
     return not (self.hijo_derecho or self.hijo_izquierdo)

   def tiene_un_hijo(self):
      return self.hijo_derecho or self.hijo_izquierdo

   def tiene_dos_hijos(self):
      return self.hijo_derecho and self.hijo_izquierdo

   def remplazar_dato_nodo(self, clave, valor, h_izq, h_der):
      self.clave= clave
      self.carga_util= valor
      self.hijo_izquierdo= h_izq
      self.hijo_derecho= h_der
      if self.tiene_hijo_izquierdo():
          self.hijo_izquierdo.padre = self
      if self.tiene_hijo_derecho():
          self.hijo_derecho.padre = self
  
   def empalmar(self):
      if self.es_hoja():
          if self.es_hijo_izquierdo():
              self.padre.hijo_izquierdo= None
          else:
              self.padre.hijo_derecho= None
      elif self.tiene_un_hijo():
          if self.tiene_hijo_izquierdo():
              if self.es_hijo_izquierdo():
                  self.padre.hijo_izquierdo= self.hijo_izquierdo
              else:
                  self.padre.hijo_derecho= self.hijo_izquierdo
              self.hijo_izquierdo.padre= self.padre
          else:
              if self.es_hijo_izquierdo():
                  self.padre.hijo_izquierdo= self.hijo_derecho
              else:
                  self.padre.hijo_derecho= self.hijo_derecho
              self.hijo_derecho.padre= self.padre

   def encontrar_sucesor(self):
      sucesor= None
      if self.tiene_hijo_derecho():
          sucesor= self.hijo_derecho.encontrar_minimo()
      else:
          if self.padre:
            if self.es_hijo_izquierdo():
              sucesor= self.padre
            else:
              self.padre.hijo_derecho= None
              sucesor= self.padre.encontrar_sucesor()
              self.padre.hijo_derecho = self
      return sucesor

   def encontrar_minimo(self):
      actual= self
      while actual.tiene_hijo_izquierdo():
          actual= actual.hijo_izquierdo
      return actual

class AVL:
   def __init__(self):
       self.raiz= None
       self.tamanio= 0

   def longitud(self):
        return self.tamanio

   def __len__(self):
       return self.tamanio

   def __iter__(self):
       return self.raiz.__iter__()

   def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz= Nodo_AVL(clave, valor)
        self.tamanIo += 1

   def _agregar(self, clave, valor, nodoActual):
      pass
   
   def __setitem__(self,c,v):
       self.agregar(c,v)
    
   def obtener(self, clave):
       if self.raiz:
           resultado= self._obtener(clave, self.raiz)
           if resultado:
                  return resultado.carga_util
           else:
                  return None
       else:
           return None

   def _obtener(self,clave,nodoActual):
       pass
   
   def __getitem__(self,clave):
       return self.obtener(clave)

   def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False
       
   def __delitem__(self,clave):
       self.eliminar(clave)