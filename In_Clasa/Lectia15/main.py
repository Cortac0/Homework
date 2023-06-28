
class Calculator:
    def __init__(self, a, b): # se foloseste pentru a trimite valori clasei
        print("Initializam clasa")
        self.a = a
        self.b = b

    def __eq__(self, __value: object) -> bool:
        print("Self:", self.a, self.b)
        print("other:", __value.a, __value.b)
        if self.a == __value.a:
            return True
        return False

    def __repr__(self) -> str:
        return f"Reprezentarea clasei de tip calculator {self.a}, {self.b}"

    def __str__(self) -> str:
        return f"String Clasa de tip calculator {self.a}, {self.b}"

    def add(self):
        result = self.a + self.b
        print(f"Add: {result}")
        return result
    
    def sub(self):
        pass
    
    

x = Calculator(2, 3)
y = Calculator(5, 2)

# x.add()
print(str(x))
print(x)
# print(x == y)