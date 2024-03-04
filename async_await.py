import asyncio

async def f(i):
    print("Hello ...", i)
    await asyncio.sleep(2)
    print("...world!", i)
    
async def main():
    await asyncio.gather(f(1), f(2))
    
asyncio.run(main())