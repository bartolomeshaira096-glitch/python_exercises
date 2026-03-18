class Text:
    def __init__(self, text):
        self.text = text

    def starts_with(self, prefix):
        if len(prefix) > len(self.text):
            return False

        return self.text[:len(prefix)] == prefix