from TP2_problema2.modulos.investigacion import TemperaturasDB

aux= TemperaturasDB()


aux.guardar_temperatura(33.2,'01/09/2049')
aux.guardar_temperatura(34,'02/09/2049')
aux.guardar_temperatura(20,'03/09/2049')
aux.guardar_temperatura(12.3,'06/09/2049')
aux.guardar_temperatura(50,'29/10/2049')
aux.guardar_temperatura(49.2,'30/10/2049')
aux.guardar_temperatura(47,'01/11/2049')


#Totalmente Funcional
print(f"{aux.devolver_temp('01/09/2049')}°C")
print(f'{aux.max_temp_rango("02/09/2049","01/11/2049")}°C')
print(f'{aux.min_temp_rango("01/09/2049","01/11/2049")}°C')





