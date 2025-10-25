# threading is use of I/O bound operations

# it is a way of achieving the concurrency in which multiple tasks are managed at a same time
# we create threads (objects or smth that will run a code) and will try wo run them asynchronusly

# for this we will first import threading module

import threading
import time


lock = threading.Lock()

def check(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        with lock:
            print(f"TIME = {round((end - start), 2)}")
    return wrapper


@check
def square(x):
    time.sleep(2) # we are sleeping our program for 2 sec
    with lock: # using this only one thread will enter there at a time
        print("ans = ",  x * x) 

# now we will create a thread by using threading
# threading.Thread(func ,args, kwargs)
t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=square, args=(2,))
t3 = threading.Thread(target=square, args=(1,))


# if we run them simply in synchronus way it will take around 2 sec of each of them so 2 * number of time func is called
# but by threading we will run them at a same time
 
start = time.perf_counter() # perf_counter is a funciton which will give us time in secs from 1970

t1.start() # start() will start the threads
t2.start()
t3.start()


t1.join()
t2.join() # join() will end those threads
t3.join()

end = time.perf_counter()

print("Total time taken is", round((end - start) , 2))



# this is one way of achieving it
# we can do this by using the contenxt manager and concurrent.futures module using the ThreadPoolExecutor


from concurrent.futures import ThreadPoolExecutor 
# by using ThreadPoolExecutor we don't have to close the thread manually

with ThreadPoolExecutor(max_workers=5) as executor: # we are giving the amount of the threads to create and if there is more task it will just reuse those threads
    # submit() will get a function and parameters to pass to the funciton 
    # it will create a future 
    t4 = executor.submit(square, 2)
    t5 = executor.submit(square, 2)
    t6 = executor.submit(square, 2) 

    # as it will create a future obj which will store the result value of the function we can also print it as
    # print(t4.result())
    # print(t5.result())
    # print(t6.result())


# let us say we have a list of values to passs we can either use the loop or the map function of Threadpool
with ThreadPoolExecutor(max_workers=3) as executor:
    t = executor.map(square, [1, 2, 3])
