car_type = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
distance = float(input("Nhập số km đã đi: "))
waiting_time = int(input("Nhập thời gian chờ (tính bằng phút): "))

if car_type == 4:
    if distance <= 0.8:
        fare = 11000
    elif distance <= 20:
        fare = 11000 + (distance - 0.8) * 12100
    else:
        fare = 11000 + 19.2 * 12100 + (distance - 20) * 10000
else:
    if distance <= 0.8:
        fare = 13000
    elif distance <= 30:
        fare = 13000 + (distance - 0.8) * 14100
    else:
        fare = 13000 + 29.2 * 14100 + (distance - 30) * 12000

waiting_fare = max(0, waiting_time - 5) * 800

total_fare = fare + waiting_fare

print("Cước taxi là:", total_fare, "VNĐ")

