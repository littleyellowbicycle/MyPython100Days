from threading import Thread
from random import randint
from time import sleep, time


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("下载%s" % self._filename)
        time_pause = randint(5, 10)
        sleep(time_pause)
        print("下载%s花了%s秒" % (self._filename, time_pause))


def main():
    start = time()
    task1 = DownloadTask("漫画算法")
    task1.start()
    task2 = DownloadTask("TensorFlow")
    task2.start()
    task1.join()
    task2.join()
    end = time()
    print("total time is %d" % (end - start))


if __name__ == "__main__":
    main()
    pass