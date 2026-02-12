# Design Patterns in Python

# 1. Singleton: Only one instance ever
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. Factory Pattern: Creating objects without specifying the class
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

def animal_factory(choice):
    animals = {"dog": Dog, "cat": Cat}
    return animals.get(choice, Dog)()

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(f"Is same instance? {s1 is s2}")
    
    pet = animal_factory("cat")
    print(f"Pet says: {pet.speak()}")
