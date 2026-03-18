numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break