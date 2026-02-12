# Day 46-60: Advanced Tools

import time

def my_decorator(func):
    def wrapper():
        print("🚀 Starting the engine...")
        func()
        print("🏁 Mission complete.")
    return wrapper

@my_decorator
def build_feature():
    print("Building a cool feature...")
    time.sleep(1)

def my_generator(n):
    for i in range(n):
        yield i * i

if __name__ == "__main__":
    build_feature()
    print("Generator values:")
    for val in my_generator(3):
        print(val)
