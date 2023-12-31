def nhap_so_nguyen_duong():
    count = 0
    last_number = None
    while True:
        try:
            number = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            if number < 0:
                raise ValueError("Lỗi nhập số âm!!!")
            if number == last_number:
                raise ValueError("Lỗi nhập lặp lại !!!")
            if number % 2 == 0:
                raise ValueError("Lỗi nhập chẵn !!!")
            last_number = number
            count += 1
            if count == 5:
                count = 0
                last_number = None
            if number == 0:
                print("Kết thúc nhập số.")
                break
        except ValueError as e:
            print(e)

nhap_so_nguyen_duong()
