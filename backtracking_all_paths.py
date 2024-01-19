def adjacency_list(graph_string):
    lines = graph_string.splitlines()
    for x in range(len(lines)):
        lines[x] = lines[x].split()
    if lines[0][0] == 'D':
        directed = True
    else:
        directed = False
    if len(lines[0]) == 3:
        weight = 0
    else:
        weight = None
    result = []
    for v in range(int(lines[0][1])):
        vertex = []
        for line in lines[1:]: 
            if weight != None:
                weight = int(line[2])
            if int(line[0]) == v:
                vertex.append((int(line[1]), 1))
            elif int(line[1]) == v and directed == False:
                vertex.append((int(line[0]), weight))
        result.append(vertex)
    return result

def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((source,), adj_list, solutions, destination)
    return solutions
    
def is_solution(candidate, destination):
    return candidate[-1] == destination

def children(candidate, adj_list):
    child_list = []
    for edge in adj_list[candidate[-1]]:
        if edge[0] not in candidate:
            child_list.append(candidate + (edge[0],))
    return child_list
    
def dfs_backtrack(candidate, input_data, output_data, destination):
    if should_prune(candidate):
        return
    if is_solution(candidate, destination):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data, destination)
            
def add_to_output(candidate, output_data):
    output_data.append(candidate)
    
def should_prune(candidate):
    return False
