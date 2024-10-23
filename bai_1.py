import math

#Nhập bán kính và chiều cao
r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ "))
#Kiểm tra điều kiện
if r > 0 and h > 0:
    #pi
    pi = 3.14
    #Tính diện tích xung quanh
    Sxq = 2 * pi * r * h
    #Tính diện tích toàn phần
    Stp = Sxq + 2 * pi * r ** 2
    #Tính thể tích
    V = pi * r ** 2 * h
    #In kết quả,làm tròn đến số thập phân thứ hai
    print(f"Diện tích xung quanh: {Sxq:.2f}")
    print(f"Diện tích toàn phần: {Stp:.2f}")
    print(f"Thể tích: {V:.2f}")
else:
    print("Bán kính và chiều cao phâir lớn hơn 0")