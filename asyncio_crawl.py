# -*- utf-8 -*-
import asyncio
import functools
import time

urls = ['url_1', 'url_2', 'url_3', 'url_4']


def cost_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"cost: {(end - start)}")

    return wrapper


async def crawl(url):
    print(f"Fetching: {url}")
    await asyncio.sleep(int(url.split('_')[-1]))
    print(f"OK {url}")


async def main(urls):
    tasks = [asyncio.create_task(crawl(url)) for url in urls]
    # for task in tasks:
    #     await task

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main(urls))
    print(f"cost time: {time.perf_counter() - start}")
