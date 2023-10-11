import random as r

nombres= ["Tommy", "Sofía", "Valentina", "Matías", "Alejandro", "Pedro", "Juan", "Valeria", "Hugo", "Isabel"]
apellidos= ["Gutierrez", "Gonzalez", "Aguirre", "Rodriguez", "Messi", "Palacios", "Alvarez", "Martinez", "Belgrano", "Sivori"]
nivel_riesgo= [1,2,3]

class Paciente:
    def __init__ (self):
        self._nombre= r.choice(nombres)
        self._apellido= r.choice(apellidos)
        self._riesgo= r.choice(nivel_riesgo)

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_riesgo(self):
        return self._riesgo
    
    def __str__(self):
        aux = self._nombre + ' '+ self._apellido + '  ' + ' ->   '+ str(self._riesgo)
        return aux
    
    def __lt__(self, paciente_comparar):
        return self._riesgo < paciente_comparar.get_riesgo()

    def __gt__(self, paciente_comparar):
        return self._riesgo > paciente_comparar.get_riesgo()