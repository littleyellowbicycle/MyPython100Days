import time


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        pass

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 60:
                    self._hour += 1
                    if self._hour == 24:
                        self._hour = 0
        pass

    def show(self):
        return ' %02d:%02d:%02d' % (self._hour, self._minute, self._second)
        pass

    pass


def main():
    timer = Clock(23, 58, 59)
    for x in range(130):
        print(timer.show())
        time.sleep(1)
        timer.run()
    pass


if __name__ == "__main__":
    main()
    pass