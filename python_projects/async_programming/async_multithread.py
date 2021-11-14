import concurrent.futures
import asyncio
import time


def blocking_func(n):
    time.sleep(0.5)
    return n**2


async def main(loop_, executor_):

    print('creating executor tasks')

    blocking_tasks = [loop_.run_in_executor(executor_, blocking_func, i) for i in range(10)]
    print('waiting for tasks to complete')
    results = await asyncio.gather(*blocking_tasks)
    print(f'results: {results}')

if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop, executor))
    finally:
        loop.close()
