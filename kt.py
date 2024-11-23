#Bài tập về chuỗi ký tự
#Dạng thứ nhất: áp dụng xử lý chuỗi ký tự bằng các phương thức có sẵn
#Bài 1: Nhận vào một chuỗi ký tự bất kỳ. Đếm số ký tự trong chuỗi.
#Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"So ky tu trong chuoi la {so_ky_tu_trong_chuoi}")
#Cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    dem = dem + 1
print(f"So ky tu trong chuoi la {dem}")

#Bài 2: Nhập vào một chuỗi bất kỳ. Xóa các khoảng trống ở đầu và cuối chuỗi
#Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")
#Cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
#"   chuoi nhap vao              "
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu

chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_dao_nguoc:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau = chuoi_dao_nguoc_xu_ly_dau + chu

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"Chuoi sau khi xoa khoang trong {chuoi_ket_qua}")

#Bài 3: Nhập vào một chuỗi bất kỳ. Xóa tất cả các khoảng trống thừa trong chuỗi
#Ví dụ: "     chuoi     nhap   vao         "
#Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}")

#Cách 2: Bài tập về nhà xử lý yêu cầu trên mà không sử dụng các phương thức





#Dạng thứ hai: áp dụng kết hợp xử lý vòng lặp và xử lý chuỗi ký tự
#Bài 1: Nhập vào một chuỗi ký tự bất kỳ. 
# Đếm xem có bao nhiêu ký tự là chữ, bao nhiêu ký tự là số và bao nhiêu ký tự đặc biệt
# isalpha(): kiểm tra chữ cái
# isdigit(): kiểm tra số

chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu = dem_chu + 1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1

print(f"So chu cai: {dem_chu}")
print(f"So so: {dem_so}")
print(f"So ky tu dac biet: {dem_ky_tu_dac_biet}")






#Bài 2: Nhập vào một số bất kỳ, kiểm tra xem số này có phải số nguyên tố hay không
while True:
# Các số nhập vào phải là số nguyên dương
    n = input("Nhap vao so nguyen duong can kiem tra: ")
    if n.isdigit() == False:
        print("Gia tri nhap vao khong phai gia tri so nguyen duong")
    else:
        break

n = int(n)
# Các số nguyên tố là các số lớn hơn 1
# Các số nguyên tố là các số chỉ chia hết cho 1 và chính nó
if n <= 1:
    print("So nay khong phai la so nguyen to")
else:
    k = n
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("So nay khong phai la so nguyen to")
            break
        k = k - 1
    else:
        print("So nay la so nguyen to")
        
# Bài 3: Nhập vào 2 số thực bất kỳ. Tính tổng 2 số thực đó
while True:
    a = input("Nhap vao so thuc a: ") #"-7.86"
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if a.isdigit() == False:
        print("Gia tri nhap vao khong phai gia tri so")
    else:    
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count("-")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("Gia tri nhap vao khong phai gia tri so")
        else:
            vi_tri_dau_gach = a.find("-")
            if vi_tri_dau_gach != 0:
                print("Gia tri nhap vao khong phai gia tri so")
            else:
                break
    
while True:
    b = input("Nhap vao so thuc b: ") #"-7.86"
    so_kiem_tra = b.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if b.isdigit() == False:
        print("Gia tri nhap vao khong phai gia tri so")
    else:    
        dem_dau_cham = b.count(".")
        dem_dau_gach = b.count("-")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("Gia tri nhap vao khong phai gia tri so")
        else:
            vi_tri_dau_gach = b.find("-")
            if vi_tri_dau_gach != 0:
                print("Gia tri nhap vao khong phai gia tri so")
            else:
                break

a = float(a)
b = float(b)
tong = a + b
print(f"Tong hai so thuc la: {tong}")