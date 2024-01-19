from collections import namedtuple
from graphviz import Graph
Node = namedtuple("Node", ["value", "left", "right"])

def plot_graph(tree, g):
    rootid = str(id(tree))
    if tree.left is None and tree.right is None:
        g.node(rootid, str(tree.value), shape='box')
    else:
        g.node(rootid, str(tree.value))
        if tree.left:
            left = plot_graph(tree.left, g)
            g.edge(rootid, left)
        if tree.right:
            right = plot_graph(tree.right, g)
            g.edge(rootid, right)
    return rootid

def binary_search_tree(nums, is_sorted=False, start=0, end=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if end is None:
        end = len(nums) -1 
    if not is_sorted:
        nums = sorted(nums)
    #n = len(nums)
    if start == end:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = (start + (((end + 1) - start) // 2)) - 1 # Halfway (approx)
        left = binary_search_tree(nums, True, start, mid)
        right = binary_search_tree(nums, True, mid+1, end)
        tree = Node(nums[mid], left, right)
    return tree
    
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)

def range_query(tree, low, high):
    """Return a list of the numbers in range min to max
       inclusive within the given binary search tree.
    """
    matches = []
    if tree.left is None and tree.right is None:  # Leaf?
        if low <= tree.value <= high:
            matches.append(tree.value)
    else: # Internal node
        if low <= tree.value and tree.left is not None:
            matches += range_query(tree.left, low, high)
        if high > tree.value and tree.right is not None:
            matches += range_query(tree.right, low, high)
    return matches