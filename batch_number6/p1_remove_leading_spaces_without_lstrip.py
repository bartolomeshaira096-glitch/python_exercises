class Text:
    def __init__(self, text):
        self.text = text
    
    def remove_leading_spaces(self):
        index = 0

        while index < len(self.text) and self.text[index] == " ":
            index += 1

        return self.text[index:]
    
text = input("Enter a string: ")

value = Text(text)

print(value.remove_leading_spaces())