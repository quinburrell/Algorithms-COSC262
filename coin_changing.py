'''
def coins_used(value, numCoins):
    result = {}
    while count > 0:
        if numCoins[index] < numcoins[last]:
            

def coins_reqd(value, coinage):
    """The minimum number of coins to represent value"""
    numCoins = [0] * (value + 1)
    for amt in range(min(coinage), value + 1):
        numCoins[amt] = 1 + min(numCoins[amt - c] for c in coinage if  amt >=  c)
    print(numCoins)
    #return coins_used(value, numCoins)
    result = {}
    derp = []
    for coin in coinage:
        result[coin] = 0
    index = len(numCoins) - 1
    last_index = index
    while index >= 0:
        index -= 1
        print(index, last_index)
        if numCoins[index] < numCoins[last_index]:
            temp = last_index - index
            result[temp] = result[temp] + 1
            last_index = index
            print(result.items())
        
    for coin in coinage:
        if result[coin] == 0:
            result.pop(coin)
        else:
            derp.append((coin, result[coin]))
    return derp
    '''
def coins_reqd(value, coinage):
    """The minimum number of coins to represent value"""
    numCoins = [0] * (value + 1)
    coins_used = [0] * (value + 1)
    for amt in range(min(coinage), value + 1):
        numCoins[amt] = 1 + min(numCoins[amt - c] for c in coinage if  amt >=  c)
        coins_used[amt] = (coin, count) for coin in coinage
    return numCoins[value]