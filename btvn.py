# Câu 8
# Viết chương trình tính điểm của sinh viên.
# Chương trình này sẽ đọc vào các loại điểm của sinh viên (điểm chuyên cần, điểm giữa kỳ, và điểm cuối kỳ) và xếp loại điểm theo quy luật sau:
diem_chuyen_can = float(input("Điểm chuyên cần là: "))
diem_giua_ki = float(input("Điểm giũa kì là: "))
diem_cuoi_ki = float(input("Điểm cuối kì là: "))
#Công thức tính điểm trung bình
diem_trung_binh = (diem_chuyen_can + diem_giua_ki + diem_cuoi_ki) / 3
if diem_trung_binh >= 9:
    print(f"Loại A")
elif 7 <= diem_trung_binh < 9:
    print(f"Loại B")
elif 5 <= diem_trung_binh < 7:
    print(f"Loại C")
elif 0 <= diem_trung_binh < 5:
    print(f"Loại D")
else:
    print(f"Điểm số không hợp lệ")


     