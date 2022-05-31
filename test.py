
items = []
prices = []
money  = 6500
while money != 0:
    print(f'you have {str(money)}')
    item = input('what is the item?')
    price = input('how much is the item?')
    money -= int(price)
    items.append(item)
    prices.append(price)

for x,y in zip(prices,items):
    print((x,y))


