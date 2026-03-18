class Text:
    def __init__(self, text):
        self.text = text

    def zero_fill(self, width):
        result = self.text

        while len(result) < width:
            result = "0" + result

        return result