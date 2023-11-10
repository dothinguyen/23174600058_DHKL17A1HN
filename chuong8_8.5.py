year = int(input("Nhập năm cần kiểm tra: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "là năm nhuận")
        else:
            print(year, "không phải là năm nhuận")
    else:
        print(year, "là năm nhuận")
else:
    print(year, "không phải là năm nhuận")

