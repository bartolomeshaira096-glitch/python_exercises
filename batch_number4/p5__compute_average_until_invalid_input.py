numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers)