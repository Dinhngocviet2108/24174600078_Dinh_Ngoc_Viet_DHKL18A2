# 3. Viết chương trình tìm số lớn nhất trong 3 số bằng Python
a = float(input("Nhập số đầu tiên: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    print(f"số lớn nhất là:" , a)
elif b >= a and b >= c:
    print(f"số lớn nhất là:" ,b)
else: 
    print(f"số lớn nhất là:" ,c)        