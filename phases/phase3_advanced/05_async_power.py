# Day 61-75: Concurrency & Async

import asyncio

async def task_one():
    print("Task 1 starting...")
    await asyncio.sleep(1)
    print("Task 1 done!")

async def task_two():
    print("Task 2 starting...")
    await asyncio.sleep(1)
    print("Task 2 done!")

async def main():
    print("Running tasks at the same time!")
    await asyncio.gather(task_one(), task_two())

if __name__ == "__main__":
    asyncio.run(main())
