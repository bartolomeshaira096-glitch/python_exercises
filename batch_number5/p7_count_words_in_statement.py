class Statement:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())
    
statement = input("Enter a complete statement: ")

text = Statement(statement)

print("Number of words:", text.count_words())