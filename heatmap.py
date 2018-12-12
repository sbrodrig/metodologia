import csv
import pandas as pd 
import folium
from folium.plugins import HeatMap

def crearHeatMap(fecha, data):
    heatmap = folium.Map(location=[-2.176049, -79.919096], zoom_start=10)
    HeatMap(data, name="heatmap", min_opacity=0.4,  max_val=1.0, radius=20, gradient={0.5:"blue", 0.75:"lime", 1:"red"}, overlay=True).add_to(heatmap)
    heatmap.save("mapas/heatmap_"+fecha+".html")


#analisis
dicDias={}                                                              #clave el dia, valor lista de las coordenadas(tupla)
datasets=[]
archivo=open("../datasets/resultados1.csv")
archivo2=open("../datasets/resultados2.csv")
archivo3=open("../datasets/resultados3.csv")
archivo4=open("../datasets/resultados4.csv")
datasets.append(archivo)
datasets.append(archivo2)
datasets.append(archivo3)
datasets.append(archivo4)

for file in datasets:
    for linea in file:
        if not linea.startswith("id"):                                  #no sea primera linea de los datasets
            linea=linea.split(",")
            carro=linea[0]
            fechaCompleta = linea[1]
            dia = fechaCompleta[:10]
            lat = float(linea[2])
            lon = float(linea[3])
            velocidad = linea[4]
            if(velocidad != "\n"):                                      #campo velocidad no sea vacio
                velocidad = float(velocidad)
                if(velocidad > 0):                                      #velocidad no sea 0
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

    file.close()

dias = []                                                                                   #arreglo con las fechas 
for dia in dicDias.keys():
    dias.append(dia)
    puntos = dicDias[dia]
    new_puntos = []
    for s in puntos:
        if s not in new_puntos:
            new_puntos.append(s)
    dicDias[dia] = new_puntos

#heatmaps
for i in range(3):
    fecha=dias[i]
    print(fecha+"\n")
    puntos = dicDias[fecha]
    crearHeatMap(fecha, puntos)


