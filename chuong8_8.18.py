Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0
0
>>> x = int(input("Nhập số nguyên x: "))
Nhập số nguyên x: 4
>>> is_perfect = sum(i for i in range(1, x) if x % i == 0) == x
>>> is_prime = x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
>>> print(x, "là số hoàn hảo." if is_perfect else "không phải là số hoàn hảo.")
4 không phải là số hoàn hảo.
>>> print(x, "là số nguyên tố." if is_prime else "không phải là số nguyên tố.")
4 không phải là số nguyên tố.
>>> 
