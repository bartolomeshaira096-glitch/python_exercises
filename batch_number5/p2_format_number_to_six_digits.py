class NumberFormatter:
    def __init__(self, number):
        self.number = number

    def to_six_digits(self):
        return f"{self.number:06d}"
    
    number = int(input("Enter a number (0-1000): "))
