class Text:
    def __init__(self, text):
        self.text = text

    def ends_with(self, suffix):
        if len(suffix) > len(self.text):
            return False

        return self.text[-len(suffix):] == suffix