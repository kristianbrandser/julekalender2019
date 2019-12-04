#https://julekalender.knowit.no/doors/ck3q4m03ubk5y0109bquxtumd

import numpy
import csv #https://stackoverflow.com/questions/24662571/python-import-csv-to-list
with open('luke4/testcoords.csv', 'r') as f:
    reader = csv.reader(f)
    skattekart = list(reader)
    f.close()

skattekart.pop(0) #Remove header row
skattekart = numpy.array(skattekart,dtype=int) #parse to numpy-array with ints
kvadratahara = numpy.zeros((3,3),dtype=int)
currentpos = numpy.array([0,0],dtype=int)

timetofindtreasure = 0
totalmoves = 0

for i in range(len(skattekart)):
    while(numpy.array_equiv(currentpos[0],skattekart[i])):
     #Not at treasuremapstep yet, need to move
        if (currentpos[0]<i[0]): #go east
            #Deposit slime
            kvadratahara.add(currentpos,1)
            totalmoves += 1
            currentpos[0] += 1

    #if (currentpos)    
    print(i)

print(currentpos)  
print(kvadratahara)