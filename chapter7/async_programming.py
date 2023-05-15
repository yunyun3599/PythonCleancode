import time
import asyncio


async def count_num_async(n):               # async def는 @coroutine 데코레이터를 대신하여 코루틴을 정의하는 새로운 방법
    for i in range(1, n + 1):
        print(f"Number {i} is counted")
        await asyncio.sleep(1)              # await는 yield from을 대신하기 위한 용도로 awaitable 객체에 대해서만 동작 (코루틴은 awaitable)
    print(f"count to {n} is finished")


async def process():
    start = time.time()
    await asyncio.wait([
        count_num_async(3),
        count_num_async(2),
        count_num_async(1),
    ])
    end = time.time()
    print(f"total consumed time: {end - start}")


if __name__ == "__main__":
    asyncio.run(process())