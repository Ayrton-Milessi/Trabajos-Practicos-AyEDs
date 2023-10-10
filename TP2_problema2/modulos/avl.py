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
