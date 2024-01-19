class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    result_table = {}
    def max_calc(index, cap):
        if (index, cap) in result_table:
            return result_table[(index, cap)]
        else:
            if index == 0 or index == 0:
                return 0
            elif items[index-1].weight > cap:
                return max_calc(index-1, cap)
            else:
                return max(max_calc(index-1, cap),
                           items[index-1].value + max_calc(index-1, cap - items[index-1].weight))
    for j in range(capacity+1):
        for i in range(len(items)+1):
            result_table[(i,j)] = max_calc(i, j)
    result = []
    i = len(items)
    j = capacity
    while i > 0 and j > 0:
        if result_table[(i,j)] != result_table[(i-1,j)]:
            j -= items[i-1].weight
            result.append(items[i-1])
        i -= 1
    return (result_table[(len(items),capacity)], result)