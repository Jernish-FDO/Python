# Speed & Profiling

import timeit
import cProfile

def expensive_operation():
    return [x**2 for x in range(10000)]

def profiling_demo():
    # timeit: Measuring small code snippets
    time_taken = timeit.timeit(expensive_operation, number=100)
    print(f"Time for 100 runs: {time_taken:.4f} seconds")

    # cProfile: Full function call analysis
    print("\nFull Profile Analysis:")
    cProfile.run('expensive_operation()')

if __name__ == "__main__":
    profiling_demo()
