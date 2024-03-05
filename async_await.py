import asyncio
import socket


class A:
    def __await__(self):
        return loop.sock_recv(self.s, 1024).__await__()

    async def __aenter__(self):
        self.s = socket.socket()
        self.s.setblocking(False)
        await loop.sock_connect(self.s, ("127.0.0.1", 5000))
        return self

    async def __aexit__(self, *args):
        self.s.close()

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await loop.sock_recv(self.s, 1024)


async def f(i):
    print("Coro", i)
    async with A() as a:
        print("Connect", i)
        async for data in a:
            print(data, i)


async def main():
    await asyncio.gather(f(1), f(2))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# asyncio.run(main())
