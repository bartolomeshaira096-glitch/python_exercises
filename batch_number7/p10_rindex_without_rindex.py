class Text:
    def __init__(self, text):
        self.text = text
        
    def custom_rindex(self, character):
        for position in range(len(self.text) - 1, -1, -1):
            if self.text[position] == character:
                return position

        return - 1
    
text = input("Enter a string: ")
character = input("Enter character to find: ")

value = Text(text)

print(value.custom_rindex(character))