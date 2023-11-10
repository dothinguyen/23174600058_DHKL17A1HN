Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0
0
>>> x = int(input("Nhập vào một số x: "))
Nhập vào một số x: 4
>>> print(f"{x} là số nguyên tố." if all(x % i != 0 for i in range(2, int(x/2)+1)) and x >= 2 else f"{x} không phải là số nguyên tố.")
4 không phải là số nguyên tố.
