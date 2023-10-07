import random as r

nombres= ["Tommy", "Sofía", "Valentina", "Matías", "Alejandro", "Pedro", "Juan", "Valeria", "Hugo", "Isabel"]
apellidos= ["Gutierrez", "Gonzalez", "Aguirre", "Rodriguez", "Messi", "Palacios", "Alvarez", "Martinez", "Belgrano", "Sivori"]
nivel_riesgo= [1,2,3]

class Paciente:
    def __init__ (self):
        indice= len(nombres)
        self.nombre= r.choice(nombres)
        self.apellido= r.choice(apellidos)
        self.riesgo= r.choice(nivel_riesgo)
