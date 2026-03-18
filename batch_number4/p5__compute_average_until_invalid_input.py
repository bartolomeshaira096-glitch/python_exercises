numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No valid numbers entered")