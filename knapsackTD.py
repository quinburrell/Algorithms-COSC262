import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

def max_value(items, capacity):
    known = {}
    def max_calc(items, capacity, index):
        if index == None:
            index = len(items) - 1
        if capacity == 0 or index < 0:
            return 0
        elif items[index].weight > capacity:
            return mem(items, capacity, index-1)
        else:
            return max(mem(items, capacity, index-1), items[index].value + 
                       mem(items, capacity - items[index].weight, index-1))    
    def mem(items, capacity, index=None):
        if (capacity, index) in known:
            return known[(capacity, index)]
        else:
            known[(capacity, index)] = max_calc(items, capacity, index)
            return known[(capacity, index)]
    return mem(items, capacity)