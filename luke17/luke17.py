import math
import numpy

def rotr(string, n):
  return string[n:] + string[:n]

def is_square(n):
  return n > -1 and math.sqrt(n) % 1 == 0

number = 0
nKvadrattall = numpy.array([], dtype=int)

for i in range(0,999999):
  #number = number + i
  #print(number)
  triangularNumber = int(i*(i+1)/2)

  for j in range (0,len(str(triangularNumber))):
        rotatedTriangle = int(rotr(str(triangularNumber), j))
        #if (int(math.sqrt(rotatedTriangle)+0.5)**2 == rotatedTriangle):
        if (is_square(rotatedTriangle)):
            print("Triangularnumber: ", triangularNumber)
            print("Perfekt square found: ", rotatedTriangle)
            #nKvadrattall += 1
            nKvadrattall = numpy.append(nKvadrattall, rotatedTriangle)
            break


print("Antall kvadrattall: ", numpy.size(nKvadrattall))
print("Kvadrattall: ", nKvadrattall)
print("Fiskekaker!")