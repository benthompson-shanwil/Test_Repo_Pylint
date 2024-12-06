class badClass:
    def __init__(self, value):
        self.value = value
    def displayValue(self):
        print("Value is: ", self.value)

def badFunction():
    print("This is bad code")
    if True:
        print("This should be indented properly")
        print("This should be indented properly")
    for i in range(0, 10):
        print(i)
    print("This should be indented properly EXTREMELY LONG LINE THAT SHOULD THROW AN ERROR IF NOT ")

obj = badClass(10)
obj.displayValue()
badFunction()