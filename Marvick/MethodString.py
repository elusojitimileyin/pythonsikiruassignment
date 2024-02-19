class MethodString:

    def __init__(self):
        self.string_name = " "

    def name_inputs(self, word):
        self.string_name = word

    def printString(self):
        return self.string_name.upper()
