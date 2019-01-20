import csv
import pandas as pd
import folium

"""def crear_mapa(archivo):
	data = pd.read_csv("datos/"+archivo)
	m = folium.Map(location=[-2.176049, -79.919096], zoom_start=12)
	folium.Choropleth(
	geo_data="sectores.geojson",
	fill_color='YlGn',
	fill_opacity=0.7,
	line_opacity=0.2,
	bins = [0,100,300,1000,1500],
	data=data,
	key_on = 'feature.properties.Name',
	columns = ['Name','NUMPOINTS']
	).add_to(m)
 	
	nombre = archivo.replace("csv","html")
	print(nombre+"\n")
	m.save(outfile='mapas_cp/'+nombre)"""


archivos = ['puntosMadrugada.csv', 'puntosManana.csv', 'puntosNoche.csv', 'puntosTarde.csv']

for ar in archivos:
	print(ar+"\n")
	#crear_mapa(ar)
	print("Se creó mapa para "+ar+"\n\n")
	data = pd.read_csv(ar)
	m = folium.Map(location=[-2.176049, -79.919096], zoom_start=12)
	folium.Choropleth(
	geo_data="sectores.geojson",
	fill_color='YlGn',
	fill_opacity=0.7,
	line_opacity=0.2,
	bins = [0,1000,5000,10000,20000],
	data=data,
	key_on = 'feature.properties.Name',
	columns = ['Name','NUMPOINTS']
	).add_to(m)
	name_ar = ar.replace('csv', 'html')
	print(name_ar+"\n")
	m.save(outfile=name_ar)

