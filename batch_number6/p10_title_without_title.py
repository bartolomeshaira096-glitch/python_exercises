class Text:
    def __init__(self, text):
        self.text = text

    def to_title_case(self):
        result = ""
        new_word = True

        for character in self.text:
            if character == " ":
                result += character
                new_word = True
            else:
                if new_word:
                    if 'a' <= character <= 'z':
                        result += chr(ord(character) - 32)
                    else:
                        result += character
                    new_word = False
                else:
                    if 'A' <= character <= 'Z':
                        result += chr(ord(character) + 32)
                    else:
                        result += character

        return result