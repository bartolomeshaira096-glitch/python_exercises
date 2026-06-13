class Text:
    def __init__(self, text):
        self.text = text 

    def to_lowercase(self):
        result = ""

        for char in self.text:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char

        return result