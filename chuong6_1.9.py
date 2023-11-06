Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0
0
>>> interest_rate = float(input("Lãi suất 1 năm (%): "))
Lãi suất 1 năm (%): 7.6
>>> deposit_amount = float(input("Số tiền gửi: "))
Số tiền gửi: 10000000
>>> deposit_months = int(input("Số tháng gửi: "))
Số tháng gửi: 6
>>> interest_amount = (deposit_amount * deposit_months) * (interest_rate / 12)
>>> print(f"Số tiền lãi là: {interest_amount:.2f}")
Số tiền lãi là: 38000000.00
>>> total_amount = deposit_amount + interest_amount
>>> print(f"Tổng số tiền : {total_amount:.2f}")
Tổng số tiền : 48000000.00
