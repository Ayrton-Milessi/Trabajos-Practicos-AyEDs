class Nodo_avl:
    def __init__(self, clave, valor, padre=None, izquierdo=None, derecho=None):
        self.clave= clave
        self.cargaUtil= valor
        self.hijoIzquierdo= izquierdo
        self.hijoDerecho= derecho
        self.padre= padre
        self.factor_equilibrio= 0

    def tiene_hijoIzquierdo(self):
        return self.hijoIzquierdo #da True si tiene hijo izquierdo
    
    def tiene_hijoDerecho(self):
        return self.hijoDerecho
    
    def es_hijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def es_hijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self #devuelve True si es hijo derecho del padre

    def es_raiz(self):
        return not self.padre #retorna True si es la raiz

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo) #si no tiene hijos, significa que es una hoja

    def tiene_un_hijo(self):
        return self.hijoDerecho or self.hijoIzquierdo #da True si tiene cualquiera de los dos hijos

    def tiene_dos_hijos(self):
        return self.hijoDerecho and self.hijoIzquierdo #da True si tiene los dos hijos

    def remplazar_dato_nodo(self, clave, valor, h_izq, h_der): #actualizamos los datos de un nodo
        self.clave= clave
        self.cargaUtil= valor
        self.hijoDerecho= h_der
        self.hijoIzquierdo= h_izq
        if self.tiene_hijoIzquierdo():
            self.hijoIzquierdo.padre = self #para que apunte a su padre
        if self.tiene_hijoDerecho():
            self.hijoDerecho.padre = self
    
    def empalmar(self):
        if self.esHoja(): #verificamos si es una hoja
            if self.es_hijoIzquierdo():
                self.padre.hijoIzquierdo= None #hacemos que el padre apunte a None
            else:
                self.padre.hijoDerecho= None

        elif self.tiene_un_hijo():
            if self.tiene_hijoIzquierdo(): #si tiene un hijo izquierdo
                if self.es_hijoIzquierdo():
                    self.padre.hijoIzquierdo= self.hijoIzquierdo #se ajusta el enlace para que el padre y el hijo izquierdo se apunten
                
                else:
                    self.padre.hijoDerecho= self.hijoIzquierdo #se ajusta el enlace para que el padre y el hijo derecho se apunten
                self.hijoIzquierdo.padre = self.padre #actualiza el enlace del padre para que apunte al padre del nodoActual
            
            else: #si tiene un hijo derecho
                self.padre.hijoDerecho= self.hijoDerecho
            self.hijoDerecho.padre= self.padre

    def encontrar_minimo(self):
        actual= self
        while actual.tiene_hijoIzquierdo():
            actual= actual.hijoIzquierdo
        return actual #retorna el valor minimo (el que mas a la izquierda esta)
            
    def encontrar_sucesor(self):
        sucesor = None
        if self.tiene_hijoDerecho():
            sucesor = self.hijoDerecho.encontrar_minimo() #buscamos el sucesor (valor minimo) del subarbol derecho
        elif self.es_hijoIzquierdo():
            sucesor = self.padre #el sucesor de un hijo izquierdo es su padre
        else:
            sucesor = self.padre.encontrar_sucesor() #si el nodo no tiene hijo derecho y no es hijo izquierdo, buscamos el sucesor en el padre
        return sucesor

class AVL:
    def __init__(self):
        self.raiz= None
        self.tamano= 0
    
    def actualizar_equilibrio(self, nodo):
        if nodo.factor_equilibrio > 1 or nodo.factor_equilibrio < -1:
            self.reequilibrar(nodo) #si no esta equilibrado
            return
        if nodo.padre != None: #si tiene padre
            if nodo.es_hijoIzquierdo():
                nodo.padre.factor_equilibrio += 1 #si es hijo izquierdo, se suma uno al factor equilibrio del padre
            elif nodo.es_hijoDerecho():
                nodo.padre.factor_equilibrio -= 1 #si es hijo derecho, se resta uno al factor equilibrio del padre
            if nodo.padre.factor_equilibrio != 0: #si el factor equilibrio es igual 0 esta equilibrado el arbol
                self.actualizar_equilibrio(nodo.padre)
    
    def agregar(self, clave, valor):
        if self.raiz: #si hay raiz
            self._agregar(clave,valor,self.raiz) #se agrega otro nodo
        else:
            self.raiz= Nodo_avl(clave,valor) #se agrega a la raiz del arbol
        self.tamano +=1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave: #si la clave es menor que la raiz, se va al subarbol izquierdo 
            if nodoActual.tiene_hijoIzquierdo(): 
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)#si ya tiene un hijo izquierdo, se llama recursivamente actulizando los valores a comparar
            else:
                nodoActual.hijoIzquierdo= Nodo_avl(clave, valor, padre=nodoActual)
                self.actualizar_equilibrio(nodoActual.hijoIzquierdo)
        else: #si la clave es mayor que la raiz, se va al subarbol derecho
            if nodoActual.tiene_hijoDerecho():
                self._agregar(clave, valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho= Nodo_avl(clave, valor, padre=nodoActual) #si no tiene hijo derecho, se agrega un nuevo nodo conectandolo con el padre
                self.actualizar_equilibrio(nodoActual.hijoDerecho)
    
    def obtener(self, clave):
        if self.raiz: #si tiene raiz
            resultado = self._obtener(clave, self.raiz) #llama a la funcion auxiliar
            if resultado: #si encontro el nodo
                return resultado.cargaUtil #retorna el valor de la carga util asociada a la clave dada
            else:
                return None #retorna None si no se encontró
        else:
            return None
        
    def _obtener(self, clave, nodoActual):
        if not nodoActual: #
            return None
        elif nodoActual.clave == clave: #si el nodo que se busca es la raiz, retorna la raiz
            return nodoActual
        elif nodoActual.clave > clave: #si el nodo es menor que la raiz
            return self._obtener(clave,nodoActual.hijoIzquierdo) #busca recursivamente en el subarbol izquierdo
        else: #si el nodo es mayor que la raiz
            return self._obtener(clave,nodoActual.hijoDerecho) #busca recursivamente en el subarbol derecho

    def eliminar(self, clave):
        if self.tamano > 1: 
            nodoAEliminar= self._obtener(clave, self.raiz) #busca el nodo que se quiere eliminar
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano= self.tamano-1 #decrementa el tamaño total del AVL ya que se quito un nodo
            else:
                raise KeyError('Error, la clave no está en el árbol') #para imprimir un mensaje por si no encuentra el nodo que se quiere eliminar
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz= None #si el nodo que se quiere eliminar es la raiz, directamente le decimos que es None
            self.tamano= self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
        
    def rotarIzquierda(self, rotRaiz):
        nuevaRaiz= rotRaiz.hijoDerecho #guardamos el hijo derecho del punto de rotacion
        rotRaiz.hijoDerecho= nuevaRaiz.hijoIzquierdo #actualizamos los enlaces
        if nuevaRaiz.hijoIzquierdo != None: #si tiene un hijo izquierdo
            nuevaRaiz.hijoIzquierdo.padre= rotRaiz #actualizamos el enlace del padre del hijo izquierdo para que apunte al punto de rotacion
        nuevaRaiz.padre= rotRaiz.padre #actualizamos el enlace padre para que apunte al mismo padre que tenía el punto de rotacion

        if rotRaiz.es_raiz(): #si es la raiz
            self.raiz= nuevaRaiz #hacemos el enlace para que apunte a nuevaRaiz
        else:
            if rotRaiz.es_hijoIzquierdo(): #si el punto de rotacion era un hijo izquierdo
                rotRaiz.padre.hijoIzquierdo= nuevaRaiz  #actualizamos el puntero del hijoIzquierdo del padre del punto de rotacion para que apunte a nuevaRaiz
            else: #si el punto de rotacion era un hijo derecho
                rotRaiz.padre.hijoDerecho= nuevaRaiz #actualizamos el puntero del hijoDerecho del padre del punto de rotacion para que apunte a nuevaRaiz
        nuevaRaiz.hijoIzquierdo= rotRaiz
        rotRaiz.padre= nuevaRaiz
        rotRaiz.factor_equilibrio= rotRaiz.factor_equilibrio + 1 - min(nuevaRaiz.factor_equilibrio, 0) #actualiza los factores de equilibrio 
        nuevaRaiz.factor_equilibrio= nuevaRaiz.factor_equilibrio + 1 + max(rotRaiz.factor_equilibrio, 0)

    def rotarDerecha(self, rotRaiz):
       nuevaRaiz= rotRaiz.hijoIzquierdo #guardamos el hijo izquierdo del punto de rotacion
       rotRaiz.hijoIzquierdo= nuevaRaiz.hijoDerecho
       if nuevaRaiz.hijoDerecho != None: #si tiene un hijo derecho
           nuevaRaiz.hijoDerecho.padre= rotRaiz #actulizamos los punteros
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
        if nodo.factor_equilibrio < 0: #si es negativo el factor de equilibrio
            if nodo.hijoDerecho.factor_equilibrio > 0: #si el factor de equlibrio del hijo derecho del nodo es postivo
                self.rotarDerecha(nodo.hijoDerecho) #rotamos a la derecha 
                self.rotarIzquierda(nodo) #y rotamos a la izquierda para reequilibrar
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factor_equilibrio > 0: #si es postitivo el factor de equilibrio
            if nodo.hijoIzquierdo.factor_equilibrio < 0: #si el factor de equlibrio del hijo izquierdo del nodo es negativo
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def remover(self, nodoActual):
        if nodoActual.esHoja(): #si es hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo: 
                nodoActual.padre.hijoIzquierdo= None #elimina el hijo izquierdo
            else:
                nodoActual.padre.hijoDerecho= None #elimina el hijo derecho
        
        elif nodoActual.tiene_un_hijo(): #si tiene un hijo
            if nodoActual.tiene_hijoIzquierdo(): 
                if nodoActual.es_hijoIzquierdo():#si el padre tiene un hijo izquierdo
                    nodoActual.hijoIzquierdo.padre= nodoActual.padre #apuntamos el hijo a su abuelo (al padre del nodo que se elimina)
                    nodoActual.padre.hijoIzquierdo= nodoActual.hijoIzquierdo #apuntamos el padre a su nuevo hijo
                elif nodoActual.es_hijoDerecho(): #si es hijo derecho
                    nodoActual.hijoIzquierdo.padre= nodoActual.padre
                    nodoActual.padre.hijoDerecho= nodoActual.hijoIzquierdo
                else: #si no es hijo derecho ni izquierdo, llama a un funcion para remplazar los datos del nodo con los de su hijo izquierdo
                    nodoActual.remplazar_dato_nodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else: #si tiene hijo derecho
                if nodoActual.es_hijoIzquierdo():
                    nodoActual.hijoDerecho.padre= nodoActual.padre
                    nodoActual.padre.hijoIzquierdo= nodoActual.hijoDerecho
                elif nodoActual.es_hijoDerecho():
                    nodoActual.hijoDerecho.padre= nodoActual.padre
                    nodoActual.padre.hijoDerecho= nodoActual.hijoDerecho
                else:
                    nodoActual.remplazar_dato_nodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

        else: #si tiene dos hijos
            aux= nodoActual.encontrar_sucesor()
            aux.empalmar()
            nodoActual.clave= aux.clave
            nodoActual.cargaUtil= aux.cargaUtil

    def __delitem__(self,clave):
        self.eliminar(clave)

    def __iter__(self):
       return self._inorden(self.raiz)
   
    def _inorden(self, avl):
        if avl is not None: # Verifico si el nodo actual (avl) no es None
            yield from self._inorden(avl.hijoIzquierdo)
            yield avl.clave
            yield from self._inorden(avl.hijoDerecho)