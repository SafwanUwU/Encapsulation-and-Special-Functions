class myClass:

    __privateVar = 27

    def __privMeth(self):
        print("I'm inside class PrivMeth Method Myclass")

    def hello(self):
        print("Private Variable Value: ",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth
print(foo.__privateVar)