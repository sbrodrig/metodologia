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
dictVelocidad={}
dictHorarias={}
dictHorariasMediciones={}
dictMesVariable={}
dictMesVariableMediciones={}
datasets=[]
archivo=open("../datasets/oct.csv")
archivo2=open("../datasets/nov.csv")
archivo3=open("../datasets/dic.csv")
archivo4=open("../datasets/nov_otros.csv")
archivo5=open("../datasets/dic_otros.csv")

datasets.append(archivo)
datasets.append(archivo2)
datasets.append(archivo3)
datasets.append(archivo4)
datasets.append(archivo5)


for file in datasets:
    for linea in file:
        if not linea.startswith("id"):                                  #no sea primera linea de los datasets
            linea=linea.split(",")
            carro=linea[0]
            fechaCompleta = linea[1]
            fecha = fechaCompleta[:10]
            lat = float(linea[2])
            long = float(linea[3])
            velocidad = linea[4]
            anio = int(fecha[:4])
            mes = int(fecha[5:7])
            dia= int(fecha[8:10])
            hora=int(fechaCompleta[11:13])
            if(velocidad != "\n"):                                     #campo velocidad no sea vacio
                velocidad = float(velocidad)

                if (hora >= 0 and hora <6):
                    if(anio,mes,"0 a 6") not in dictHorarias.keys():
                        dictHorarias[(anio, mes,"0 a 6")] = []
                        dictHorarias[(anio, mes,"0 a 6")].append(velocidad)
                    else:
                        dictHorarias[(anio, mes,"0 a 6")].append(velocidad)
                elif (hora>5 and hora <12):
                    if (anio, mes,"6 a 12") not in dictHorarias.keys():
                        dictHorarias[(anio, mes,"6 a 12")] = []
                        dictHorarias[(anio, mes,"6 a 12")].append(velocidad)
                    else:
                        dictHorarias[(anio, mes,"6 a 12")].append(velocidad)
                elif (hora>11 and hora <18):
                    if (anio, mes,"12 a 18") not in dictHorarias.keys():
                        dictHorarias[(anio, mes,"12 a 18")] = []
                        dictHorarias[(anio, mes,"12 a 18")].append(velocidad)
                    else:
                        dictHorarias[(anio, mes,"12 a 18")].append(velocidad)
                elif (hora>17 and hora <=23):
                    if (anio, mes,"18 a 0") not in dictHorarias.keys():
                        dictHorarias[(anio, mes,"18 a 0")] = []
                        dictHorarias[(anio, mes,"18 a 0")].append(velocidad)
                    else:
                        dictHorarias[(anio, mes,"18 a 0")].append(velocidad)

                if mes==10:
                    if dia not in dictMesVariable.keys():
                        dictMesVariable[dia]=[]
                    else:
                        dictMesVariable[dia].append(velocidad)


                if (anio, mes) not in dictVelocidad.keys():
                    dictVelocidad[(anio, mes)] = []
                    dictVelocidad[(anio, mes)].append(velocidad)
                else:
                    dictVelocidad[(anio, mes)].append(velocidad)


                if fecha not in dicDias.keys():
                        dicDias[fecha]=[]
                        coordenadas=(lat,long)
                        dicDias[fecha].append(coordenadas)
                else:
                        coordenadas = (lat, long)
                        dicDias[fecha].append(coordenadas)

                if carro not in dicCarros.keys():
                        dicCarros[carro]={}
                        carroActual= dicCarros[carro]
                        if fecha not in carroActual.keys():
                            carroActual[fecha] = []
                            coordenadas = (lat, long)
                            carroActual[fecha].append(coordenadas)
                        else:
                            coordenadas = (lat, long)
                            carroActual[fecha].append(coordenadas)
                else:
                        carroActual = dicCarros[carro]
                        if fecha not in carroActual.keys():
                            carroActual[fecha] = []
                            coordenadas = (lat, long)
                            carroActual[fecha].append(coordenadas)
                        else:
                            coordenadas = (lat, long)
                            carroActual[fecha].append(coordenadas)
    file.close()

for auto in dicCarros.keys():
    print(auto)

print(len(dicCarros))                                                               #cantidad de autos

dictValidarAutos={}
for auto in dicCarros.keys():
    for dia,valor in dicCarros[auto].items():
        anio = int(dia[:4])
        mes = int(dia[5:7])
        if auto not in dictValidarAutos.keys():
            dictValidarAutos[auto]=[]
            dictValidarAutos[auto].append((anio, mes))
        if (anio,mes) not in dictValidarAutos[auto]:
            dictValidarAutos[auto].append((anio,mes))

print(dictValidarAutos)

totalcomunes=0
for lista in dictValidarAutos.values():
    if len(lista)==3:
        totalcomunes+=1
print(totalcomunes)

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
dictVeloMediciones=extraerPuntos(dictVelocidad)
dictHorariasMediciones=extraerPuntos(dictHorarias)
dictMesVariableMediciones=extraerPuntos(dictMesVariable)

print(dictAutoMediciones)
print(dictDiaMediciones)
print(dictVeloMediciones)
print(dictHorariasMediciones)
print(dictMesVariableMediciones)





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
plt.xlabel("Año-Mes")
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
plt.xlabel("Año-Mes")
plt.ylabel("Cantidad de tramas")


mediav=[]
desviacionv=[]
fechav=[]

x=list(dictVeloMediciones.keys())
y=list(dictVeloMediciones.values())

x.sort()

for i in y:
    mediav.append(i[0])
    desviacionv.append(i[1])

for i in x:
    fechav.append(str(i[0])+"-"+str(i[1]))

fechav2=range(len(fechav))

plt.figure(3)
plt.plot(fechav2, mediav,label="Media")
plt.plot(fechav2,desviacionv,label="Desviación Estandar")
plt.xticks(fechav2, fechav)
plt.legend()
plt.xlabel("Año-Mes")
plt.ylabel("Velocidad")

media=[]
desviacion=[]
fecha=[]

x=list(dictHorariasMediciones.keys())
y=list(dictHorariasMediciones.values())

x.sort()

for i in y:
    media.append(i[0])
    desviacion.append(i[1])

for i in x:
    fecha.append(str(i[0])+"-"+str(i[1])+"-"+str(i[2]))

fecha2=range(len(fecha))

plt.figure(4)
plt.plot(fecha2, media,label="Media")
plt.plot(fecha2,desviacion,label="Desviación Estandar")
plt.xticks(fecha2, fecha)
plt.legend()
plt.xlabel("Horario-Año-Mes")
plt.ylabel("Velocidad")

media=[]
desviacion=[]
fecha=[]

x=list(dictMesVariableMediciones.keys())
print(x)
y=list(dictMesVariableMediciones.values())

x.sort()

for i in y:
    media.append(i[0])
    desviacion.append(i[1])

for i in x:
    fecha.append(str(i))

fecha2=range(len(fecha))

plt.figure(5)
plt.plot(fecha2, media,label="Media")
plt.plot(fecha2,desviacion,label="Desviación Estandar")
plt.xticks(fecha2, fecha)
plt.legend()
plt.xlabel("Octubre 2018")
plt.ylabel("Velocidad")


plt.show()

