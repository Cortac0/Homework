
class Test:
    class_var = 0
    def __init__(self, instance_var):
        self.instance_var = 0
    
    def display(self):
        print("self.class", self.class_var)
        print("self.instance_var", self.instance_var)

        try:
            print("self.new_var", self.new_var)
        except AttributeError:
            pass

    def modify(self, new_value):
        self.class_var = new_value
        self.instance_var = new_value

    
x = Test(0)

x.display()

x.modify(1)
x.display()

x.class_var = 2
x.instance_var = 2
x.display()

x.new_var = 3
x.modify(3)
x.display()
