def coroutine(f):
    print("decorator start")
    gen = f()
    next(gen)
    return gen


@coroutine
def coro():
    print("coro start")
    i = yield
    print("coro:", i)
    i = yield i + 1
    print("coro:", i)
    yield i + 1


def main():
    print("main start")
    i = coro.send(1)
    print("main:", i)
    i = coro.send(i + 1)
    print("main:", i)



main()
