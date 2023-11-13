import cv2 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
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
            average.putpixel((x, y),(gray, gray, gray))
    return average
def TinhHistogram(HinhXamPIL):
    his = np.zeros(256)
    w = HinhXamPIL.size[0]
    h = HinhXamPIL.size[1]
    for x  in range (w):
        for y in range (h):
            gR, gG, gB = HinhXamPIL.getpixel((x, y))
            his[gR] += 1
    return his
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Bieu Do Histogram Anh Xam', figsize=(((w,h))), dpi=100)
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, his, color='orange')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()
def TinhHistogramAnhMauRGB(HinhAnhMauPIL):
    r_channel, g_channel, b_channel = HinhAnhMauPIL.split()
    his_r = np.array(r_channel.histogram())
    his_g = np.array(g_channel.histogram())
    his_b = np.array(b_channel.histogram())
    return his_r, his_g, his_b
def VeBieuDoHistogramRGB(his_r, his_g, his_b):
    w = 10
    h = 6
    plt.figure('Biểu đồ Histogram ảnh RGB', figsize=((w, h)), dpi=100)
    trucX = np.arange(256)
    plt.plot(trucX, his_r, color='red', label='Red')
    plt.plot(trucX, his_g, color='green', label='Green')
    plt.plot(trucX, his_b, color='blue', label='Blue')
    plt.title('Biểu đồ Histogram ảnh RGB')
    plt.xlabel('Giá trị pixel')
    plt.ylabel('Số lượng pixel')
    plt.legend()
    plt.show()
filehinh = r'C:\Users\Admin\Documents\New folder\bird_small.jpg'
imgPIL = Image.open(filehinh)
HinhXamPIL = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)
his = TinhHistogram(HinhXamPIL)
HinhXamCV = np.array(HinhXamPIL)
cv2.imshow('Anh muc xam', HinhXamCV)
VeBieuDoHistogram(his)
his_r, his_g, his_b = TinhHistogramAnhMauRGB(imgPIL)
VeBieuDoHistogramRGB(his_r, his_g, his_b)
cv2.waitKey(0)
cv2.destroyAllWindows()