class Text:
    def __init__(self, text):
        self.text = text

    def reverse_case(self):
        result = ""

        for char in self.text:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            elif 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char

        return result
    
text = input("Enter a string: ")

value = Text(text)

print(value.reverse_case())