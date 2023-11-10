room_type = int(input("Nhập mã loại phòng (1-8): "))
num_nights = int(input("Nhập số đêm lưu trú: "))

if room_type == 1:
    if num_nights <= 1:
        total_cost = 1260000
    elif num_nights <= 3:
        total_cost = 1260000 * 0.75 * num_nights
    else:
        total_cost = 1260000 * 0.7 * num_nights
elif room_type == 2:
    if num_nights <= 1:
        total_cost = 1550000
    elif num_nights <= 3:
        total_cost = 1550000 * 0.75 * num_nights
    else:
        total_cost = 1550000 * 0.7 * num_nights
elif room_type == 3:
    if num_nights <= 1:
        total_cost = 1830000
    elif num_nights <= 3:
        total_cost = 1830000 * 0.75 * num_nights
    else:
        total_cost = 1830000 * 0.7 * num_nights
elif room_type == 4:
    if num_nights <= 1:
        total_cost = 1830000
    elif num_nights <= 3:
        total_cost = 1830000 * 0.75 * num_nights
    else:
        total_cost = 1830000 * 0.7 * num_nights
elif room_type == 5:
    if num_nights <= 1:
        total_cost = 2120000
    elif num_nights <= 3:
        total_cost = 2120000 * 0.75 * num_nights
    else:
        total_cost = 2120000 * 0.7 * num_nights
elif room_type == 6:
    if num_nights <= 1:
        total_cost = 2120000
    elif num_nights <= 3:
        total_cost = 2120000 * 0.75 * num_nights
    else:
        total_cost = 2120000 * 0.7 * num_nights
elif room_type == 7:
    if num_nights <= 1:
        total_cost = 2540000
    elif num_nights <= 3:
        total_cost = 2540000 * 0.75 * num_nights
    else:
        total_cost = 2540000 * 0.7 * num_nights
elif room_type == 8:
    if num_nights <= 1:
        total_cost = 4800000
    elif num_nights <= 3:
        total_cost = 4800000 * 0.75 * num_nights
    else:
        total_cost = 4800000 * 0.7 * num_nights
else:
    print("Mã loại phòng không hợp lệ")
    total_cost = 0

print("Tiền thuê phòng là:", total_cost, "VNĐ")
