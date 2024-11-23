import math
#Nhập giá trị của a, b, c
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
#Điều kiện
if a < 0 and  b < 0 and c < 0:
    print("Thỏa mãn yêu cầu bài toán")
    #Công thức
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    if delta > 0:
        print("Phương trình có 2 nghiệm phân biệt:",x1 = (( -b + math.sqrt(delta)) / 2 * a ),x2 = (( -b - math.sqrt(delta)) / 2 * a ))
    if delta == 0:
        print("Phương trình có nghiệm kép:", x3 = (-b /( 2 * a)))
                
else:
        print("Không thoar mãn yêu cầu bài toán")
    
    

