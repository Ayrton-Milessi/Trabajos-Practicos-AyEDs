from random import randint, choices
import datetime

nombres= ["Sofía", "Jorge", "Matías", "Alejandro", "Pedro", "Juan", "Valeria", "Agustina"]
apellidos= ["Gonzalez", "Perez", "Rodriguez", "Messi", "Palacios", "Alvarez", "Martinez", "Sivori"]
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6] #probabilidades de aparición de cada tipo de paciente

class Paciente:
    def __init__(self): #constructor que inicializa un nuevo paciente
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)] 
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__tiempo_llegada = datetime.datetime.now() #toma la hora de llegada del paciente

    def get_nombre(self): #obtiene el nombre del paciente
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self): #obtiene la descripcion del nivel de riesgo del paciente
        return self.__descripcion
    
    def get_tiempo_llegada(self):
       return self.__tiempo_llegada
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    
    def __lt__(self, paciente_comparar): #metodo de comparacion 'menor que' para ordenar los pacientes
        if self.__riesgo == paciente_comparar.__riesgo: #si los niveles de riesgo son iguales, utiliza el tiempo de llegada
            return self.__tiempo_llegada < paciente_comparar.__tiempo_llegada 
        return self.__riesgo < paciente_comparar.__riesgo #si los niveles de riesgo son diferentes, compara los niveles de riesgo

    def __gt__(self, paciente_comparar): #metodo de comparacion 'mayor que' para ordenar los pacientes
        if self.__riesgo == paciente_comparar.__riesgo: 
            return self.__tiempo_llegada > paciente_comparar.__tiempo_llegada
        return self.__riesgo > paciente_comparar.__riesgo 