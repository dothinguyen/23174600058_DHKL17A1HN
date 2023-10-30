x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))

a, b = x, y
while a != b:
    if a < b:
        a += x
    else:
        b += y

bcnn = a

print("BCNN của hai số", x, "và", y, "là:", bcnn)
