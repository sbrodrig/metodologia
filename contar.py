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
archivo=open("datasets/resultados1.csv")
archivo2=open("datasets/resultados2.csv")
archivo3=open("datasets/resultados3.csv")
archivo4=open("datasets/resultados4.csv")
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
    if (mes,anio) not in dictTrazasDia.keys():
        dictTrazasDia[(mes,anio)]=[]
        dictTrazasDia[(mes,anio)].append(len(dicDias[dia]))
    else:
        dictTrazasDia[(mes, anio)].append(len(dicDias[dia]))

for auto in dicCarros.values():
    for dia in auto.keys():
        anio = int(dia[:4])
        mes = int(dia[5:7])
        if (mes, anio) not in dictTrazasAuto.keys():
            dictTrazasAuto[(mes, anio)]=[]
            dictTrazasAuto[(mes, anio)].append(len(auto[dia]))
        else:
            dictTrazasAuto[(mes, anio)].append(len(auto[dia]))

dictDiaMediciones=extraerPuntos(dictTrazasDia)
dictAutoMediciones=extraerPuntos(dictTrazasAuto)

print(dictAutoMediciones)
print(dictDiaMediciones)

