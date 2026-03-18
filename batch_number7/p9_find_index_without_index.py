class Text:
    def __init__(self, text):
        self.text = text

    def custom_index(self, character):
        for position in range(len(self.text)):
            if self.text[position] == character:
                return position

        return -1

text = input("Enter a string: ")
character = input("Enter character to find: ")

value = Text(text)

print(value.custom_index(character))