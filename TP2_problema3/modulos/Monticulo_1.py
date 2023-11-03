import heapq

class MonticuloMinimo:
    def __init__(self):
        self.lista = []

    def insertar(self, k):
        heapq.heappush(self, k)

    def eliminarMin(self):
        return heapq.heappop(self)

    def __len__(self):
        return len(self.lista)