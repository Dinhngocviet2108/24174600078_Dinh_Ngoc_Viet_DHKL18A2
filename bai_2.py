import math
#Nhập giá trị của x
x = float(input("Nhập gái trị của x: "))
#Tử số
tu_so = -x + math.sqrt(x ** 2 + 4)
#Mẫu số
mau_so = (x ** 4 +1) ** (1/7)
#Kết quả 
ket_qua = tu_so / mau_so
print("Kết quả là:",round(ket_qua, 2))
#Khhông cần điều kiện
