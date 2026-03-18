class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def to_uppercase(self):
        return self.fullname.upper()
    
fullname = input("Enter your full name: ")

person = FullName(fullname)

print(person.to_uppercase())