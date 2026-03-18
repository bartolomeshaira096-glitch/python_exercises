numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    highest = max(numbers)