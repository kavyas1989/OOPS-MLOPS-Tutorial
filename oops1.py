##intialte a class

class employee :
    #special method/magic method/dunder method - constructor
    def __init__(self) :
        self.id = 123
        self.salary = 42500
        self.designation = "ADSE"

    #functions defined inside class is a method, outside is function

    def travel(self , destination):
        print(f"Employee is now travelling to {destination}")

##create an object/instance of the class

kabir = employee()

# print(kabir.salary)
# kabir.travel("chennai")
print(type(kabir))