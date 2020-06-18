class calc:
    def __init__(self):
        nothing = 0

    def add(self, a, b):
        self.a = a
        self.b = b
        print(a+b)
        return(a+b)
    
    def Print(self):
        print("Welcome to calc class")

calculator = calc()

addition = calculator.add(1,1)

print(addition)
