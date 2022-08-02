import time
import asyncio


async def delivery(name, meal_time):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(meal_time)
    print(f"{name} 식사 완료! ({meal_time}시간 소요)")
    print(f"{name} 그릇 수거 완료!")


async def main():
    await asyncio.gather(
        delivery("A", 10),
        delivery("B", 5),
        delivery("C", 3)
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
