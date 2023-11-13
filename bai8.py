import cv2
from PIL import Image
import numpy as np
import math

def ChuyenDoiRGBSangHSI(imgPIL):
    Hue = Image.new(imgPIL.mode, imgPIL.size)
    Saturation = Image.new(imgPIL.mode, imgPIL.size)
    Value = Image.new(imgPIL.mode, imgPIL.size)
    HSV = Image.new(imgPIL.mode, imgPIL.size)

    width = imgPIL.size[0]
    heigh = imgPIL.size[1]

    for x in range(width):
        for y in range(heigh):
            R, G, B = imgPIL.getpixel((x,y))
            
            if R == 0 and G == 0 and B == 0 and (R-G)*(R-G)+(R-B)*(G-B) == 0:
                Hue.putpixel((x, y), (0, 0, 0))
                Saturation.putpixel((x, y), (0, 0, 0))
                Value.putpixel((x, y), (0, 0, 0))
                HSV.putpixel((x, y), (0, 0, 0))
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
                V = np.uint8(max(R,G,B))
                
                Hue.putpixel((x,y),(H,H,H))
                Saturation.putpixel((x,y), (S,S,S))
                Value.putpixel((x,y),(V,V,V))
                HSV.putpixel((x,y),(V, S, H))

    HueRGB = np.array(Hue)
    SaturationRGB = np.array(Saturation)
    ValueRGB = np.array(Value) 
    HSVRGB= np.array(HSV)
    return HueRGB, SaturationRGB, ValueRGB, HSVRGB


filehinh = r'lena_colour.png'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)
imgPIL = imgPIL.convert('RGB')

Hue, Saturation, Value, HSVImg = ChuyenDoiRGBSangHSI(imgPIL)























cv2.imshow('RGB_original', img)
cv2.imshow('Hue', Hue)
cv2.imshow('Saturation', Saturation)
cv2.imshow('Value', Value)
cv2.imshow('HSVImg', HSVImg)
cv2.waitKey(0)
cv2.destroyAllWindows
