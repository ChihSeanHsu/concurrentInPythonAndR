# concurency package
import concurrent.futures

import datetime
import functools
import time
import requests
import os

URLS = [
    'https://docs.python.org/3/library/ast.html',
    'https://docs.python.org/3/library/abc.html',
    'https://docs.python.org/3/library/time.html',
    'https://docs.python.org/3/library/os.html',
    'https://docs.python.org/3/library/sys.html',
    'https://docs.python.org/3/library/io.html',
    'https://docs.python.org/3/library/pdb.html',
    'https://docs.python.org/3/library/weakref.html'
]

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

# use cocurrent
@timer
def get_content(url):
    print(url)
    print(f'{url} | ', th.current_thread().name, f' | pid:', os.getpid(), f' | parent id:', os.getppid())
    return requests.get(url).text

@timer
def thread_scrap():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(get_content, url): url for url in URLS}
        print(future_to_url)
        
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Execption as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page length is %d' % (url, len(data)))

@timer
def processing_scrap():
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        future_to_url = {}
        for key, value in zip(URLS, executor.map(get_content, URLS)):
            future_to_url[key] = value
            print('%r page length is %d' % (key, len(value)))

                
@timer
def main():
    for url in URLS:
        try:
            data = get_content(url)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page length is %d' % (url, len(data)))
            
main()

thread_scrap()
print('-' * 50)
processing_scrap()
