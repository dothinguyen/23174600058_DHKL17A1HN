a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

p = (a + b + c) / 2
S = (p*(p-a)*(p-b)*(p-c)) ** 0.5

print(f"Diện tích tam giác là {S}")
