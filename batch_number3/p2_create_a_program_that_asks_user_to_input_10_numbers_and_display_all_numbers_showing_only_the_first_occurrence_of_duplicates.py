numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

displayed = []

for number in numbers:
    if number not in displayed:
        print(number)
        displayed.append(number)