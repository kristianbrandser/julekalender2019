from PIL import Image, ImageFilter
import numpy

#https://julekalender.knowit.no/doors/ck3r9zcm6bu7d0109solzlvjy

#Eit bilete på 1 x 5 pixlar
#[[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]]

#vil bli obfuskert til

#[[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]]

testmushImageArray =numpy.asarray([[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]])
testwishImageArray = numpy.asarray([[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]])
#testwishImage = Image.fromarray(testwishImageArray)
#testwishImage.save("luke6/testwish.png")
testmushImageArray.bitwise_xor()


mushImage = Image.open("luke6/mush.png")
#mushImage.show()
mushArray = numpy.array(mushImage)
mushImage.close()

#wishImage = Image.new(mode = "RGB", size = mushImage.size, color = "black" ) 
wishArray = numpy.array(mushArray)
numpy.savetxt("luke6/mush.csv", mushArray.flatten(),delimiter=',') #for SSC
#wishArray.bitwise_xor()

wishImage = Image.fromarray(wishArray)
wishImage.save("luke6/wish.png")
wishImage.close()
#https://www.mathworks.com/matlabcentral/answers/222730-how-to-encrypt-and-decrypt-rgb-image-using-logical-xor-operation
#EncryptedImage = bitxor(FirstImage, SecondImage);

#https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.bitwise_xor.html

#https://pillow.readthedocs.io/en/stable/reference/ImageChops.html#PIL.ImageChops.logical_xor

#Les inn mushedimage og map til numpy
#Gjør invers XOR (XOR) på numpy med pixlene
#Lagre unobfuscated image
