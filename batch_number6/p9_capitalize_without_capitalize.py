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