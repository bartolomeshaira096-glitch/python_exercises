class Text:
    def __init__(self, text):
        self.text = text
        
    def left_justify(self, width):
        result = self.text

        while len(result) < width:
            result += " "

        return result
    
text = input("Enter a string: ")
width = int(input("Enter total width: "))

value = Text(text)

print(f"'{value.left_justify(width)}'")