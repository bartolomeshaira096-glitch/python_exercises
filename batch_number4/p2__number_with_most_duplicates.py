numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

most_number = None
highest_count = 0

for num in numbers:
    count = numbers.count(num)
    if count > highest_count:
        highest_count = count
        most_number = num