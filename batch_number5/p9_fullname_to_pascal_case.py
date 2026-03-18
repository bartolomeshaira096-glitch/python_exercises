class FullName:
    def __init__(self, fullname):
        self.fullname = fullname

    def to_pascal_case(self):
        words = self.fullname.split()
        return ''.join(word.capitalize() for word in words)