# 🎯 Python Interview Cracker

Hey buddy, if you're looking for a job, these are the questions that come up ALL the time. Let's get you ready!

## 1. What is the difference between List and Tuple?
- **List**: Mutable (you can change it), uses `[]`.
- **Tuple**: Immutable (locked in), uses `()`. Tuples are slightly faster and use less memory!

## 2. What is the Global Interpreter Lock (GIL)?
It's a "lock" that allows only one thread to hold the control of the Python interpreter. This means Python doesn't do "true" multi-threading for CPU tasks, which is why we use `multiprocessing` for heavy lifting!

## 3. How does Memory Management work in Python?
Python uses **Private Heap Space**. It has a built-in **Garbage Collector** that uses reference counting to clear out objects that are no longer being used.

## 4. What are Decorators?
They are functions that wrap other functions to modify their behavior without changing the original code. Think of it like a "plugin" for a function!

## 5. What is `__init__`?
It's the "constructor" method in a class. It runs automatically as soon as you create a new object to set things up.

---
**Pro-Tip**: Always mention "Readability" and "The Zen of Python" in interviews. Hiring managers love that stuff! 🤜🤛
