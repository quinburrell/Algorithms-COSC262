def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions

def is_solution(candidate, input_data):
    return len(candidate) == len(input_data)
    
def children(candidate, input_data):
    children_list = []
    for i in input_data:
        if i not in candidate:
            children_list.append(candidate + (i,))
    return children_list

def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

def add_to_output(candidate, output_data):
    output_data.append(candidate)
    
def should_prune(candidate):
    return False

