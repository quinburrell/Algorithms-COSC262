def fractional_knapsack(capacity, items):
    value = 0
    weight_value = lambda item: item[1] / item[2]
    items.sort(reverse=True, key=weight_value)
    for item in items:
        if capacity >= item[2]:
            value += item[1]
            capacity -= item[2]
        else:
            value += capacity * weight_value(item)
            capacity = 0
    return value
    
# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))