from TP2_problema2.modulos.investigacion import TemperaturasDB

aux= TemperaturasDB()

aux.guardar_temperatura(30,"19/01/2049")
aux.guardar_temperatura(23,"20/01/2049")
aux.guardar_temperatura(11,"27/01/2049")
aux.guardar_temperatura(50,"28/03/2049")
aux.guardar_temperatura(43,"29/03/2049")


print(aux.max_temp_rango("29/03/2049","28/03/2049")) #No Funcional
