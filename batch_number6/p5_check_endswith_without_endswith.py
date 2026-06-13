class Text:
    def __init__(self, text):
        self.text = text

    def ends_with(self, suffix):
        if len(suffix) > len(self.text):
            return False

        return self.text[-len(suffix):] == suffix
    
text = input("Enter a string: ")
suffix = input("Enter suffix to check: ")

value = Text(text)

print(value.ends_with(suffix))