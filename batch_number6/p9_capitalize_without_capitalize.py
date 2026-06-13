class Text:
    def __init__(self, text):
        self.text = text
    
    def capitalize_text(self):
        if len(self.text) == 0:
            return self.text

        result = ""