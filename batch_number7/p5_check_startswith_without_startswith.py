class Text:
    def __init__(self, text):
        self.text = text

    def starts_with(self, prefix):
        if len(prefix) > len(self.text):
            return False

        return self.text[:len(prefix)] == prefix
    
text = input("Enter a string: ")
prefix = input("Enter prefix to check: ")

value = Text(text)

print(value.starts_with(prefix))