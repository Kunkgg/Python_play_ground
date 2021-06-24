# -*- coding: utf-8 -*-
import asyncio


async def worker_1():
    await asyncio.sleep(1)
    return 1


async def worker_2():
    await asyncio.sleep(1)
    return 2 / 0


async def worker_3():
    await asyncio.sleep(3)
    return 3


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    task3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task3.cancel()

    res = await asyncio.gather(task1, task2, task3, return_exceptions=True)
    print(res)


asyncio.run(main())
