numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

        if numbers.count(num) == 1:
            print("Unique")
        else:
            print("Duplicate")