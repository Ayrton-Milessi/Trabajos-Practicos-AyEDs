class MonticuloBinarioMaximo:
    def __init__(self):
        self.tuplaMonticulo = [(float ("-inf"),)]
        self.tamanoActual = 0

    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.tuplaMonticulo[i][0] > self.tuplaMonticulo[i // 2][0]:  #cambiamos la comparación a '>'
                temporal = self.tuplaMonticulo[i // 2]
                self.tuplaMonticulo[i // 2] = self.tuplaMonticulo[i]
                self.tuplaMonticulo[i] = temporal
            i = i // 2

    def insertar(self, k):
        self.tuplaMonticulo.append(k)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)
            if self.tuplaMonticulo[i][0] < self.tuplaMonticulo[hm][0]:  #cambiamos la comparación a '>'
                temporal = self.tuplaMonticulo[i]
                self.tuplaMonticulo[i] = self.tuplaMonticulo[hm]
                self.tuplaMonticulo[hm] = temporal
            i = hm

    def hijoMax(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.tuplaMonticulo[i * 2][0] > self.tuplaMonticulo[i * 2 + 1][0]:  #cambiamos la comparación a '>'
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMax(self):
        valorSacado = self.tuplaMonticulo[1]
        self.tuplaMonticulo[1] = self.tuplaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.tuplaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.tuplaMonticulo = [(float("-inf"),)] + unaLista[:]  # Cambiamos el valor inicial a negativo infinito
        while i > 0:
            self.infiltAbajo(i)
            i -= 1

    def decrementarClave(self, i, nuevo_valor):
        if i not in self.tuplaMonticulo:  # maneja si está fuera del rango
            return
        if nuevo_valor > self.tuplaMonticulo[i][0]:  #cambiamos la comparación a '>'
            self.tuplaMonticulo[i] = (nuevo_valor, self.tuplaMonticulo[i][1])
            self.infiltArriba(i)
        elif nuevo_valor < self.tuplaMonticulo[i][0]:  #cambiamos la comparación a '>'
            self.tuplaMonticulo[i] = (nuevo_valor, self.tuplaMonticulo[i][1])
            self.infiltAbajo(i)

    def estaVacia(self):
        return self.tamanoActual == 0

    def __iter__(self):
        for i in range(1, len(self.tuplaMonticulo)):
            yield self.tuplaMonticulo[i]
