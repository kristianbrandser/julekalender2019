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