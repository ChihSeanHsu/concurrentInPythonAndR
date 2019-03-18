# concurency package
import threading as th
import multiprocessing as mp
import concurrent.futures
import asyncio
import aiohttp

import datetime
import functools
import time
import requests
import os

# use multiprocessing and threading

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

# Fibonacci
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# do fib and show some info about thread and process
def do_some_fib(n, start):
    finish = fib(n)
    print(f'{n} ', th.current_thread().name)
    print(f'{n} pid:', os.getpid())
    print(f'{n} parent id:', os.getppid())
    print(f'Complete {n} levels FIB. Answer is {finish}. Cost time {datetime.datetime.now() - start}\n')


FIBS = [35, 28, 1, 25, 10]
@timer
def threading_fib():
    threads = []
    for i in range(len(FIBS)):
        threads.append(th.Thread(target=do_some_fib, args=(FIBS[i], datetime.datetime.now())))
        threads[i].start()

    for i in range(len(FIBS)):
        threads[i].join()
        
@timer
def processing_fib():
    processes = []
    for i in range(len(FIBS)):
        processes.append(mp.Process(target=do_some_fib, args=(FIBS[i], datetime.datetime.now())))
        processes[i].start()  
    for i in range(len(FIBS)):
        processes[i].join()
        
@timer    
def sync_fib():
    for i in FIBS:
        do_some_fib(i, datetime.datetime.now())
        
sync_fib()

threading_fib()
print('-' * 50)
processing_fib()
