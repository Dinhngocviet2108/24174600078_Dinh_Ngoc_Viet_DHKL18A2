#BAI2
import math
x = float(input("Nhập hoành độ điểm M: "))
y = float(input("Nhập tung độ điểm M: "))
a = float(input("Nhập hoành độ tâm hình tròn: "))
b = float(input("Nhập tung độ tâm hình tròn : "))
R = float(input("Nhập bán kính hình tròn: "))
khoang_cach = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if khoang_cach <= R:
    print(f"True")
else:
    print(f"False")


# BAI3. Viết chương trình tìm số lớn nhất trong 3 số bằng Python
a = float(input("Nhập số đầu tiên: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    print(f"số lớn nhất là:" , a)
elif b >= a and b >= c:
    print(f"số lớn nhất là:" ,b)
else:
    print(f"số lớn nhất là:" ,c)

# BAI 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.

a = float(input("Nhập cạnh đầu tiên: "))
b = float(input("Nhập cạnh thứ 2: "))
c = float(input("Nhập cạnh thứ 3: "))
if a + b > c or a + c > b or b + c > a:
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print(f"Tam giác vuông")
    elif a == b == c:
        print(f"Tam giác đều")
    elif a == b or a == c or b == c:
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
            print(f"Tam giác vuông cân")
        else:
            print(f"Tam giác cân")
else:
    print(f"Không phải 3 cạnh của tam giác")
    
    
    
# BAI5. Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm
a = str(input("Nhập chữ cái: "))
if a in ( 'u' , 'e' , 'o' , 'a' , 'i' ):
    print(f"Đây là một nguyên âm: ")
else:
    print(f"Đây là một phụ âm: ")


# BAI6 Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
a = str(input("Nhập thể loại: "))
if a == 'phim tình cảm':
    print(f" i love u ")
    print(f" how i met your mother")
elif a == 'phim kinh dị':
    print(f" ma sơ")
    print(f" quỷ quyệt ")
elif a == 'phim hoạt hình':
    print(f"doraemon")
    print(f"dragonball")
    print(f"onepiece")
elif a == 'phim khoa học viễn tưởng':
    print(f"avatar")
    print(f"starwar")
else:
    print(f"phim không tồn tại")


# BAI8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập.
a = str(input("Nhập điểm sinh viên: "))
if a == 'A':
    print(f"sinh viên xuất sắc")
elif a == 'B':
    print(f"sinh viên loại giỏi")
elif a == 'C':
    print(f"sinh viên loại khá")
elif a == 'D':
    print(f"sinh viên loại trung bình")
elif a == 'E':
    print(f"sinh viên loại yếu")
elif a == 'F':
    print(f"sinh viên loại kém")
else:
    print(f"điểm không hợp lệ")


#BAI 9. Tính cước tacxi:
import math
a = float(input("Nhập loại xe: "))
b = float(input("Nhập thời gian chờ(phút): "))
if 0 <= b <= 5:
    tien_cho = 0
if b > 5:
    tien_cho = (b * 800) - (5 * 800) 
if a == 4:
    so_km = float(input("Nhập số km:"))
    # b = float(input("Nhập thời gian chờ: "))
    if so_km <= 0.8: 
        print(f"Giá tiền :", 11000 + tien_cho  )
    elif so_km <= 20:
        print(f"Giá tiền là :",12100 * so_km + tien_cho )
    elif so_km > 20:
        print(f"Giá tiền là :",12100 * 20 + 10000 * so_km + b + tien_cho )      
elif a == 7:
    so_km_la = float(input("Nhập số km:"))
    if so_km_la <= 0.8:
        print(f"Giá tiền: ", 13000 + tien_cho )
    elif so_km_la <= 30:
        print(f"Giá tiền là :", 14100 * so_km_la + tien_cho )
    elif so_km_la > 30:
        print(f"Giá tiền là :",14100 * 30 + 12000 * so_km_la + tien_cho )
else:
    print(f"Nhập sai loại xe")



#BAI 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng 
# lương thực sự mà nhân viên đó nhận được).
a = float(input("Nhập lương nhân viên (triệu VND): "))
if a >= 15:
    print(f"Thuế là:", 0.30 * a)
    print(f"Lương ròng là:",a - (0.30 * a)) 
elif 7 <= a < 15:
    print(f"Thuế là:", 0.20 * a)
    print(f"Lương ròng là:",a - (0.20 * a))   
elif 0 <= a < 7:
    print(f"Thuế là:", 0.10 * a)
    print(f"Lương ròng là:",a - (0.10 * a))
else:
    print(f"Lương không hợp lệ")     





