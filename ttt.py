 #Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4
nhap_chuoi = input("Nhập chuỗi kí tự :")
so_tu = len(nhap_chuoi.split())
print("Số từ là:",so_tu)


#Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”
ho_ten = input("Nhập họ tên đầy đủ: ")
ho = ho_ten.split()[0]
ten = ho_ten.split()[-1]
print("Họ:",ho, "Tên:",ten)

 #Bài 4: Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường

a = input("Nhập vào chuỗi ký tự: ")

chu_viet_hoa = 0
chu_viet_thuong= 0

for char in a:
    if char.isupper():  
        chu_viet_hoa += 1
    elif char.islower():  
        chu_viet_thuong += 1
print(f"Số chữ cái viết hoa: {chu_viet_hoa}")
print(f"Số chữ cái viết thường: {chu_viet_thuong}")


    
# Bài 6:  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không

a = input("Nhập vào một chuỗi: ")

# Kiểm tra chuỗi có phải là số âm không
if a.startswith('-') and a[1:].isdigit():
    print("Chuỗi là số âm.")
else:
    print("Chuỗi không phải là số âm.")

# Bài 7: Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không

a = input("Nhập vào chuỗi ký tự: ")

if a.count('.') == 1:
    truoc,sau = a.split('.')
    if truoc.isdigit() and sau.isdigit():
        print(f"'{a}' là một số thập phân")
    else:
        print(f"'{a}' không phải số thập phân")
#Số nguyên
elif a.isdigit():
    print(f"'{a}' là một số thập phân hợp lệ")
else:
    print(f"'{a}' không phải là một số thập phân hợp lệ")
    
    