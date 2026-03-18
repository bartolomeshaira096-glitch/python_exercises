class Text:
    def __init__(self, text):
        self.text = text

    def custom_count(self, character):
        counter = 0

        for ch in self.text:
            if ch == character:
                counter += 1

        return counter