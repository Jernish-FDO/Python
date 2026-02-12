# Standard Library Superpowers

from collections import Counter, namedtuple, deque
import itertools
from pathlib import Path

def collections_demo():
    # Counter: Easy counting
    text = "apple banana apple orange banana apple"
    counts = Counter(text.split())
    print(f"Counts: {counts}")

    # Namedtuple: Readable tuples
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Point: {p.x}, {p.y}")

def itertools_demo():
    # Combinations and Permutations
    items = ['A', 'B', 'C']
    print("Combinations of 2:")
    print(list(itertools.combinations(items, 2)))

def pathlib_demo():
    # Modern path handling
    current_dir = Path(".")
    print(f"Current directory: {current_dir.absolute()}")

if __name__ == "__main__":
    collections_demo()
    itertools_demo()
    pathlib_demo()
