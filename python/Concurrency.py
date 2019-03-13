#!/usr/bin/env python
# coding: utf-8

# In[33]:


import threading as th
import multiprocessing as mp
import datetime
import functools
import time


# In[34]:


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def do_some_fib(n):
    start = datetime.datetime.now()
    finish = fib(n)
    print(f'Complete {n} levels FIB. Answer is {finish}. Cost time {datetime.datetime.now() - start}\n')
    


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


# In[13]:


do_some_fib(35)


# In[24]:


FIBS = [35, 28, 1, 25, 10]


# In[35]:


@timer
def threading_fib():
    threads = []
    for i in range(len(FIBS)):
        threads.append(th.Thread(target=do_some_fib, args=(FIBS[i],)))
        threads[i].start()

    for i in range(len(FIBS)):
        threads[i].join()


# In[36]:


@timer
def processing_fib():
    processes = []
    for i in range(len(FIBS)):
        processes.append(mp.Process(target=do_some_fib, args=(FIBS[i],)))
        processes[i].start()  
    for i in range(len(FIBS)):
        processes[i].join()


# In[ ]:





# In[ ]:




