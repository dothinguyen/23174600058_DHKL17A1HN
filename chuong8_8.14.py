n = int(input("Nhập vào số lượng số nguyên N: "))

sum = 0
for i in range(n):
    num = int(input(f"Nhập số nguyên thứ {i+1}: "))
    sum += num

print("Tổng của các số nguyên là:", sum)

