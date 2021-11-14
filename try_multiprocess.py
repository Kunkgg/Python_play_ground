from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Pool
import multiprocessing
from time import sleep
import time
import os

result = []


class Worker:
    def __init__(self, shared_result):
        self.result = shared_result

    def do(self, n):
        process_info(n)
        res = n ** 2
        self.result.append(res)
        sleep(2)
        return res

    def get_result(self):
        return self.result


def process_info(name):
    print(f"Process name: {name}")
    print(f"PID: {multiprocessing.current_process()}")

def f(n, shared_result):
    process_info(n)
    res = n ** 2
    shared_result.append(res)
    sleep(2)
    return res


if __name__ == '__main__':
    start_time = time.time()
    process_info(__name__)
    # with Manager() as mg:
        # shared_result = mg.list()
        # p1 = Process(target=f, args=(1, shared_result))
        # p2 = Process(target=f, args=(2, shared_result))
        # p3 = Process(target=f, args=(3, shared_result))
        # p4 = Process(target=f, args=(4, shared_result))
        # p1.start()
        # p1.join()
        # p2.start()
        # p2.join()
        # p3.start()
        # p3.join()
        # p4.start()
        # p4.join()
        # print(f"result: {shared_result}")

    with Manager() as mg:
        shared_result = mg.list()
        worker = Worker(shared_result)
        with Pool(processes=4) as pool, Manager() as mg:
            pool.map(worker.do, range(4))
            print(f"work result: {worker.get_result()}")
        # pool.join()

        print(f"work result: {worker.get_result()}")

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    print("Finished.")
    print(f"Costed time: {time.time() - start_time}")
