# concurency package
import asyncio
import aiohttp

import datetime
import functools
import time
import os

# cal cost time
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
async def fetch_url(session, url):
    print(url, ' function start!!')
    start = datetime.datetime.now()
    async with session.get(url, timeout=60 * 60) as response:
        print(url, ' Starto | ', th.current_thread().name, f' | pid: {os.getpid()}', f' | parent id: {os.getppid()}')
        html = await response.text()
        print(url, f' Length is {len(html)}. And spend {datetime.datetime.now() - start}')

async def fetch_all_urls(session, urls, loop):
    print('fetch_all_urls start')
    await asyncio.gather(*[fetch_url(session, url) for url in urls],
    return_exceptions=True)
    print('fetch_all_urls Finish.')

@timer
async def get_htmls(urls):
    print('get_htmls start')
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(loop=loop, connector=connector) as session:
        await fetch_all_urls(session, urls, loop)
    print(f'I\'m in get_htmls')

print(URLS)
start = datetime.datetime.now()
loop = asyncio.get_event_loop()
loop.run_until_complete(get_htmls(URLS))
print(f'I\'m Finish. {datetime.datetime.now() - start}')
