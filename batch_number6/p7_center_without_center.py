class Text:
    def __init__(self, text):
        self.text = text
    
    def center_text(self, width):
        total_spaces = width - len(self.text)

        if total_spaces <= 0:
            return self.text

        left_spaces = total_spaces // 2
        right_spaces = total_spaces - left_spaces

        return (" " * left_spaces) + self.text + (" " * right_spaces)