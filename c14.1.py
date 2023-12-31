def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Độ dài cạnh phải là số dương"
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Ba cạnh không thỏa mãn điều kiện của tam giác"
    else:
        return "Ba cạnh là độ dài của một tam giác"

try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    
    print(kiem_tra_tam_giac(a, b, c))
except ValueError:
    print("Độ dài cạnh phải là một số")