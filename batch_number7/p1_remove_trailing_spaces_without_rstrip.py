class Text:
    def __init__(self, text):
        self.text = text

    def remove_trailing_spaces(self):
        index = len(self.text) - 1

        while index >= 0 and self.text[index] == " ":
            index -= 1

        return self.text[:index + 1]
