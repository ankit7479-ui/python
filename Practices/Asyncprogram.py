import asyncio

async def greet():
    await asyncio.sleep(1)
    print("Hello Asyncio !")
    
asyncio.run(greet())    