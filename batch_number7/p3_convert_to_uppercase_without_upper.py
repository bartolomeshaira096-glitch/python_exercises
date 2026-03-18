class Text:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        result = ""

        for character in self.text:
            if 'a' <= character <= 'z':
                result += chr(ord(character) - 32)
            else:
                result += character

        return result