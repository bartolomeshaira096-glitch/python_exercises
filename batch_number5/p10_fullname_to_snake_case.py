class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def to_snake_case(self):
        return "_".join(self.fullname.lower().split())

fullname = input("Enter your full name: ")

person = FullName(fullname)

print(person.to_snake_case())