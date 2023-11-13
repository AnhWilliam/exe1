import cv2
from PIL import Image
import numpy as np

filehinh = r'C:\Users\Admin\Documents\New folder\lena_colour.png'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)

Y= Image.new(imgPIL.mode, imgPIL.size)
Cr = Image.new(imgPIL.mode, imgPIL.size)
Cb = Image.new(imgPIL.mode, imgPIL.size)
YCrCbimg = Image.new(imgPIL.mode, imgPIL.size)

width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(width):
    for y in range(height):
        pixel_values = imgPIL.getpixel((x, y))
        R = pixel_values[0]
        G = pixel_values[1]
        B = pixel_values[2]
        
        ky=np.uint8(16 + (65.738*R/256) + (129.057*G/256) + (25.064*B/256))
        kCr=np.uint8(128 - (37.945*R/256) - (74.494*G/256) + (112.439*B/256))
        kCb=np.uint8(128 + (112.439*R/256) - (94.154*G/256) - (18.285*B/256))
        
        Y.putpixel((x,y), (ky, ky, ky))
        Cr.putpixel((x,y), (kCr, kCr, kCr))
        Cb.putpixel((x,y), (kCb, kCb, kCb))
        YCrCbimg.putpixel((x,y),(kCb,kCr,ky))

anhY = np.array(Y)
anhCr = np.array(Cr)
anhCb = np.array(Cb)
anhCrCb = np.array(YCrCbimg)
cv2.imshow('Kenh Y', anhY)
cv2.imshow('Kenh Cr', anhCr)
cv2.imshow('Kenh Cb', anhCb)
cv2.imshow('Kenh YCrCb', anhCrCb)
cv2.waitKey(0)
cv2.destroyAllWindows