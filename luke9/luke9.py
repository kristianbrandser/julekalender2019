import math
import numpy
import unittest

#https://julekalender.knowit.no/doors/ck3vosq73cw370109qnk7nu17

# Et Krampustall er definert som et tall n der produktet av n*n (n2) kan splittes i to tall a og b, 
# hvor a+b = n (a og b trenger ikke ha like mange siffer, 
# splitten kan altså være ujevn). 
# I tillegg kan ingen av tallene kan være 0.

testkrampusTallrekke = numpy.array([45, 100, 53219, 74742, 11502, 27846, 6834, 38442, 60767, 45])
krampusTallrekke = numpy.loadtxt("luke9/krampus.txt", dtype=int)
sumKrampus = 0

def isKrampus(n):
    n2 = n*n
    #ndigits = int(math.log10(n2)+1)
    ndigits = len(str(n2))  
       
    for nn in range(1,ndigits+1):
        a = int(n2/(10**nn))
        b = int(n2%(10**nn))
        if (a+b == n and a != 0 and b != 0):
            print("Fant krampustall: " + str(n))
            return True
    else: 
        return False
    
for n in krampusTallrekke:
    if (isKrampus(n)):
        sumKrampus += n

print("Sum av krampustall: " + str(sumKrampus))

class krampusTest(unittest.TestCase):
    def testKrampetall(self):
        self.assertEqual(isKrampus(45), True)
    def testEdgeKrampe(self):
        self.assertEqual(isKrampus(100), False)
        self.assertEqual(isKrampus(0), False)
    def testIkkeKrampetall(self):
        self.assertEqual(isKrampus(53219), False)

if __name__ == '__main__':
    unittest.main()