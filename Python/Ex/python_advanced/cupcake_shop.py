from collections import deque


def stock_availability(flavours, *args):
    box_flavours = deque(flavours)
    param = args[0]
    if param == 'delivery':
        for stock in args[1:]:
            box_flavours.append(stock)
    elif param == 'sell':
        if len(args[1:]) == 0:
            box_flavours.popleft()
        elif str(args[1]).isdigit():
            [box_flavours.popleft()for i in range(args[1])]
        else:
            for stock in args[1:]:
                while stock in box_flavours:
                    box_flavours.remove(stock)

    return list(box_flavours)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
