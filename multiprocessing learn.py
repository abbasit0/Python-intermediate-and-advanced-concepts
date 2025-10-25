import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor


def add(x, y):
    time.sleep(2)
    result = x + y
    print(f"The sum is {result}")
    return result


if __name__ == "__main__":
    # Using multiprocessing.Process without direct return of results
    start = time.perf_counter()

    v1 = multiprocessing.Process(target=add, args=(4, 1))
    v2 = multiprocessing.Process(target=add, args=(2, 1))
    v3 = multiprocessing.Process(target=add, args=(4, 8))

    v1.start()
    v2.start()
    v3.start()

    v1.join()
    v2.join()
    v3.join()

    end = time.perf_counter()

    print(f'Time taken = {round(end - start, 2)}')

    # Using ProcessPoolExecutor with result retrieval
    with ProcessPoolExecutor() as executor:
        m1 = executor.submit(add, 1, 2)
        m2 = executor.submit(add, 4, 1)

        # Retrieve and print the actual results (this will also wait for task completion)
        print(m1.result())
        print(m2.result())
