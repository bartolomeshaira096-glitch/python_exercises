class Text:
    def __init__(self, text):
        self.text = 
        
    def is_uppercase(self):
        has_letter = False

        for char in self.text:
            if 'a' <= char <= 'z':
                return False
            elif 'A' <= char <= 'Z':
                has_letter = True

        return has_letter