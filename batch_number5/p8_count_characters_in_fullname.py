class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def count_characters(self):
        return len(self.fullname)
    
fullname = input("Enter your full name: ")

person = FullName(fullname)

print("Number of characters:", person.count_characters())