from PIL import Image, ImageFilter
import numpy

#https://julekalender.knowit.no/doors/ck3r9zcm6bu7d0109solzlvjy

#Eit bilete på 1 x 5 pixlar
#[[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]]

#vil bli obfuskert til

#[[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]]


testmushImageArray =numpy.asarray([[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]])
testwishImageArray = numpy.asarray([[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]])
#add 0,0,0 as first pixel in mush-array and shift-left
#testmushImageArrayShifted = numpy.asarray([[0,0,0], [240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160]])
#testmushImageArrayShifted = numpy.insert(testmushImageArray, 0,0,0)
#testmushImageArrayShifted = testmushImageArrayShifted[:-1].copy()
testmushImageArrayShifted = numpy.roll(testmushImageArray,1, axis=(0))
print(testmushImageArrayShifted)
#test magic
testXORedImageArray = numpy.bitwise_xor(testmushImageArray, testmushImageArrayShifted)
if (numpy.array_equal(testwishImageArray, testXORedImageArray)):
    print("Succcess in reverse XOR numpy test arrays")


mushImage = Image.open("luke6/mush.png")
#mushImage.show()
mushImageArray = numpy.array(mushImage)
mushImage.close()

#For SSC
#numpy.savetxt("luke6/mush.csv", mushImageArray.flatten(),delimiter=',')

#mushImageArrayShifted = numpy.insert(mushImageArray, 0,0,0)
#mushImageArrayShifted = mushImageArrayShifted[:-1].copy()
mushImageArrayShifted = numpy.roll(mushImageArray,1, axis=(1))

#do magic
XORedImageArray = numpy.bitwise_xor(mushImageArray, mushImageArrayShifted)

wishImage = Image.fromarray(XORedImageArray)
wishImage.save("luke6/wish.png")
wishImage.close()

##PSEUDOCODE
#Les inn mushedimage og map til numpy
#Gjør invers XOR (XOR) på numpy med pixlene
#Lagre unobfuscated image