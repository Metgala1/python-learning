import asyncio

async def get_price():
    await asyncio.sleep(1)
    return 500

async def get_quantity():
    await asyncio.sleep(1)
    return 4

my_price = 0
my_quantity = 0

async def main():
    price , quantity = await asyncio.gather(
        get_price(),
        get_quantity()
    )
    global my_price, my_quantity
    
    my_price += price
    my_quantity += quantity
    
    total = price * quantity
    
    print(f"Total: {total}")

asyncio.run(main())

print(my_price)
print(my_quantity)