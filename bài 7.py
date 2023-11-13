import cv2
import numpy as np
from PIL import Image
import math

def ChuyenDoiRGBSangHSI(imgPIL):
    Hue = Image.new(imgPIL.mode, imgPIL.size)
    Saturation = Image.new(imgPIL.mode, imgPIL.size)
    Intensity = Image.new(imgPIL.mode, imgPIL.size)
    HSIImg = Image.new(imgPIL.mode, imgPIL.size)

    width = imgPIL.size[0]
    heigh = imgPIL.size[1]

    for x in range(width):
        for y in range(heigh):
            R, G, B = imgPIL.getpixel((x,y))
            
            if R == 0 and G == 0 and B == 0 and (R-G)*(R-G)+(R-B)*(G-B) == 0:
                Hue.putpixel((x, y), (0, 0, 0))
                Saturation.putpixel((x, y), (0, 0, 0))
                Intensity.putpixel((x, y), (0, 0, 0))
                HSIImg.putpixel((x, y), (0, 0, 0))
            else:
            
                t1 = ((R-G)+(R-B))/2
                t2 = math.sqrt(((R-G)*(R-G)+(R-B)*(G-B)))
                if t2 != 0:
                    t = t1/t2
                    theta = math.acos(t)

                    H = 0
                    if (B <= G):
                        H = theta
                    else:
                        H = 2*math.pi - theta
                
                H = np.uint8(H*180/math.pi)

                Min = min(R,G,B)
                S = 1 -3*Min/(R+G+B)
                S = np.uint8(S*255)

                I = np.uint8((R+G+B)/3)
                
                Hue.putpixel((x,y),(H,H,H))
                Saturation.putpixel((x,y), (S,S,S))
                Intensity.putpixel((x,y),(I,I,I))
                HSIImg.putpixel((x,y),(I, S, H))

    HueRGB = np.array(Hue)
    SatRGB = np.array(Saturation)
    InRGB = np.array(Intensity) 
    HSIRGB = np.array(HSIImg)

    return HueRGB, SatRGB, InRGB, HSIRGB

link = r'lena_colour.png'
img = cv2.imread(link,cv2.IMREAD_COLOR)
imgPIL = Image.open(link)
imgPIL = imgPIL.convert('RGB')


Hue, Saturation, Intensity, HSIImg = ChuyenDoiRGBSangHSI(imgPIL)

cv2.imshow('RGB_original', img)
cv2.imshow('Hue',Hue)
cv2.imshow('Saturation', Saturation)
cv2.imshow('Intensity',Intensity)
cv2.imshow('HSIImg', HSIImg)

cv2.waitKey(0)
cv2.destroyAllWindows()