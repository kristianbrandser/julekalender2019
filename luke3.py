import numpy as np
from PIL import Image
import io
import textwrap


print("Hell world!")

#Antar A4 format, ratio 1,1414, vi vet summen av pixels, 720720, regner oss frem til at
#dimensjonene mes sannsnynligvis er 906 x 795
imageWidth = 906
imageHeight = 795

f = open("luke3-img.txt", "r")
flatpakke = f.read()
f.close

wrapper = textwrap.TextWrapper(width=imageWidth)
pakkeTekst = wrapper.wrap(flatpakke)

pakkefil = open("luke3-img-pakke.txt","w+")
pakkefil.writelines(pakkeTekst)
#pakkefil.close

#TODO: Lage bilde ut i fra wrappet tekst

array2d = np.zeros([imageHeight, imageWidth], dtype=np.uint8)





#print(len(pakkeTekst))
#print(len(pakkeTekst[0]))
#print(pakkeTekst[0][3])

img = Image.new(mode = "RGB", size = (imageWidth, imageHeight), color = "black" ) 



for x in range (imageWidth):
    for y in range (imageHeight):
        if ((pakkeTekst[y])[x]) == "1":
           img.putpixel( (x,y), (240,240,240))


img.show()
img.save("luke3-img-pakke.png")
img.close()

pakkefil.close()
