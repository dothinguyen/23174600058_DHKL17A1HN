n = int(input("Nhập số lượng số: "))

numbers = list(range(1, n+1))
reversed_numbers = numbers[::-1]
odd_numbers = [num for num in reversed_numbers if num % 2 != 0]

print("Dãy số đảo ngược chỉ gồm các số lẻ là:", odd_numbers)

