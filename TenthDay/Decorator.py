import functools


class log():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("start call")
        self.func(*args, **kwargs)
        print("stop call")


@log
def calltest():
    print("calltest")


def main():
    calltest()


if __name__ == "__main__":
    main()
    pass
