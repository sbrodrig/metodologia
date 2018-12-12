import matplotlib.pyplot as plt
#funciones que calculan la media y la desviacion
def calcularMedia(trazasMes):                   #recibe una lista con todas las trazas/auto o trazas/dia de ese mes
    sum=0
    for factor in trazasMes:
        sum += factor
    return float(sum/len(trazasMes))            #retorna la media de las trazas/auto o trazas/dia de ese mes

def calcularDesviacion(trazasMes):              #recibe una lista con todas las trazas/auto o trazas/dia de ese mes
    sum=0
    for factor in trazasMes:
        trazacuadrada = factor*factor
        sum+= trazacuadrada
    med = float(sum/len(trazasMes))
    mediacuadrada = float(calcularMedia(trazasMes)*calcularMedia(trazasMes))
    varianza = med-mediacuadrada
    return pow(varianza, 0.5)                   #retorna la desviacion de las trazas/auto o trazas/dia de ese mes

# funcion de extraccion de puntos para las graficas(media y desviacion)
def extraerPuntos(diccionario):                 #recibe un diccionario
    dict = {}
    for metrica in diccionario.keys():
        media = calcularMedia(diccionario[metrica])
        desviacion = calcularDesviacion(diccionario[metrica])
        puntos = (media, desviacion)
        dict[metrica] = puntos
    return dict                                 #retorna un diccionario con clave (mes, anio) y valor (media, desviacion)


#analisis
dicCarros={}                                                            #clave el auto, valor diccionario con clave dia y valor lista de coordenadas(tupla)
dicDias={}                                                              #clave el dia, valor lista de las coordenadas(tupla)
dictTrazasDia={}
dictTrazasAuto={}
datasets=[]
archivo=open("../datasets/resultados1.csv")
archivo2=open("../datasets/resultados2.csv")
archivo3=open("../datasets/resultados3.csv")
archivo4=open("../datasets/resultados4.csv")
#archivo5=open("../datasets/resultados5.csv")

datasets.append(archivo)
datasets.append(archivo2)
datasets.append(archivo3)
datasets.append(archivo4)
#datasets.append(archivo5)

for file in datasets:
    for linea in file:
        if not linea.startswith("id"):                                  #no sea primera linea de los datasets
            linea=linea.split(",")
            carro=linea[0]
            fechaCompleta = linea[1]
            dia = fechaCompleta[:10]
            lat = float(linea[2])
            long = float(linea[3])
            velocidad = linea[4]
            if(velocidad != "\n"):                                      #campo velocidad no sea vacio
                velocidad = float(velocidad)
                if(velocidad > 0):                                      #velocidad no sea 0
                    if dia not in dicDias.keys():
                        dicDias[dia]=[]
                        coordenadas=(lat,long)
                        dicDias[dia].append(coordenadas)
                    else:
                        coordenadas = (lat, long)
                        dicDias[dia].append(coordenadas)

                    if carro not in dicCarros.keys():
                        dicCarros[carro]={}
                        carroActual= dicCarros[carro]
                        if dia not in carroActual.keys():
                            carroActual[dia] = []
                            coordenadas = (lat, long)
                            carroActual[dia].append(coordenadas)
                        else:
                            coordenadas = (lat, long)
                            carroActual[dia].append(coordenadas)
                    else:
                        carroActual = dicCarros[carro]
                        if dia not in carroActual.keys():
                            carroActual[dia] = []
                            coordenadas = (lat, long)
                            carroActual[dia].append(coordenadas)
                        else:
                            coordenadas = (lat, long)
                            carroActual[dia].append(coordenadas)
    file.close()

for auto in dicCarros.keys():
    print(auto)

print(len(dicCarros))                                                               #cantidad de autos

for dia in dicDias.keys():
    anio = int(dia[:4])
    mes = int(dia[5:7])
    if (anio,mes) not in dictTrazasDia.keys():
        dictTrazasDia[(anio,mes)]=[]
        dictTrazasDia[(anio,mes)].append(len(dicDias[dia]))
    else:
        dictTrazasDia[(anio,mes)].append(len(dicDias[dia]))

for auto in dicCarros.values():
    for dia in auto.keys():
        anio = int(dia[:4])
        mes = int(dia[5:7])
        if (anio,mes) not in dictTrazasAuto.keys():
            dictTrazasAuto[(anio,mes)]=[]
            dictTrazasAuto[(anio,mes)].append(len(auto[dia]))
        else:
            dictTrazasAuto[(anio,mes)].append(len(auto[dia]))

dictDiaMediciones=extraerPuntos(dictTrazasDia)
dictAutoMediciones=extraerPuntos(dictTrazasAuto)

print(dictAutoMediciones)
print(dictDiaMediciones)



media=[]
desviacion=[]
fecha=[]

x=list(dictAutoMediciones.keys())
y=list(dictAutoMediciones.values())

x.sort()

for i in y:
    media.append(i[0])
    desviacion.append(i[1])

for i in x:
    fecha.append(str(i[0])+"-"+str(i[1]))

fecha2=range(len(fecha))

plt.figure(1)
plt.plot(fecha2, media,label="Media")
plt.plot(fecha2,desviacion,label="Desviación Estandar")
plt.xticks(fecha2, fecha)
plt.legend()
plt.xlabel("Mes-Año")
plt.ylabel("Trazas por auto")



mediaDia=[]
desviacionDia=[]
fechaDia=[]

x=list(dictDiaMediciones.keys())
y=list(dictDiaMediciones.values())

x.sort()

for i in y:
    mediaDia.append(i[0])
    desviacionDia.append(i[1])

for i in x:
    fechaDia.append(str(i[0])+"-"+str(i[1]))

fechaDia2=range(len(fechaDia))

plt.figure(2)
plt.plot(fechaDia2, mediaDia,label="Media")
plt.plot(fechaDia2,desviacionDia,label="Desviación Estandar")
plt.xticks(fechaDia2, fechaDia)
plt.legend()
plt.xlabel("Mes-Año")
plt.ylabel("Trazas por día")

plt.show()


