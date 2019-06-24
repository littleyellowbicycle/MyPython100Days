from multiprocessing import Process, Queue
from time import time, sleep


def count(res_queue, cur_list):
    res = 0
    for num in cur_list:
        res += num
    res_queue.put(res)


def main():
    rge = [x for x in range(1, 10000001)]
    process = []
    index = 0
    res_queue = Queue()
    for _ in range(8):
        p = Process(target=count, args=(res_queue, rge[index:index + 1250000]))
        index += 1250000
        process.append(p)
        p.start()
    start = time()
    for p in process:
        p.join()
    total = 0
    while not res_queue.empty():
        total += res_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')

    pass


if __name__ == "__main__":
    main()
    pass