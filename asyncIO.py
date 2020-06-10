import asyncio


async def print_odd_even(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print("True and running the process btw", start, end)
        if i % 2 != 0:
            await asyncio.sleep(0.0001)


async def main():
    task_1 = loop.create_task(print_odd_even(1, 20))
    task_2 = loop.create_task(print_odd_even(22, 30))
    task_3 = loop.create_task(print_odd_even(40, 50))
    await asyncio.wait([task_1, task_2, task_3])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
