import cv2
from PIL import Image
import numpy as np

#Khai báo đường dẫn file hình

filehinh = r'lena_colour.png'

img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu dùng thư viện PIL dùng để thực hiện tác vụ xử lí và tính toán 

imgPIL = Image.open(filehinh)

# Tạo ảnh có cùng kích thước và mode với ảnh PIL dùng để chứa kết quả RGB sang CMYK

KenhmauCyan = Image.new(imgPIL.mode, imgPIL.size)
KenhmauMeganta = Image.new(imgPIL.mode, imgPIL.size)
KenhmauYellow = Image.new(imgPIL.mode, imgPIL.size)
KenhmauBlack = Image.new(imgPIL.mode, imgPIL.size)



#lấy kích thước của ảnh từ imgPIL
width = len(img[0])
height = len(img[1])

#mỗi ảnh là 1 ma trận 2 chiều nên dùng 2 hàm for để đọc các điểm ảnh
for x in range(width):
    for y in range(height):
        #lấy giá trị điểm ảnh tại vị trí (x,y)h
        pixel_values = imgPIL.getpixel((x, y))
        R = pixel_values[0]
        G = pixel_values[1]
        B = pixel_values[2]
        
        #Cyan (xanh dương) là kết hợp green và blue nên red = 0
        KenhmauCyan.putpixel((x,y), (B, G, 0))
        
        #Magenta (tím) là sự kết hợp giữa red và blue nên green = 0
        KenhmauMeganta.putpixel((x,y), (B, 0, R))
        
        #Yellow (Vàng) là sự kết hợp giữa Red và Green nên Blue = 0
        KenhmauYellow.putpixel((x,y), (0, G, R))
        
        #lấy giá trị min trong 3 giá trị RGB
        MIN = min(R, G, B)
        KenhmauBlack.putpixel((x,y), (MIN, MIN, MIN))

# Chuyển ảnh từ PIL sang OpenCV
Cyan = np.array(KenhmauCyan)
Meganta = np.array(KenhmauMeganta)
Yellow = np.array(KenhmauYellow)
Black = np.array(KenhmauBlack)



cv2.imshow('Kenh Cyan', Cyan)
cv2.imshow('Kenh Meganta', Meganta)
cv2.imshow('Kenh Yellow', Yellow)
cv2.imshow('Kenh Black', Black)


cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình

cv2.destroyAllWindows