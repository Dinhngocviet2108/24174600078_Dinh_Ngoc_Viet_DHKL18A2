# a = ["abc", "def", "ghijk", 1, 2, 3] 
# b = a
# b[0] = "chuoi thay doi"
# print(a)
# print(b)

#Thay đổi giá trị trong danh sách
a = ["abc", "def", "ghijk", 1, 2, 3]
a[3] = 10
a[1:4] = [6,7,8]
print(a)
#Độ dài của danh sách
print(len(a))
#Phương thưcs thêm và bớt
a.append("abcd")
a.append([ 1,2,3 ])
print(a)
#Thêm nhiều phần tử vào danh sách
a.extend([1,1,1])
print(a)
#Xóa tất cả các phần tử trong danh sách
a.clear()
#Lấy phần tử cùng ra khỏi danh sách
b = a.pop()
print(a)
print(b)
#Xóa một phần tử trong chuỗi
a.remove("abc")
#Thêm 1 phần tử vào vị trí index
a.insert(3, "kkk")
#Đếm số lần xuất hiện của phần tử trong danh sách
a.count("abc")
#Đảo ngược danh sách
a.reverse()
#Trả về ví trí xuất hiện đầu tiên của phần tử trong danh sách
a.index(1)
#Sắp xếp danh sách
a.sort(reverse=True)

