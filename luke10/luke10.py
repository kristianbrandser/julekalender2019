import numpy

#https://julekalender.knowit.no/doors/ck3yevkngdqko0109dffrev8n
# Tannkremen kommer i tuber på 125 milliliter.
# Sjampoen kommer i flasker på 300 milliliter.
# Toalettpapiret kommer på ruller på 25 meter.

# Svaret vi skal frem til er produktet av følgende 5 tall:
# Antall hele tuber tannkrem brukt i 2018.
# Antall hele flasker sjampo brukt i 2018.
# Antall hele toalettruller brukt i 2018.
# Antall milliliter sjampo brukt på søndager.
# Antall meter toalettpapir brukt på onsdager.

f = open('luke10/logg.txt', 'r')
loggTxt = f.readlines()
f.close()

loggListNp = numpy.loadtxt("luke10/logg.txt", dtype=int)
#print(loggTxt)

#Add to start ["dato", "tannkrem", "sjampo", "toalettpapir"]
#loggList = numpy.zeros((1462,4),dtype=str)
loggList = ["dato", ["tannkrem", "sjampo", "toalettpapir"]]
print(loggListNp)

for element in range(len(loggTxt)):
    if (loggTxt[element].find(":")!=-1):
        #loggList.append(loggTxt[element][0:6])
        dato = loggTxt[element][0:6]
        tannkrem = " ml tannkrem"
        sjampo = " ml sjampo"
        toalettpapir = " meter toalettpapir"
        print(element, dato, tannkrem, sjampo, toalettpapir)
    
