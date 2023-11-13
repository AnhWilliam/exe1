import cv2 
import numpy as np
from PIL import Image

filehinh = r'lena_colour.png'

imgPIL = Image.open(filehinh)               
binary = Image.new(imgPIL.mode, imgPIL.size)   
width = binary.size[0]                         
height = binary.size[1]
nguong = 120

for x in range(width):
    for y in range(height):
        pixel_values = imgPIL.getpixel((x, y))
        R = pixel_values[0]
        G = pixel_values[1]
        B = pixel_values[2]
        gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
        if (gray < nguong):
            binary.putpixel((x, y), (0, 0, 0))
        else:
            binary.putpixel((x, y), (255, 255, 255))
   
        
anhnhiphan=np.array(binary)
img=cv2.imread(filehinh,cv2.IMREAD_COLOR) 
cv2.imshow('Anh mau RGB goc',img)
cv2.imshow('Anh RGB chuyen sang ma nhi phan Binary',anhnhiphan)

cv2.waitKey(0)
cv2.destroyAllWindows()
