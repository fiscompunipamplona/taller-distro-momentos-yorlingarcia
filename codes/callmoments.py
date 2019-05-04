import matplotlib.pyplot as plt
import numpy as np
from momento_yorlin import Momento
import bz2

###############################################################
# lee el archivo .bz2 y guarda la tercera columna de numeros
# teniendo en cuenta que solo lee las listas mayores a 2 columnas
n = 0
datos = []
with bz2.open( input ("Please, enter the filename: "), "rt" ) as bz_file:
    for line in bz_file:
        rline = line.rstrip('\n').split(' ')
        if len(rline) >= 3:
            if rline[0] != "#":
                datos.append(rline[2])
#        n += 1
#        if n == 60:
#            break
#print (datos)
################################################################
# valor minimo y maximo del arrreglo
aux1 = float (datos[0])
aux2 = float (datos[0])
aux3 = float (datos[0])
aux4 = 0

for i in range(len(datos)):
    if aux1 < float(datos[i]):
        aux1 = float(datos[i])
    if aux2 > float(datos[i]):
        aux2 = float(datos[i])

#print ("mayor: %0.4f, menor: %0.4f\n" %(aux1, aux2))
Datmin = aux2
Datmax = aux1

nbins = 100
binwidth = (Datmax - Datmin)/nbins 
###############################################################
#crear un histograma
hist1 = []
hist = []
pos = []
[hist1.append(0) for i in range(nbins)]
# convierte a datos en un arreglo tipo float
for i in range(len(datos)):
    datos[i]=float (datos[i])
# determina los valores del histograma
for i in datos:
    hist1[ int(i) ] += 1
# elimina la cantida de ceros del histograma
# teniendo en cuenta que un dato se repite almenos una vez
# es decir un dato existe una vez
for i in range(len(hist1)):
    if hist1[i] != 0:
        pos.append(i)
        hist.append(hist1[i])

#../data/Chitaga_2016_08_12_12h00.dat.bz2 #
outDisdat = open("datafile.dat","w")
outDisdat.write("# startbin %0.4f endbin %0.4f nbins %d\n" % (Datmin, Datmax, nbins))
for i in range(len(hist)):
    outDisdat.write('%0.2f  %0.2f\n' % (pos[i] ,hist[i]))
outDisdat.close()
#############################################################
inData = open("datafile.dat","r")
x = []
y = []
for i in inData:
    column = i.split()
    if column[0] != "#":
        x.append(float(column[0]))
        y.append(float(column[1]))        
mt = Momento()
inData = open("datafile.dat","r")
[media, N] = mt.momento1(inData)
#inData = open("datafile.dat","r")
sigma = mt.momento2(media, N)
mt.momento3(media, N, sigma)
mt.momento4(media, N, sigma)
# realiza la grafica del histograma
#plt.bar(x,y)
#plt.ylabel('frecuencia')
#plt.xlabel('clase')
#plt.title("histograma")
plt.step(x,y, where = 'mid', color = 'b', linewidth = 1)#une con saltos
#plt.plot(x,y)# une puntos con lineas
plt.xlabel('clase')
plt.ylabel('frecuencia')
plt.title('Histograma')
plt.show()

