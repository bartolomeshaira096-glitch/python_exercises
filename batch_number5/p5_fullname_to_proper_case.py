class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def to_proper_case(self):
        return self.fullname.title()
    
fullname = input("Enter your full name: ")

person = FullName(fullname)

print(person.to_proper_case())