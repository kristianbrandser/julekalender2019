#https://julekalender.knowit.no/doors/ck3q4m03ubk5y0109bquxtumd

import numpy
import csv #https://stackoverflow.com/questions/24662571/python-import-csv-to-list
with open('luke4/testcoords.csv', 'r') as f:
    reader = csv.reader(f)
    skattekart = list(reader)
    f.close()

skattekart.pop(0) #Remove header row
skattekart = numpy.array(skattekart,dtype=int) #parse to numpy-array with ints
kvadratahara = numpy.zeros((3,2),dtype=int) #map (possible with slime column)
currentpos = numpy.array([0,0],dtype=int)
#slimetracks - holds info om slimebuildup
#moves - holds info on path

totaltimetofindtreasure = 0
totalmovestofindtreasure = 0

# Så lenge vi ikke har funnet skatten
    #sett neste skattekartsteg
    #gå til rett x koordinat
    #oppdater antall steg
        #absolutt forskjell i x-verdi mellom steg og nåværende posisjon
    #oppdater tidbrukt på strekke
        #sjekk om det er slim på veien
    #oppdater slimspor
        #økt slik på hver av koordinatene passer med +=1

    #gå til rett y koordinat
    #oppdater antall steg
    #oppdater tidbrukt på strekke
    #oppdater slimspor

    #//oppdater skattekart steg som besøkt    
    #gå til neste skattekart steg

    #siste skattekart steg ? profit!
    


for i in range(len(skattekart)):
    #while(numpy.array_equiv(currentpos[0],skattekart[i])):
     #Not at treasuremapstep yet, need to move
     #kan anteglivis gjøre dette mye enklere med vektor-mattematikk. 
     #Obs. må sjekke etter slimspor på veien (ved kalkulering av tid ihverfall)
     #Obs2. må legge fra seg slimspor underveis
        #hvis x-verdi av currentpos < x-verdi av gjeldende skattekart steg go east
            #Deposit slime
            ##kvadratahara.add(currentpos,1)
            #totalmoves += 1
            #oppdater tid brukt
            #Oppdater current pos
            #currentpos[0] += 1
        #hvis x-verdi av currentpos 
    print(skattekart[i])

print(currentpos)  
print(kvadratahara)