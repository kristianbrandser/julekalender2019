from PIL import Image
import io
import textwrap


print("Knowit Julekalender 2019 - Luke3")

#Antar A4 format for det har jo tegningene på IKEA, ratio 1:1.4142, vi vet antall pixels (chars), 720720, regner oss frem til at
#dimensjonene  sannsnynligvis er ca. 1009 x 714
#SQRT (720720/1,4142). => Minste lengde er 714. lengste er 714*1,4142
#imageWidth = 1009
#imageHeight = 714

imageWidth =  715 #715 <- Rett antall pxler og gir oss bokstaver...
imageHeight = 1008 #1008 

#Fasit; 1287x560
imageWidth =  1287 
imageHeight = 560 

f = open("luke3/luke3-img2.txt", "r")
flatpakke = f.read()
f.close

print ("Antall pixler: " + str(imageHeight*imageWidth) + "(" + str(imageWidth) + "x" + str(imageHeight) + "), Antall tegn: " + str(len(flatpakke)))
#wrappe kick-ass lang streng til stringliste basert på antall pixler i bredden
wrapper = textwrap.TextWrapper(width=imageWidth)
pakkeTekst = wrapper.wrap(flatpakke)

pakkefil = open("luke3/luke3-img-pakke.txt","w+")
pakkefil.writelines(pakkeTekst)
pakkefil.close

print(len(pakkeTekst))
print(len(pakkeTekst[0]))
print(pakkeTekst[0][3]) #Test av parsing, skal være Y

img = Image.new(mode = "RGB", size = (imageWidth, imageHeight), color = "black" ) 



for x in range (imageWidth):
    for y in range (imageHeight):
        if ((pakkeTekst[y])[x]) == "1":
           img.putpixel( (x,y), (240,240,240))


img.show()
img.save("luke3/luke3-img-pakke.png")
img.close()
