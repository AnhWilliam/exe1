import cv2
from PIL import Image
import numpy as np
filehinh = r'lena_colour.png'
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
imgPIL = Image.open(filehinh)
average = Image.new(imgPIL.mode, imgPIL.size)
width = average.size[0]
height = average.size[1]
for x in range(width):
    for y in range(height):
        pixel_values = imgPIL.getpixel((x, y))
        R = pixel_values[0]
        G = pixel_values[1]
        B = pixel_values[2]
        Min = min(R, G, B)
        Max = max(R, G, B)
        gray = np.uint8((Min + Max) / 2)
        average.putpixel((x, y), (gray, gray, gray))
anhmucxam = np.array(average)
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh muc xam dung Lightness', anhmucxam)
cv2.waitKey(0)
cv2.destroyAllWindows()