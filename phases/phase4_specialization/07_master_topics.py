# Day 91+: Beyond the 90 Days - Master Topics

def metaprogramming_demo():
    # Creating a class dynamically using type()
    DynamicBuddy = type('DynamicBuddy', (), {'greet': lambda self: print("Hi from the void!")})
    b = DynamicBuddy()
    b.greet()

class Validator(type):
    # Metaclass to enforce naming conventions
    def __new__(cls, name, bases, dct):
        if not name.istitle():
            raise TypeError("Class names must be TitleCase, buddy!")
        return super().__new__(cls, name, bases, dct)

class GoodBuddy(metaclass=Validator):
    pass

def memory_tips():
    # Using slots to save memory
    class SlimBuddy:
        __slots__ = ['name', 'age']
        def __init__(self, name, age):
            self.name = name
            self.age = age

if __name__ == "__main__":
    metaprogramming_demo()
    print("Metaclass validation passed!")
