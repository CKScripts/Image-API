import urllib.request
import os
from PIL import Image
from fastapi import FastAPI

App = FastAPI()

@App.get("/")
def read_root():
    return {"Hello": "World"}

ImageName = "Test.png"
ImageURL = "https://forecast.weather.gov/wwamap/png/US.png"

LoadingImage = urllib.request.urlretrieve(ImageURL,ImageName)
FullImage = Image.open(ImageName)
FullImageRGB = FullImage.convert("RGB")
FullImageSize = FullImageRGB.size

PixelData = {}

os.remove(ImageName)
#print("Processing image, this may take a few minutes.")

for X in range(FullImageSize[0]):
    for Y in range(FullImageSize[1]):
        #print("({XValue},{YValue}) = {PixelValue}".format(XValue = X,YValue = Y,PixelValue = FullImageRGB.getpixel((X,Y))))
        PixelData[X,Y] = FullImageRGB.getpixel((X,Y))

#print("Finished! Pixel Data: {PixelTable}".format(PixelTable = PixelData))