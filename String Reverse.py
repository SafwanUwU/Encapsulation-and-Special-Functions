class class_reverse:
    
    def __init__(self, s):
        self.s = s
    
    def revStr(self):
        return self.s[::-1]
    
    def __str__(self):
        return f"Reversed string: {self.revStr()}"
# User input
str_input = input("Enter the word to be reversed: ")

o1 = class_reverse(str_input)
print(o1)
