class Text:
    def __init__(self, text):
        self.text = text

    def remove_prefix(self, prefix):
        if self.text[:len(prefix)] == prefix:
            return self.text[len(prefix):]

        return self.text