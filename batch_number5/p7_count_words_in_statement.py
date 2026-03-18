class Statement:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())