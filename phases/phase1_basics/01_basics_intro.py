# Day 1-15: The Absolute Basics

def variables_and_types():
    name = "Python Buddy"
    age = 30
    is_learning = True
    print(f"Name: {name}, Age: {age}, Learning: {is_learning}")

def control_flow():
    score = 85
    if score >= 90:
        print("A - You're a wizard!")
    elif score >= 80:
        print("B - Solid work, buddy!")
    else:
        print("Keep practicing!")

def loops_example():
    for i in range(5):
        print(f"Looping... {i}")

if __name__ == "__main__":
    variables_and_types()
    control_flow()
    loops_example()
