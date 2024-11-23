# # # # # Câu lệnh vòng lặp while
# # # # # n = 10
# # # # # while n > 2: #True
# # # # #     print("chạy vòng lặp",n)
# # # # #     n = n - 1
# # # # # Vong lặp ưhile cũng hỗ trỡ break, continue và else
 
 
 
# # # # # Continue
# # # # # n = 10
# # # # # while n > 2: 
# # # # #     n = n - 1
# # # # #     if n == 6:
# # # # #         continue
# # # # #     print("chạy vòng lặp",n)
    
    
# # # # # else
# # # # # n = 10
# # # # # while n > 2: 
# # # # #     n = n - 1
# # # # #     if n == 6:
# # # # #         continue
# # # # # else:
# # # # #     print("chạy câu lệnh else",n)
# # # # #  
# # # # # n = 10
# # # # # while n > 2: 
# # # # #     n = n - 1
# # # # #     if n == 6:
# # # # #         break
# # # # # else:
# # # # #     print("chạy câu lệnh else",n)
    
# # # #     #Câu 1
# # # # # for i in range(1, 100, 2):
# # # # #     print(i)




import math
n = int(input("Nhập vào số n: "))

print("Các số chính phương nhỏ hơn", n, "là:")
for i in range(1, int(math.sqrt(n)) + 1):
    print(i * i)



#Bài 3
n = 50
a = 0
b = 1
print("50 số đầu tiên trong dãy Fibonacci là: ")
for _ in range(n):
    print(a, end = " ")
    a, b = b, a + b





#Bài 4
a = int(input("Nhập vào một số: "))
#Là số nguyên tố
la_so_nguyen_to = True

#Nếu số <= 1 thì không phải số nguyên tố
if a <= 1:
    la_so_nguyen_to = False
else:
    # Dùng vòng lặp để kiểm tra ước số từ 2 đến căn bậc hai của số đó
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            la_so_nguyen_to = False
            break 
if la_so_nguyen_to:
    print(a, "là số nguyên tố.")
else:
    print(a, "không phải là số nguyên tố.")



#Bài 5
# Nhập vào một số 
a = int(input("Nhập vào một số: "))
#Tính tổng các ước thực của số đó(không bao gồm chính nó)
tong_uoc_so = 0
for i in range(1, a // 2 + 1):
    if a % i == 0:
        tong_uoc_so += i
if tong_uoc_so == a:
    print(a, "là số hoàn hảo.")
else:
    print(a, "không phải là số hoàn hảo."),




# Nhập số n
n = int(input("Nhập vào số n: "))
print("Các số nguyên tố nhỏ hơn", n, "là: ")
# Kiểm tra từng số từ 2 đến n-1
for a in range(2, n):
    so_nguyen_to = True
    for i in range(2, int(a ** 0.5) + 1):  
        if a % i == 0:
            so_nguyen_to = False  
            break 
    if so_nguyen_to:
        print(a, end=" ")




# Nhập vào số n
n = int(input("Nhập vào số n: "))
print("Các số hoàn hảo nhỏ hơn", n, "là: ")
# Duyệt từng số từ 1 đến n-1 để kiểm tra số hoàn hảo
for a in range(1, n):
    so_nguyen_to = 0  
    # Tìm tổng các ước số của a
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            so_nguyen_to += i
    if so_nguyen_to == a:
        print(a, end=" ")







#Bài 11
# Nhập vào hai số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

while b != 0:
    a, b = b, a % b

print("Ước chung lớn nhất của hai số là:", a)









# Nhập hai số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

# Tính BCNN
bcnn = abs(a * b) // x 

# In kết quả
print("Bội chung nhỏ nhất của hai số là:", bcnn)







# Nhập một số
n = int(input("Nhập một số: "))
#Kiểm tra
la_so_chinh_phuong = False
# Duyệt qua các số từ 0 đến n/2 để tìm số chính phương
for i in range(n + 1):
    if i * i == n:
        la_so_chinh_phuong = True
        break
    
if la_so_chinh_phuong:
    print(n, "là số chính phương.")
else:
    print(n, "không phải là số chính phương.")







# Nhập tử số và mẫu số
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

def ucln(x, y):
    while y != 0:
        x, y = y, x % y
    return x
#mẫu số phải khác 0
if mau_so == 0:
    print("Mẫu số không thể bằng 0!")
else:
    gcd = ucln(abs(tu_so), abs(mau_so)) 
    # Tối giản phân số
    tu_so_toi_gian = tu_so // gcd
    phan_so_toi_gian = mau_so // gcd
     # Nếu mẫu số âm, chuyển dấu âm sang tử số
    if phan_so_toi_gian < 0:  
        tu_so_toi_gian = -tu_so_toi_gian
        phan_so_toi_gian = -phan_so_toi_gian
    print(f"Phân số đã tối giản là: {tu_so_toi_gian}/{phan_so_toi_gian}")








# Nhập vào số
n = int(input("Nhập một số: "))
# Lưu các thừa số nguyên tố
factors = []
# Kiểm tra chia hết cho 2 
while n % 2 == 0:
     factors.append(2)
     n //= 2
# Kiểm tra các số lẻ từ 3 đến sqrt(n)
i = 3
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2

# Nếu n còn lại là một số nguyên tố lớn hơn 2
if n > 2:
    factors.append(n)
ket_qua = " * ".join(map(str,  factors))
print(f"{n} => {ket_qua}")






# Nhập số n
n = int(input("Nhập số n: "))

# S1: Tính tổng 1 + 2 + 3 + ... + n
S1 = 0
for i in range(1, n + 1):
    S1 += i
print(f"S1 = {S1}")
# S2: Tính tích 1 * 2 * 3 * ... * (n - 1)
S2 = 1
for i in range(1, n):
    S2 *= i
print(f"S2 = {S2}")
# S3: Tính 1 - 1/2 + 1/3 - 1/4 + ... + ((-1)**n) / n
S3 = 0
for i in range(1, n + 1):
    S3 += (-1) ** (i + 1) * (1 / i)
print(f"S3 = {S3}")








# Nhập lựa chọn
print("Chọn loại: ")
print("1. Chuyển từ hệ cơ số 10 sang hệ cơ số 2")
print("2. Chuyển từ hệ cơ số 2 sang hệ cơ số 10")
choice = int(input("Nhập lựa chọn (1 hoặc 2): "))
if choice == 1:
    a = int(input("Nhập số trong hệ cơ số 10: "))
    b = bin(a)[2:]
    print(f"Số {a} trong hệ cơ số 10 chuyển sang hệ cơ số 2 là: {b}")
elif choice == 2:
    b = input("Nhập số trong hệ cơ số 2: ")
    a = int(b, 2) 
    print(f"Số {b} trong hệ cơ số 2 chuyển sang hệ cơ số 10 là: {a}")
else:
    print("Lựa chọn không hợp lệ.")








# Nhập số dòng của Tam giác Floyd
n = int(input("Nhập số dòng của Tam giác Floyd: "))
a = 1  
for i in range(1, n+1):
    for j in range(i):
        print(a, end=" ")
        a += 1
    print()  
# Nhập số dòng của Tam giác Pascal
n = int(input("Nhập số dòng của Tam giác Pascal: "))
# Khởi tạo tam giác Pascal
tam_giac = []
for i in range(n):
    hang = [1] * (i + 1) 
    for j in range(1, i):
        hang[j] = tam_giac[i-1][j-1] + tam_giac[i-1][j] 
    tam_giac.append(hang)

# In ra tam giác Pascal
for hang in tam_giac:
    print(" ".join(map(str, hang)).center(n*2))
