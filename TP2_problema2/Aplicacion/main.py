from TP2_problema2.modulos.investigacion import TemperaturasDB

aux= TemperaturasDB()

aux.guardar_temperatura(30,'07/10/2023')
aux.guardar_temperatura(23,'08/10/2023')
aux.guardar_temperatura(13,'09/10/2023')
aux.guardar_temperatura(40,'30/12/2023')

#Totalmente Funcional
print(f'{aux.max_temp_rango("07/10/2023","30/12/2023")}°C')
print(f'{aux.min_temp_rango("07/10/2023","30/12/2023")}°C')
#

