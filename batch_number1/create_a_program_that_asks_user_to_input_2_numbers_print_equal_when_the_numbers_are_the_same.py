first_number = float(input("enter first number: "))
second_number = float(input("enter second number: "))

if first_number > second_number:
    print(f"the bigger number is:", first_number)
elif second_number > first_number:
    print(f"the bigger number is:" , second_number)
else:
    print("both are equal")