def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print("Ước chung lớn nhất của", a, "và", b, "là:", ucln(a, b))

