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