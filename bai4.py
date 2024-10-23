#Bài 4

#Nhập hằng số 
U = 220.0
I = 2.7
gia_tien = 7000.0
#Nhập thời gian
t = float(input("nhap thoi gian(giay):"))
if t > 0:
    #Tính tiền điện
    tien_dien = ( U * I * t * gia_tien ) / (3600 * 1000)
    #Kết quả
    print("số tiền phải trả là: " , tien_dien) 
else:
    print("thoi gian su dung lon hon 0")