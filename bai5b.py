import cv2 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def TinhHistogramRGB(HinhXamPIL):
    r_channel, g_channel, b_channel = HinhXamPIL.split()
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
his_r, his_g, his_b = TinhHistogramRGB(imgPIL)
VeBieuDoHistogramRGB(his_r, his_g, his_b)
cv2.waitKey(0)
cv2.destroyAllWindows()