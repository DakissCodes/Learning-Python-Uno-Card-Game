
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


def two_sum(nums,target):
    for _ in nums:
        for i in nums:
            if _ + i == target and _ != i:
                return [i for i,n in enumerate(nums) if n == _]
            elif nums.count(_) > 1 and _ == i:
                return [nums.index(_),nums.index(i)]
    return None

two_sum([3,2,4],6)