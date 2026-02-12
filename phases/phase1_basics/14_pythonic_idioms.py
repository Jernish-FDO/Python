# Pythonic Idioms & Zen

def zen_of_python():
    import this
    # "Explicit is better than implicit."
    # "Simple is better than complex."

def pythonic_tips():
    # 1. Unpacking
    a, b = 1, 2
    a, b = b, a # Swap
    
    # 2. List Comprehensions (The Pythonic Way)
    squares = [x*x for x in range(5)]
    
    # 3. Zip for parallel iteration
    names = ["A", "B"]
    scores = [10, 20]
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

if __name__ == "__main__":
    zen_of_python()
    pythonic_tips()
