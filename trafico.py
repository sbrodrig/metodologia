import math
from datetime import time,datetime
import folium
from folium.plugins import HeatMap


def calcularLos(speed):
    return int((0.151231*speed)+(0.636927*2)-2.17765)

def calcularDist(lat1,long1,lat2,long2):
    puntoA=69.1*(lat2-lat1)
    puntoB=69.1*(long2-long1)*math.cos(lat1/57.3)
    return math.sqrt(puntoA**2+puntoB**2)


def fechita(strHora):
    tiempo=strHora.split(":")
    hora=int(tiempo[0])
    min=int(tiempo[1])
    seg=int(tiempo[2][:2])
    hora2=datetime(1,1,1,hora,min,seg)
    return hora2

def calcularSpeed(dist,temp):
    return dist/temp*3.6


a="id;DateTime;Latitude;Longitude;Speed"
def quitarRepetidos(archivo):
    dic={}
    for linea in archivo:
        if not linea.startswith("id"):
            linea=linea.split(",")
            if linea[0] not in dic:
                dicCarro = {}
                coord = (linea[2],linea[3])
                dicCarro[coord] = [linea[1], linea[4]]
                dic[linea[0]] = dicCarro
            else:
                diccionario = dic[linea[0]]
                coor = (linea[2], linea[3])
                if coor not in diccionario:
                    diccionario[coor] = [linea[1], linea[4]]

    #escribir archivo sin repetidos
    for clave in dic.keys():
        dicA = dic[clave]





def cargarDatos(archivo):
    dic={}
    for linea in archivo:
        if not linea.startswith("id"):
            linea=linea.split(",")

            fechaC=linea[1][:10]

            fecha=fechaC.split("-")
            mes=fecha[1]

            if mes =="10":
                print(mes)
                fechaEntrada=fechaC
                horaEntrada=linea[1][11:]
                carro = linea[0]
                lat = float(linea[2])
                long = float(linea[3])
                if fechaEntrada not in dic.keys():
                    dic[fechaEntrada]={}
                    if carro not in dic[fechaEntrada].keys():
                        dic[fechaEntrada][carro]={}
                        dic[fechaEntrada][carro][horaEntrada]=(lat,long)
                    else:
                        dic[fechaEntrada][carro][horaEntrada] = (lat, long)
                else:
                    if carro not in dic[fechaEntrada].keys():
                        dic[fechaEntrada][carro]={}
                        dic[fechaEntrada][carro][horaEntrada]=(lat,long)
                    else:
                        dic[fechaEntrada][carro][horaEntrada] = (lat, long)
    return dic

def puntosDeTrafico(diccionario):
    dicc={}
    for fecha in diccionario.keys():

        for carro in diccionario[fecha].keys():
            horas=diccionario[fecha][carro].keys()
            horas=list(horas)
            horas.sort()

            for i in range (1,len(horas)):
                horai=horas[i-1]
                horaf=horas[i]

                tuplai=diccionario[fecha][carro][horai]
                tuplaf=diccionario[fecha][carro][horaf]
                taim=(fechita(horaf)-fechita(horai)).seconds
                #print(taim)
                dista=calcularDist(tuplai[0],tuplai[1],tuplaf[0],tuplaf[1])
                #print(dista)
                spid=calcularSpeed(dista,taim)
                #print(spid)
                los=calcularLos(spid)
                #print(los)
                if los <=1:
                    if fecha not in dicc.keys():
                        dicc[fecha]=[]
                        dicc[fecha].append(list(tuplai))
                        dicc[fecha].append(list(tuplaf))

                    else:
                        dicc[fecha].append(list(tuplai))
                        dicc[fecha].append(list(tuplaf))
    return dicc

def crearHeatMap(fecha, data):
    heatmap = folium.Map(location=[-2.176049, -79.919096], zoom_start=12)
    HeatMap(data, name="heatmap", min_opacity=0.4,  max_val=1.0, radius=5, gradient={0.5:"blue", 0.75:"lime", 1:"red"}, overlay=True).add_to(heatmap)
    heatmap.save(fecha+".html")



archivo=open("../datasets/oct (2).csv")
datoscargados=cargarDatos(archivo)
print(datoscargados)
puntos=puntosDeTrafico(datoscargados)
archivo.close()
for dia in puntos.keys():
    crearHeatMap(dia,puntos[dia])






