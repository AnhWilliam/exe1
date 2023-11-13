import cv2
from PIL import Image
import numpy as np

filehinh = r'lena_colour.png'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)

KX = Image.new(imgPIL.mode, imgPIL.size)
KY = Image.new(imgPIL.mode, imgPIL.size)
KZ= Image.new(imgPIL.mode, imgPIL.size)
KXYZimg = Image.new(imgPIL.mode, imgPIL.size)

width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        pixel_values = imgPIL.getpixel((x, y))
        R = pixel_values[0]
        G = pixel_values[1]
        B = pixel_values[2]
        
        X=np.uint8(R * 0.4124564 + G * 0.3575761 + B * 0.1804375)
        Y=np.uint8(R * 0.2126729 + G * 0.7151522 + B * 0.0721750)
        Z=np.uint8(R * 0.0193339 + G * 0.1191920 + B * 0.9503041)
        
        KX.putpixel((x,y), (X, X, X))
        KY.putpixel((x,y), (Y, Y, Y))
        KZ.putpixel((x,y), (Z, Z, Z))
        KXYZimg.putpixel((x,y),(Z,Y,X))

anhX = np.array(KX)
anhY = np.array(KY)
anhZ = np.array(KZ)
anhXYZ = np.array(KXYZimg)
cv2.imshow('Kenh X', anhX)
cv2.imshow('Kenh Y', anhY)
cv2.imshow('Kenh Z', anhZ)
cv2.imshow('Kenh XYZ', anhXYZ)
cv2.waitKey(0)
cv2.destroyAllWindows