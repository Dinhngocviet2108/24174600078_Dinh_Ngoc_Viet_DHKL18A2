# #Bài tập về chuỗi kí tự
# #Dạng thứ nhất : áp dụng xử lí chuỗi kí tự bằng các phương thức có sẵn
# #Bài 1: Nhập vào 1 chuỗi kí tự bất kì. Đếm số trong chuỗi
# #Cách 1:
# chuoi_nhap_vao = input("Nhập vào chuỗi kí tự: ")
# so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
# print(f"Số kí tự trong chuỗi là {so_ky_tu_trong_chuoi}")
# #Cách 2:
# chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
# dem = 0
# for chu in chuoi_nhap_vao:
#     dem = dem + 1
#     print(f"Số ký tự trong chuỗi là {dem}")
    
# #Bài 2:
# #Cách 1
# chuoi_nhap_vao = input("Nhạp chuỗi bất kỳ: ")
# chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
# print(f"Chuỗi sau khi đã xóa khoảng trống {chuoi_da_xoa_khoang_trong}")
# #Cách 2
# chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")
# # chuỗi nhậo vào
# chuoi_xu_li_dau = ""
# kiem_tra_dau = False
# for chu in chuoi_nhap_vao:
#     if chu == " " and kiem_tra_dau == False:
#         continue
#     else:
#         kiem_tra_dau == True
#         chuoi_xu_li_dau = chuoi_xu_li_dau + chu
        
        
# #Bài 3 :Nhập vào một chuỗi bất kì. Xóa tất cả khoảng trống thừa trong chuỗi
# #Ví dụ: "    chuoi    nhap   vao          "
# #Cách 1:
# chuoi_nhap_vao = input("Nhập vào chuỗi bất kì: ")



# chuoi_ket_qua = " ".join(cach_chuoi)
        