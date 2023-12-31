#10.1
import math
a,b,c=eval(input("Nhap cac so a,b,c la:"))
print("Max=",max(a,b,c))
print("Min=",min(a,b,c))
#10.2
import math
x=eval(input("nhap x la:"))
print("Gia tri tuyet doi cua",x,"la:",abs(x))
#10.3
x=int(input("nhap gia tri x la:"))
n=int(input("nhap gia tri n la:"))
print((math.pow(x,2)+1)*n)
#10.4
import math
x=int(input("nhap gia tri x la:"))
n=int(input("nhap gia tri n la:"))
print(math.pow((pow(x,2)+x+1),n)+math.pow((pow(x,2)-x+1),n))
#10.5
import math
def kiem_tra_ma_zip():
    ma_zip = input("Nhap ma zip la:")
    if len(ma_zip) != 6:
        return False
    for ky_tu in ma_zip:
        if not '0' <= ky_tu <= '9':
            return False
    return True

print(kiem_tra_ma_zip())
#10.6
import math
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm")
#10.7
def process_string(s, s_sub, s_find, s_replace):
    # In chuỗi s
    print("Chuỗi s ban đầu:", s)

    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    s = s.strip()
    print("Chuỗi s sau khi loại bỏ khoảng trắng:", s)

    # In chuỗi với ký tự đầu chuỗi viết hoa
    s = s.capitalize()
    print("Chuỗi s sau khi viết hoa ký tự đầu:", s)

    # Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
    count = s.count(s_sub)
    print("Số lần chuỗi con", s_sub, "xuất hiện trong chuỗi s:", count)

    # Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau khi tìm kiếm và thay thế
    s = s.replace(s_find, s_replace)
    print("Chuỗi s sau khi thay thế", s_find, "bằng", s_replace, ":", s)


# Thử nghiệm chương trình với dữ liệu mẫu
s = "    hello world   "
s_sub = "o"
s_find = "world"
s_replace = "Python"
process_string(s, s_sub, s_find, s_replace)
#10.8
import datetime

def process_date(input_date):
    try:
        # Chuyển đổi ngày tháng năm từ chuỗi sang đối tượng datetime
        date_object = datetime.datetime.strptime(input_date, '%d-%m-%Y')

        # Xuất ngày theo định dạng ngày-tháng-năm
        formatted_date = date_object.strftime('%d-%m-%Y')
        print("Ngày theo định dạng ngày-tháng-năm:", formatted_date)

        # Kiểm tra xem năm nhập vào có phải là năm nhuận hay không
        is_leap_year = "Năm nhuận" if date_object.year % 4 == 0 and (date_object.year % 100 != 0 or date_object.year % 400 == 0) else "Không phải năm nhuận"
        print("Năm nhập vào có phải là năm nhuận hay không:", is_leap_year)

        # Cho biết ngày/tháng/năm nhập vào là thứ mấy
        day_of_week = date_object.strftime('%A')
        print("Ngày/tháng/năm nhập vào là thứ:", day_of_week)

