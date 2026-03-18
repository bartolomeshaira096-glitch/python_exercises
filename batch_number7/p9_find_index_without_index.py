class Text:
    def __init__(self, text):
        self.text = text

    def custom_index(self, character):
        for position in range(len(self.text)):
            if self.text[position] == character:
                return position

        return -1
