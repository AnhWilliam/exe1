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
        gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
        average.putpixel((x, y), (gray, gray, gray))
anhmucxam = np.array(average)
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh muc xam dung Luminance', anhmucxam)
cv2.waitKey(0)
cv2.destroyAllWindows()