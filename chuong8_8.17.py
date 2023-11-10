def bcnn(a, b):
    gcd = ucln(a, b)
    return (a * b) // gcd

def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn(a, b))

