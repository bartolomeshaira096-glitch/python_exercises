class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def to_lowercase(self):
        return self.fullname.lower()
    
fullname = input("Enter your full name: ")

person = FullName(fullname)

print(person.to_lowercase())