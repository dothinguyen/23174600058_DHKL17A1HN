#9.2
def nam_am_lich(nam_duong_lich):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    can_index = (nam_duong_lich + 6) % 10
    chi_index = (nam_duong_lich + 8) % 12

    nam_am = can[can_index] + " " + chi[chi_index]

    return nam_am

nam = int(input("Nhập năm dương lịch: "))
nam_am = nam_am_lich(nam)
print(f"Năm âm lịch tương ứng là: {nam_am}")
   
   #9.3
def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao ** 2)
    return bmi

chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

bmi = tinh_bmi(chieu_cao, can_nang)
print("Chỉ số BMI của bạn là:", bmi)
if bmi < 18.5:
    print("Bạn đang gầy")
elif 18.5 <= bmi < 25:
    print("Bạn có cân nặng bình thường")
elif 25 <= bmi < 30:
    print("Bạn béo phì cấp độ 1")
elif 30 <= bmi < 35:
    print("Bạn béo phì cấp độ 2")
else:
    print("Bạn béo phì cấp độ 3")

#9.4
def tinh_S(n, x):
    S = (x**2 + 1)**n
    return S

n = int(input("Nhập giá trị của n: "))
x = int(input("Nhập giá trị của x: "))

ket_qua = tinh_S(n, x)
print("Giá trị của S là:", ket_qua)

#9.5
def tinh_A(n, x):
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A

n = int(input("Nhập giá trị của n: "))
x = int(input("Nhập giá trị của x: "))

ket_qua = tinh_A(n, x)
print("Giá trị của A là:", ket_qua)
#9.6
def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

x = int(input("Nhập một số nguyên dương: "))

if kiem_tra_so_nguyen_to(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không phải là số nguyên tố")
# 9.7
def phan_nguyen_phep_chia(a, b):
    return a // b
x = 10
y = 3
ket_qua = phan_nguyen_phep_chia(x, y)
print("Phần nguyên của phép chia", x, "cho", y, "là:", ket_qua)
