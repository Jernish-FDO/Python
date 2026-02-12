# Day 31-45: OOP Basics

class Buddy:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def celebrate(self):
        print(f"🎉 {self.name} just reached Level {self.level}!")

class DeveloperBuddy(Buddy):
    def code(self):
        print(f"💻 {self.name} is smashing some Python code!")

if __name__ == "__main__":
    jernish = DeveloperBuddy("Jernish", 99)
    jernish.celebrate()
    jernish.code()
