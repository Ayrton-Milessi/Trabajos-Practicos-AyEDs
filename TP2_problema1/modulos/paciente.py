from random import randint, choices
import datetime

nombres= ["Sofía", "Jorge", "Matías", "Alejandro", "Pedro", "Juan", "Valeria", "Agustina"]
apellidos= ["Gonzalez", "Perez", "Rodriguez", "Messi", "Palacios", "Alvarez", "Martinez", "Sivori"]
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.tiempo_llegada = datetime.datetime.now()

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    
    def __lt__(self, paciente_comparar):
        if self.__riesgo == paciente_comparar.__riesgo:
            return self.tiempo_llegada < paciente_comparar.tiempo_llegada
        return self.__riesgo < paciente_comparar.__riesgo

    def __gt__(self, paciente_comparar):
        if self.__riesgo == paciente_comparar.__riesgo:
            return self.tiempo_llegada > paciente_comparar.tiempo_llegada
        return self.__riesgo > paciente_comparar.__riesgo