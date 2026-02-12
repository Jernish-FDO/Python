# Modern Python Tools (3.10+)

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Project:
    name: str
    priority: int
    tags: List[str]

def modern_features():
    # Walrus operator (:=)
    if (n := len("Buddy")) > 3:
        print(f"Long name: {n} chars")

    # Structural Pattern Matching (Python 3.10+)
    command = "quit"
    match command:
        case "start": print("Let's go!")
        case "quit": print("Goodbye, buddy!")
        case _: print("Unknown command")

if __name__ == "__main__":
    modern_features()
    p = Project("Python Master", 1, ["coding", "fun"])
    print(f"Project: {p}")
