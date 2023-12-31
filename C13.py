#13.1
# Tạo và mở tập tin để ghi văn bản
with open('HumptyDumpty.txt', 'w') as file:
    # Ghi nội dung vào tập tin
    file.write("Humpty dumpty saton a wall,\n")
    file.write("humpty dumpty had a great fall.\n")
    file.write("All the king's horses and all the king's men\n")
    file.write("couldn't put Humpty together again.\n")           
print("Tập tin đã được tạo và ghi thành công.")
# Mở tập tin để đọc
try:
    with open('HumptyDumpty.txt', 'r') as file:
        # Đọc toàn bộ nội dung của tập tin
        content = file.read()
        
        # In nội dung của tập tin
        print(content)
except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
#13.2
try:
    # Mở tập tin để đọc
    with open('HumptyDumpty.txt', 'r') as file:
        # Đọc nội dung của tập tin
        content = file.read()

        # Hiển thị nội dung của tập tin
        print("Nội dung của tập tin:")
        print(content)

        # Đếm số ký tự
        so_ky_tu = len(content)
        print(f"Tập tin có {so_ky_tu} ký tự.")

except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
#13.3
def write_to_file(file_name, content):
    try:
        # Mở tập tin trong chế độ ghi
        with open(file_name, 'w') as file:
            # Ghi nội dung vào tập tin
            file.write(content)
        print(f'Đã ghi nội dung vào tập tin {file_name}')

        # Đọc và in nội dung tập tin sau khi ghi
        read_and_print_file(file_name)

    except Exception as e:
        print(f'Lỗi: {e}')

def read_and_print_file(file_name):
    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc và in nội dung tập tin
            file_content = file.read()
            print(f'Nội dung của tập tin {file_name} sau khi ghi:')
            print(file_content)
    except FileNotFoundError:
        print(f'Tập tin {file_name} không tồn tại.')

def main():
    # Nhập tên tập tin từ người dùng
    file_name = input('Nhập tên tập tin (.txt): ')

    # Kiểm tra xem tên tập tin có kết thúc bằng .txt hay không
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Nhập nội dung từ người dùng
    content = input('Nhập nội dung: ')

    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc nội dung cũ của tập tin
            old_content = file.read()

            # Kiểm tra nếu có nội dung cũ
            if old_content:
                # Xóa nội dung cũ
                write_to_file(file_name, content)
            else:
                # Ghi nội dung mới vào tập tin
                write_to_file(file_name, content)

    except FileNotFoundError:
        # Tập tin chưa tồn tại, tạo tập tin và ghi nội dung vào
        write_to_file(file_name, content)

if __name__ == "__main__":
    main()
#13.4
def write_to_file(file_name, content):
    try:
        # Mở tập tin trong chế độ ghi
        with open(file_name, 'w') as file:
            # Ghi nội dung vào tập tin
            file.write(content)
        print(f'Đã ghi nội dung vào tập tin {file_name}')

        # Đọc và in nội dung tập tin sau khi ghi
        read_and_print_file(file_name)

    except Exception as e:
        print(f'Lỗi: {e}')

def read_and_print_file(file_name):
    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc và in nội dung tập tin
            file_content = file.read()
            print(f'Nội dung của tập tin {file_name} sau khi ghi:')
            print(file_content)
    except FileNotFoundError:
        print(f'Tập tin {file_name} không tồn tại.')

def main():
    # Nhập tên tập tin từ người dùng
    file_name = input('Nhập tên tập tin (.txt): ')

    # Kiểm tra xem tên tập tin có kết thúc bằng .txt hay không
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Nhập nội dung từ người dùng
    content = input('Nhập nội dung: ')

    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc nội dung cũ của tập tin
            old_content = file.read()

            # Kiểm tra nếu có nội dung cũ
            if old_content:
                # Xóa nội dung cũ
                write_to_file(file_name, content)
            else:
                # Ghi nội dung mới vào tập tin
                write_to_file(file_name, content)

    except FileNotFoundError:
        # Tập tin chưa tồn tại, tạo tập tin và ghi nội dung vào
        write_to_file(file_name, content)

if __name__ == "__main__":
    main()
def main():
    while True:
        choice = int(input("Người dùng có muốn tiếp tục ghi nữa hay không? (1 để tiếp tục, 0 để dừng): "))
        
        if choice == 1:
            # Ghi tiếp tục
            print("Đang tiếp tục ghi...")
            # Thêm mã của bạn ở đây
            
        elif choice == 0:
            print("Người dùng đã chọn dừng. Kết thúc chương trình.")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
#13.5
import csv

def write_csv_file(file_name, content):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            # Tạo đối tượng ghi CSV
            writer = csv.writer(file)

            # Ghi nội dung vào tập tin CSV
            for row in content:
                writer.writerow(row)
            
            print(f"Đã ghi nội dung vào tập tin '{file_name}'.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin CSV cần tạo và ghi nội dung(cuối file .csv): ")

    content = []
    while True:
        row = input("Nhập nội dung cho dòng (nhập '0' để kết thúc): ")
        if row.lower() == '0':
            break
        content.append(row.split(','))

    write_csv_file(file_name, content)

if __name__ == "__main__":
    main()
#13.6
import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            # Đọc tập tin CSV
            reader = csv.reader(file)
            
            # In nội dung từng dòng
            for row in reader:
                print(row)
                
    except FileNotFoundError:
        print(f"Tập tin '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def write_phone_numbers(file_name, phone_numbers):
    try:
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
            # Tạo đối tượng ghi CSV
            writer = csv.writer(file)

            # Ghi danh sách số điện thoại và tên người vào cuối tập tin
            for phone_number, person_name in phone_numbers:
                writer.writerow([person_name, phone_number])

            print(f"Đã ghi danh sách số điện thoại vào cuối tập tin '{file_name}'.")
    
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin CSV cần ghi số điện thoại và tên vào: ")

    phone_numbers = []
    while True:
        person_name = input("Nhập tên người (nhập 'done' để kết thúc): ")
        if person_name.lower() == 'done':
            break
        phone_number = input("Nhập số điện thoại: ")
        phone_numbers.append((phone_number, person_name))

    write_phone_numbers(file_name, phone_numbers)

    # Xuất nội dung tập tin vừa ghi
    print("\nNội dung tập tin sau khi ghi:")
    read_csv_file(file_name)

if __name__ == "__main__":
    main()
