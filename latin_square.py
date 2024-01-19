import copy

def latin_squares(square):
    """Given a square (matrix) computes and returns Latin squares
    that can be obtained by replacing Nones with digits."""
    solutions = []
    dfs_backtrack(square, solutions)
    return solutions

def is_solution(candidate):
    for row in candidate:
        if None in row:
            return False
    return True

def children(candidate):
    child_list = []
    for x in range(len(candidate)):
        for y in range(len(candidate)):
            if candidate[x][y] == None:
                break
        if candidate[x][y] == None:
            break
    for num in range(len(candidate)):
        temp = []
        for row in candidate:
            temp.append(list(row))
        temp[x][y] = num 
        child_list.append(temp)
    return child_list
    
def should_prune(candidate):
    for x in range(len(candidate)):
        for y in range(len(candidate)):
            if candidate[x][y] != None:
                if candidate[x][y] in candidate[x][y+1:]:
                    return True
                for i in range(x+1, len(candidate)):
                    if candidate[x][y] == candidate[i][y]:
                        return True
    
def dfs_backtrack(candidate, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(copy.deepcopy(candidate))


def square_from_str(square_str):
    """Takes a string representation of a square and returns a matrix                                                                                                              
    (list of lists) representation where blanks are replaced with None."""
    return [[None if c == '-' else int(c) for c in line.strip()] for
            line in square_str.splitlines()]


def square_to_str(square):
    """Returns the string representation of the given square matrix."""
    return '\n'.join(''.join(str(c) for c in row) for row in square)

