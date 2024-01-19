"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    known = {}
    def cell_cost(row, col):
        if (row, col) in known:
            return known[(row, col)]
        else:
            if col in range(n_cols):
                if row == 0:
                    return 0
                else:
                    cost = grid[row-1][col]
                    cost += min(cell_cost(row-1, col + delta) for delta in range(-1, 2))
                    return cost
            else:
                return INFINITY
    for i in range(n_rows+1):
        for j in range(n_cols):
            known[(i, j)] = cell_cost(i, j) 
            print('coords',i,j)
            print(known[(i,j)])
    result = min(known[(n_rows, index)] for index in range(n_cols))
    return result
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))
