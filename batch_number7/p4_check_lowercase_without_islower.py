class Text:
    def __init__(self, text):
        self.text = text

    def is_lowercase(self):
        has_letter = False

        for character in self.text:
            if 'A' <= character <= 'Z':
                return False
            elif 'a' <= character <= 'z':
                has_letter = True

        return has_letter
    
text = input("Enter a string: ")

value = Text(text)

print(value.is_lowercase())