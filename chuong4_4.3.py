m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n > m): "))
if m > 0 and n > 0 and m < n:
    print("Các số chia hết cho", m, "trong khoảng từ 1 đến", n, "là:")
    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=" ")
else:
    print("Số nhập vào không hợp lệ")
