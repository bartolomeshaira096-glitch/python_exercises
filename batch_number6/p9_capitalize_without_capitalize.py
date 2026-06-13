class Text:
    def __init__(self, text):
        self.text = text
    
    def capitalize_text(self):
        if len(self.text) == 0:
            return self.text

        result = ""

        first_char = self.text[0]

        if 'a' <= first_char <= 'z':
            result += chr(ord(first_char) - 32)
        else:
            result += first_char

        for char in self.text[1:]:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char

        return result
    
text = input("Enter a string: ")

value = Text(text)

print(value.capitalize_text())