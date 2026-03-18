class Text:
    def __init__(self, text):
        self.text = text

    def right_justify(self, width):
        result = self.text

        while len(result) < width:
            result = " " + result

        return result