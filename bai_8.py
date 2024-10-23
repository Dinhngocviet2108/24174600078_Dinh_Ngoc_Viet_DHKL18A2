import math
#Nhập giá trị của x
x = float(input("Nhập giá trị của x: "))
#Điều kiện x>1
if x > 1:
    #Công thức
    log4_x = math.log(x) / math.log(4)
    logx_2 = math.log(2) / math.log(x)
    f_x = log4_x + logx_2
    #Kết quả làm tròn đến số thập phân thứ hai
    print("Giá trị của f(x) là:", round(f_x, 2))
else:
    print("Giá trị của x phải lớn hơn 1")