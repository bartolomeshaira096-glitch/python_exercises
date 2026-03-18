numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

numbers.sort(reverse=True)

for num in numbers:
    print(num)