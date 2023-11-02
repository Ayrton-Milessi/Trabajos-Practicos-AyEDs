import heapq

class MonticuloMinimo:
    def __init__(self):
        self.lista = []

    def insertar(self, k):
        heapq.heappush(self.lista, k)

    def eliminarMin(self):
        return heapq.heappop(self.lista)

    def __len__(self):
        return len(self.lista)