import asyncio


async def get_item(i):
    await asyncio.sleep(i)
    return f'item {i}'


async def get_items(num_itens):
    print('getting items')

    item_coros = [asyncio.create_task(get_item(i)) for i in range(num_itens)]
    print('waiting for tasks to complete')
    completed, pending = await asyncio.wait(item_coros)
    results = [task.result() for task in completed]
    print(f'results: {results}')
    print(pending)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(get_items(20))
finally:
    loop.close()