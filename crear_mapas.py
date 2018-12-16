import csv
import folium
from folium.plugins import HeatMap

def crearHeatMap(fecha, data):
    heatmap = folium.Map(location=[-2.176049, -79.919096], zoom_start=10)
    HeatMap(data, name="heatmap", min_opacity=0.4,  max_val=1.0, radius=5, gradient={0.5:"blue", 0.75:"lime", 1:"red"}, overlay=True).add_to(heatmap)
    heatmap.save("mapas/heatmap_"+fecha+".html")


dicDias={}

f = open("puntos_fechas.csv")
f1 = f.readlines()

for line in f1:
    linea=line.split(",")
    dia = linea[0]
    carro=linea[1]
    lat = float(linea[2])
    lon = float(linea[3])
    if dia not in dicDias.keys():
        dicDias[dia] = []
        coordenadas = [lat,lon]
        c = dicDias[dia]
        c.append(coordenadas)
        dicDias[dia] = c
    else:
        coordenadas = [lat,lon]
        c = dicDias[dia]
        c.append(coordenadas)
        dicDias[dia] = c

print("Se terminó de leer archivo\n\n")
f.close()


for dia in dicDias.keys():
    print("Creando mapa...\n")
    puntos = dicDias[dia]
    crearHeatMap(dia, puntos)
    print("Se creó mapa de "+dia+"\n\n")