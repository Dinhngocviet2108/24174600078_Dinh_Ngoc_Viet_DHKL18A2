# # a = str(input("Nhap vao chuoi: "))
# # if a == "in ra man hinh" :
# #      print(f"Dinh Ngoc Viet")

# import math
# a = float(input("Nhap toa do A: "))
# b = float(input("Nhap toa do B: "))
# c = float(input("Nhap toa do C: "))
# print(f"AH=")

import math
n = int(input("Nhap so nguyen duong: "))
if n > 0:
  print(f"Bang cuu chuong cua cac so nho hon n la{n}")
  for i in range(1,n):
    print(f"cuu chuong{i}")
  for j in range(1,11):
      print(f"{i} x {j} = {i * j}")   
else:
    print(f"Nhap sai")
     