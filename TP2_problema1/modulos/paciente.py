import random as r

nombres= ["Tommy", "Sofía", "Valentina", "Matías", "Alejandro", "Pedro", "Juan", "Valeria", "Hugo", "Isabel"]
apellidos= ["Gutierrez", "Gonzalez", "Aguirre", "Rodriguez", "Messi", "Palacios", "Alvarez", "Martinez", "Belgrano", "Sivori"]
nivel_riesgo= [1,2,3]

class Paciente:
    def _init__ (self):
        indice= len(nombres)
        self.nombre= r.randint(0, indice)
        self.apellido= r.randint(0, indice)
        self.riesgo= nivel_riesgo[r.randint(0,2)]
        