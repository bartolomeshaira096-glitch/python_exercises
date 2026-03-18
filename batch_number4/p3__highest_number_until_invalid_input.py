numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    highest = max(numbers)
    print("Highest number:", highest)
else:
    print("No valid numbers entered")