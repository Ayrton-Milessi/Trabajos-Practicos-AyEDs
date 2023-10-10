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

class Nodo_AVL:
   def __init__(self, clave, valor, izquierdo= None, derecho= None, padre= None)
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
     return self.padre and self.padre.hijo_derecjo == self

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

   def agregar(self,clave, valor):
      if self.raiz:
         self._agregar(clave, valor, self.raiz)
      else:
         self.raiz= Nodo_AVL (clave, valor)
      self.tamanio += 1