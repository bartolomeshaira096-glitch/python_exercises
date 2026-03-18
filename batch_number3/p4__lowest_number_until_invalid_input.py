numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
if numbers:
    print("Lowest number:", min(numbers))
else:
    print("No valid numbers entered")