
import cv2
from PIL import Image
import numpy as np

filehinh = r'C:\Users\Admin\Documents\New folder\lena_colour.png'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)

Smoothed3 = Image.new(imgPIL.mode, imgPIL.size)
Smoothed5 = Image.new(imgPIL.mode, imgPIL.size)
Smoothed7= Image.new(imgPIL.mode, imgPIL.size)
Smoothed9 = Image.new(imgPIL.mode, imgPIL.size)

width = imgPIL.size[0]
height = imgPIL.size[1]

for x in range(1,width):
    for y in range(1,height-1):
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-1, x+2):
            for j in range(y-1,y+2):
                if 0 <= i < width and 0 <= j < height:
                    pixel_values = imgPIL.getpixel((i, j))
                    R = pixel_values[0]
                    G = pixel_values[1]
                    B = pixel_values[2]

                    Rs += R
                    Gs += G
                    Bs += B
        K = 3*3 
        Rs = int(Rs/K)
        Gs = int(Gs/K)
        Bs = int(Bs/K)
        Smoothed3.putpixel((x,y),(Bs,Gs,Rs))


for x in range(2,width):
    for y in range(2,height-2):
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-2, x+3):
            for j in range(y-2,y+3):
                if 0 <= i < width and 0 <= j < height:
                    pixel_values = imgPIL.getpixel((i, j))
                    R = pixel_values[0]
                    G = pixel_values[1]
                    B = pixel_values[2]

                    Rs += R
                    Gs += G
                    Bs += B
        K = 5*5 
        Rs = int(Rs/K)
        Gs = int(Gs/K)
        Bs = int(Bs/K)
        Smoothed5.putpixel((x,y),(Bs,Gs,Rs))

for x in range(3,width):
    for y in range(3,height-3):
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-3, x+4):
            for j in range(y-3,y+4):
                if 0 <= i < width and 0 <= j < height:
                    pixel_values = imgPIL.getpixel((i, j))
                    R = pixel_values[0]
                    G = pixel_values[1]
                    B = pixel_values[2]

                    Rs += R
                    Gs += G
                    Bs += B
        K = 7*7 
        Rs = int(Rs/K)
        Gs = int(Gs/K)
        Bs = int(Bs/K)
        Smoothed7.putpixel((x,y),(Bs,Gs,Rs))

for x in range(4,width):
    for y in range(4,height-4):
        Rs = 0
        Gs = 0
        Bs = 0
        for i in range(x-4, x+5):
            for j in range(y-4,y+5):
                if 0 <= i < width and 0 <= j < height:
                    pixel_values = imgPIL.getpixel((i, j))
                    R = pixel_values[0]
                    G = pixel_values[1]
                    B = pixel_values[2]

                    Rs += R
                    Gs += G
                    Bs += B
        K = 9*9 
        Rs = int(Rs/K)
        Gs = int(Gs/K)
        Bs = int(Bs/K)
        Smoothed9.putpixel((x,y),(Bs,Gs,Rs))

anh3 = np.array(Smoothed3)
anh5 = np.array(Smoothed5)
anh7 = np.array(Smoothed7)
anh9 = np.array(Smoothed9)
cv2.imshow('Hinh co gai lenar goc',img)
cv2.imshow('Hinh lam muot 3x3', anh3)
cv2.imshow('Hinh lam muot 5x5', anh5)
cv2.imshow('Hinh lam muot 7x7', anh7)
cv2.imshow('Hinh lam muot 9x9', anh9)
cv2.waitKey(0)
cv2.destroyAllWindows
