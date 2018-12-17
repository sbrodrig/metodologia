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


archivos = ['puntos_2018-03-02.csv', 'puntos_2018-03-03.csv', 'puntos_2018-03-04.csv', 'puntos_2018-03-05.csv', 'puntos_2018-03-06.csv', 
'puntos_2018-03-07.csv', 'puntos_2018-03-08.csv', 'puntos_2018-03-09.csv', 'puntos_2018-03-10.csv', 'puntos_2018-03-11.csv', 'puntos_2018-03-12.csv',
'puntos_2018-03-13.csv', 'puntos_2018-03-14.csv', 'puntos_2018-03-15.csv', 'puntos_2018-03-16.csv', 'puntos_2018-03-17.csv', 'puntos_2018-03-18.csv', 
'puntos_2018-03-19.csv', 'puntos_2018-03-20.csv', 'puntos_2018-03-21.csv', 'puntos_2018-03-22.csv', 'puntos_2018-03-23.csv', 'puntos_2018-03-24.csv', 
'puntos_2018-03-25.csv', 'puntos_2018-03-26.csv', 'puntos_2018-03-27.csv', 'puntos_2018-03-28.csv', 'puntos_2018-03-29.csv', 'puntos_2018-03-30.csv', 
'puntos_2018-03-31.csv']

"""for ar in archivos:
	print("hola")
	print(ar+"\n")
	crear_mapa(ar)
	print("Se creó mapa para "+ar+"\n\n")"""

data = pd.read_csv("datos/puntos_2018-03-05.csv")
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
 	
m.save(outfile='mapas_cp/2018-03-03.html')

