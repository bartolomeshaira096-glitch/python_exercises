class Text:
    def __init__(self, text):
        self.text = text

    def remove_suffix(self, suffix):
        if len(suffix) > len(self.text):
            return self.text

        if self.text[-len(suffix):] == suffix:
            return self.text[:-len(suffix)]

        return self.text