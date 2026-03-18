class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def reverse_case(self):
        return self.fullname.swapcase()
    
fullname = input("Enter your full name: ")

person = FullName(fullname)

print(person.reverse_case())