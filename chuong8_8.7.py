kwh = float(input("Nhập số kWh đã sử dụng: "))

if kwh <= 50:
    total_cost = kwh * 1678
elif kwh <= 100:
    total_cost = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    total_cost = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
elif kwh <= 300:
    total_cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
elif kwh <= 400:
    total_cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
else:
    total_cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

print("Tiền điện là:", total_cost, "VNĐ")
