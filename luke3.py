from PIL import Image
import io
import textwrap


print("Hell world!")

#Antar A4 format for det har jo tegningene på IKEA, ratio 1,414, vi vet antall pixels (chars), 720720, regner oss frem til at
#dimensjonene  sannsnynligvis er 1009 x 714
imageWidth = 1009
imageHeight = 714


f = open("luke3-img2.txt", "r")
flatpakke = f.read()
f.close

print ("Antall pixler: " + str(imageHeight*imageWidth) + "(" + str(imageWidth) + "x" + str(imageHeight) + "), Antall tegn: " + str(len(flatpakke)))
#wrappe kick-ass lang streng til stringliste basert på antall pixler i bredden
wrapper = textwrap.TextWrapper(width=imageWidth)
pakkeTekst = wrapper.wrap(flatpakke)

pakkefil = open("luke3-img-pakke.txt","w+")
pakkefil.writelines(pakkeTekst)
pakkefil.close

print(len(pakkeTekst))
print(len(pakkeTekst[0]))
print(pakkeTekst[0][3]) #Y

img = Image.new(mode = "RGB", size = (imageWidth, imageHeight), color = "black" ) 



for x in range (imageWidth):
    for y in range (imageHeight):
        if ((pakkeTekst[y])[x]) == "1":
           img.putpixel( (x,y), (240,240,240))


img.show()
img.save("luke3-img-pakke.png")
img.close()
